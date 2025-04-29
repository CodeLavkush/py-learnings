from pymongo import MongoClient
from bson import ObjectId

DB_URI = "mongodb+srv://thanos_45:thanos45@cluster0.sh7nb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(DB_URI, tlsAllowInvalidCertificates = True)

db = client["todos"]
todos_collection = db["todo"]

print(todos_collection)

def list_todos():
    for todo in todos_collection.find():
        if todo['todo']:
            print(f"ID: {todo['_id']}, Todo: {todo['todo']}")
        else:
            print("Empty todo...")

def add_new_todo():
    todo = input("Enter your todo: ")

    todos_collection.insert_one({'todo': todo})

def update_todo():
    list_todos()

    todo_id = input("Enter todo Id: ")
    new_todo = input("Enter new todo: ")

    todos_collection.update_one(
        {'_id': ObjectId(todo_id)},
        {"$set": {'todo': new_todo}}
    )

def delete_todo():
    list_todos()

    todo_id = input("Enter todo Id: ")

    todos_collection.delete_one({'_id': ObjectId(todo_id)})

def main():
    while True:
        print("\nTodo app | choose an option")
        print("1.List all todos")
        print("2.Add new todo")
        print("3.Update a todo")
        print("4.Delete a todo")
        print("5.Exit the program")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_todos()
            case 2:
                add_new_todo()
            case 3:
                update_todo()
            case 4:
                delete_todo()
            case 5:
                break
            case _:
                print("Invalid input")

if __name__ == "__main__":
    main()