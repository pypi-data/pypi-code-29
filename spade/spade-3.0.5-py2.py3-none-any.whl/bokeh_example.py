from spade import agent

import spade.bokeh_server

import random

from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature


class Ag(spade.bokeh_server.BokehServerMixin, agent.Agent):

    async def controller2(self, request):
        script = self.bokeh_server.get_plot_script("/plot2")

        return {"script": script}

    def setup(self):

        self.web.add_get("/plot2", self.controller2, "plot.html")

        self.web.start(port=10000)
        self.bokeh_server.start()

        self.bokeh_server.add_plot("/plot2", self.modify_doc)

    def modify_doc(self, doc):
        df = sea_surface_temperature.copy()
        source = ColumnDataSource(data=df)

        plot = figure(x_axis_type='datetime', y_range=(0, 25), y_axis_label='Temperature (Celsius)',
                      title="Sea Surface Temperature at 43.18, -70.43")
        plot.line('time', 'temperature', source=source)

        def callback(attr, old, new):
            if new == 0:
                data = df
            else:
                data = df.rolling('{0}D'.format(new)).mean()
            source.data = ColumnDataSource(data=data).data

        slider = Slider(start=0, end=30, value=0, step=1, title="Smoothing by N Days")
        slider.on_change('value', callback)

        def update():
            new = random.randint(1, 30)
            data = df.rolling('{0}D'.format(new)).mean()
            source.stream(data)

        # doc.add_periodic_callback(update, 1000)

        doc.add_root(column(slider, plot))


a = Ag("jpalanca@gtirouter.dsic.upv.es", "test")
a.start()
