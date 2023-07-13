# Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
# the color parameter.
# Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
# dimensions parameter.

import plotly.express as px
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris)

fig = px.scatter_matrix(data_frame=iris,dimensions=['sepal_length','sepal_width','petal_length','petal_width'],color='species')
fig.show()