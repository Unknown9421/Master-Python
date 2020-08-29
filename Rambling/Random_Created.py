import random
import string
import secrets


def random_name(length):
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for letter in range(length))
    return name


# print(secrets.choice(list(range(1994, 2020))))
#
# print(secrets.randbelow(1000000)/secrets.choice([10000, 100000, 100000000, 100000000]))

# print([{"customer_name": random_name,"financial_statement_year": secrets.choice(list(range(1994, 2020))),"current_ratio": secrets.randbelow(1000000) / secrets.choice([10000, 100000, 100000000, 100000000]),"detect": None } for index in range(50000)])

for i in [{"customer_name": random_name(8),"financial_statement_year": secrets.choice(list(range(1994, 2020))),"current_ratio": secrets.randbelow(1000000) / secrets.choice([10000, 100000, 100000000, 100000000]),"detect": None } for index in range(50000)]:
    print(i)