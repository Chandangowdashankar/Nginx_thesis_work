import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Data for each OS
data = {
    'OS': ['ubuntu:latest (ubuntu 24.04)', 'alpine:latest (alpine 3.20.1)', 'debian:latest (debian 12.6)'],
    'UNKNOWN': [0, 0, 0],
    'LOW': [7, 0, 57],
    'MEDIUM': [2, 2, 13],
    'HIGH': [0, 0, 1],
    'CRITICAL': [0, 0, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add a Total column
df['Total'] = df[['UNKNOWN', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL']].sum(axis=1)

# Prepare data for pie chart
fig_pie = px.pie(df, names='OS', values='Total', title='Total Vulnerabilities by OS')

# Prepare data for bar chart
fig_bar = go.Figure()
vulnerability_types = ['UNKNOWN', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL']

for vuln in vulnerability_types:
    fig_bar.add_trace(go.Bar(
        x=df['OS'],
        y=df[vuln],
        name=vuln
    ))

fig_bar.update_layout(
    barmode='stack',
    title='Vulnerabilities by Severity and OS',
    xaxis_title='OS',
    yaxis_title='Count'
)

# Show the charts
fig_pie.show()
fig_bar.show()
