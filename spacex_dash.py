# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                 {'label': 'All Sites', 'value': 'ALL'},
                                                 {'label': 'CCAFS LC-40', 'value': 'site0'},
                                                 {'label': 'VAFB SLC-4E', 'value': 'site1'},
                                                 {'label': 'KSC LC-39A', 'value': 'site2'},
                                                 {'label': 'CCAFS SLC-40', 'value': 'site3'},
                                             ],
                                             value='ALL',
                                             placeholder="place holder here",
                                             searchable=True
                                             ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0',
                                                       2500: '2500',
                                                       5000: '5000',
                                                       7500: '7500',
                                                       10000: '10000'},
                                                value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])


# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class',
                     names='Launch Site',
                     title='Total Success Launches by Site')
        return fig
    # return the outcomes piechart for a selected site
    elif entered_site == 'site0':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40']
        fig0 = px.pie(filtered_df, names='class',
                      title='Total Success Launches for site CCAFS LC-40')
        return fig0
    elif entered_site == 'site1':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'VAFB SLC-4E']
        fig1 = px.pie(filtered_df, names='class',
                      title='Total Success Launches for site VAFB SLC-4E')
        return fig1
    elif entered_site == 'site2':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'KSC LC-39A']
        fig2 = px.pie(filtered_df, names='class',
                      title='Total Success Launches for site KSC LC-39A')
        return fig2
    elif entered_site == 'site3':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'CCAFS SLC-40']
        fig3 = px.pie(filtered_df, names='class',
                      title='Total Success Launches for site CCAFS SLC-40')
        return fig3
    else:
        return True

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'), Input(component_id='payload-slider', component_property='value'))


def get_scatter_chart(entered_site, entered_payload):
    if entered_site == 'ALL':
        filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(entered_payload[0], entered_payload[1])]
        fig = px.scatter(spacex_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Correlation between Payload and Success for all Sites')
        return fig
    elif entered_site == 'site0':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'CCAFS LC-40']
        filtered_df = filtered_df[filtered_df['Payload Mass (kg)'].between(entered_payload[0], entered_payload[1])]
        fig1 = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Correlation between Payload and Success for site CCAFS LC-40')
        return fig1
    elif entered_site == 'site1':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'VAFB SLC-4E']
        filtered_df = filtered_df[filtered_df['Payload Mass (kg)'].between(entered_payload[0], entered_payload[1])]
        fig2 = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Correlation between Payload and Success for site VAFB SLC-4E')
        return fig2
    elif entered_site == 'site2':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'KSC LC-39A']
        filtered_df = filtered_df[filtered_df['Payload Mass (kg)'].between(entered_payload[0], entered_payload[1])]
        fig3 = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Correlation between Payload and Success for site KSC LC-39A')
        return fig3
    elif entered_site =='site3':
        filtered_df = spacex_df[spacex_df['Launch Site'] == 'CCAFS SLC-40']
        filtered_df = filtered_df[filtered_df['Payload Mass (kg)'].between(entered_payload[0], entered_payload[1])]
        fig4 = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Correlation between Payload and Success for site CCAFS SLC-40')
        return fig4

# Run the app
if __name__ == '__main__':
    app.run_server()

#%%
