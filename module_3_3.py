def print_params(a=1, b='note', c=True):
    print(a, b, c)


print_params(69, 'death', False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [24, 'Naruto', [1, 2]]
values_dict = {'a': 1, 'b': 'note', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Sasuke']
print_params(*values_list_2, 42)
