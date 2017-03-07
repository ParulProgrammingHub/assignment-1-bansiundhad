# enter value in centimetre and convert it to meter and kilometer.
cm=input("enter the value in centimeter :")
m=float(cm/100)
km=float(m/1000)
choice=input("enter 1 to convert in meter and 2 to convert in kilometer")
if choice==1:
    print "the distance in meter is %s"%(m)
elif choice==2:
    print "the distance in kilometer is %s"%km
else:
    print"enter the valid choice"
r=raw_input("press any key to exit")
