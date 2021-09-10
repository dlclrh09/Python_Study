# class Country: #class의 이름은 Country
#     Korea = Country() #인스턴스 = 클래스() 정의 → 인스턴스 생성하기
#     Cuba = Country()
#     Turkey = Country()

# class Country: #class의 이름은 Country
#     def export(self): #메소드 → Export을 할거야!
#         print ("Country exports.") #Country는 exports를 한다!

# Korea = Country()
# Korea.export() #exports 해주세요!

# init, self 알기

# class cafe: #cafe클래스 만든다.
#     coffee=cafe #coffee를 cafe클래스에 넣는다.

# class cafe:
#     def __init__(self): #initialize의 약자 / self는 자기자신을 받는다.
#        print("스타벅스는 coldbrew가 최고입니다.")

# coldbrew = cafe()

# class Cafe:
#     def __init__(self, name: str, taste: str, price: int):  #init 생성자
#         self.name = name #인스턴트 속성
#         self.taste = taste
#         self.price = price

# coldbrew = Cafe("coldbrew","bitter", 5000)
# print(coldbrew.name, coldbrew.taste, coldbrew.price)

# 상속 알기

# class cafe: #부모클래스
#     def __init__(self):
#         print("스타벅스는 coldbrew가 최고입니다.")
#
# class cafe2(cafe): #자식클래스
#     def __init__(self):
#         print("스타벅스는 americano도 맛있습니다.")
#
# americano = cafe2()

# class cafe: #부모클래스
#     def __init__(self):
#         print("스타벅스는 coldbrew가 최고입니다.")
#
# class cafe2(cafe): {} #자식클래스
    # def __init__(self):
    #     super().__init__() #cafe를 상속을 받았기 때문에 부모의 생성자를 호출한다.

americano = cafe2()
