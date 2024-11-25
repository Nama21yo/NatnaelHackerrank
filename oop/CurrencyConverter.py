class CurrencyConverter:
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate  # Conversion rate to the target currency
    
    def get_currency(self):
        return self.currency
    
    def get_rate(self):
        return self.rate
    
    def set_currency(self, new_currency):
        self.currency = new_currency
    
    def set_rate(self, new_rate):
        if new_rate > 0:
            self.rate = new_rate
        else:
            raise ValueError("Rate must be positive.")
    
    def convert(self, amount):
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        return amount * self.rate

# Create a CurrencyConverter object
usd_to_eur = CurrencyConverter("EUR", 0.85)

# Get current currency and rate
print("Currency:", usd_to_eur.get_currency())
print("Rate:", usd_to_eur.get_rate())

# Convert an amount
amount_in_usd = 100
amount_in_eur = usd_to_eur.convert(amount_in_usd)
print(f"${amount_in_usd} USD is equal to €{amount_in_eur:.2f}")

# Update currency and rate
usd_to_eur.set_currency("GBP")
usd_to_eur.set_rate(0.75)

# Convert with updated settings
print("\nUpdated Conversion:")
amount_in_gbp = usd_to_eur.convert(amount_in_usd)
print(f"${amount_in_usd} USD is equal to £{amount_in_gbp:.2f}")
