# animal = "강아지"
# name = "꼬미"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3


# print("우리집 " + animal + "의 이름은 " + name + "예요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# 애완동물을 소개해 주세요~


# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")


# print(1+1)
# print(5*2)


# print(2**3) #제곱
# print(5%3) #나머지 구하기
# print(10%3) #나머지 구하기
# print(10//3) #몫을 구하기

# print(10 > 3) #True
# print(4 >= 7) #False
# print(10 < 3) #False
# print(5 <= 5) #True
# print(3 == 3) #같다
# print(4 == 2) #False
# print(3 + 4 == 7) #True

# print(1 != 3) #같지않다
# print(not(1 != 3)) #not은 반대

# print((3 > 0) & (3 < 5)) #and 조건

# print((3 > 0) or (3 < 5)) #둘 중 하나만 트루면 트루나옴
# print((3 > 0) | (3 < 5)) #or와 마찬가지

# print(5 > 4 > 7) #False


# print(2 + 3 * 4) 
# print((2 + 3) * 4)
# number = 2 + 4 * 3
# print(number) 
# number = number + 2
# number += 2
# print(number)
# number *= 2
# number /= 2
# number -= 2
# number %= 2 #퍼센트는 나머지


# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))

# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) #제곱근(루트)


# from random import *

# print(random()) #0.0~1.0 미만의 임의의 값 생성
# print(random() * 10) #0.0~ 10.0미만의 임의의 값 생성
# print(int(random() * 10))
# print(int(random() * 10 ))

# print(randrange(1, 46))
# print(randint(1, 45))



from random import * #파이썬에서 제공하는 랜덤

# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) #0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) #0~10미만의 임의의 값 생성

# print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) #1~10 이하의 임의의 값 생성

# print(int(random()*45)+1) #로또

# print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45)) #1~45 이하의 임의의 값 생성



# sentence = '나는 소년입니다'
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


# jumin = "981030-1234567"
# #성별정보는 7번째에 위치

# #[]는 몇번째 문자를 가져오느냐, 
# #컴퓨터에서는 첫번째 index는 0

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0 ~ 2직전까지, 0,1번 째
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# #맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) #해당글자가 대문자인지 판단
# print(len(python)) #문자 길이
# print(python.replace("Python", "Java"))

# index = python.index("n") #문자의 위치
# print(index)
# index = python.index("n", index + 1)
# print(index)


# print(python.find("Java")) #없으면 -1 반환
# print(python.index("Java")) #Java라는 단어가 없어서 에러

# #find와 index의 차이

# print(python.count("n"))


#-- 문자열 포맷 --

# print("a" + "b")
# print("a" , "b")

#방법 1
# print("나는 %d살입니다" % 20) #d는 정수
# print("나는 %s을 좋아해요." % "파이썬") #s는 문자열
# print("Apple은 %c로 시작해요." % "A") #c는 문자

#방법 2
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파랑", "빨강"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파랑", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파랑", "빨강"))



# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨강"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨강", age = 20))

# #방법 4
# age = 20
# color = "빨강"

# print(f"나는 {age}살이며, {color}색을 좋아해요.")
# #밖의 변수 사용시 f


#탈출문자
#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")

#역슬러시 어떠한 따옴표 -> 문장내에서 따옴표 그대로 나옴
#\\ : 문장 내에서 \
# print("c:\\Users\\")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스 (한글자 삭제)
print("redd\bApple")

#\t : 탭
print("Red\tApple")

#리스트 []

#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)

# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# #한명씩 뒤에서 꺼냄
# # print(subway.pop())
# # print(subway)

# #같은 이름의 사람이 몇명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
# print(subway)

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# # num_list.reverse()
# # print(num_list)

# # #모두 지우기
# # num_list.clear()
# # print(num_list)


# #다양한 자료형 함께 사용
# num_list = [5,4,3,2,1]
# mix_list = ["조세호", 20, True]
# # print(mix_list)

# num_list.extend(mix_list)
# print(num_list)

#####사전#####
#키에 대한 중복이 허용되지 않음

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# 5라는 키가 없어서 오류 후 프로그램 종료
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #Key들만 출력
# print(cabinet.keys())
# #value들만 출력
# print(cabinet.items())
# #쌍으로 출력 
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)
