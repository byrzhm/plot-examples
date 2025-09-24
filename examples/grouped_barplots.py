import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

if not os.path.exists("img"):
    os.makedirs("img")

sns.set_theme(style="whitegrid")

filepath = 'data/penguins.csv'
penguins = pd.read_csv(filepath)

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=penguins, kind="bar",
    x="species", y="body_mass_g", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("")

plt.savefig("img/grouped_barplots.svg", format="svg")
# plt.show()