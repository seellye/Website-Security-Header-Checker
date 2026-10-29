import requests
url = input("Type the URL: (example: https://www.google.com) ")
if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url
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

present = 0
missing = 0

for header in security_headers:
    if header in headers:
        print(f"[+] {header}: Present")
        valor = headers[header]
        if len(valor) > 80: 
            valor = valor[:80] + "..."
        print(f"    Value: {valor}")
        present += 1
    else:
        print(f"[-] {header}: Missing")
        missing += 1

print(f"\nSummary: {present} present, {missing} missing.")