# initnum = 19
# age = int(input("나이 :"))

# if initnum < age : 
#     print("성인")
# print("조건 외부 코드")


# weight = int(input('무게 :'))
# if weight < 60 :
#     print("야식 가능")
# if weight > 65 :
#     print("다이어트 시작")
# if weight == 70 :
#     print("70임")
# if weight != 71 :
#     print("71 아니군")


# num01 = int(input("첫번째 정수 입력"))
# num02 = int(input("두번째 정수 입력"))

# print(num01, num02)
# if num01 > num02 :
#     print("%d가 %d보다 큽니다" %(num01, num02))    
# if num01 < num02 :
#     print(f"{num01}가 {num02}보다 작습니다")    
# if num01 == num02 :
#     print(f"{num01}가 {num02}랑 같습니다")   

# print(num01, num02)
# if num01 > num02 :
#     print("%d가 %d보다 큽니다" %(num01, num02))    
# elif num01 < num02 :
#     print(f"{num01}가 {num02}보다 작습니다")    
# else :
#     print(f"{num01}가 {num02}랑 같습니다")   


# money = int(input('현재 얼마만큼의 돈을 가지고 있나요?\n'))
# init = 30000
# if money >= init :
#     print('택시를 탄다')
#     talk = str(input('말할거면 YES, 아니면 NO\n'))
    
#     # print(talk)
#     if talk == "YES":
#         print('대화한다')
#     elif talk == "NO":
#         print('안한다')
# else :
#     print('걸어간다')




# a = input('정수a :')
# b = input('정수b :')
# if a > b :
#     print(a)
# else :
#     print(b)


# weight = int(input('짐의 무게는 얼마입니까? '))
# a = 10
# if weight >= a :
#     weight1 = weight//10
#     b = weight1 * 10000
#     print(f"짐의 무게는 {weight}이며 수수료는 {b}입니다")
# else :
#     print('10kg 미만이라 x')



# num_list = list(range(1,11))
# print(num_list)
# a = int(input('숫자 하나를 입력하세요 '))
# if a in num_list :
#     print(f"입력하신 숫자는 num_list {num_list.index(a)}에 존재 합니다")
# else : 
#     print(f"입력하신 숫자{a}는 num_list에 없습니다")



# a = int(input('정수를 입력하세요 '))
# if a%2 == 0 :
#     print(f"정수 {a}는 짝수입니다")
# else :
#     print(f"정수 {a}는 홀수입니다")


# num = int(input('자연수 하나를 입력하세요 :'))
# # mok, namu = divmod(num,10) #몫 나머지 나오는 같은거임
# mok = num // 10
# namu = num % 10
# if num % (mok+namu) == 0 :
#     print('하사드')
# else :
#     print("아님")



# a = 100
# if a > 10 :
#     print("10 보다 큽니다")
# elif a > 20 :
#     print("20 보다 큽니다")
    

# money = 1005
# if money > 10000 :
#     print("택시")
# elif 2000 < money :
#     print("버스")
# elif 1000 < money :
#     print("킥보드")
# else :
#     print("걸어간다")



a = float(input("당신의 학점을 입력하시오\n"))

if 4.0 <= a <= 4.5 :
    c = "A"
elif 3.0 <= a :
    c = "B"
else :
    c = "F"

print(c)