import pandas as pd
import numpy as np
from flask import Flask, render_template
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def ndash():
	
	df = pd.DataFrame( { "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas" ], "Amount": [4,2,1,2,4,5], "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"] })
	
	fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
	
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	
	return render_template("ndash.html", graphJSON=graphJSON)
	