my_dict = {'Lyubov': 2000, 'Misha': 1995}
print(my_dict)
print(my_dict['Lyubov'])
print(my_dict.get('Olga'))
print(my_dict)
my_dict.update({'Yuriy':1975,'Lidia':1951})
print(my_dict)
k = my_dict.pop('Lyubov')
print(k)
print(my_dict)

my_set = {7,8,5,9,1,7,8,9}
print(my_set)
print(my_set.add(10))
print(my_set)
print(my_set.add(50))
print(my_set)
print(my_set.discard(50))
print(my_set)