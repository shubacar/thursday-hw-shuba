def add_number_digits(n):
    result=0
    while n!=0:
        result = result + n
        n = n - 1
    return(result)


add_dg_reults = add_number_digits(10)
print(f"sum of  numbers is {add_dg_reults}")
