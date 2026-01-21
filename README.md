# 🛡️ Production-Grade Crypto Trading Bot (End-to-End System)

A **full-stack crypto trading bot architecture** built in Python that combines:

- Live market data (WebSockets)
- Strategy & indicator logic
- Risk management (stop-loss)
- Trade logging (SQLite)
- Real-time monitoring dashboard (Streamlit)

This project demonstrates how individual trading components come together to form a **production-style trading system** (paper / simulated execution).

---

## 🧠 System Overview
Binance WebSocket
->
Live Streamer (Async)
->
Trading Brain (Indicators + Logic)
->
Risk Manager (Stop-Loss)
->
Trade Logger (SQLite)
->
Streamlit Dashboard (Monitoring)

---

## 🚀 Features

### 🔹 Live Market Data
- Real-time BTC/USDT price stream using **Binance WebSockets**
- Fully asynchronous, non-blocking pipeline

### 🔹 Trading Strategy
- Simple **SMA-based trend detection**
- Generates `BULLISH` / `BEARISH` signals
- Modular logic (easy to upgrade)

### 🔹 Risk Management
- Fixed percentage **stop-loss**
- Automatic exit on downside protection
- Capital preservation focus

### 🔹 Trade Logging
- Persistent trade history stored in **SQLite**
- Logs:
  - Timestamp
  - Symbol
  - Price
  - Signal (BUY / SELL / STOP_LOSS)
  - Account balance

### 🔹 Production Dashboard
- Built with **Streamlit**
- Live trade history table
- Balance over time visualization
- Manual refresh for stability

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **AsyncIO**
- **WebSockets**
- **SQLite**
- **Pandas**
- **NLTK (VADER)**
- **Streamlit**
- **Binance WebSocket API**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Production-Grade-Bot.git
cd Production-Grade-Bot
