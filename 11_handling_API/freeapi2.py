import requests

def fetch_users():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    jsonData = response.json()
    
    if jsonData["success"] and "data" in jsonData:
        users = jsonData["data"]["data"]
        for user in users:
            user_gender = user["gender"]
            user_title = user["name"]["title"]
            user_firstName = user["name"]["first"]
            user_lastName = user["name"]["last"]
            user_city = user["location"]["city"] 
            user_state = user["location"]["state"] 
            user_country = user["location"]["country"]
            user_email = user["email"]

            print("\n")
            print("*" * 80)
            print(f"Name: {user_title} {user_firstName} {user_lastName}")
            print(f"Gender: {user_gender}")
            print(f"Address: {user_city}, {user_state}, {user_country}")
            print(f"Email: {user_email}")
            print("*" * 80)
    else:
        raise Exception("Failed to fetch data...")

def main():
    fetch_users()

if __name__ == "__main__":
    main()