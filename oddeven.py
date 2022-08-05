# get a number and get the number of even and odd digits
def odd_even(n):
    even_numb=0
    odd_numb=0
    while n!=0:
        cur_digit = n % 10
        n=n//10
        if cur_digit % 2:
            odd_numb = odd_numb + 1
        else:
            even_numb = even_numb + 1

    return [even_numb, odd_numb]


results_odd_even= odd_even(32246)
print(f"even number, odd number {results_odd_even}")