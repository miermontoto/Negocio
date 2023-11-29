# pip install dash
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import seaborn as sns
app = dash.Dash()
df = sns.load_dataset('titanic')
fig = px.scatter(
df,
x="fare",
y="age",
size="pclass",
color="alive",
hover_name="embark_town",
log_x=True,
size_max=60
)
app.layout = html.Div(children = [
html.H1(children='Titanic Dashboard'),
dcc.Graph(id="fare_vs_age", figure=fig)])

if __name__ == "__main__":
    app.run_server(debug=True)