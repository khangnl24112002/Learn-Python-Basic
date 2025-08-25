name = "Khang"
# print(f"Hello {name}")
# a, b = 3, 5
# print(f"{a} + {b} = {a + b}")

# List
fruits = ['banana', 'apple', 'cherry']

fruits.append('mango')
fruits.remove('apple')
fruits.insert(2, 'zzz')
# print(fruits)

# Dictionary
personal_info = {
    'name': "Khang Nguyen",
    'gender': "male",
    "age": 33,
    "country": "Vietnam",
}

personal_info['name'] = 'Minh Nguyen'
personal_info['email'] = 'khang@gmail.com'
del personal_info['country']

for (key, value) in personal_info.items():
    print(key, value)

# print(personal_info)

# tuple
vector_coordinates = (3.43, 4.55, 0.22, -4.33, 9.11, -6.33)
x, y, z, t, u, v = vector_coordinates
print(vector_coordinates[0])
# print(x, y, z, t, u, v)

# Set
num = {1, 2, 3, 2, 2, 4, 3, 5}
num.add(8)
print(num)
print(4 in num)