# Ejemplo de dashboard con Dash
# Juan Francisco Mier Montoto, UO283319

# Importar las bibliotecas necesarias
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


df = px.data.gapminder()  # Cargar datos de Gapminder
app = dash.Dash(__name__)  # Inicializar la aplicación Dash

# Definir el layout de la app
app.layout = html.Div([
    html.H1("Gapminder + Dash + Asia + Inteligencia de Negocio"),
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': i, 'value': i} for i in df['continent'].unique()],
        value='Asia'
    ),
    dcc.Graph(id='life-exp-vs-gdp')
])


# Definir el callback para actualizar el gráfico
@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    [Input('continent-dropdown', 'value')]
)
def update_figure(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="country",
                     hover_name="country", log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
