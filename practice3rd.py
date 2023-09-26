######함수


# 함수정의 : def + 함수이름 + 괄호 + 콜론
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else :
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     if balance >= money:
#         print("출금이 완료되었습니다. 수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format((balance - money), (balance - money-commission)))
#         return balance - money, balance - money - commission
#     else :
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
    
# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# balance, commission = withdraw_night(balance, 200)


######기본값


# 입력시 줄바꿈: \후 enter
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "JAVA")

# 같은 학교, 같은 학년, 같은 반 수업. -> 이때 기본 값 사용
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")


######키워드값


# 키워드 = 값을 해도 순서 상관없이 값을 호출할 수 있음
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


######가변인자


# end=" " 문장을 출력하고 이어서 다음 문장출력 *줄바꿈없이*
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 24, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 20, "Python", "", "", "", "")

# 가변인자 사용 시
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 24, "Python", "Java", "C", "C++", "C#", "JAVASCRIPT")
# profile("김태호", 20, "Python")


######지역변수와 전역변수


# 지역변수는 함수 내에서만 쓸 수 있는 것
# 전역변수는 프로그램 어디서든 부를 수 있는 것

# gun = 10

# def checkpoint(soilders): 
#     global gun  ## 전역 공간에 있는 gun 사용(권장사항 X)
#     gun = gun - soilders
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soilders):
#     gun = gun - soilders
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))


######QUIZ


# 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 개인의 키에 적당한 체중

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else :
#         return height * height *21
    
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))


######표준입출력

# print("Python", "Java", sep=" vs ", end="? ") ## 표기로 분리
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "java", file = sys.stdout)
# print("Python", "java", file = sys.stderr)

