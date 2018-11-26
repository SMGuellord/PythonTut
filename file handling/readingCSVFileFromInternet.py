from urllib import request


goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOGL?period1=1540464235&period2=1543142635&interval=1d&events=history&crumb=QVztDyyIs8Z'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url) #request connection to url
    csv = response.read() #store response data to csv
    csv_str = str(csv) #convert the csc value to string
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv' #r stand for raw.
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line +"\n")
    fx.close()


download_stock_data(goog_url)