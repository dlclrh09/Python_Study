def spam():
    print(eggs) #선언된 변수가 없는데 출력이 되다보니 오류가 뜸
    eggs = 'spam local'


eggs = 'global'
spam()

