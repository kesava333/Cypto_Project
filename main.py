bitcoin_price = int(43000)
eth_price = int(4200)
ada_price = 1.8

def crypto_pre(year, correction):
  try:
    year_input = int(year)
    if year_input > 2021 & year_input >0:
     print(f"Bitcoin predicted price for {year_input} is {bitcoin_price * correction}")
     print(f"Ethereum predicted price for {year_input} is {eth_price* correction}")
     print(f"Cardano predicted price for {year_input} is {ada_price * correction}")
    else:
     print("Please enter valid year i.e. any year above 2021")
  except ValueError:
      print("Please enter a Number, don't destroy my APP")


## I have to work with user input
year_no = input("Hey! Please enter the Year, we will send you the predicted price \n input ---->  ")
print(f"Price Prediction For Year {year_no}")
crypto_pre(year_no, 1.2)





