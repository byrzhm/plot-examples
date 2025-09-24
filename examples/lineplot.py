import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

if not os.path.exists("img"):
    os.makedirs("img")

sns.set_theme(style="darkgrid")

filepath = 'data/fmri.csv'
fmri = pd.read_csv(filepath)

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)


plt.savefig("img/lineplot.svg", format="svg")
# plt.show()