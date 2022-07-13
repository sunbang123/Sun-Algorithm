# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# # 3 2
# 첫째 줄에 A-B를 출력한다.
# # 1

# Memo: input은 입력되는 모든 것을 문자열로 취급한다.
# Memo: split는
A, B = input().split()

print(int(A) - int(B))