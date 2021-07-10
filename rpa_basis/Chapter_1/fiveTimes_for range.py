#정해진 횟수만큼 반복할 수 있음
print('my name is')
for i in range(5): #i=변수
    print('jimme five times('+str(i)+')') #1:5라면 0부터4까지
print('my name is')
i=0
while i<5:
    print('jimme five times('+str(i)+')')
    i=i+1
# #
total=0
for num in range(101):
    total = total + num#0+0부터 010까지
print(total) # 1회차 total = 0, num = 0 / 2회차: num = 1, total = 0 + 1 = 1
# #
for i in range(12, 16):
    print(i) #12부터 16 앞까지 출력

for i in range(0, 10, 2): #최대 3개
    print(i) #0부터 10 앞까지 출력하지만 간격은 2만큼

for i in range(5, -1, -1):
    print(i) #5를 시작으로 -1 뺸만큼 출력하며, -1 앞까지 출력