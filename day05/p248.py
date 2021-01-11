#map

def mymap(n):
    return n /3

score = [93,87,65,100]

for i in map(mymap,score):
    print(i)

print('------------')

for i in map(lambda x:x/3,score):
    print(i)