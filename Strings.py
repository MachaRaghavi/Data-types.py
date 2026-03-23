x = 'Raghavi'
y = "Macha"

print(x, y)

# triple quotes for multiple strings
a = """The AI trend is improving day by day"""
print(a)

print(x[2])  # At specific position
print(len(y))  # length of string

# string slicing
print(y[:5])
print(x[3:6])
print(x[2:-5])

# Modifying the strings
z = "Happy days"
print(z.upper())
print(z.lower())
print(z.strip())
print(z.replace("H", "h"))
print(z.split(" "))

# string concatenation
print(x + y)
print(x + " " + y)

c = 19
print(f"{x}:{c}")
