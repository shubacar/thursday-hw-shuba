#split the string in half and swap them
#find the length of the string and divide by 2
#pass that length as index

def split_strings(str):
    length=len(str) // 2
    str1=str[length:]
    str2=str[0:length]
    print(str1+str2)

split_strings('done')
#odd number --particulars