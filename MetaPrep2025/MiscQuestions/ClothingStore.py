# A clothing store made a sale of 14 t-shirts of 4 different types.
#
# Knowing that the prices of each type are:
# - Type 1: $21.00 usd
# - Type 2: $27.00 usd
# - Type 3: $32.00 usd
# - Type 4: $31.00 usd
#
# And that the sale was $341.00 in total.
# How many t-shirts of each kind were sold?
#
# https://www.facebook.com/share/p/1D3X78JPbY/

if __name__=="__main__":
    result = [(x,y,z,t)
                for x in range(1,15)\
                for y in range(1,15)\
                for z in range(1,15)\
                for t in range(1,15)\
                if x + y + z + t == 14 and \
                   21*x + 27*y + 32*z + 31*t == 341]
    print(result)
