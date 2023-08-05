import time
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def print_progress(progress):
    print(f"Hacking in progress: {progress}%")
    time.sleep(0.3)

print("      ~~HACKER SIMULATOR~~    ")
print("Welcome to the Hacker Simulator!")
print("You are a skilled hacker on a secret mission.")
print("Your objective: Hack into the top-secret Wi-Fi network.")
print("To begin, choose an action:")
print("1 - Start hacking the Wi-Fi network")
print("2 - Exit")

action = input("Enter your choice: ")

if action == '1':
    print("Initiating hacking sequence...")
    for progress in range(0, 101, 2):
        print_progress(progress)
    print("Gaining access to the Wi-Fi network...")
    time.sleep(2)
    for progress in range(10, 101, 10):
        print_progress(progress)
    print("Cracking security protocols...")
    time.sleep(2)
    for progress in range(20, 101, 10):
        print_progress(progress)
    print("Bypassing firewalls...")
    time.sleep(2)
    for progress in range(30, 101, 10):
        print_progress(progress)
    print("Extracting Wi-Fi password...")
    time.sleep(2)
    for progress in range(40, 101, 10):
        print_progress(progress)

    # Generate a random password
    password_length = random.randint(12, 20)  # Random length between 12 and 20 characters
    random_password = generate_random_password(password_length)

    print("Success! You've obtained the password.")
    time.sleep(1)
    print("Password:", random_password)
    print("IP: 192.168.0.1")

    # Extra features (same as before)
    connect_choice = input("Do you want to connect to the hacked Wi-Fi network? (yes/no): ")
    if connect_choice.lower() == 'yes':
        print("Connecting...")
        time.sleep(2)
        print("Successfully connected to the Wi-Fi network!")
        time.sleep(1)
    else:
        print("Exiting without connecting to the Wi-Fi network.")

    print("Thank you for using the Hacker Simulator!")
    print("Please rate the program from 1 to 5 stars:")
    rating = int(input("> "))
    if 1 <= rating <= 5:
        if rating == 5:
            print("Wow! Thank you for your fantastic rating!")
        elif rating >= 4:
            print("Thank you for your positive feedback!")
        elif rating == 3:
            print("We appreciate your average rating. We'll keep improving!")
        else:
            print("We're sorry to hear that. We'll work harder to improve.")
    else:
        print("Invalid rating. Thanks for trying out the Hacker Simulator!")
else:
    print("Exiting the Hacker Simulator. Goodbye!")