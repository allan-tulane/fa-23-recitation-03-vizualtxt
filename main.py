"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # just converts the result from a BinaryNumber to an int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):

    # set base case
    if x.decimal_val <= 1 and y.decimal_val <= 1:
      return BinaryNumber(x.decimal_val * y.decimal_val)
      
    else:
      # create and pad binary vectors from x and y
      xVec = x.binary_vec
      yVec = y.binary_vec
      xVec, yVec = pad(xVec, yVec)
      
      # split vector and set n
      x_left, x_right = split_number(xVec)
      y_left, y_right = split_number(yVec)
      
      n = len(xVec)

      # multiplication and recursion
      term1 = bit_shift(_quadratic_multiply(x_left, y_left), n).decimal_val
      term2 = bit_shift(_quadratic_multiply(x_left, y_right), n//2).decimal_val
      term3 = bit_shift(_quadratic_multiply(x_right, y_left), n//2).decimal_val
      term4 = _quadratic_multiply(x_right, y_right).decimal_val
      
      return BinaryNumber(term1 + term2 + term3 + term4)
  
    pass
    ###
    
def test_quadratic_multiply(x, y, f):
  
    start = time.time()
  
    # multiply two numbers x, y using function f
    f(BinaryNumber(x), BinaryNumber(y))
  
    return (time.time() - start)*1000

print(test_quadratic_multiply(2, 10, quadratic_multiply))
print(test_quadratic_multiply(2, 10000, quadratic_multiply))
print(test_quadratic_multiply(2000, 1000, quadratic_multiply))
