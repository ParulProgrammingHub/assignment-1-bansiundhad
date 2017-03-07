# python program to enter value in days and convert in form of years, monyth and days
n=input("enter the no of days : ")
year=n/360
num=n%360
month=num/360
days=num%360
print "the no of year is : %s"%year
print "the no of month is : %s"%month
print "the no of days is : %s"%days
r=raw_input("press any key to exit")
