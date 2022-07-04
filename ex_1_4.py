stoka = '2020-10-24 18:30'
strok1 = stoka.split(' ')
print(strok1)
stroka_1_1 = strok1[0].split('-')
stroka_2_1 = strok1[1].split(':')
print(stroka_1_1)
slovar = {}
slovar['year']= stroka_1_1[0]
slovar['month']= stroka_1_1[1]
slovar['day']= stroka_1_1[2]
slovar['time']=stroka_2_1[0]
slovar['minutes']=stroka_2_1[1]
print(slovar)