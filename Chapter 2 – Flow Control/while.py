#while True인동안은 계속실행
spam=0
if spam < 5:
    print('hello jenny.')
    spam = spam+1

spam=0
while spam < 5: #spam < 5 조건이 False가 될 때까지 출력
    print('hello world.')
    spam = spam+1
print(spam)