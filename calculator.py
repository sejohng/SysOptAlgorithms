def calculate_quotient_and_remainder(a, b):
    """
    Calculate the quotient and remainder of dividing a by b.

    Parameters:
    a (int): The dividend.
    b (int): The divisor.

    Returns:
    tuple: A tuple containing the quotient and remainder.
    """
    if b == 0:
        return "Division by zero is not allowed."

    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Example usage
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

result = calculate_quotient_and_remainder(dividend, divisor)
print("Quotient:", result[0])
print("Remainder:", result[1])
