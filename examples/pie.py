import matplotlib.pyplot as plt
import seaborn as sns
import os

if not os.path.exists("img"):
    os.makedirs("img")

data = [44, 45, 40, 41, 39]
labels = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5']

# declaring exploding pie
explode = [0, 0.1, 0, 0, 0]

# define Seaborn color palette to use
colors = sns.color_palette('bright')

# plotting data on chart
plt.pie(data, labels=labels, colors=colors, explode=explode, autopct='%.0f%%')
plt.savefig("img/pie.svg", format="svg")
# plt.show()
