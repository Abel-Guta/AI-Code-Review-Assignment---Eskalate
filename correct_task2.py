# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

def count_valid_emails(emails):
   
    if emails is None:
        return 0
    
    count = 0
  
    email_pattern = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
    
    for email in emails:
        # Skip non-string entries safely
        if not isinstance(email, str):
            continue
        
        # Strip whitespace and validate
        email = email.strip()
        
        if email_pattern.match(email):
            count += 1
    
    return count


