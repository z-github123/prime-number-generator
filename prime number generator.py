
numberinrangelist = range(2,100)

for number in numberinrangelist:
  isprime = True
  divisors = range(2,number)
  for divisor in divisors: 
    if number%divisor == 0:
      isprime = False
  if isprime == True:
    print number
      
      
raw_input()
