file12 = open("9.12抵达航班.txt",'r',encoding='UTF-8')
file13 = open("9.13抵达航班.txt",'r',encoding='UTF-8')
lines12 = file12.read().splitlines()
lines13 = file13.read().splitlines()
time12 = lines12[3::7]
time13 = lines13[3::7]
dict = {}
for i in time12:
    if dict.__contains__('2019-09-12 '+i):
        dict['2019-09-12 '+i] += 1
    else:
        dict['2019-09-12 '+i] = 1
for i in time13:
    if dict.__contains__('2019-09-13 '+i):
        dict['2019-09-13 '+i] += 1
    else:
        dict['2019-09-13 '+i] = 1      
to = open('航班统计.csv','w',encoding='GBK')  
for i , j in dict.items():
    to.write(i + ',' + str(j) + '\n')