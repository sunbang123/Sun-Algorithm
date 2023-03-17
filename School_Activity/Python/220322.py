"""
b = 1;
c = 2;
a = b+c;
print(a);
b = 3;
a = b + c; #a를 재선언해야 해요
print(a);

"""
"""
a = 2;
b = 3;
c = a + b;
print(c);

"""
"""
import calendar

calendar.setfirstweekday(6)
# 첫번째 시작하는 날을 여섯번째로 설정하겠다. SUN이 처음으로 오도록.
# python 에서는 1, 2, 3 순이 아닌 0,1,2 순 이다. 7번째요일 SUN은 weekday(6).
calendar.prmonth(2022, 4)

"""
"""
import turtle; # 거북이가 떠 있는 프로그램을 실행한다.

turtle.bgcolor("lavender");

t=turtle.Turtle() # 거북이 실행을 t로 선언 한다.
t.shape("turtle"); # t의 모양을 거북이로 하겠다.
#t.forward(100); # 거북이를 100만큼 앞으로 가겠다.
t.speed(0);

"""
"""
import turtle

t = turtle.Turtle()

t.shape("turtle")

a=0

while a<6: # 안에 있는 요소를 무한대로 반복합니다.    
# if a<1000으로 하면 무한대로 거북이가 돌고 다른 코드는 실행안됩니다... 낭비!!
    t.fd(100) # forward를 줄여서 fd로 썼어요.
    t.left(60)
    a+=1 # a가 6에 도달할때까지 거북이가 돌아요.

"""
"""
import turtle

t = turtle.Turtle()

t.shape("turtle") # 별다른 명령어를 안적으면 거북이를 중앙으로 위치하게 함.
a = 0
t.penup()

while a < 3:
    t.fd(100)
    t.left(120)
    a += 1

t.pendown()

"""
import turtle

t = turtle.Turtle()

t.shape("turtle")

a = 0

t.penup() # 펜을 들어서 그림을 안그려요.
t.left(180)
t.fd(300)
t.left(180)
t.pendown() # 펜을 다시 내려놔요

while a < 3:
    t.fd(100)
    t.left(120)
    a += 1

t.pendown()
t.penup() # 펜을 들어서 그림을 안그려요.
t.fd(200)
t.pendown() # 펜을 다시 내려놔요

a = 0

while a < 4:
    t.fd(100)
    t.left(90)
    a += 1

t.pendown()
t.penup() # 펜을 들어서 그림을 안그려요.
t.fd(200)
t.pendown() # 펜을 다시 내려놔요

a = 0

while a < 5:
    t.fd(100)
    t.left(72)
    a += 1
