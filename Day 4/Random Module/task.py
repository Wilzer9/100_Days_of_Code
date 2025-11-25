import random


ram = random.randint(1, 10) #Gera numeros aleratorios
print(ram)


random_number_0_to_1 = random.Random()
print(random_number_0_to_1)

random_float = round(random.uniform(1, 10), 2)
print(random_float)

moeda = random.randint(1, 2)

if moeda == 1:
    print("Heads")
else:
    print("Tails")
