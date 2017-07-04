
def isprime(number):
  for divisor in range (2, number):
    if number%divisor == 0:
      return False
  return True
    
for number in range(2,1000):
  if isprime (number):
    print number