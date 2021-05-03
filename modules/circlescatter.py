import pandas as pd
import numpy as np
import bokeh as bk


from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import CheckboxGroup, Tabs
from bokeh.layouts import row, WidgetBox

def circlescatter_tab(data):

    #list of names ('alpha', 'beta', ...)
    available_identifiers = list(data[0])

    def make_dataset(identifiers):
        
        new_data = pd.DataFrame()

        #new_data will contain data for the entries given in the input
        for i, identifier in enumerate(identifiers):
            subset = data[data[0] == identifier]

            new_data = new_data.append(subset)

        #convert final data into columndatasource for bokeh
        cds = ColumnDataSource(data={
        'name': new_data[0],
        'x': new_data[1],
        'y': new_data[2],
        })
        
        return cds

    def make_plot(src):
        p = figure(plot_width = 700, plot_height = 700, 
                    title = 'Test data',
                    x_axis_label = 'x label', y_axis_label = 'y label',
                    x_range = (0, 10), y_range = (0, 10))

        #draw graph using data from make_dataset func - note that you have to use a cds
        #and then refer to data via column names
        p.circle(source = src, x='x', y='y', size=20, color="navy", alpha=0.5)

        return p
    
    def update(attr, old, new):
        data_to_plot = [selection.labels[i] for i in selection.active]

        new_src = make_dataset(data_to_plot)

        src.data.update(new_src.data)
    
    # selection data comes from checkboxes
    selection = CheckboxGroup(labels=available_identifiers, active = [0, 1, 2, 3, 4])
    # Update the plot when the value is changed - on_change calls update function
    selection.on_change('active', update)

    initial_data = [selection.labels[i] for i in selection.active]

    src = make_dataset(initial_data)

    p = make_plot(src)

    controls = WidgetBox(selection)

    layout = row(controls, p)

    #make tab
    tab = Panel(child=layout, title = 'Circles')

    return tab