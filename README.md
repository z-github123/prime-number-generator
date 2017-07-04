# prime-number-generator
can generate a list of 1000 prime numbers!

for number in numberinrangelist:  
  isprime = True  
  divisors = range(2,number)  
  for divisor in divisors:     
    if number%divisor == 0:      
      isprime = False  
  if isprime == True:    
    print number
