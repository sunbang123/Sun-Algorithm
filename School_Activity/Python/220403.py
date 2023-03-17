#복습 (예제 작성) 결과

"I eat %d apples." % 3
'I eat 3 apples.'

"I eat %s apples." % "five"
'I eat five apples.'

number = 3
"I eat %d apples." % number
'I eat 3 apples.'

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

"I have %s apples" % 3
'I have 3 apples'

"rate is %s" % 3.234
'rate is 3.234'

"Error is %d%." % 98
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    "Error is %d%." % 98
ValueError: incomplete format

"Error is %d%%." % 98
'Error is 98%.'

"%10s" % "hi"
'        hi'

"%-10s" % "hi"
'hi        '

"%-10sjane." % 'hi'
'hi        jane.'

"%0.4f" % 3.42134234
'3.4213'

"%10.4f" % 3.42134234
'    3.4213'

"I eat {0} apples".format(3)
'I eat 3 apples'

"I eat {0} apples".format(number)
'I eat 10 apples'

number = 3
"I eat {0} apples".format(number)
'I eat 3 apples'

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day)
'I ate 10 apples. so I was sick for three days.'

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

# 자리 표시자 {: } 내에서 형식 지정 유형을 추가하여 결과 형식을 지정할 수 있습니다.

"{0:>10}".format("hi")
'        hi'

"{0:^10}".format("hi")
'    hi    '

"{0:=^10}".format("hi")
'====hi===='

"{0:!<10}".format("hi")
'hi!!!!!!!!'

y = 3.42134234
"{0:0.4f}".format(y)
'3.4213'

"{0:10.4f}".format(y)
'    3.4213'

"{{ and }}".format()
'{ and }'

name = "홍길동"
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

age=30
f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'

d = {'name':'홍길동','age':30}
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
f"나는 내년이면 {age+1}살이 된다."
'나는 내년이면 31살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# d라는 변수에서 name의 이름을 가진 값을 뽑아내기 위하여 ["name"]이라고 작성한다.
'나의 이름은 홍길동입니다. 나이는 30입니다.'

f'{"hi":<10}'
'hi        '

f'{"hi":>10}'
'        hi'

f'{"hi":^10}'
'    hi    '

f'{"hi":=^10}'
'====hi===='

f'{"hi":!<10}'
'hi!!!!!!!!'

y = 3.42134234
f'{y:0.4f}'
'3.4213'

f'{y:10.4f}'
'    3.4213'

f'{{ and }}'
'{ and }'

a = "hobby"
a.count('b')
2

a = "Python is the best choice"
a.find('b')
14
# a.find('o') 가장 왼쪽에서부터 읽었을때 먼저 나오는 o를 세 준다.

a.find('k')
-1 # 존재하지 않기 때문에!

a = "Life is too short"
a.index('t')
8

a.index('k')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.index('k')
ValueError: substring not found # 존재하지 않기 때문에!

",".join('abcd')
'a,b,c,d'

",".join(['a','b','c','d'])
'a,b,c,d'

a = "hi"
a.upper()
'HI'

a = "HI"
a.lower()
'hi'

a = " hi "
a.lstrip()
'hi '

a = " hi "
a.rstrip()
' hi'

a = " hi "
a.strip()
'hi'

a = "Life is too short"
a.replace("Life", "Your leg")
'Your leg is too short'

a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']
# 스페이스, 탭 엔터를 기준으로 문자를 분할하여 리스트로 만들어 준다.

b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']
# 문자를 ''안의 :를 기준으로 분할하여 리스트로 만들어 준다.
