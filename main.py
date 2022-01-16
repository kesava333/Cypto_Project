bitcoin_price = 43000
eth_price = 4200
ada_price = 1.80

def crypto_pre(year, annual_correction):
    print(f"Bitcoin predicted price for {year} is {bitcoin_price * annual_correction}")
    print(f"Ethereum predicted price for {year} is {eth_price* annual_correction}")
    print(f"Cardano predicted price for {year} is {ada_price * annual_correction}")

print("  \003 Price Prediction For Year 2022   \003")
crypto_pre(2022, 1.2)
print("\n \003  \b Price Prediction for Year 2023  \003")
crypto_pre(2023, 1.4)


