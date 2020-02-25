from bs4 import BeautifulSoup
import operator
soup = BeautifulSoup(open('size.html','r',encoding='UTF-8'))
x = soup.find_all(text='机型')
x = [i.parent.findNext('p').text.strip() for i in x]
print(len(x))
dict = {}
for i in x:
    if dict.__contains__(i):
        dict[i] += 1
    else:
        dict[i] = 1
print(len(dict))
sorted_dict=sorted(dict.items(),key=operator.itemgetter(1))
to = open('res.csv','w',encoding='UTF-8')
for i,j in sorted_dict:
    to.write(i+','+str(j)+'\n')

