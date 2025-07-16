import dash
from dash import html

# Import the change cdn plugin
from dash_change_cdn_plugin import setup_change_cdn_plugin

# Enable the change cdn plugin for the current app
setup_change_cdn_plugin()

# Remember to set serve_locally=False
app = dash.Dash(__name__, serve_locally=False)

app.layout = html.Div("Test App", style={"padding": 50})

if __name__ == "__main__":
    app.run()
