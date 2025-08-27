def math_toolkit(a, b):
    """This program takes in two integers and return their 
    sum, product, division and multiplication in a dictionary-like format.
    It uses the idea of separation of concerns as in the math_toolkit function 
    handles the calculation, the read_number function handles the input validation
    while the main function handles the result."""
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": (a / b) if b != 0 else None,
    }
def read_number(prompt, maxtries=3):
    """Simple input helper that accepts int or float."""
    tries = 0
    while tries < maxtries:
        num_input = input(prompt).strip()
        try:
            # Try int first to keep nice integers; fall back to float
            return int(num_input) if num_input.isdigit() else float(num_input)
        except ValueError:
            tries += 1
            print(f"You have {maxtries - tries} attempt left")
    print("You have made far tooo many invalid Number of Attempt")
    return None

def main() -> None:
    print("=== Day 17: Math Toolkit ===")
    a = read_number("Enter the first number: ")
    b = read_number("Enter the second number: ")
    if a is None or b is None:
        return

    results = math_toolkit(a, b)
    print("\nResults:")
    print(f"Sum: {results['sum']:10.2f}")
    print(f"Difference: {results['difference']:10.2f}")
    print(f"Product: {results['product']:10.2f}")
    if results["quotient"] is None:
        print("  Quotient:     undefined (division by zero)")
    else:
        print(f"  Quotient: {results['quotient']:10.2f}")

if __name__ == "__main__":
    main()
