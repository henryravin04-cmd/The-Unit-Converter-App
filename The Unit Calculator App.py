def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def menu():
    while True:
        print("\n=====  Unit Converter =====")
        print("1. Kilometers ➝ Miles")
        print("2. Miles ➝ Kilometers")
        print("3. Celsius ➝ Fahrenheit")
        print("4. Fahrenheit ➝ Celsius")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            km = float(input("Enter kilometers: "))
            print(f"✅ {km} km = {km_to_miles(km):.2f} miles")

        elif choice == "2":
            miles = float(input("Enter miles: "))
            print(f"✅ {miles} miles = {miles_to_km(miles):.2f} km")

        elif choice == "3":
            c = float(input("Enter Celsius: "))
            print(f"✅ {c}°C = {celsius_to_fahrenheit(c):.2f}°F")

        elif choice == "4":
            f = float(input("Enter Fahrenheit: "))
            print(f"✅ {f}°F = {fahrenheit_to_celsius(f):.2f}°C")

        elif choice == "5":
            print(" Exiting Unit Converter.")
            break
        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    menu()