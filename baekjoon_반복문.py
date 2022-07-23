#반복문 1 구구단 2739
n=int(input())
for i in range(1,10):
    print(n,'*',i,'=',n*i)

n=int(input())
i=int()
for i in range(0,9): #숫자니까 0부터 시작해서 9까지
    i=i+1
    print(n,'*',i,'=',n*i)

#반복문 2 A+B-3 10950
n=int(input())         #반복할 테스트 케이스 n개 주어짐
for i in range(n):     #받은 케이스만큼 반복해주기
    a,b=map(int,input().split())  #각 테스트 케이스마다 입력받은 a,b
    print(a+b)

#반복문3 합 8393
a=int(input())  #테스트 케이스 a개 주어짐
sum=0
for i in range (a+1):
    sum+=1
print(sum)
#
n=int(input())
for i in range(0,n):
    n+=1
print(n)
#반복문 4 빠른 A+B 15552
#import sys
t=int(input().rstrip())  # input 대신 sys.stdin.readline.rstrip() #rstrip: 공백제거
for i in range(t):
    a,b=map(int,input().split())  #input = sys.stdin.readline.rstrip()
    print(a+b)
#sys.stdin.readline()사용: 시간이 더 빠르다

#반복문 5 N찍기 2741
n=int(input())
for i in range(1,n+1): #i:for문에서 하나씩 증가될 변수 ,i의 범위는 1부터 n까지
    print(i)

n=int(input())
for i in range(n):
    print(i+1)

#반복문 6 기찍 N 2742
n=int(input())
for i in range(n):   #i는 변화하는 변수(얼만큼 변하는가)
    print(n-i)
#반복문 7 A+B-7 11021
n=int(input())
for i in range(1, n+1):
     a, b = map(int, input().split())
     print("Case #" , str(i) , ":", a + b)   #print 하는 위치 조심하자!!tab!!

#반복문 8 A+B-8  11022
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    print("Case #" , str(i) , ":" ,a, "+" ,b, "=", a+b)  #print 하는 위치 조심!
#반복문 9 별 찍기-1  2438
n=int(input())
for i in range(1,n+1):
    print('*'*i)  #'*': 반복하는 것

#반복문 10 별 찍기-2  2439
n=int(input())       #n번 반복
for i in range (1,n+1):  #i는 변화하는 변수
    print(''*(n-i),'*'*i)

#반복문 11 X보다 작은 수 10871
n,x=map(int,input().split())        # n= 총 입력할 개수
a=list(map(int,input().split()))    #수열은 정수형으로 list 만들어서 저장
for i in range(n):
    if a[i]<x:
        print(a[i],end='')       #end='': 현재 출력값과 다음 출력값을 이어주는 역할,
                                 #같은 줄에 바로 뒤에 출력하기 위해서 사용
                                 #자동으로 개행하지 못하게 출력하는 것
#반복문 12 A+B-5  10952
while True:
    a,b=map(int,input().split())
    if(a==0 and b==0):
        break
    else:
        print(a+b)

#반복문 13 A+B-4  10951
while True:       #반복 횟수 제한이 없다!!!
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        exit()

#반복문 14 더하기 사이클  1110
n=int(input())      #입력받을 수
num=n                #n아라는 변수에 num 선언: num은 돌고 돌아올 n과 같은수
i=0                  #i번 동안 반복 = 사이클 길이
while True:
    a = num // 10        # 2 (십의 자리)
    b = num % 10        # 6  (일의 자리)
    c = (a + b) % 10    # 8
    num = (b * 10) + c  # 68
    i=i+1
    if(num==n):
        break
print(i)

