# +	Addition	x + y	
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / 
# %	Modulus	x % 
# **	Exponentiation	x ** 
# //	Floor division	x // 

# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	

# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	



# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y	

# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#Exercises
print (10 * 5)
#50

print (10 / 2)
#5

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Code working

if 5 != 10:
  print("5 and 10 is not equal")
#Code working

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")