def incr_number(test_data):
    test_data[-1] += 1
    for i in reversed(range (1, len(test_data))):
        if test_data[i]!=10:
            break
        test_data[i]=0
        test_data[i-1]+=1

    if test_data[0]==10:
        test_data[0]=1
        test_data.append(0)
    print(test_data)


test_data=[1,0,0]
incr_number(test_data)