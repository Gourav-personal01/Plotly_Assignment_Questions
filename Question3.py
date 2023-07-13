# Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
# the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
# column with the color parameter.

# Solution ---
import plotly.express as px
import plotly.graph_objects as go

tips_df = px.data.tips()

fig = px.histogram(tips_df, x="sex", y="total_bill", color="day", pattern_shape="smoker")

fig.update_layout(
    title="Histogram of Total Bill by Sex",
    xaxis_title="Sex",
    yaxis_title="Total Bill",
    barmode="group",
    legend_title="Day"
)

fig.show()
