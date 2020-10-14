import pandas_alive

covid_df = pandas_alive.load_dataset()

covid_df.plot_animated(filename='examples/example-barh-chart.gif')
