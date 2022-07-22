#조건문 #1 두 수 비교하기 1330
A,B = map(int,input().split())     #a,b 를 map 함수를 이용해 각각 정수(int)로 분리해서 input()으로 입력을 받겠다.
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")                    # '='으로 하지 않게 조심하자!!

#조건문 #2 시험 성적 9498

score= int(input(""))
if score>=90:
    print("A")
elif 80 <=score <90:
    print("B")
elif 70<=score <80:
    print("C")
elif 60<=score <70:
    print("D")
else:
    print("F")

#조건문 #3 윤년풀이 2753

year = int(input())
if year%4==0 and year%100!=0:            #!= : 같지 않다
    print("1")
elif year%4==0 and year%400==0:          #== :  양쪽값이 같다
    print("1")
else:
    print("0")

#조건문 #3 윤년풀이 2753

year = int(input())
if year%4==0 and year%100!=0:            #!= : 같지 않다
    print("1")
elif year%4==0 and year%400==0:          #== :  양쪽값이 같다
    print("1")
else:
    print("0")

#조건문 #5 알람시계 2884

hour, min = map(int,input().split())   # hour,min = input() .split()
                                       # hour= int(hour) , min = int(min)

if min >= 45:
    print(hour, min-45)
elif hour>0 and min < 45:
    print(hour-1, min+15)
else:
    print(23, min+15)                  #0시 일때 시간 23시로 출력되야함

#조건문 #6  오븐시계 2525

hour, min = map(int, input().split())
time = int(input())

hour+= time // 60   #시간이니까 // (몫), 왼쪽변수에 오른쪽 값을 더하고 결과를 왼쪽 변수에 할당하는것
                    #70분이면 1시간 10분 중 1을 나타내는 것
min+= time % 60     #분이니까 % (나머지)

if min >= 60:       #b는 60이 넘으면 a에 영향, a는 24시를 넘으면 0으로 바꾸면 됨
    hour += 1
    min -= 60

if hour >= 24:
    hour -= 24

print(hour, min)

#조건문 #7 주사위 세개 2480

a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)