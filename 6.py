#Q.1-Calculate Area of a Sphere
def sphere(rad):
    area=4*3.14*rad*rad
    print(area)

rad=int(input('Enter Radius:'))
sphere(rad
       )

#Q.2-Prints All the Perfect Numbers Between 1 and 1000

def perfect(num):
    sum=0
    x=1
    while x<num:
        if(num%x==0):
            sum=sum+x
        x+=1
        
    if num!=1 and sum==num:
         print (num)
         
print('The Perfect Numbers are:')
for x in range (1,1000):
    perfect(x)

#Q.3-Print Multiplication Table of a User Defined Number
def multiplication():
    n=int(input('Enter integer:'))
    for i in range(1,11):
        print(n,'x',i,'=',n*i)

multiplication()
    
#Q.4-Calculate Power of a Number Using Recursion
def exponent(base,exp):
    
    if(exp==1):
        return base
    else:
        return base*exponent(base,exp-1)
base=int(input("Enter base: "))
exp=int(input("Enter exponential number: "))
x=exponent(base,exp)
print(x)
