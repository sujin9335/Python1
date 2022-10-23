# list_num = [1,2,3,4]
# print(list_num, type(list_num))

# list_word = ["1","2","3","4"]
# print(list_word, type(list_word))

# print(list_num[0], type(list_num[0]))
# print(list_word[0], type(list_word[0]))


# list_ex1 = ['a', "b", "c", [1, 2, 3]]
# print(list_ex1[3])
# number = list_ex1[3]
# print("number : ", number)
# print(number[0]+number[2])


# num = [1, 2, 3, 4, 5]
# print(num[0:2])
# num_sliching = num[2:]
# print(num_sliching)


# list_rage = list(range(1,101,2))
# print(list_rage)

# list_01 = ["A", "B"]
# print(len(list_01))

# word = "python is fun"
# print(len(word))


# list_num = [1, 3, 5, 7, 9, 10]
# print(list_num[2])
# list_num[2] = 3
# print(list_num[2])
# print(list_num)
# list_num[2:] = [10, 20 ,30, 40]
# print(list_num)


# list_num = [1, 3, 5, 1, 1, 10]
# print(list_num.count("1"))
# print(list_num.count(1))

# list_num = list(range(1,11))
# print("삭제전:", list_num)
# list_num[0:1] = []
# print(list_num)
# del list_num[0]
# print("삭제후:", list_num)
# print(list_num)


# list_test = list()
# print(list_test, type(list_test))
# list_test.append("1")
# list_test.append(1) #하나만 넣어짐
# print(list_test)

# list_test.insert(1,1.5)
# print(list_test)

# list_test.extend([5,6,7,6])
# print(list_test)



# list_word = [5, 6, 7, 8, 1, 5]
# # print(list_word.sort()) # None 으로 출력됨
# list_word.reverse()
# print(list_word)

# list_lang = ['banana', 'cat', 'egg', 'apple', 'door']
# # list_lang.sort()
# # list_lang.reverse()
# list_lang.sort(reverse=True)
# print(list_lang)
# print(list_lang.index("egg"))

# print(list_lang.pop(1)) #선택한 위치의 요소를 뺸 값 표시
# print(list_lang)

msg = "I love python"
print(msg.split())
list_msg = msg.split()
print(list_msg)

listTomMsg = " ".join(list_msg) # ""안에 값을 변경하면 추가됨
print(listTomMsg)
listTomMsg = ";".join(list_msg) # ""안에 값을 변경하면 추가됨
print(listTomMsg)

