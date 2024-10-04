# utils.py - Utility functions for validating and processing scraped data

import re

def validate_data(data):
    # Patterns for credit card numbers, CVV, usernames, passwords, and emails
    cc_pattern = r'\b(?:\d[ -]*?){13,16}\b'  # Credit card numbers (13-16 digits)
    cvv_pattern = r'\b\d{3,4}\b'  # CVV numbers (3 or 4 digits)
    username_pattern = r'\buser(?:name)?[:\s]*[a-zA-Z0-9_.-]{3,20}\b'  # Username pattern
    password_pattern = r'\bpass(?:word)?[:\s]*[a-zA-Z0-9@#*$%^&+=!?_-]{6,}\b'  # Password pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Email addresses

    sensitive_patterns = [cc_pattern, cvv_pattern, username_pattern, password_pattern, email_pattern]

    # Search for any sensitive pattern
    for pattern in sensitive_patterns:
        if re.search(pattern, data):
            print(f"Sensitive data found matching pattern: {pattern}")
            return True
    return False
