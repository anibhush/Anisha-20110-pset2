import csv
import requests

csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

req = requests.get(csv_url)
url_content = req.content
csv_file = open('Anisha-20110-pset2/data/raw/winequality.csv', 'wb')

csv_file.write(url_content)
csv_file.close()


