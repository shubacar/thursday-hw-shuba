#verify if the string and reverse of the string are equal to each other , then they are palindrome
#o(1)

def is_palindrome(s):
    reversed_string=s[::-1]
    if s == reversed_string:
        return True
    else:
        return False

result=is_palindrome('hannah')
print(result)