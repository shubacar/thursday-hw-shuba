#reverse integer and print it
#o(1)

def reverse_int(n):
    string = str(n)
    if (string[0] == '-'):
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

reversed_num = reverse_int(51234)
print(reversed_num)