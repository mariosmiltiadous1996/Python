# -*- coding: utf-8 -*-
a,b,c=input()
if a>=b>=c :
 print 'Οι πλευρές με φθίνουσα σειρά μεγέθους είναι: ' ,a,b,c
 Pmax=a
 Pmes=b
 Pmin=c
elif b>=a>=c :
 print 'Οι πλευρές με φθίνουσα σειρά μεγέθους είναι: ' ,b,a,c
 Pmax=b
 Pmes=a
 Pmin=c
elif a>=c>=b :
 print 'Οι πλευρές με φθίνουσα σειρά μεγέθους είναι: ' ,a,c,b
 Pmax=a
 Pmes=c
 Pmin=b
elif b>=c>=a :
 print 'Οι πλευρές με φθίνουσα σειρά μεγέθους είναι: ' ,b,c,a
 Pmax=b
 Pmes=c
 Pmin=a
elif c>=a>=b :
 print 'Οι πλευρές με φθίνουσα σειρά μεγέθους είναι: ' ,c,a,b
 Pmax=c
 Pmes=a
 Pmin=b
else  :
 print 'Οι πλευρές με φθίνουσα σειρά μεγέθους είναι: ' ,c,b,a
 Pmax=c
 Pmes=b
 Pmin=a
if Pmax>Pmes+Pmin :
    print "Δεν ισχύει η τριγωνική ανισότητα"
else :
    print 'Η περίμετρος του τριγώνου είναι: ', Pmax+Pmes+Pmin
    t=(a+b+c)/2.0 
    print 'Το εμβαδόν του τριγώνου είναι: ' ,(t*(t-a)*(t-b)*(t-c))**.5
    if a==b==c :
        print 'Το τρίγωνο είναι ισόπλευρο'
    elif a==b or a==c or b==c :
        print 'Το τρίγωνο είναι ισοσκελές'
    else :
        print 'Το τρίγωνο είναι σκαληνό'
    if Pmax**2==Pmes**2+Pmin**2 :
        print 'To τρίγωνο είναι ορθογώνιο'
    elif Pmax**2>Pmes**2+Pmin**2 :
        print 'To τρίγωνο είναι αμβλυγώνιο'
    else :
        print 'Το τρίγωνο είναι οξυγώνιο'
