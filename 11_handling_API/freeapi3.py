import requests

def fetch_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"

    response = requests.get(url)
    jsonData = response.json()

    if jsonData["success"] and "data" in jsonData:
        product_data = jsonData["data"]["data"]

        for product in product_data:
            product_id = product["id"]
            product_title = product["title"]
            product_desc = product["description"]
            product_price = product["price"]
            product_rating = product["rating"]
            product_stock = product["stock"]
            product_brand = product["brand"]
            product_category = product["category"]

            if product_rating < 2:
                rating = "1 star"
            elif product_rating < 3:
                rating = "2 stars"
            elif product_rating < 4:
                rating = "3 stars"
            elif product_rating < 5:
                rating = "4 stars"
            else:
                rating = "5 stars"

            print("\n")
            print("*" * 80)
            print(f"{product_id}. {product_title}")
            print(f"Description: {product_desc}")
            print(f"Price: {product_price}Rs | Rating: {rating} | In Stock: {product_stock}")
            print(f"Brand: {product_brand} | Category: {product_category}")
            print("*" * 80)



def main():
    fetch_products()

if __name__ == "__main__":
    main()