import random

numbers = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10))
sort = sorted(numbers)
print(f'Os números são: {sort}')
print(f'O Maior número é {sort[0]}')
print(f'O Menor número é {sort[-1]}')
