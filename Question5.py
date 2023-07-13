# Q5. What is Distplot? Using Plotly express, plot a distplot.

# Solution ---

# A distplot is a statistical plot that shows the distribution of a dataset. It is a combination of a histogram and a kernel density estimate (KDE). The histogram shows the frequency of each value in the dataset, and the KDE shows the smoothed distribution of the data.
# Displot is depricated from the plotly library and histogram is also the same like Displot.

import plotly.express as px

df = px.data.iris()

fig = px.histogram(df["petal_length"])

fig.show()
