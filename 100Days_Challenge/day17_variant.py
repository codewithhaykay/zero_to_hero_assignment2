def day17_math_toolkit():
    """This program takes in two integers and return their 
    sum, product, division and multiplication in a dictionary-like format.
    It employs the use of the concept of function inside a function"""
    
    print("=== Day 17: Math Toolkit ===")
    def num(prompt, max_entry=3):
        attempt = 0
        while attempt < max_entry:
            try:
                return float(input(prompt).strip())
            except ValueError:
                attempt += 1
                print(f"You have {max_entry - attempt} attempt(s) left")
        print("You have made too many invalid entries")

    a = num("Enter the first number: ")
    b = num("Enter the second number: ")
    if a is None or b is None:
        return

    print("\nResults:")
    print(f"  Sum:        {a + b}")
    print(f"  Difference: {a - b}")
    print(f"  Product:    {a * b}")
    print("  Quotient:   " + ("undefined (division by zero)" if b == 0 else str(a / b)))

if __name__ == "__main__":
    day17_math_toolkit()


