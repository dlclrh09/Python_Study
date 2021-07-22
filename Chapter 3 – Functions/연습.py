def spam():
    eggs = 99  # 지역변수
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs2 = 0
    print(ham)


spam()  # spam을 호출하면 우선 지역변수가 생성되고 출력은 안됨! 그리고 아래 bacon 변수가 실행되고 순차적으로 출력함!
bacon()
