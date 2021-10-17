import math 
#cosx=1+0-x**2/2!+0+x**4/4!...=1-x**/2!+x**4/4!-x**6/6!
n=55

def t_cos(x):
    sum=1
    num=1
    den=1
    pow=2
    for i in range(0,n):
        num*=(pow-1)*pow
        den*=(pow-1)*pow
        if pow%4==0:
            sum=(num+x**pow)/den
        else:
            sum=(num-x**pow)/den
        pow+=2
        num=sum*den
    return sum

print(math.cos(3.7))
print(t_cos(3.7))
