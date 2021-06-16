import csv
lst = []
with open('tickers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        lst.append(line)
tickers = lst[0][0].split('\n')
validate = []
for n in tickers:
    stonks = n.split(',')
    validate.append(stonks[0])
print(validate)

