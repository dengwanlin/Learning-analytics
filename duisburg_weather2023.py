#%%
import pandas as pd
import plotly.graph_objects as go
#import plotly.express as px
#%%
data = pd.read_csv('Duisburg_Weather_2023.csv')

print(data.head(2))
#%%
data['time'] = pd.to_datetime(data['time'])
month_list = data['time'].dt.month_name().unique().tolist()
print(f"month_list:{month_list}")
#%%
month_prcp = [0] * len(month_list)
month_tavg = [0] * len(month_list)

grouped = data.groupby(data['time'].dt.month)
for month, group in grouped:
    index = month - 1
    month_prcp[index] = group['prcp'].sum()
    month_tavg[index] = group['tavg'].mean()


month_prcp = [round(x, 2) for x in month_prcp]
month_prcp = [float(i) for i in month_prcp]
month_tavg = [round(x, 2) for x in month_tavg]
month_tavg = [float(i) for i in month_tavg]

print(f"month precipation :{month_prcp}")
print(f"month average temperature :{month_tavg}")
#%%
categories = month_list

fig = go.Figure()


# Add total precipitation data to the radar chart, and set the hover template to display the average temperature and corresponding precipitation information (the average temperature here needs to be obtained from previous data)
fig.add_trace(go.Scatterpolar(
    r=month_prcp,
    theta=categories,
    fill='toself',
    name='Precipitation',
    hovertemplate="Month: %{theta}<br>Precipitation: %{r}mm<br>",
    #customdata=[[tavg] for tavg in month_tavg]
))

#%%
# Add average temperature data to the radar chart, and set the hover template to display the average temperature and corresponding precipitation information.
fig.add_trace(go.Scatterpolar(
    r=month_tavg,
    theta=categories,
    fill='toself',
    name='Average Temperature',
    hovertemplate="month: %{theta}<br>Temperature: %{customdata[0]}°C",
    customdata=[[tavg] for tavg in month_tavg]
))
#%%
# Setting up the radar chart layout
fig.update_layout(
    polar=dict(
        angularaxis=dict(
            ticktext=categories,
            tickvals=list(range(len(categories))),
        ),
        radialaxis=dict(
            visible=True,
            range=[0, max(max(month_prcp), max(month_tavg))]
        )
    ),
    showlegend=True,
    legend=dict(
        #x=1,
        #y=0,
        xanchor='right',
        yanchor='bottom',
        bordercolor="Black",
        borderwidth=0.5,
        title=dict(
            text="Legend",
            font=dict(
                size=12,
                color="Black"
            )
        )
    ),
    title=dict(
        text="Duisburg_weather2023",
        y=0.01,  # Set the title's y position closer to the bottom
        x=0.5,
        xanchor='center',
        yanchor='bottom'
    )
)
#%%
# Add temperature and precipitation scale annotations to the angle axis (month axis)
for i, month in enumerate(month_list):
    fig.add_annotation(
        x=month_list[i],
        y=month_tavg[i],
        text="Temp: {}°C<br>Precip: {}mm".format(month_tavg[i], month_prcp[i]),
        showarrow=False,
        yshift=10,  # Adjust the vertical position according to the actual situation
        font=dict(
            size=10
        )
    )
fig.update_layout(
    width=600,  # Set the width in pixels. You can adjust the value as needed.
    height=600  # Set the height in pixels, which can also be adjusted as needed
)

# Show Radar Chart
fig.show()
#%%
import gc
del fig
gc.collect()
#fig = go.Figure()

# Creating a subgraph
from plotly.subplots import make_subplots
fig = make_subplots(rows = 1, cols = 2, specs = [[{"type": "polar"}, {"type": "polar"}]])

# Add precipitation data to the first radar chart
fig.add_trace(go.Scatterpolar(
    r = month_prcp,
    theta = month_list,
    fill = 'toself',
    name = 'Precipitation',
    hovertemplate="Month: %{theta}<br>Precipitation: %{r}mm<br>",
), row = 1, col = 1)

# Set up the layout for the first radar chart
fig.update_polars(radialaxis = dict(visible = True, range = [0, max(month_prcp)]), angularaxis = dict(ticktext = month_list, tickvals = list(range(len(month_list)))), row = 1, col = 1)

# Add average temperature data to the second radar chart
fig.add_trace(go.Scatterpolar(
    r = month_tavg,
    theta = month_list,
    fill = 'toself',
    name = 'Average Temperature',
    hovertemplate="month: %{theta}<br>Temperature: %{customdata[0]}°C",
    customdata=[[tavg] for tavg in month_tavg]
), row = 1, col = 2)

# Set up the layout for the second radar chart
fig.update_polars(radialaxis = dict(visible = True, range = [0, max(month_tavg)]), angularaxis = dict(ticktext = month_list, tickvals = list(range(len(month_list)))), row = 1, col = 2)

# Update overall layout
fig.update_layout(
    showlegend = True,
    title_text = "Monthly Precipitation and Average Temperature",
    title_x = 0.5,  #
    title_y = 0.05  #
)

fig.show()
#%%
#Now I want to delete the figure and then use other methods to show the data
import gc
del fig
gc.collect()
fig = go.Figure()
#%%
# Create a bar chart
bar_trace = go.Bar(
    x = month_list,
    y = month_prcp,
    name = 'Precipitation',
    marker = dict(color = 'blue')
)
#%%
line_trace = go.Scatter(
    x = month_list,
    y = month_tavg,
    name = 'Average Temperature',
    yaxis = 'y2',  # Specifies to use the second y-axis
    line = dict(color = 'red')
)
#%%
# Set the layout
layout = go.Layout(
    #title = 'Monthly Precipitation and Average Temperature',
    xaxis = dict(title = 'Month'),
    yaxis = dict(title = 'Precipitation'),
    yaxis2 = dict(
        title = 'Average Temperature',
        overlaying = 'y',
        side = 'right'
    ),
    title=dict(
        text="Duisburg_weather2023",
        y=0,  # Set the title's y position closer to the bottom
        x=0.5,

        xanchor='center',
        yanchor='bottom'
    ),
     margin=dict(
        t=50,  # top margin
        b=100  # bottom margin
          )

)
#%%
fig.update_layout(
    width=600,  # Set the width in pixels. You can adjust the value as needed.
    height=600  # Set the height in pixels, which can also be adjusted as needed
)
# Create graphics objects and add tracks
fig = go.Figure(data = [bar_trace, line_trace], layout = layout)
fig.show()