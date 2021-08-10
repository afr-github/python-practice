import math

# start with any positive int.
# sum the square of its digits
# until it equals 1, if so, it is a happy number, else is not.

class numsq(object):
    def isHappy(self, n):
        def sqsum(num):
            result = 0
            while num > 0:
                r = num % 10
                result = result + math.pow(r,2)
                num = num // 10
            return result
        seen = set()
        while(sqsum(n) not in seen):
            sum1 = sqsum(n)
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1
        return False


number = numsq()
f8 = set()

for num in range(0,100,1):
    if number.isHappy(num) == True:
        f8.add(num)
        if len(f8) > 7:
            break


print(f8)

    
