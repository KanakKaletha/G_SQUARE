import requests
from datetime import datetime, timedelta

def get_stock_data(symbol):
    # Set the API endpoint and parameters
    url = 'https://globalhistorical.xignite.com/v3/xGlobalHistorical.json/GetGlobalHistoricalTradesRange'
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    params = {
        'IdentifierType': 'Symbol',
        'Identifier': symbol,
        'IdentifierAsOfDate': end_date.strftime('%m/%d/%Y'),
        'AdjustmentMethod': 'All',
        'StartDate': start_date.strftime('%m/%d/%Y'),
        'EndDate': end_date.strftime('%m/%d/%Y'),
        '_token': 'BE0FAABE5A284DCBA5892CE8EAAE0B06'
    }

    # Make the API request
    response = requests.get(url, params=params)
    data = response.json()

    # Process the data as needed
    quotes = data['HistoricalQuotes']
    dates = [item['Date'] for item in quotes]
    prices = [item['Close'] for item in quotes]

    return dates, prices


# token=072A01E1ED4C4274B58978C060E54DA2
# token=BE0FAABE5A284DCBA5892CE8EAAE0B06