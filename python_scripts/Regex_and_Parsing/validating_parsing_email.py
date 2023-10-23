import email.utils
import re

n = int(input())

for _ in range(n):
    email_str = input()
    parse_email = email.utils.parseaddr(email_str)

    email_pattern = r"^[a-zA-Z][a-zA-Z0-9_\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

    addr_match = re.match(email_pattern, parse_email[1])

    if addr_match:
        print(email.utils.formataddr((parse_email[0], parse_email[1])))
