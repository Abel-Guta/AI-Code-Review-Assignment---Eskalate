# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
    
    if values is None:
        return 0
    
    total = 0
    count = 0
    
    for v in values:
        # Skip None values
        if v is None:
            continue
        
        # Safely handle type conversion
        try:
            numeric_value = float(v)
            total += numeric_value
            count += 1
        except (TypeError, ValueError):
            # Skip non-numeric values
            continue
    
    # Guard against division by zero
    if count == 0:
        return 0
    
    return total / count
