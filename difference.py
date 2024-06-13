import utime

startdate = utime.localtime(1616861486)
enddate = utime.localtime(1718295086)

longMonth =  [1, 3,5,7,8,10,12]

def howManyDayInTheMonth(year, month):
    i = 0
    day = 30
    while i < len(longMonth):
        if(month == longMonth[i]):
            day = 31
            break
        i+=1
        
    if month == 2:

        if(year%4==0 and year%100!=0 or year%400==0):
            day = 29
        else:
            day = 28
    return day

def differenceDay(d1, d2):
    a = utime.mktime(d2) - utime.mktime(d1)
    return (a / 60 / 60 / 24)
    
def differenceMonthDay(d1, d2):
    d1 = list(d1)
    d2 = list(d2)
    #Quand c'est la même année
    if d2[2] - d1[2] == 0 and d2[0] - d1[0] == 0:
        return ([d2[1] - d1[1], 0])
    elif d2[0] - d1[0] == 0 and d2[1] >= d1[1] and d2[2] > d1[2]:
        return ([d2[1] - d1[1], d2[2] - d1[2]])
    elif d2[0] - d1[0] == 0 and d2[1] == d1[1] + 1 and d2[2] < d1[2]:
        a = utime.mktime(d2) - utime.mktime(d1)
        a =  (a / 60 / 60 / 24)
        return([0, a])
    elif d2[0] - d1[0] == 0 and d2[1] > d1[1]+1 and d2[2] < d1[2]:
        #Nombre de jour restant pour compléter le premier mois
        a = howManyDayInTheMonth(d1[0], d1[1]) - d1[2]
        #nombre de mois
        b = d2[1] - d1[1] - 1
        #nombre de jours du dernier mois
        c = d2[2]
        c = a + c
        return([b, c])
        
    #Quand c'est l'année  d'après
    
    #Quand c'est le même jour (donc on comptera que en mois)
    if d2[2] - d1[2] == 0 and d2[0] == d1[0] + 1:
        a = 12 - d1[1]
        b = d2[1]
        return ([a + b, 0])
    #quand c'est un jour supérieur (ça fera forcément plus qu'un mois)
    elif d2[0] == d1[0] + 1 and d2[2] > d1[2]:
        a = 12 - d1[1]
        b = d2[1]
        c = d2[2] - d1[2]
        return ([a+b, c])
    #Quand c'est un jour inférieur et c'est janvier et décembre (donc -d'un mois)
    elif d2[0] == d1[0] +1 and d1[1] == 12 and d2[1] == 1 and d2[2] < d1[2]:
        a = utime.mktime(d2) - utime.mktime(d1)
        a =  (a / 60 / 60 / 24)
        return([0, a])
    #Quand c'est un jour inférieur autre que janvier-décembre donc pluss d'un mois
    elif d2[0] == d1[0] +1 and d2[2] < d1[2]:
        #Nombre de jour restant pour compléter le premier mois
        a = howManyDayInTheMonth(d1[0], d1[1]) - d1[2]
        #nombre de mois
        b = 12-d1[1]-1+ d2[1]
        #nombre de jours du dernier mois
        c = d2[2]
        c = a + c
        return([b, c])
    
    #quand c'est plus d'1 année après
    if d2[2] - d1[2] == 0 and d2[0] > d1[0] + 1:
        a = 12 - d1[1]
        b = d2[1]
        d = (d2[0] -d1[0] - 1) * 12
        return ([a + b + d, 0])
    elif d2[0] > d1[0] + 1 and d2[2] > d1[2]:
        a = 12 - d1[1]
        b = d2[1]
        d = (d2[0] -d1[0] - 1) * 12
        c = d2[2] - d1[2]
        return ([a+b+d, c])
    elif d2[0] > d1[0] +1 and d2[2] < d1[2]:
        print("caca")
        #Nombre de jour restant pour compléter le premier mois
        a = howManyDayInTheMonth(d1[0], d1[1]) - d1[2]
        #nombre de mois
        b = (12-d1[1]-1+ d2[1]) + ((d2[0] -d1[0] - 1) * 12)
        #nombre de jours du dernier mois
        c = d2[2]
        c = a + c
        return([b, c])
    
    print(d1)
    print(d2)
    

def differenceYearMonthDay(d1, d2):
    a = differenceMonthDay(d1,d2)
    return(a[0] // 12, a[0] % 12, a[1])

def differenceHours(d1,d2):
    a = utime.mktime(d2) - utime.mktime(d1)
    return (a / 60 / 60)


print(differenceMonthDay(startdate, enddate))
