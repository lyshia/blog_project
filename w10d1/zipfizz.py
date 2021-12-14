for i in range(0, 17): 
  if i  % 3 == 0 and i % 5 == 0:
      print('fizzbuzz')
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)