from itertools import count

multiples_of_three = count(step=3)

for n in multiples_of_three:
    if n > 100:
        print(n)