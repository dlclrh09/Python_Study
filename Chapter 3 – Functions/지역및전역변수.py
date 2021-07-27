# 지역변수: 함수 안에서만 선언하는 변수 / 전역 범위에서 사용 불가!
# 전역변수: 어디서는 사용 가능한 변수


# eggs = 31337  # 어디서든 가능한 전역변수


# def spam():
#     eggs = 3  # 지역변수 → 전역변수에 있는 변수 사용 / 이 자리를 벗어나면 X

#     print(eggs)
# 궁금! 지역변수가 왜 필요할까~? 지역변수 안 쓰고 전역변수만 쓰면 편할텐데
# 음.. 다른 함수랑 중복이 되지 않아서 관리가 편한다고 함..


def spam():
    eggs = 99  # 지역변수
    bacon()
    print(eggs)


def bacon():
    ham = 101  # 지역변수
    tomato()
    eggs = 0 # 지역변수

def tomato():
    eggs = 1


spam()
bacon()
