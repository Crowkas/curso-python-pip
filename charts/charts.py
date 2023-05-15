import matplotlib.pyplot as plt
import random

values = 3
values_list = []
for i in range(values):
    while True:
        i = random.randint(1, 100)
        if i not in values_list:
            values_list.append(i)
            break

var_1, var_2, var_3 = values_list

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [var_1, var_2, var_3]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels, autopct='%1.1f%%')
    plt.savefig('pie.png')
    plt.close()
