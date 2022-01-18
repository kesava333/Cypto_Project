bitcoin_price = int(43000)
eth_price = int(4200)
ada_price = float(1.8)

def crypto_pre(year_no_element, correction):
  try:
    year_input = int(year_no_element)
    if year_input > 2021 & year_input >0:
       print(f"Bitcoin predicted price for {year_input} is {bitcoin_price * correction}")
       print(f"Ethereum predicted price for {year_input} is {eth_price* correction}")
       print(f"Cardano predicted price for {year_input} is {ada_price * correction}")
    elif year_input <=0:
       print("Please enter valid year i.e. any year above 2021 or a non negative number or non zero")
  except ValueError:
       print("Please enter a Number, don't destroy my APP")


## I have to work with user input
year_no=0
while year_no != "exit":
   year_no = input("Hey! Please enter the Year, we will send you the predicted price \n input ---->  ")
   correction_input = float(input(f"Please enter Correction Input:\n"))
   ##print(f"Price Prediction For Year {year_no}")
   for year_no_element in year_no.split(","):
       print(f"Price Prediction For Year {year_no_element}")
       crypto_pre(year_no_element, correction_input)





