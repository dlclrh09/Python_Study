import random  # random 모듈

for i in range(5):  # 0~4까지 5바로 직전까지 0 1 2 3 4 < 5번 반복
    print(random.randint(1, 10))  # random.randint 모듈 안에 있는 함수
    # 1이상 10이하의 숫자가 random으로 출력됨

# 여러개의 모듈 부르기
# import random, sts, os, math

# from import 문
from random import *  # 전체(*)
for i in range(5):
    print(randint(1, 10))  
#이해하기 쉽게 from random 보다 import 사용

import sys
