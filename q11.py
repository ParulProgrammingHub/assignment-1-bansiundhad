# calculate compound interest using function compound_interest(principal,time,rate)
p=int(input("enter the principal amount :"))
t=int(input("enter time in years :"))
r=int(input("enter the interest percenage :"))
def compound_interest(principal,time,rate) :
    x=(1+(rate/100))**time
    interest_value=(principal*x-principal)
    return interest_value
print"the compound interest value is :%f"%compound_interest(p,t,r)
print"press any key to exit"
