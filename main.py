import asyncio
from engine.streamer import get_live_stream
from engine.brain import TradingBrain
from engine.risk import RiskManager
from data.database import MarketDB

async def main():
    db = MarketDB()
    brain = TradingBrain()
    risk = RiskManager(stop_loss_pct=0.01)
    
    balance = 1000.0
    entry_price = 0
    in_position = False
    price_history = []

    print("--- Production Bot Started ---")

    async for data in get_live_stream():
        price = float(data['c'])
        price_history.append(price)
        
        # Get Logic Signal
        signal = brain.calculate_indicators(price_history)
        
        # Check Risk
        if in_position and risk.check_stop_loss(entry_price, price):
            balance = (balance / entry_price) * price
            in_position = False
            entry_price = 0
            db.log_event("BTC/USDT", price, "STOP_LOSS", balance)
            print(f"🛑 STOP LOSS TRIGGERED at {price}")

        # Execute Strategy
        if signal == "BULLISH" and not in_position:
            entry_price = price
            in_position = True
            db.log_event("BTC/USDT", price, "BUY", balance)
            print(f"🚀 BUY SIGNAL at {price}")
            
        elif signal == "BEARISH" and in_position:
            balance = (balance / entry_price) * price
            in_position = False
            entry_price = 0
            db.log_event("BTC/USDT", price, "SELL", balance)
            print(f"💰 SELL SIGNAL at {price} | Balance: {balance:.2f}")

if __name__ == "__main__":
    asyncio.run(main())