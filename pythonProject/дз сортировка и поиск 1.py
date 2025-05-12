import random
def my sort(mass):
    for i in range(len(mass)):
        for i in range(len(mass)):



mass = [random.randint(-10,10) for i in range(10)]
sr_z = sum(mass)/len(mass)
if sr_z < 0:
    my_sort_one(mass)
else:
    my_sort_two(mass)


