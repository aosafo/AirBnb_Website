import datetime
import plotly
import pymongo
from plotly.graph_objs import Layout, Scatter


def main():
    """Main Function
    """

    eth_last_price = []
    eth_best_bid = []
    eth_best_ask = []
    eth_timestamp = []

    btc_last_price = []
    btc_best_bid = []
    btc_best_ask = []
    btc_timestamp = []

    client = pymongo.MongoClient('localhost', 27017)
    db = client.btc
    collection = db['ticks']

    try:
        for rec in collection.find({"instrument":"ETH"}):
            eth_last_price.append(rec['lastPrice'])
            eth_best_bid.append(rec['bestBid'])
            eth_best_ask.append(rec['bestAsk'])
            eth_ts = datetime.datetime.fromtimestamp(rec['timestamp'])
            eth_timestamp.append(eth_ts)
    except Exception as err:
        print(err)


    eth_lp = Scatter(
        y=eth_last_price,
        x=eth_timestamp,
        name='ETH Last Price',
        mode='lines+markers')

    eth_bb = Scatter(
        y=eth_best_bid,
        x=eth_timestamp,
        name='ETH Best Bid',
        mode='lines+markers')

    eth_ba = Scatter(
        y=eth_best_ask,
        x=eth_timestamp,
        name='ETH Best Ask',
        mode='lines+markers')

    btc_lp = Scatter(
        y=btc_last_price,
        x=btc_timestamp,
        name='BTC Last Price minus 10^1',
        mode='lines+markers')

    btc_bb = Scatter(
        y=btc_best_bid,
        x=btc_timestamp,
        name='BTC Best Bid minus 10^1',
        mode='lines+markers')

    btc_ba = Scatter(
        y=btc_best_ask,
        x=btc_timestamp,
        name='BTC Best Ask minus 10^1',
        mode='lines+markers')

    plotly.offline.plot(
        {
            'data': [eth_lp, eth_bb, eth_ba, btc_lp, btc_bb, btc_ba],
            'layout': Layout(title="BTC Markets Graph")},
        filename=r"btc.html", auto_open=True)

if __name__ == "__main__":
    main()