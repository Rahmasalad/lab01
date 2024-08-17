def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.453592

def feet_to_centimeters(feet):
    """Convert feet to centimeters."""
    return feet * 30.48

def main():
    """Main function to handle user input and conversion."""
    print("Welcome to the Weight and Height Converter!")

    try:
        weight_lbs = float(input("Enter weight in pounds: "))
        height_ft = float(input("Enter height in feet: "))

        weight_kg = pounds_to_kilograms(weight_lbs)
        height_cm = feet_to_centimeters(height_ft)

        print(f"Weight: {weight_kg:.2f} kilograms")
        print(f"Height: {height_cm:.2f} centimeters")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
