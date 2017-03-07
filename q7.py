# program to calculate third angle using function
angle1=input("enter the 1st angle :")
angle2=input("enter the 2nd angle :")
def thirdangle(angle1,angle2):
    angle=180-(angle1+angle2)
    return angle
print "the third angle is :%s" %thirdangle(angle1,angle2)
r=raw_input("press any key to exit")
