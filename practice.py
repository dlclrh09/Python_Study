# print(5)
# print(-10)
# print(3.14)
# print(1000) 
# print(5+3)
# print(2*8)
# print(3*(3+1))
# print('픙선')
# print("나비")
# print("ㅋ"*9)
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not (5>10))
# #강아지 소개할게요
# # animal="강아지"
# # name="노을"
# # age=4
# # hobby="낮잠"
# # is_adult=age>=3

# print("우리집" + animal+"의 이름은"+name+"예요")
# hobby = "공놀이"
# print(name+"는" , age, "살이며" +hobby+ "을 아주 좋아해요")
# #print(name+"는" + str(age)+"살이며" +hobby+ "을 아주 좋아해요")
# print(name + "는 어른일까요?"+ str(is_adult))
# #하유미
# print("하유미")
# ''' 이렇게
# 하면
# 여러문장이
# 주석처리 
# 됩니다'''

# # ㅋ
# # ㅋ
# # ㅋ
# # ㅋ


# #왼쪽정렬 {0:<}
# #오른쪽정렬 {0:>}
# #가운데정렬 {{0:^}

# station = "사당"
# station1 = "신도림"
# station2 = "인청공항"
# print(station  +  station1  +  station2 +"행 열차가 들어오고 있습니다.")
# print(station + "행 열차가 들어오고 있습니다.")



# print(1+1)
# print(3-2)
# print(6/3) # 2 
# print(2**3)
# print(5%3)
# print(10%3)
# print(5//3)
# print(10//3)
# print(4 >=7)
# print(3==3) #True
# print(1 !=3) #!= 는 앞뒤가 같지 않다는 뜻
# print(not(1 !=3))
# print(6//3)
# print((3>0 or 3>5))
# print(abs(-5))
# print(pow(4,2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))
# from random import *

# print(random())
# print(random()*10)
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10)) # 0~10 미만의 임의의 값
# print(int(random()*10)+1) # 1~10 미만의 임의의



# # for i in range(1,11,2): #1,3,5,7,9
# #     print('{0:^10}' .format("◆"*i)) # 가운데 정렬 / 그 숫자가 < 10일 경우 format으로 다이아*i값 명령
# # for i in range(9,0,-2): #9,7,5,3,1
# #     print('{0:^10}' .format("◆"*i)) # 가운데 정렬 /그 숫자가 < 10일 경우 format으로 다이아*i값 명령


# # print("ㅋㅋㅋㅋㅋ 애기야 숙제 끝났다")
# # print("ㅋ"*9)

# # diamond= int(input("diamond는 몇 줄?"))
# # for i in range(1,diamond,2) :
# #     print('{0:^10}' .format("◆"*i))
# # for i in range(diamond-1,0,-2) :
# #     print('{0:^10}' .format("◆"*i))

# # diamond= int(input("diamond는 몇 줄?"))
# # for i in range(1,diamond,2) :
# #     print(""  , "◆"*(2*i-1))

# #*
# # star= int(input("좌측별은 몇 줄?"))
# # for i in range(1, star+1) :
# #     for n in range(i) :
# #         print("*", end="")
# #     print("")

# # star= int(input("우측별은 몇 줄?")) #5
# # for i in range(1, star+1) : # i는 1,2,3,4까지 반복
# #     print(" "*(star-i)+"*"*i) #star가 5일 때 
# # print("")

# # star= int(input("가운데별은 몇 줄?"))
# # for i in range(1, star+1) :
# #     print(" "*(star-i)+"*"*i+"*"*(i-1))
# # print("")

# # dia= int(input("dia는 몇 줄?")) 
# # for i in range(1, dia+1) :
# #     print(" "*(dia-i)+"◆"*i+"◆"*(i-1))
# # for n in range(dia-1,0,-1): #star-1부터 1까지 1씩 감소
# #     print(" "*(dia-n)+"◆"*n+"◆"*(n-1))
# # print("")

