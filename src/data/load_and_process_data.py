import csv
import requests

csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

req = requests.get(csv_url)
url_content = req.content
csv_file = open('data/raw/winequality.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

reader = csv.reader(open("data/raw/winequality.csv", "r"), delimiter=';')
writer = csv.writer(open("data/processed/winequality.csv", 'w'), delimiter=',')

writer.writerows(reader)

