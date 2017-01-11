def plot_df(df, ticker):
    
    from bokeh.charts import TimeSeries
    from bokeh.io import save, output_file
    output_file('templates/stock_price.html')
    
    colnames = list(df.columns)
    colnames.remove('date')
    #colnames.remove('ticker')
    p_title = 'Stock price plot for '+ ticker
    p = TimeSeries(df, x = 'date', y = colnames, color = colnames,  title = p_title , ylabel = 'Stock Prices', legend = True)
    save(p)
    #return ('stock_price.html')