# #2020.11.08_Sun
# HAYUMI = "MY NAME IS YUMI"
# print(HAYUMI.lower()) #소문자 변환
# print(HAYUMI.upper()) #대문자 변환
# print(HAYUMI[0].isupper()) #0=1번째가 대문자?
# print(HAYUMI[0].islower()) #0=1번째가 소문자?
# print(len(HAYUMI)) #len
# print(HAYUMI.replace("YUMI", "Cami")) #replace 원하는 글자 변환

# #문자열 처리 함수
# index = HAYUMI.index("I") #index라는 변수를 만들고, hayumi의 변수 값에서 "문자"를 몇번 째에 있는지 찾는 것
# print(index)
# index = HAYUMI.index("I",index+1) #앞에서 찾은 위치 다음 I부터 찾기 / 위에 INDEX=5, +1이니깐 6번째 찾기
# print(index)
# print(HAYUMI.find("g")) #원하는 값이 변수에 없으면 -1로 반환 
# # print(HAYUMI.index("g")) #원하는 값이 변수에 없으면 오류
# print(HAYUMI.count("I")) # hayumi 라는 변수에서 i가 몇번 나오는지 카운트

# 문자열 포맷
# 방법1
# print("나는 %d살입니다." % 20) #%d d는 -> 정수값 / 문장 뒤 %넣고 원하는 정수값
# print("나는 %s를 좋아합니다." %"고양이") #%s s(string)는 -> 문장 뒤 %넣고 원하는 문자열 
# print("Apple은 %c로 시작합니다." %"A") #%c c(character)는 -> 문자 (한글씩)
# print("나는 %s와 %s를 좋아합니다." %("고양이", "강아지")) #%s s는 -> 문자열 
# # %d대신 %s로 가능! 

# 방법2
# print("나는 {}살입니다." .format(20))
# print("나는 {}와 {}를 좋아합니다." .format("강아지","고양이"))
# print("나는 {0}와 {1}를 좋아합니다." .format("강아지","고양이")) #중괄호 {0}, {1} 0번째, 1번째
# print("나는 {1}와 {0}를 좋아합니다." .format("강아지","고양이")) #중괄호 {1}, {0} 순서 응용 / 순번에 맞게 

# 방법3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="blue")) #age=20 / color=blue 변수처럼 format에 넣기
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color="blue", age=20))

# 방법4
# 변수 먼저 만들기
# age=20
# color="blue"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") #문장 앞 f

# 탈출문자
#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타") #두줄로 출력하고 싶을 때, \n

# \",\' 는 문장 내에서 따옴표 ("") ('') 로 해석 가능
# 나는 "하윰"
print("나는 \"하윰\" 입니다.") # 큰따옴표 앞에 \ 넣어주기
print("나는 \'하윰\' 입니다.") # 작은따옴표 앞에 \ 넣어주기

#\\ : 문장 내에서 \ 하나로 변경
print("C:\\Users\\gkdbal\Desktop\\ PythonWorkspace>") #문장에 역\있을 때, 더블\로 처리

#\r : 커서 맨 앞으로 이동
print("red apple\rpine")  #red 자리에 pine으로 변경

#\b : 백스페이스 역할(앞글자 지우기) 
print("진진\b혁")

#\t : tab 키 (4칸 혹은 8칸씩 이동)
print("yu\tmi")

#퀴즈#
 # Q) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
 # http://naver.com
 #규칙1 :http:// 부분은 제외 > naver.com
 #규칙2 : 처음 만나는 점(.) 이후 부분은 제외 >naver
 #규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 +"!" 구성
#예) 생성된 비밀번호: nav51!

#변수만들기
index="http://naver.com"
#index 변수 슬라이싱 하기 위해 다른 변수 만들기
url=index.replace("http://","")
print(url)
# ur=url[:url.index(".")] #슬라이싱, 주민등록번호 한거 
url=url[:5] #슬라이싱, 주민등록번호 한거 
print(url)
password = url[0:3] + str(len(url))+ str(url.count("i")) + "!" # 문자열이라 앞에 str로 묶어줌
print(password)
print("{}의 비밀번호는 {}입니다.".format(index, password))
