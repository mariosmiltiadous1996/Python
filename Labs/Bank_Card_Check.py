# -*- coding: utf-8 -*-
#
a=raw_input()
L=[" ","-"]
while a!="END" or a!="end":
    b=len(a)
    f1=0
    f2=0
    j1=0
    j2=0
    if b==16:
        for i in range(16):
            if a[i].isalpha():
                j1=j1+1
        if j1<>0:
            print False
            a=raw_input()
        if int(a[0])<4 or int(a[0])>7:
            print False
        if int(a[0])==4 or int(a[0])==5 or int(a[0])==6 or int(a[0])==7:
            c=[]
            d=[]
            g=[]
            for i in range(0,15,2):
                c=c+[int(a[i])]
            for i in range(8):
                d=d+[2*c[i]]
            for i in range(8):
                if d[i]>=10:
                    f=d[i]%10+1
                    g=g+[f]
                else:
                    g=g+[d[i]]
            for i in range(8):
                f2=f2+g[i]
            for i in range(1,16,2):
                f1=f1+int(a[i])
            fol=f1+f2
            if fol%10!=0:
                print False
            else:
                print True
    elif b==19:
        j2=0
        if a[4]==L[0] and a[9]==L[0] and a[14]==L[0]:
            print True
            j2=j2+1
        if a[4]==L[1] and a[9]==L[1] and a[14]==L[1]:
            print True
            j2=j2+1
        if j2==0:
            print False
    if b<>16 and b<>19:
        print False
        a=raw_input()
    if a=="END" or a=="end":
        break
        if b<>16 and b<>19:
        print False
    a=raw_input()
    if a=="END" or a=="end":
      break
