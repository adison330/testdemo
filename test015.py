#! usr/bin/evn python
a = 1
a = "hello"
a = [1,2,3]
a = [3,2,1]

demo_list = [1,2,3]

print("定义列表后的内存地址 %d" % id(demo_list))
print(demo_list)

demo_list.append(999)
print(demo_list)

demo_list.pop(0)
print(demo_list)

demo_list.remove(2)
print(demo_list)

demo_list[0] = 10
print(demo_list)

print("修改数据后的内存地址 %d" % id(demo_list))

demo_dict = {"name" : "小明"}
print("定义字典后的内存地址为 %d" % id(demo_dict))

demo_dict["age"] = 18
print(demo_dict)

demo_dict.pop("name")
print(demo_dict)

demo_dict["name"] = "老王"
print(demo_dict)

print("修改字典后的内存地址为 %d" % id(demo_dict))