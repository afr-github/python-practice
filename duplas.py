#opt.1 

###
# num = [1,2,8,2,1,5,5,0,1,0,7,3]
# count = 0

#for index in range(0,11,1):
#    if num[index] + num[index+1] == 10:
#        count += 1
#print(count)


#opt.2
#num = [1,2,8,2,1,5,5,0,1,0,7,3]
#count2 = 0

#def duplas(a,b) -> int:
#    if a + b == 10:
#        return 1
#    else:
#        return 0

#for index in range(len(num)-1):
#    count2 += duplas(num[index], num[index+1])

#print(count2)



#opt. 3
num = [1,2,8,2,1,5,5,0,1,0,7,3]
a = 0
b = 0 
total = 0

class duplas:
    
    def __init__(self, a, b): 
        self.a = a
        self.b = b
        self.total = 0
        #print("a: {}, b: {}".format(a,b))

    def cantOf10s(self):
        if (self.a + self.b == 10):
            self.total += 1


        return self.total


for i in range(len(num)-1):
    total += duplas(num[i],num[i+1]).cantOf10s()

print(total)