# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0
    count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            total += order.get("amount", 0)
            count += 1

    if count == 0:
        return 0  # or None, depending on requirements

    return total / count
