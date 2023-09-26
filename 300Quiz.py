###### 300제



# 125번
# phone_no = input("휴대전화 번호 입력: ")
# num = phone_no.split("-")[0]

# if num == "011":
#     company = "SKT"
# elif num == "016":
#     company = "KT"
# elif num == "019":
#     company = "LGU"
# else :
#     company = "알수없음"

# print("당신은 {0} 사용자입니다.".format(company))


# 126번

# post_num = input("우편번호: ")
# city = post_num[2]
# if city in (0,1,2):
#     print("강북구")


# 126번 : 우편번호 -> 구 출력하기

# 한글 변수 권장 X
# 우편번호 = 0

# postal_code = input("우편번호: ")
# postal_code = postal_code[2]

# if postal_code in ("0", "1", "2"):
#     gu = "강북구"
# elif postal_code in ("4", "5", "6"):
#     gu = "도봉구"
# else:
#     gu = "노원구"

# print(gu)


# 169번
# num = 0
# for i in range(1,11):
#     if i%2 == 1:
#         num += i
#     else:
#         continue

# print("합 : {0}".format(num))


# 220번
# def print_max(a, b, c):
#     max_num = a
#     if b > a:
#         max_num = b
#         if c > b:
#             max_num = c
#     print(max_num)

# print_max(5,12,23)

# def print_max(a,b,c):
#     # return max(a,b,c)
#     max_value = a
#     if b > max_value:
#         max_value = b
#     if c > max_value:
#         max_value = c

#     print(max_value)

# print_max(0,-8,-1)


# 234번
# def pickup_even(items):
#     results = []
#     for i in items:
#         if i%2 == 0:
#             results.append(i)
#     return results
    
# R = pickup_even([3,4,5,6,7,8])
# print(R)

# 리스트 컨프리헨션
# def pickup_even(items):
#     return [i for i in items if i%2 == 0]

# print(pickup_even([3,4,5,6,7,8]))






# 292번
# f = open("C:/Users/SKW/Desktop/매수종목2.txt", 'w')
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()


# 293번
# import csv
# f = open("C:/Users/SKW/Desktop/매수종목.csv", "w", encoding="cp949", newline='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.59])
# writer.writerow(["NAVER", "035420", 55.82])
# f.close()



# 141번
#하나씩 나오기
# list = [100, 200, 300]
# new_list = []
# for i in list:
#     print(i+10)
#리스트로 나오기
# list = [100, 200, 300]
# new_list = []
# for i in list:
#     i += 10
#     new_list.append(i)
# print(new_list)

# 142번
# list = ["김밥", "라면", "튀김"]
# for i in list:
#     print("오늘의 메뉴: {0}".format(i))

# 143번
# list = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in list:
#     print(len(i))

# 151
# list = [3, -20, -3, 44]
# for i in list:
#     if i < 0:
#         print(i)

# list = ["A", "b", "c", "D"]
# for i in list:
#     if i.isupper() == False:
#         print(i)

list = []
for i in range(2002, 2051):
    if i%4 == 2:
        list.append(i)

print(list)









