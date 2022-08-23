str = "This is a sample 'string'"
print ('yy' in str)
str2='yellow character'
print(str2[0])
print(str2[:9])
print(str2[4:])
print(str2[8:-1])

str3='this is a wonderful day'
str4=' nice test'
print(str3+str4)

for c in str4:
    print(c)

length=len(str4)
#print(length)
#print(str3.lower())
#print(str4.upper())

str5=str3.split()
for word in str5:
    if(len(word)>=4):
        print(word)

list_of_words=['This',' is',' a',' list']
joined_string= ''.join(list_of_words)
print(joined_string)

str7='  oranges and lemons '
str8=str7.strip()
print(str7)
print(str8)
replaced_string=str8.replace('o','0')
print(replaced_string)
found_string=replaced_string.find('l')
print(found_string)

str9=('This is a {} formatted string')
str10=str9.format(6)
print(str10)