﻿a = 3
for i in range(2001,2101,1):
    m19 = 19*(i % 19)
    m4 = 4*(i % 7)
    m2 = 2*(i % 4)
    v2 = (16+m19) % 30
    v1 = (6*v2+m4+m2) % 7
    p = v1+v2
    d = a + p
    if p>27 :
        print 'Η ημερομηνία του Πάσχα για το ' + str(i) + ' είναι' + str(d-30) + ' Μαίου. '
    else:
        print 'Η ημερομηνία του Πάσχα για το ' + str(i) + ' είναι '   + str(d) + ' Απριλίου. '
