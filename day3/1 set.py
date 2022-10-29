s01 = {1,2,3,4}
s02 = {1,2,3,1,1,1,13,3}
s03 = {'a', 'b', 'b', 'b', 'c'}

# set_to_list = list(s03)
# set_to_list.sort() # sort = 정령

# print(type(s01), s01)
# print(type(s02), s02)
# print(type(s03), s03)
# print(type(set_to_list), set_to_list)



s1 = {1,2,3,4}
s2 = {3,4,5,6,6}
print("합집합 :", s1|s2)
print("합집합 :", s1.union(s2))
print("교집합 :", s1 & s2)
print("교집합 :", s1.intersection(s2))
print("차집합 :", s1 - s2)
print("차집합 :", s1.difference(s2))
s1.add(11)
print(s1)
s1.update([111,222])
print(s1)
s1.remove(111)
print(s1)
s1.discard(222)
print(s1)

# s3 = set()
# for a in s1:
#     for b in s2:
#         if a == b:
#             s3.add(a)
# print(s3)
