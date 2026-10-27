# Email Validator Using Python

## Description

Email Validator is a simple Python project that checks whether an email address follows a basic, expected format. It identifies common formatting mistakes using Python string methods and conditional statements.

## Features

* Checks whether the email contains exactly one `@` symbol.
* Verifies that the username and domain are not empty.
* Detects consecutive dots (`..`).
* Checks whether the domain contains a dot.
* Identifies common email formatting errors.
* Provides clear validation results.

## Technologies Used

* Python 3
* String Manipulation
* Conditional Statements
* Functions

## How to Run

**Step 1:** Clone this repository or download the project files.

**Step 2:** Open a terminal in the project folder.

**Step 3:** Run the following command:

```bash
python email_validator.py
```

**Step 4:** Enter an email address when prompted.

## Sample Output

```text
Enter your email address: example@gmail.com
Email format looks valid.
```

### Invalid Email Example

```text
Enter your email address: examplegmail.com
Invalid email format.
```

## Learning Outcomes

* Understanding Python functions.
* Working with string methods.
* Using conditional statements.
* Accepting and validating user input.
* Building beginner-friendly Python applications.

## Limitations

This program performs basic email-format validation only. It does not verify whether an email address exists, whether its domain accepts email, or whether the user owns the address.

