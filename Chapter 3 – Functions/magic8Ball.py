# x = 'hello'
# print(len(x))  # len: 5 → 이런게 반환값

# 모듈 불러오기 import _______ < 모듈 만들어진 함수

import random


def getAnswer(answerNumber):  # return은 한번 실행되면 끝~
    if answerNumber == 1:  # answerNumber 값이 1이면 retutn 값 'It is certain' 하고 끝
        return 'It is certain'  # 이건 확실해
    elif answerNumber == 2:  # answerNumber 값이 1이 아니고 2면 return 'It is decidedly so' 끝
        return 'It is decidedly so'  # 이거 확실해 그래
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'  # 답 다시!
    elif answerNumber == 5:
        return 'Ask again later'  # 조금 이따 다시 물어보자
    elif answerNumber == 6:
        return 'Concentrate and ask again'  # 집중하고 다시 물어보자
    elif answerNumber == 7:
        return 'My reply is no'  # 내 대답은... no!
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'  # 아주 확실해


# r = random.randint(1, 9)  # 매개변수 1~8 > r임 ?? 
# fortune = getAnswer(r)  # 매개변수 r로 호출됨
# print(fortune)

print(getAnswer(random.randint(1, 9)))  # 위에 세줄을 한번에도 가능
