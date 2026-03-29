from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    new_username = input("What is your name? ")
    contents = json.dumps(new_username)
    path.write_text(contents)
    new_user_path = Path("guest_book.txt")
    with new_user_path.open("a") as file:
        file.write(new_username + "\n")
    return new_username
    

def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        user_response = input(f"Are you {username}? (y/n)")
        new_username = get_new_username(path)
        if user_response == "y":
            print(f"Hello, {username}! it's nice to see you again.")
        else:
            print(f"Welcome, {username}! We'll be sure to remember you next time.")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
    



greet_user()
