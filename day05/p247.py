#filter

def myfilter1(n):
    return n >= 90
def myfilter2(n):
    return n >= 80


score = [90,80,60,100]

for i in filter(myfilter2, score):
        print(i)

# print('----------------------')
# in filter(lambda x: x >= 90, score):
#     print(i)