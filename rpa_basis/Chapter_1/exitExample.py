import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.') #프로그램을 멈추기 위해서 input에 exit를 입력

