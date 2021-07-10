#continue에 도착하는 순간! 다시 while문으로 이동

while True:
    print('who are you?')
    name=input()
    if name != 'joe':
        continue # if이 True면 다시 아래 문장으로 이동
    print('hello, joe. what is the password? (it is s a fish.)')
    password=input()
    if password=='swordfish': #password가 swordfish가 아니면 처음부터
        break
print('access granted')