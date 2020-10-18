import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1")
