# 1. VARIABLES AND DATA TYPES

age = 19
percentage = 95.5
name = "Gayatri"
is_student = True

print("----- VARIABLES AND DATA TYPES -----")
print("Age:", age)
print("Data Type of age:", type(age))

print("Percentage:", percentage)
print("Data Type of percentage:", type(percentage))

print("Name:", name)
print("Data Type of name:", type(name))

print("Is Student:", is_student)
print("Data Type of is_student:", type(is_student))

# 2. ARITHMETIC OPERATORS

a = 10
b = 3

print("\n----- ARITHMETIC OPERATORS -----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 3. ASSIGNMENT OPERATORS

x = 10

print("\n----- ASSIGNMENT OPERATORS -----")
print("Initial value:", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)

x //= 2
print("x //= 2:", x)

x %= 3
print("x %= 3:", x)

x **= 2
print("x **= 2:", x)

# 4. COMPARISON OPERATORS

p = 10
q = 5

print("\n----- COMPARISON OPERATORS -----")
print("p == q:", p == q)
print("p != q:", p != q)
print("p > q:", p > q)
print("p < q:", p < q)
print("p >= q:", p >= q)
print("p <= q:", p <= q)

# 5. LOGICAL OPERATORS

a = True
b = False

print("\n----- LOGICAL OPERATORS -----")
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# 6. MEMBERSHIP OPERATORS

fruits = ["apple", "banana", "mango"]

print("\n----- MEMBERSHIP OPERATORS -----")
print("'apple' in fruits:", "apple" in fruits)
print("'grapes' in fruits:", "grapes" in fruits)
print("'grapes' not in fruits:", "grapes" not in fruits)

# 7. IDENTITY OPERATORS

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("\n----- IDENTITY OPERATORS -----")
print("x is y:", x is y)
print("x is z:", x is z)
print("x is not z:", x is not z)

# 8. BITWISE OPERATORS

a = 10
b = 4

print("\n----- BITWISE OPERATORS -----")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)
