# Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.

# Solution ---
import seaborn as sns
import plotly.graph_objects as go
tips = sns.load_dataset('tips')
print(tips)

fig = go.Figure()
fig.add_trace(go.Box(x=tips.total_bill,y = tips.tip))
fig.show()