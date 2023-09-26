###### IF문

# girl_group = "오마이걸"
# if girl_group == "뉴진스":
#     print("Hype boy")
# elif girl_group == "아이브":
#     print("I am")
# else:
#     print("딱히..")


# input활용

# girl_group = input("어떤 걸그룹 좋아해?")
# if girl_group == "뉴진스":
#     print("Hype boy")
# elif girl_group == "아이브":
#     print("I am")
# else:
#     print("딱히..")


# int와 input활용(숫자형식)

# time = int(input("축제에 걸그룹 몇시에 와?"))
# 24시간 #
# if time >= 22:
#     print("여유 있게 볼 수 있겠다")
# elif time >= 20:
#     print("빨리가면 볼 수 있겠다")
# elif time < 20:
#     print("세미나라서 못 보겠다..")


###### for문 (범위 반복, 변수지정)

# 특별히 어떤 값을 넣을 때
# for waiting_num in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_num))

# 0부터 순차적으로 반복
# for waiting_num in range(7):
#     print("대기번호 : {0}".format(waiting_num))

# 3부터 7을 순차적으로 반복
# for waiting_num in range(3,8):
#     print("대기번호 : {0}".format(waiting_num))

# 변수지정 후에 반복
# starbucks = ["김", "이", "박"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))


###### while문 (어떤 조건이 만족할 때까지 반복)
# customer = "손님"
# index = 5
# while index >= 1:
#     print("{0}, 안으로 안내해드릴게요. {1}팀 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("마감하겠습니다. 죄송합니다.")

# 무한반복
# customer = "손님"
# index = 1
# while True:
#     print("{0}, 안으로 들어오세요. 오늘 방문손님 {1}팀입니다.".format(customer, index))
#     index += 1
# Ctrl + C : 무한루프 중단    

# 조건반복
# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     person = input("손님 성함이 어떻게 되세요?")
#     if person == customer:
#         print("{0}님, 감사합니다!".format(customer))


###### continue 활용
# absent = [3, 7]
# no_book = [13]
# for student in range(1, 21): ## 변수 student 1, 20까지 반복
    # if student in absent: ## 조건을 걸어줘(while이 아님)
    #     continue ## 컨티뉴를 만나게 된다면 아래 문장 실행안하고 스킵
    # elif student in no_book:
    #     print("오늘 수업 여기까지. {0}번은 교무실로 따라와!".format(student))
    #     break ## 브레이크를 만나면 뒤에 뭐가 있던 반복문을 탈출
    # print("{0}번, 일어나서 책 읽어줘".format(student))


###### 한줄 for문 (i같은 변수 지정)
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["심건우", "박랑희", "강민석", "Akti"]
# print(students)
# students = [len(i) for i in students]
# print(students)


###### QUIZ

# from random import *
# cnt = 0
# for customer in range(1,51):
#     time = randrange(5, 51)
#     if time >= 5 and time <=15:
#         print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
#         cnt += 1
#     else :
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
    
# print("총 탑승 승객 : {0} 분".format(cnt))


######로또 퀴즈
# from random import *
# lotto = []

# while len(lotto) < 6:
#     num = randint(1,45)
#     if num not in lotto:
#         lotto.append(num)

# print(lotto)

# from random import *
# my_lotto = [3,6,18,19,26,41]

# while True:
#     lotto = []

#     while len(lotto) < 6:
#         num = randint(1,45)
#         if num not in lotto:
#             lotto.append(num)

#     if len(set(lotto).intersection(my_lotto)) >= 3:
#         print(f"{len(set(lotto).intersection(my_lotto))}개 : 당첨")
#         break
#     else:
#         print(f"{len(set(lotto).intersection(my_lotto))}개 : 낙첨")
