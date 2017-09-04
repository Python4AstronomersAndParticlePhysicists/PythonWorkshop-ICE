import numpy as np

numbers = np.random.normal(2, 3, 10000)

print('mean:', np.mean(numbers))
print('std:', np.std(numbers))

mask = np.logical_or(numbers <= -1, numbers >= 5)

print('Outside 1 sigma:', len(numbers[mask]) / len(numbers))

mask = numbers >= 0

print('n>0:', len(numbers[mask]))
print('std, where x > 0:', np.std(numbers[mask]))
