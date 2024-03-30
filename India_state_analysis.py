import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.io as pio
import warnings
warnings.filterwarnings('ignore')
pio.renderers.default = 'browser'
india_states = json.load(open("states_india.geojson", "r"))
state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
    
df = pd.read_csv("state.csv")
df["National Share (%)"] = df["National Share (%)"].apply(lambda x: x.replace("%", ""))
df["Decadal growth(2001-2012)"] = df["Decadal growth(2001-2012)"].apply(lambda x: x.replace("%", ""))
capital=df['Name'][18]='Delhi'
x=df['National Share (%)']
y=df['literacy rate']
plt.plot(x,y)
plt.xticks(rotation=90)
plt.xlabel('national share(%)')
plt.ylabel('literacy rate of state')
plt.show()
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='Name',
    color='Population',
    hover_data=["literacy rate",'sex ratio','Area(km^2)',"National Share (%)"],
    title="India state analysis",
    color_continuous_scale='Reds'
)             
fig.update_geos(fitbounds="locations", visible=False)
fig.show()                