# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# # 1 2
# 첫째 줄에 A+B를 출력한다.
# # 3

# Memo: input은 입력되는 모든 것을 문자열로 취급한다.
#       split 함수는 매개변수를 기준으로 문자열을 자른다. (없으면 공백)
A, B = input().split()

print(int(A) + int(B))

# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# # 3 2
# 첫째 줄에 A-B를 출력한다.
# # 1

# Memo: input은 입력되는 모든 것을 문자열로 취급한다.
# Memo: split는
A, B = input().split()

print(int(A) - int(B))

# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# # 1 2
# 첫째 줄에 A×B를 출력한다.
# # 2

# Memo: input은 입력되는 모든 것을 문자열로 취급한다.
A, B = input().split()

print(int(A) * int(B))

# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
# # 1 3
# 10-9 이하의 오차를 허용한다는 말은 꼭 소수 9번째 자리까지만 출력하라는 뜻이 아니다.
# # 0.33333333333333333333333333333333

# 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
# # 4 5
# 10-9 이하의 오차를 허용한다는 말은 꼭 소수 9번째 자리까지만 출력하라는 뜻이 아니다.
# # 0.8

A, B = input().split()

print(int(A) / int(B))

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000) # 7 3
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다. 
# # 10
# # 4
# # 21
# # 2
# # 1

A, B = input().split()

A = int(A)
B = int(B)

print(A + B)
print(A - B)
print(A * B)
print(A // B) # 몫 만을 구해주는 연산자(//)
print(A % B)

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# # 5 8 4
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
# # 1
# # 1
# # 0
# # 0

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)