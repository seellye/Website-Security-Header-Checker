import requests
url = input("Type the URL: (example: https://www.google.com) ")
try:
    answer = requests.get(url, timeout=5)
    headers = answer.headers
except Exception as error:
    print("\nError: Could not connect to the website.")
    print("Please check the URL and try again.")
    exit()

security_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]
print("\nAnalysis result:\n")
for header in security_headers:
    if header in headers:
        print(f"[+] {header}: Present")
    else:
        print(f"[-] {header}: Missing")