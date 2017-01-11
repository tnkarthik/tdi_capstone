from flask import Flask, render_template, request, redirect
from plot_data import get_data
from plot_df import plot_df

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    #return render_template('index.html')
    if request.method == 'GET':
        return render_template('index.html', message = 'GOOG')
    else:
        
        result = request.form
        #colnames.remove('ticker')
        ticker = result['ticker']
        ticker = ticker.upper()
        
        colnames = [str(result[x]) for x in result.keys() if x != 'ticker']
        
        if not colnames:
            colnames = ['open','close']

        df  = get_data( ticker = ticker, selected_cols = colnames)
        
        if not df.empty:
            plot_df(df, ticker)
            return render_template('stock_price.html')
        
        else:
            return render_template('index.html', message ="INVALID-SYMBOL")
        

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=33000)
