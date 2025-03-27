a = int(input())
b = int(input())
if(a>=0):
    if((a*b)>109):
        print((a*b)-109)
if(a<=0):
    if((a*b)<109):
        print(109+(a*b))