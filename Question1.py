# Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
# scatter plot for age and fare columns in the titanic dataset.

# Solution --- 
import seaborn as sns
import plotly.graph_objects as go
titanic = sns.load_dataset('titanic')
titanic

fig = go.Figure()
fig.add_trace(go.Scatter(x=titanic.age,y = titanic.fare))
fig.show()