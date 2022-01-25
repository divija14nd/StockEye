import investpy
import pandas as pd
import matplotlib as plt
import plotly.graph_objects as go
import plotly.express as px
from Web.models import Verdict

#----------------------------------------RECOMMENDATION FUNCTION-------------------------------------------------------

def recommend(stock_symbol):
    stock_values = investpy.technical.moving_averages(name=stock_symbol, country = "India", product_type = "Stock", interval='daily')
    try:
        sma_values = stock_values['sma_value'].tolist()
        if ((((abs(sma_values[2] - sma_values[1])/sma_values[1])*100) <= 0.75) & (((abs(sma_values[2] - sma_values[0])/sma_values[0])*100) <= 0.75)):
            return("Strongly Recommend")
        elif (((abs(sma_values[2] - sma_values[1])/sma_values[1])*100) <= 1.0 ):
            return("Recomended")
        elif (((abs(sma_values[1] - sma_values[0])/sma_values[0])*100) <= 1.0):
            return("Recomended")
        else :
            return("Not Recomended")
    except:
        return("no sma")
    

def priceGraph(stock_name):

    plot_df = investpy.stocks.get_stock_historical_data(stock= stock_name, country="India", from_date="01/01/2021", to_date="21/01/2022", as_json=False, order='ascending', interval='Daily')
    fig = px.line(plot_df, x=plot_df.index, y="Close",title = stock_name)
    fig.update_layout(margin=dict(l=200, r=500, t=200, b=200))
    fig.show()
        
#----------------------------------------STOCK LIST------------------------------------------------------------

stock_list = ['ASPN','RELI','TCS','TAMO','SBI','HDBK','WIPR','INFY','BJFN','APSE','ADEL','TEML','AXBK','KTKM','BAJA','NEST','MAHM','SUN','ULTC','LART','JSTL','YESB','HLL','ITC','HZNC','CIPL','MRCO','GAIL','BOB','HDFC','GOCP','IDBI']

# -----------------------------------------CREATING RECOMMENDATION DATAFRAME--------------------------------------------------


for i in range(len(stock_list)):
    ver = Verdict(
        stock = stock_list[i],
        verdict = recommend(stock_list[i])
    )
    ver.save()



