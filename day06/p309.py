f = None
f = open('text.txt','rt',encoding='UTF-8')
f.seek(3,0)
text = f.read()
print(len(text))
print(text)