DicSortNames=[
{"name": "John","age":10},
{"name": "Doe","age":20},
{"name": "Michael","age":15}
]
print("The list printed sorting by age:")
print(sorted(DicSortNames, key=lambda x: x['age']))
print("\r")
