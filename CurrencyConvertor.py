import requests

api_key = "API key"

#frc = "USD"
#toc = "INR"

frc = input("Enter currency type1:")
fr = int(input("Enter the amount to be converted:"))
toc = input("Enter currency type2:")

frc = frc.upper()
toc = toc.upper()

base = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
main = base+"from_currency="+frc+"&to_currency="+toc+"&apikey="+api_key

response = requests.get(main)
result = response.json()

key = result['Realtime Currency Exchange Rate']
rate = key['5. Exchange Rate']

r = float(rate)
to = (r*fr)

#print(key)
#print(rate)
print(f' {frc} : {fr} ')
print(f' {toc} : {to}')

