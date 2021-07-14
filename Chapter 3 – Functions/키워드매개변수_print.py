# random.randint(1,10) ≠ random.randint(10,1)
# 키워드 매개변수는 print() end / sep 매개변수 끝, 사이 어떤 것이 출력돠는지 알려줌

# print('hello')
# print('bye')
# 두 줄로 출력

print('hello', '',  end='is')  # end='' 줄바꿈 // 문자의 끝을 조작
print('', 'bye')
# 출력결과물: hello is bye


print('hello', 'bye',  sep=',')  # sep='' 띄어쓰기 // 각 인자들을 분리 separate
# 출력결과물: hello,bye
# 내가 sep='' 사이에 콤마를 넣어서 hello, bye 두 인자 사이에 콤바로 분리됨

# ★예제★
print('저의 이름은 무엇을까요?', '', end='')
print('제니', '입니다.', sep=' ')
# 출력결과물: 저의 이름은 무엇을까요? 제니 입니다.
