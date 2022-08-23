#Prompt the user to enter 3 numbers and find the maximum
# a=10, b=15, c=20

a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))
c = int(input("Enter the value for c:"))

def max_three(a,b,c):
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    else:
        return c


max_number = max_three(a,b,c)
print(f"Maximum of the three is {max_number}")