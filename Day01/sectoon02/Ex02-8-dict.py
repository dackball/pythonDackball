'''

Dictionary
   Key:value 로 이루어진 쌍으로 데이터 값을 저장하는데 사용
   키값 중 불가
'''

thisdict = {
"brand" : "구찌",
"model" : "g001",
"year" : 2022
}
print(thisdict)

'''
키 이름을 사용하여 참조 할 수 있다
'''

# 값 가져오기
thisdict = {
"brand" : "구찌",
"model" : "g001",
"year" : 2022
}
print(thisdict["brand"])
print(thisdict.get("model"))

# 추가하기
thisdict = {
"brand" : "Foed",
"model" : "Mustang",
"year" : 1984
}

thisdict["color"] = "red"
print(thisdict)
thisdict.update({"bgColor" : "black"})
print(thisdict)

# 변경하기
thisdict["color"] = "yellow"
thisdict.update({"bgColor" : "blue"})
print(thisdict)

# 제거하기
thisdict.pop("model")
print(thisdict)




#  마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)






