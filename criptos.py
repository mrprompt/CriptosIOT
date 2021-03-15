def do_criptos():
    import urequests as requests
    from config import CRIPTOS

    moedas = []

    for moeda in CRIPTOS:
        """
        {
            'ticker': {
                    'high': 14481.47000000,
                    'low': 13706.00002000,
                    'vol': 443.73564488,
                    'last': 14447.01000000,
                    'buy': 14447.00100000,
                    'sell': 14447.01000000,
                    'date': 1502977646
                }
        }
        """
        response = requests.get('https://www.mercadobitcoin.net/api/{}/ticker/'.format(moeda))
        currency = response.json()
        value = {'moeda': moeda, 'compra': currency['ticker']['buy'], 'venda': currency['ticker']['sell']}

        moedas.append(value)

    return moedas


if __name__ == "__main__":
    criptos = do_criptos()
    
    print(criptos)
