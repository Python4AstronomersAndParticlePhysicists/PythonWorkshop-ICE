# Exercise 1.1
N = 100
new_divisors_list = [[j for j in range(1, i + 1) if i % j == 0] for i in range(1, N + 1)]
print('The two lists are equal: {}'.format(all_divisors_list == new_divisors_list))

# Exercise 2.1
print('The CI for mu is {:.2f} \xb1 {:.2f} with a significance level of {:.0%}'.format(x, m, r))

# Exercise 3.1
s = 'This course is ridiculous. I wish I had not enrolled'
print(''.join(filter(lambda x: x in 'aeiouAEIOU', s)))

# Exercise 5.1
(ex_dict_2['type'] == 'raw' and ex_dict_2['data']) or \
(ex_dict_2['type'] == 'sum' and sum(ex_dict_2['data'])) or None

# Exercise 4.1
init = time.clock()
new_species = ','.join([l[4] for l in iris_lines[1:]])
end = time.clock()
new_comp_time = end - init
print('computation took {:0.8} seconds'.format(end - init))
print('Is it the same? {}'.format(new_species == species))
print('{:0.8} times faster!!!'.format(comp_time/new_comp_time))
