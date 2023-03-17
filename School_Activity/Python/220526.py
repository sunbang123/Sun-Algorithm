# 3자리수 랜덤
# 숫자 1~9까지 사용
# 중복숫자 사용x
#
# 3자리수 입력 받기
# 스트라이크, 볼, 아웃
# 버그 수정

import random as r

random_list = []
while True:
    i = r.randint(1,9)
    if i not in random_list: # 중복된 내용이 없으면
        random_list.append(i)
    if len(random_list) == 3:
        break
random_set = set(random_list)

while True:
    n = int(input("3자리수 입력 : "))
    num_list = list(map(int, str(n)))
    num_set = set(num_list)
    if(n < 100 or n > 1000):
        print("3자리수를 입력하시오.\n\n")
    elif(len(num_set)!=3):
        print("중복하지 않는 세자리수를 입력하세요.\n")
    elif(num_set&{0} == {0}):
        print("입력하는 수는 0을 포함하지 않아야 합니다.\n")
    else:
        break

cnt_strike = 0
for i,j in zip(random_list,num_list):
    if(i == j):
        cnt_strike += 1
cnt_ball = len(random_set&num_set)-cnt_strike
cnt_out = len(num_set-random_set)
print(cnt_strike,"S ",cnt_ball,"B ",cnt_out,"O")
print("정답: ", random_list, "사용자 입력: ", num_list)