"""
10-5
Guest Book: Write a while loop that prompts users for their name. Collect all the names that are 
entered, and then write these names to a file called guest_book.txt. Make sure each entry appears
on a new line in the file.
"""
from pathlib import Path

path = Path("Unit10/guest_book.txt")

response = ''
guest_list = []

while response != 'q':
    print("Please provide your name to add to the guestbook.")
    response = input("(Type q to quit): ")
    if response != 'q':
        guest_list.append(response)

path.write_text('\n'.join(guest_list))