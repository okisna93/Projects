import pandas as pd 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.express as px 
from dash.dependencies import Output, Input 

#Add DataFrame
df=pd.DataFrame({
    "Fruit":["Apple","Oranges","Bananas","Apples","Oranges","Bananas"],
    "Amount":[4,1,2,2,4,5],
    "City":["SF","SF","SF","NYC","MTL","NYC"]
})

# Add a bar graph figure
app=dash.Dash() 
fig=px.bar(df,x="Fruit",y="Amount",color="City",barmode="group")

app.layout=html.Div(children=[
    html.H1(children='Dashboard',style={'textAlign':'center'}),
    
    # Create Dropdown
    dcc.Dropdown(options=[{'label':'New York City','value':'NYC'},
                          {'label':'Montréal','value':'MTL' },
                          {'label':'San Francisco','value':'SF'}],
                          value='NYC'# Providing a value for dropdown
                          ),

    # Bar Graph
    
    dcc.Graph(id="example-graph-2",figure=fig)

])

if __name__=="__main__":
    app.run_server()