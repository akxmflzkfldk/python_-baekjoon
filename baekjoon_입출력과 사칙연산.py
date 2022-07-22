#1차원 배열 #5 평균  1546

subject = int(input())                      #과목 수
scores = list(map(int, input().split()))
max_score= max(scores)

new_score=[]                                #list의 변수 이름: 새로운 빈 리스트를 만들기
for score in scores:
    new_score.append(score/max_score*100)   #빈 리스트에 .append로 새로운 점수 생성
print(sum(new_score) /subject)

#입출력과 사칙연산 #10 ??! 10926

print(input() + "??!")       # ","가 아니라 "+"로 해야함


