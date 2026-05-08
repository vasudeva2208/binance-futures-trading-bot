# Binance Futures Testnet Trading Bot

## Features

- Market Orders
- Limit Orders
- BUY and SELL support
- CLI-based input
- Logging
- Error handling
- Validation

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure API Keys

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Run MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## Run LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000
```