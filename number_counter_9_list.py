def array_count9(nums):
  #Creating the list x as a way to hold all the results the nines variable will store in it
  x = []
  nines = 0
  for i in range(len(nums[:])):
    for k in range(i+1):
      #In this loop the variable nines will be reseted to 0 and the test variable will change to the next word in the sequence.
      nines = 0
      test = str(nums[k])
      for j in range(len(test[:])):
        if '9' in  test[j]:
          nines = nines+1
    x.append(nines)
        
  return x