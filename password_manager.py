import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Try generating a password and printing it
print("Generated Password:", generate_password())

import json

def save_password(website, username, password):
    data = {
        website: {
            "username": username,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(data)

    with open("data.json", "w") as file:
        json.dump(existing_data, file, indent=4)

    print("✅ Password saved successfully!")
def search_password(website):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                print(f"🌐 Website: {website}")
                print(f"👤 Username: {data[website]['username']}")
                print(f"🔐 Password: {data[website]['password']}")
            else:
                print("❌ No details found for that website.")
    except FileNotFoundError:
        print("⚠️ No saved data found.")
# Test searching for a password
search_password("facebook.com")
# 👉 Test the save function
website = "facebook.com"
username = "afira.fb@gmail.com"
password = generate_password()

save_password(website, username, password)
search_password("facebook.com")
while True:
    print("\n🔐 PASSWORD MANAGER MENU 🔐")
    print("1. Generate Password")
    print("2. Save New Password")
    print("3. Search for Saved Password")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        length = int(input("Enter password length: "))
        print("Generated Password:", generate_password(length))

    elif choice == "2":
        site = input("Enter website name: ")
        user = input("Enter username/email: ")
        pwd = input("Enter password (leave blank to auto-generate): ")
        if pwd == "":
            pwd = generate_password()
            print("Generated Password:", pwd)
        save_password(site, user, pwd)

    elif choice == "3":
        site = input("Enter website to search: ")
        search_password(site)

    elif choice == "4":
        print("👋 Exiting Password Manager. Bye Afira!")
        break

    else:
        print("⚠️ Invalid option. Please choose 1-4.")
