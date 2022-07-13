# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# # 100
# 시험 성적을 출력한다.
# # A

n = input()

n = int(n)

if n>=0 and n<=100:
    if n>=90 and n<=100:
        print("A")
    elif n>=80 and n<=89:
        print("B")
    elif n>=70 and n<=79:
        print("C")
    elif n>=60 and n<=69:
        print("D")
    else:
        print("F")