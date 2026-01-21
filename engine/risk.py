class RiskManager:
    def __init__(self, stop_loss_pct=0.01):
        self.stop_loss_pct = stop_loss_pct

    def check_stop_loss(self, entry_price, current_price):
        if entry_price == 0: return False
        change = (current_price - entry_price) / entry_price
        return change <= -self.stop_loss_pct