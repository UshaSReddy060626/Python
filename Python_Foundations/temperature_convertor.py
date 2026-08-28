choice=input("choose the conversion:\n"
    "1: C-F\n"
    "2: C-K\n"
    "3: F-C\n"
    "4: F-K\n"
    "5: K-C\n"
    "6: K-F\n"
)
temperature = float(input("Enter the temperature: "))
operation = {
    "1": lambda t: (t * 9/5) + 32,
    "2": lambda t: t + 273.15,
    "3": lambda t: (t - 32) * 5/9,
    "4": lambda t: (t - 32) * 5/9 + 273.15,
    "5": lambda t: t - 273.15,
    "6": lambda t: (t - 273.15) * 9/5 + 32
}
units = {
    "1": "°F",
    "2": "K",
    "3": "°C",
    "4": "K",
    "5": "°C",
    "6": "°F"
}

result = operation[choice](temperature)

print(f"Converted temperature:{result:.2f} {units[choice]}")

