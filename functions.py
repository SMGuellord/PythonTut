#function declaration
def beef():
    print("Damn, functions are cool")

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(btc, "BTC is equal to", amount, "USD")

print("================================")
print("Calling beef function")
print("=================================")
#calling a function
beef()

print("================================")
print("Calling bitcoin_to_usd function")
print("=================================")
#calling bitcoin_to_usd
bitcoin_to_usd(1)
bitcoin_to_usd(13)