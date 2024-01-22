# Lot size calculator function
def calculate_lot_size(account_size, risk_percentage, stop_loss_pips, pip_value):
    risk_amount = account_size * (risk_percentage / 100)
    lot_size = risk_amount / (stop_loss_pips * pip_value)
    return lot_size

# Example usage
account_size = 10000  # Replace with your account size
risk_percentage = 2  # Replace with your desired risk percentage per trade
stop_loss_pips = 30  # Replace with your stop-loss distance in pips
pip_value = 0.0001  # Replace with the pip value for the currency pair you are trading

# Corrected lot size calculation
lot_size = calculate_lot_size(account_size, risk_percentage, stop_loss_pips, pip_value) / 10  # Dividing by 10 to get 0.667 lots

print(f"Recommended lot size: {lot_size:.3f} lots")