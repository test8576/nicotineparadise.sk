import requests

url = "https://www.snusfarmer.com/en/collection/"

with open("choose_brand.html", "r") as file:
    index_copy = file.read()
    copy = str(index_copy)
    

brands = dict()
create_brands = dict()
for page_index in range(1, 29):
    req = requests.get(url + f"page{str(page_index)}.ajax")
    req = req.json()
    for i in range(len(req["products"])):
        try:
            full_title = req["products"][i]["fulltitle"]
            variant = req["products"][i]["variant"]
            id_ = req["products"][i]["id"]
            image = req["products"][i]["image"].replace("50x50x2/","")
            real_price = req["products"][i]["price"]["price"]
            brand = req["products"][i]["brand"]["title"]
            brand_image = req["products"][i]["brand"]["image"]

            if 5.0 < real_price:
                price = real_price + 0.3
            
            elif 3.0 < real_price <= 5.0:
                price = real_price + 0.4

            elif 2.0 < real_price <= 3.0:
                price = real_price + 0.8

            elif 1.0 < real_price <= 2.0:
                price = real_price*1.5

            elif 0 < real_price <= 1.0:
                price = 1.99

            price = "%.2f" % round(price, 2)

            data = [full_title, variant, id_, image, price]

            if brand not in brands.keys():
                brands[brand] = tuple()

            brands[brand] += (data, )

            create_brands[brand] = brand_image
        except:
            pass
        
for brand in create_brands:
    brand_copy = str(copy)
    brand_html = f"""
    <div class="brand">
        <a href="brands/{brand}.html">
        <p>{brand}</p>
        <img src={create_brands[brand]}>
        </a>
    </div>
    <div class="main">
    """
    brand_copy = brand_copy.replace('<div class="main">',
                                    brand_html)

    with open(f"brands/{brand}.html", "w+") as f:

        brand_copy = brand_copy.replace('<link rel="stylesheet" href="css/info.css" type="text/css">',
                                        """<link rel="stylesheet" href="../css/info.css" type="text/css">
    <link rel="stylesheet" href="../css/index.css" type="text/css">""")

        brand_copy = brand_copy.replace('<link rel="stylesheet" href="css/nav.css" type="text/css">',
                                        '<link rel="stylesheet" href="../css/nav.css" type="text/css">')

        brand_copy = brand_copy.replace('<link rel="stylesheet" href="css/footer.css" type="text/css">',
                                        '<link rel="stylesheet" href="../css/footer.css" type="text/css">')

        brand_copy = brand_copy.replace("js/burger.js",
                                        "../js/burger.js")

        brand_copy = brand_copy.replace("gallery/icon.png",
                                        "../gallery/icon.png")

        brand_copy = brand_copy.replace("gallery/logo.png",
                                        "../gallery/logo.png")

        brand_copy = brand_copy.replace("index.html",
                                        "../index.html")

        brand_copy = brand_copy.replace("contact.html",
                                        "../contact.html")

        brand_copy = brand_copy.replace("order_other.html",
                                        "../order_other.html")

        brand_copy = brand_copy.replace("choose_brand.html",
                                        "../choose_brand.html")

        brand_copy = brand_copy.replace("gallery/instagram.png",
                                        "../gallery/instagram.png")

        brand_copy = brand_copy.replace("css/choose_brand.css",
                                        "../css/choose_brand.css")

        for data in brands[brand]:
            specific_brand = f"""
            <div class="product">
                <p class="name">{data[0]}</p>
                <img src="{data[3]}">
                <div class="product-bottom">
                    <p class="price">€{data[4]}</p>
                    <p> </p>
                    <h3>{data[1]}</h3>
                </div>
            </div>
            <!--replace_here_XX_YY-->
            """
            brand_copy = brand_copy.replace("<!--replace_here_XX_YY-->",
                                            specific_brand)
        f.write(brand_copy)
        

print("done")
