a = 'Hello World!'
print(a*6)
print(len(a))
print('Hello' in  a)

print(a[0:5]) # 左闭右开 Hello
print(a[:5]) # 左闭右开 Hello
print(a[6:]) # 左闭右开 Hello

print(a.lower())
print(a.replace('o','Q'))

b = 'How are you?{}'
c = 55 # int
print ( a + b.format(c))