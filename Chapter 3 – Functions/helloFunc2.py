def hello(name):  # hello 함수 안에 name 이라는 파리미터 지정
    print('hello ' + name)


hello('alice')  # ←매개변수 문자열 'alice'가 피라미터(name)를 받으면서 hello+alice 출력
hello('bob')  # ←매개변수가 문자열 'bob'이 피라미터를(name) 받으면서 hello+bob 출력


def hello2(name):  # hello 함수 안에 name 이라는 파리미터 지정
    print('hello ' + name)


hello2('bob')
print(name) # < 이렇게 하면 출력 오류가 남! 왜? name이 파라미터 bob으로 받으면서 name 변수가 없어짐