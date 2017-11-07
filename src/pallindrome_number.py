
# TODO: Find all one digit to 10 digit numbers for which abcd * 4 = dcba

def find_all_palindrome():
    for number in range(1000,10000):
      number=str(number)
      num_rev = int(number[::-1])
      number=int(number)
      if number*4==num_rev:
        return number
x=find_all_palindrome()
print (x)
