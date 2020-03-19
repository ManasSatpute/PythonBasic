dict1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
dict2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}
print({**dict1,**dict2})
dict1.update(dict2)
print(dict1)