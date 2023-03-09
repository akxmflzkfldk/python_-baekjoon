1차원 배열 #1 최소, 최대 10818

a = int(input())                       #정수의 개수 입력 받기
num= list(map(int, input().split()))   #정수 입력, 'input().split()'로 공백 구분
print(min(num),max(num))

#sort 함수 사용

n = int(input())

array = list(map(int, input().split()))
array.sort()    
print(array[0],array[-1])         #array[0] :최소값 array[-1](= array[n-1]) : 최대값

#.sort()함수 : 오름차순- 디폴트값  .sort(reverse=False) : 오름차순 .sort(reverse=True) : 내림차순
```

a = int(input())                       #정수의 개수 입력 받기
num= list(map(int, input().split()))   #정수 입력, 'input().split()'로 공백 구분
print(min(num),max(num))

#sort 함수 사용

n = int(input())

array = list(map(int, input().split()))
array.sort()    
print(array[0],array[-1])         #array[0] :최소값 array[-1](= array[n-1]) : 최대값

#.sort()함수 : 오름차순- 디폴트값  .sort(reverse=False) : 오름차순 / .sort(reverse=True) : 내림차순

1차원 배열 #2 최댓값 2562

list = []                     # 숫자를 넣는 공간
for i in range(9):            #for문으로 9번 반복(첫번째 줄 부터 아홉 번째 줄까지 한줄에 하나의 자연수 입력)
    list.append(int(input())) # 숫자를 입력
print(max(list))
print(list.index(max(list))+1)   #위치 찾기(index는 0부터 시작하니까 +1)

#index()함수 : 배열이나 문자열에서 특정값의 위치를 찾아준다.

#
A = list()
for i in range(9):
    A.append(int(input()))

print(max(A))
print(A.index(max(A))+1)


1차원 배열 #3 숫자의 개수 2577

a=int(input())  #150
b=int(input())  #266
c=int(input())  #427
result=list(str(a*b*c))  #[1,7,0,3,7,3,0,0] 

for i in range(10):    #i = 0~9
    print(result.count(str(i)))  #i를 문자열(str)로 바꿔서 몇 개인지 count

#str은 list로 변형해주면 각각의 index로 저장됨(문자열로 바꾸기)
#정수(int)를 문자열 (str)로 바꾼 뒤 list함수 이용해서 리스트화
#count 함수를 사용하기 위해서 정수 (int)가 아닌 문자열 (str)로 바꾼 뒤 출력


1차원 배열 #3 숫자의 개수 2577

a=int(input())  #150
b=int(input())  #266
c=int(input())  #427
result=list(str(a*b*c))  #[1,7,0,3,7,3,0,0] 

for i in range(10):    #i = 0~9
    print(result.count(str(i)))  #i를 문자열(str)로 바꿔서 몇 개인지 count

#str은 list로 변형해주면 각각의 index로 저장됨(문자열로 바꾸기)
#정수(int)를 문자열 (str)로 바꾼 뒤 list함수 이용해서 리스트화
#count 함수를 사용하기 위해서 정수 (int)가 아닌 문자열 (str)로 바꾼 뒤 출력


1차원 배열 #5 평균  1546

subject = int(input())                      #과목 수
scores = list(map(int, input().split()))
max_score= max(scores)

new_score=[]                                #list의 변수 이름: 새로운 빈 리스트를 만들기
for score in scores:
    new_score.append(score/max_score*100)   #빈 리스트에 .append로 새로운 점수 생성
print(sum(new_score) /subject)

1차원 배열 #5 평균  1546

subject = int(input())                      #과목 수
scores = list(map(int, input().split()))
max_score= max(scores)

new_score=[]                                #list의 변수 이름: 새로운 빈 리스트를 만들기
for score in scores:
    new_score.append(score/max_score*100)   #빈 리스트에 .append로 새로운 점수 생성
print(sum(new_score) /subject)

1차원 배열 #5 평균  1546

subject = int(input())                      #과목 수
scores = list(map(int, input().split()))
max_score= max(scores)

new_score=[]                                #list의 변수 이름: 새로운 빈 리스트를 만들기
for score in scores:
    new_score.append(score/max_score*100)   #빈 리스트에 .append로 새로운 점수 생성
print(sum(new_score) /subject)

