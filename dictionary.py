dic = {
    "dron":"name",
    "kishor":"surname",
    6023:"dron"
}
print(dic[6023])
info ={"name":"dron","age":20,"Eligible":True}
print(info)
print(info['name'])
print(info.get('name'))
print(info.keys())
print(info.values())
for key in info.keys():
    print(info[key])
print(info.items())