import re

def validate_date_of_birth(date_of_birth):
    """
    Regular expression to validate date of birth in the format YYYY-MM-DD.
    Criteria:
    - YYYY: 4 digits for the year
    - MM: 2 digits for the month (01-12)
    - DD: 2 digits for the day (01-31)
    """
    dob_regex = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(dob_regex, date_of_birth)

def validate_password(password):
    """
    Regular expression to validate password.
    Criteria:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - Does not contain any special characters
    """
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    return re.match(password_regex, password)

def validate_registration(username, email, date_of_birth, password):
    """
    Validate user registration fields and provide specific feedback for invalid fields.
    """
    errors = []
    if len(username) < 3:
        errors.append("Username is too short. It must be at least 3 characters long.")
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        errors.append("Invalid email format.")
    if not validate_date_of_birth(date_of_birth):
        errors.append("Invalid date of birth format. Please use YYYY-MM-DD.")
    if not validate_password(password):
        errors.append("Invalid password format. Password must be at least 8 characters long, "
                      "contain at least one uppercase letter, one lowercase letter, and one digit, "
                      "and should not contain any special characters.")
    
    return errors

# Example usage
username = "user123"
email = "user@example.com"
date_of_birth = "2000-01-01"
password = "Password123"

validation_errors = validate_registration(username, email, date_of_birth, password)
if validation_errors:
    for error in validation_errors:
        print(error)
else:
    print("Registration successful!")
