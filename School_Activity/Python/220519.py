# 3자리수 랜덤 출력
# 숫자 1~9까지 사용
# 중복숫자 사용x
# 배열 이용하기
# random 함수를 사용할 수 있도록!
# import random as r - random을 r로 치환해줘요~

import random
import random as r

# 배열 설정
# 배열 안에 배열이 들어가고 형을 신경쓰지 않음...
arr = []

while True:
    i = r.randint(1,9)
    #중복 없애는 함수
    if i not in arr:
        arr.append(i)
    if len(arr) == 3:
        break
print(arr)

# arr[] = random.randint(1,9)
# arr[]에 int가 들어가지 않음!!
