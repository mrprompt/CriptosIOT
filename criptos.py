def do_criptos(moeda):
    import urequests as requests

    """
    {
        "symbol": "BTCBRL",
        "priceChange": "-15970.00000000",
        "priceChangePercent": "-4.726",
        "weightedAvgPrice": "324399.27840539",
        "prevClosePrice": "337918.00000000",
        "lastPrice": "321948.00000000",
        "lastQty": "0.00035800",
        "bidPrice": "321521.00000000",
        "bidQty": "0.00893300",
        "askPrice": "321925.00000000",
        "askQty": "0.16552600",
        "openPrice": "337918.00000000",
        "highPrice": "344150.00000000",
        "lowPrice": "313000.00000000",
        "volume": "293.13333400",
        "quoteVolume": "95092242.02616700",
        "openTime": 1615757622491,
        "closeTime": 1615844022491,
        "firstId": 2483667,
        "lastId": 2523977,
        "count": 40311
    }
    """
    
    try:
        # response = requests.get('https://vapi.binance.com/api/v3/ticker/price?symbol={}'.format(moeda))
        response = requests.get('https://api.binance.com/api/v3/ticker/24hr?symbol={}'.format(moeda))
        currency = response.json()
        value = {'moeda': moeda, 'compra': currency['askPrice'], 'venda': currency['bidPrice']}
        
        return value
    except Exception:
        print(response.text)
        pass


if __name__ == "__main__":
    criptos = do_criptos('BTCBRL')
    
    print(criptos)

