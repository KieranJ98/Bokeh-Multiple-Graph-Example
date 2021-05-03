# Pandas for data management
import pandas as pd

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Custom modules
from modules.circlescatter import circlescatter_tab
from modules.squarescatter import squarescatter_tab

data = pd.read_csv('data/data.csv', header=None)

tab1 = circlescatter_tab(data)
tab2 = squarescatter_tab(data)

tabs = Tabs(tabs = [tab1, tab2])

curdoc().add_root(tabs)

#"bokeh serve --show main.py"

#meant to run above command with directory? look into this
#widgetbox is deprecated - use "bokeh.models.column" instead