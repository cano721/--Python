#Dictionary
score = (1,2,3,4,5) #tuple
item = ['item1',1000,1]; #list

item2 = {'name' : 'item1', 'price' : 1000, 'count':1} #dictionary

#print(item2['pri']) 없는걸하면 에러
print(item2.get('pri','empty'))

if 'count' in item2:
    print(item2.get('count') *100)

item2['date'] = '20200105'
del(item2['date'])
print(item2)