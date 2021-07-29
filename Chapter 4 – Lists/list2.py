#인덱스로 리스트 안의 값 변경
spam=['cat','bat', 'rat', 'elephat']
spam[1]= 'aardvark' # 1번 자리에 aardvark를 할당하라
print(spam)
spam[2]= spam[1] #2번과 1번자리가 같다
spam[-1] = 12345
print(spam)