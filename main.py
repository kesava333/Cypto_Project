bitcoin_price = int(43000)
eth_price = int(4200)
ada_price = int(1.80)

def crypto_pre(year, annual_correction):
    correction = int(annual_correction)
    if year > 2021:
     print(f"Bitcoin predicted price for {year} is {bitcoin_price * correction}")
     print(f"Ethereum predicted price for {year} is {eth_price* correction}")
     print(f"Cardano predicted price for {year} is {ada_price * correction}")
    else:
     print("Please enter valid year i.e. any year above 2021")


print("  \003 Price Prediction For Year 2022   \003")
crypto_pre(2022, 1.2)
print("\n \003  \b Price Prediction for Year 2023  \003")
crypto_pre(2023, 1.4)
crypto_pre(2021,1.0)


