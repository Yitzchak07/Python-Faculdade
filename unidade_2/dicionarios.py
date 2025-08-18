dict1 = {}
dict1["nome"] = "Isac"
dict1["idade"] = 18

dict2 = {'nome':'Isac','idade':18}

dict3 = dict([('nome','Isac'),('idade',18)])
dict4 = dict(zip(['nome','idade'],['Isac',18]))

print(dict1 == dict2 == dict3 == dict4)
print(dict1)