def validate_email(email):
    email = email.strip()

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if not local or not domain:
        return False

    if local.startswith(".") or local.endswith("."):
        return False

    if ".." in email:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


email = input("Enter your email address: ")

if validate_email(email):
    print("Email format looks valid.")
else:
    print("Invalid email format.")
```

**Sample output:**

```text
Enter your email address: example@gmail.com
Email format looks valid.
```

**GitHub README description:** A simple email-format validation program built with Python string operations and conditional statements. It checks common formatting mistakes but does not verify whether an email address exists.
