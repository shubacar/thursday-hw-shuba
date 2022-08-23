#verify if the string has all unique characters

def verify_unique(strset):
  results={''}
  for x in strset:
    if x not in results:
      results.add(x)


  if len(strset) == len(results) - 1:
    return True
  else:
    return False

ret_result = verify_unique('one')
print(ret_result)
#not unique -street