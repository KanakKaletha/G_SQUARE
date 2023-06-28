import matplotlib.pyplot as plt
from django.conf import settings
import os
import seaborn as sns

def generate_chart(dates, prices):
    dates = dates[::-1]

    plt.plot(dates, prices, marker='o',markerfacecolor='orange', markeredgecolor='orange')
    plt.xlabel('Date')
    plt.xticks(rotation='vertical')
    plt.ylabel('Closing Price')
    plt.title('Stock Price Last 30 Days')

    # labels
    for x, y in zip(dates, prices):
        label = "{:.2f}".format(y)
        plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,8), ha='center', rotation=90,fontsize=8)

    #top margin
    plt.subplots_adjust(top=0.90)
    
    
    # y-axis limit
    ymin, ymax = plt.ylim()
    plt.ylim(ymin, ymax + 4)

    file_name = 'chartMSFT.png'
    file_path = os.path.join(settings.BASE_DIR, 'static', file_name)
    if os.path.exists(file_path):
        os.remove(file_path)

    plt.savefig(file_path)





 


""" def generate_chart(dates, prices):
    # Set the style and color palette
    sns.set(style="darkgrid")
    sns.set_palette("husl")

    # Generate the chart
    plt.plot(dates, prices)
    plt.xlabel('Date')
    plt.xticks(rotation='vertical')
    plt.ylabel('Closing Price')
    plt.title('Stock Price for Last 30 Days')

    # Reverse the x-axis
    ax = plt.gca()
    ax.invert_xaxis()

    # Adjust the bottom margin to make space for the xticks
    plt.subplots_adjust(bottom=0.2)

    # Save the chart as an image file
    file_name = 'chart3D_MSFT.png'
    file_path = os.path.join(settings.BASE_DIR, 'static', file_name)
    plt.savefig(file_path)
 """