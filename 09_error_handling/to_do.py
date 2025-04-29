import json

file_name = 'todo.txt'

def load_todos():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo(todos):
    with open(file_name, 'w') as file:
        json.dump(todos, file)

def list_all_todos(todos):
    try:
        print("\n")
        print("-" * 80)
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")
        print("-" * 80)
    except Exception:
        return []

def add_new_todo(todos):
    todo = input("Enter a task: ")

    todos.append(todo)
    save_todo(todos)

def update_todo(todos):
    list_all_todos(todos)

    index = int(input("Enter task no: "))
    new_todo = input("Enter new task: ")

    todos[index - 1] = new_todo
    save_todo(todos)

def delete_todo(todos):
    list_all_todos(todos)

    index = int(input("Enter task number to delete: "))

    del todos[index - 1]
    save_todo(todos)

def main():
    while True:
        todos = load_todos()
        
        print("\nTo Do program | Choose an option\n")
        print("1.List all the tasks")
        print("2.Add new tasks")
        print("3.Update tasks")
        print("4.Delete tasks")
        print("5.Exit the program")
        choice = int(input("Enter a choice(1-5): "))

        match choice:
            case 1:
                list_all_todos(todos)
            case 2:
                add_new_todo(todos)
            case 3:
                update_todo(todos)
            case 4:
                delete_todo(todos)
            case 5:
                break
            case _:
                print("Invalid Input...")

if __name__ == "__main__":
    main()