#애완동물을 소개해 주세요!
animal= "강아지"
name="노을이"
age=4 #정수형 자료이기 때문에 따옴표 없음
hobby="산책"
is_adult=age>=5


print("우리집" +animal+"의 이름은 "+ name +"예요")
hobby='공놀이'
#print(name +"는" +str(age)+ "살이며," +hobby+"을 아주 좋아해요") 설명이 필요한 부분에 주석을 사용함 '#'
''' 여러문장 한번에 처리 할 때, 작음 따옴표 3개'''
# 컨트롤+/ 한번에
# print(name,"는" ,age, "살이며," ,hobby,"을 아주 좋아해요") #플러스 대신 콤마 활용 가능하며, str는 제외된다
# print(name +"는 아이일까요?" +str(is_adult))