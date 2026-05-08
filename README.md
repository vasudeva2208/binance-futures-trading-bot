# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot for Binance Futures Testnet.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI-based input
- Logging
- Error handling
- Input validation

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
├── requirements.txt
├── README.md
└── .env
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/vasudeva2208/binance-futures-trading-bot.git
```

## Move Into Project Folder

```bash
cd binance-futures-trading-bot
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure API Keys

Create a `.env` file in project root.

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

# Run MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

# Run LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000
```

---

# Logging

Logs are stored in:

```text
logs/trading_bot.log
```

---

# Assumptions

- Binance Futures Testnet account is configured
- API keys are valid
- User has Python 3 installed
- Internet connection is available