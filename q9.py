# enter marks of 5 subject and find mean of 5 subject,calculate percentage.if percentage is less than 35 print fail else print pass.
maths=input("marks obtained in maths :")
mi=input("marks obtained in mi :")
co=input("marks obtained in co :")
dbms=input("marks obtained in dbms :")
py=input("marks obtained in py :")
total=maths + mi + co + dbms + py
avg=total/5.0
print "the mean is :%s"%avg
per=(total*100)/250
if per<=35 :
    print"YOU HAVE FAILD THE EXAM AND YOU HAVE SCORED %s"%per
else:
    print"YOU HAVE PASS THE EXAM AND YOU HAVE SCORED %s"%per
r=raw_input("press any key to exit")
    
    
