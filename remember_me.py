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
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        user_response = input(f"Are you {username}? (y/n)")
        if user_response == "y":
            print(f"Hello, {username}! it's nice to see you again")
        else:
            print("What is your name? ")
        print(f"Welcome, {username}! We'll be sure to remember you next time.")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
    



greet_user()
