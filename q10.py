# calculate simple interest using function simple_interest(principal,time,rate)
p=int(input("enter the principal amount :"))
t=int(input("enter time in years :"))
r=int(input("enter the interest percenage :"))
def simple_interest(principal,time,rate) :
    interest_value=(principal*time*rate)/100
    return interest_value
print"the simple interest value is :%f"%simple_interest(p,t,r)
print"press any key to exit"
