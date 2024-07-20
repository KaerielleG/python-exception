#task1
def main():
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        
        print(f"The temperature in Celsius is: {celsius:.2f}")
    
    except ValueError:
       print("Please enter a valid number for the temperature.")
       
#task2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

#task3
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    except ValueError:
        print("Please enter a valid number for the temperature.")
    else:
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()
    
#task4
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    try:
        
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    except ValueError:
        
        print("Please enter a valid number for the temperature.")
    else:
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")

if __name__ == "__main__":
    main()

       
       