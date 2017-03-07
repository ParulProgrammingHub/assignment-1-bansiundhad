#compute the value of n+nn+nnn when input is n+nn+nnn
n=input("enter the value of n :")
nn=str(n)+str(n)
nnn=nn+str(n)
r=n+int(nn)+int(nnn)
print "result is :%d"%r
r=raw_input("press any key tp exit")
