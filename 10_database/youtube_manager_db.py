import sqlite3

DB_NAME = 'youtube_videos.db'

try:
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
except sqlite3.Error as e:
    print(f"Error while connecting to DB: {e}")

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")

    rows = cursor.fetchall()

    if not rows:
        print("Empty videos...")
    else:
        print("\n")
        print("*" * 80)
        for row in rows:
            video_id, name, time = row
            print(f"{video_id}. {name} - {time}")
        print("*" * 80)
        
def add_videos():
    name = input("Enter video title: ")
    time = input("Enter video time: ")

    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))

    print("Video added successfully")

    connection.commit()


def update_videos():
    video_id = int(input("Enter video id: "))
    new_name = input("Enter new video name: ")
    new_time = input("Enter new video time: ")

    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    print("Video updated successfully")

    connection.commit()

def delete_videos():
    list_all_videos()
    video_id = int(input("Enter video id: "))
    
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    print("Video deleted successfully")
    connection.commit()

def main():  
    while True:
        print("\nYoutube manager app with DB")
        print("1.List videos")
        print("2.Add videos")
        print("3.Update videos")
        print("4.Delete videos")
        print("5.Exit the program")

        choice = int(input("Enter a choice: "))

        match choice:
            case 1:
                list_all_videos()
            case 2:
                add_videos()
            case 3:
                update_videos()
            case 4:
                delete_videos()
            case 5:
                break
            case _:
                print("Invalid input")

    connection.close()

if __name__ == "__main__":
    main()