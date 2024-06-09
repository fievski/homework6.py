# Практическое задание по теме: "Словари и множества"
# Словари
my_dict = {'Dima' : 2001, 'Igor' : 1997, 'Dasha' : 2008}
my_dict['Lera'] = 2003
my_dict.update({'Kira' : 1989, 'Aurora' : 1999})
print(my_dict.get('Dasha'))
print(my_dict.get('Lera'))
print(my_dict)
del my_dict['Lera']
print(my_dict)

# Множества
my_set = {1, 7, 4, 'Строка', True, (0, 5 , 7, 4)}
print(my_set.add(10))
print(my_set.add(11))
print(my_set)
print(my_set.remove(1))
print(my_set)
