# class PlayerCharecter:
#     def __init__(self, name):
#         self.name = name

#     def run(self):
#         return self


# player1 = PlayerCharecter('Mike')
# print(player1)
# print(player1.run())
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add nother Cat
# class Garfield(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []
# si = Simon("Simon",2)
# sa = Sally("Sally",4)
# ga = Garfield("Garfield",7)
# my_cats.extend([si,sa,ga])
# #3 Instantiate the Pet class with all your cats use variable my_pets
# pets = Pets(my_cats)
# #4 Output all of the cats walking using the my_pets instance
# pets.walk()

# print(dir(pets))

# class SuperList(list):
#     def __len__(self):
#         counter = 0
#         for i in self:
#             counter +=1
#         return counter

#     def __str__(self):
#         str_item = []
#         for i in self:
#             str_item.append(i)
#         return ' '.join(str_item)

# my_list = SuperList()

# my_list.extend(['1','2','3'])
# print(my_list[0])
# print(len(my_list))
# print(issubclass(SuperList,list))
# print(str(my_list))

# from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def my_cap(item = ''):
#     return item.upper()

# print(list(map(my_cap,my_pets)))

# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
# #my_numbers.sort()
# print(list(zip(my_strings,sorted(my_numbers))))

# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def get_Scores_Above_50(item):
#     if(item > 50):
#         return item
# print(list(filter(get_Scores_Above_50,scores)))
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# def my_accumalator(acc,item):
#     return acc+item
# print(reduce(my_accumalator,scores,0)+reduce(my_accumalator,my_numbers,0))
# print(reduce(my_accumalator,scores,reduce(my_accumalator,my_numbers,0)))
# print(reduce(my_accumalator,(scores+my_numbers)))
# square
# my_list = [5,4,3]

# print(list(map(lambda i:pow(i,2),my_list)))

# #sort the last item tuple
# a = [(0,2),(4,3),(9,9),(10,-1)]
# a.sort(key=lambda i:i[1])
# print(a)

# print([x**2 for x in range(1,99) if x % 2 == 0])

# my_dict = {num:num**2 for num in [1,2,3]}
# print(my_dict)
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# [duplicates.append(li) for li in some_list if some_list.count(li) > 1 and li not in duplicates ]
# print(duplicates)
# decorator pattern
# def my_decorator(func):
#     def wrap_func(*args,**kwargs):
#         print("*" * (len(args[0]) + 6))
#         func(*args,**kwargs)
#         print("*" * (len(args[0]) + 6))
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji ='😋'):
#     print(greeting +  emoji)

# hello("God is good, all the time","😄")

# from time import time
# def performance(fn):
#     def wrapper_fn():
#         t1 = time()
#         fn()
#         t2 = time()
#         print(f"it took {(t2 - t1)} sec")
#     return wrapper_fn

# @performance
# def long_running_fn():
#     for i in range(10000000):
#         i * 5

# long_running_fn()
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': False #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#   def wrap_fn(*args,**kwargs):
#       if args[0]["valid"]:
#         return fn(*args,**kwargs)
#       else:
#         print(f"{args[0]['name']} invalid user access")
#   return wrap_fn


# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)


# def special_for(iterable):
#       iterator = iter(iterable)
#       while True:
#           try:
#             iterator*5
#             next(iterator)
#           except StopIteration:
#             break


# class MyGen:
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#     MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration

# gen = MyGen(1,100)
# for i in gen:
#     print(i)
def fab(n):
    a, b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fab(20):
    print(i, end=' ')    