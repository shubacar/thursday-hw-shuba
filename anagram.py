#anagram. check if both the strings have same characters
#abcde
#dcbea
#o(1)

def find_anagram(str1,str2):
    if len(str1) != len(str2):
        return False

    if sorted(str1)!= sorted(str2):
        return False
    else:
        return True


result=find_anagram('tree45','treu')
print(result)