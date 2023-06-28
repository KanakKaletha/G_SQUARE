from django.shortcuts import render
from stocks.forms import StockForm
from stocks.xignite import get_stock_data
from stocks.charts import generate_chart

from django.shortcuts import render


def stock_view(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            print(symbol)
            dates, prices = get_stock_data(symbol)
            chart = generate_chart(dates, prices)
            return render(request, 'chart.html', {'chart': chart})
    else:
        form = StockForm()
    return render(request, 'form.html', {'form': form})




def chart_view(request):
    return render(request, 'chart.html')
