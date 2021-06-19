x=1
y=2
a=5
z = x / y 
# print(z)

my_dogs = "jesse, amy"
# print(my_dogs)

# print("hello world")
# print("hello world 2")
# print("hello \n world 2")
# print("hello \t world 2")
# print(len('hello '))

mystring = 'hello jesses world'
# print(mystring)
# print(mystring[0])
# print(mystring[2])
# print(mystring[-2])
# print(mystring[6])
# print(mystring[6:])
# print(mystring[6:11])

mystring2 = '0123456789'
# print(mystring2[::3])
# print(mystring2[::2])


# string cancatenation
name = "sam"
last_letters = name[1:]
# print(last_letters)
# print('P' + last_letters)

# using uppercase method
x = 'heLLo World'
# print(x.upper()) # HELLO WORLD
# print(x.lower()) # hello world
# print(x.split('e')) # ['h', 'LLo World']

# print('This is a string {}'.format('INSERTED'))
# print('The {2} {1} {0}' .format('fox','brown','quick'))
# print('The {0} {0} {0}' .format('fox','brown','quick'))
# print('The {q} {b} {f}' .format(f='fox', b='brown', q='quick'))
# print('The {q} {q} {q}' .format(f='fox', b='brown', q='quick'))

result=1.0246879
# print("the result is {r:1.2f}" .format(r=result)) # the result is 1.02
# print("the result is {r:10.2f}" .format(r=result)) # the result is       1.02

name = 'jesse'
age = 27
# print('hello, his name is {}'.format(name)) # old way
# print(f'hello, his name is {name}') # new python 3.6
# print(f'His name is {name} and he is {age} years old')


# my_list = [1,2,3]
# print(len(my_list))
# new_list = ['one', 'two', 'three']
# print(my_list + new_list)
# new_list.append('four')
# print(my_list + new_list)
# new_list.pop()
# print(my_list + new_list)
# new_list.pop(0)
# print(my_list + new_list)


letter_list = ['a','e','c','b','d']
num_list = [4,2,3,7,9]

# letter_list.sort()
# print(letter_list)
# num_list.sort()
# print(num_list)



# dictionaries
my_dict = {
 'key1':'value1',
 'key2':'value2',
}
# print(my_dict['key1'])

prices = {
 'apples': 1.99,
 'oranges': 2.06,
 'peaches': 2.50,
 'bananas': 0.59,
 'grapes': 1.39,
 'nuts': 4.99,
}

# print(prices['apples'])

d = {
 'k1':[1,2,3],
 'k2':['hello world'],
 'k3':{
   'kk1':1.99,
   'kk2':2.99,
   'kk3':[1,2,3,4,5,6]
   },
 'k4':['apple','milk','cheese']}
# print(d['k1'])
# print(d['k1'][0])
# print(d['k3']['kk3'][-1])

# print(d.keys())
# print(d.values())