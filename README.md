# Binance Futures Testnet Trading Bot

A modular, command-line trading bot built in Python for executing trades on the Binance Futures Testnet. This project emphasizes clean architecture, strict input validation, secure credential management, and comprehensive logging.

---

## 🏗️ Project Architecture

* **`cli.py`**: The main entry point. Parses commandline arguments and orchestrates the application flow.
* **`bot/validators.py`**: A strict input validation layer (bouncer) ensuring no malformed data reaches the API.
* **`bot/client.py`**: Manages the secure, authenticated connection to the Binance Testnet.
* **`bot/orders.py`**: Constructs payloads and executes `MARKET` and `LIMIT` orders with proper Binance API mapping.
* **`bot/logging_config.py`**: A dual channel logger that outputs formatted summaries to the terminal and detailed technical records to `trading_bot.log`.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Amit-M-14/Trading-Bot.git
cd Trading-Bot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# On Windows (Git Bash)
source venv/Scripts/activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

For security, API keys are not hardcoded. Create a `.env` file in the project root directory (this file should be git ignored) and add your Binance Futures Testnet credentials:

```env
BINANCE_TESTNET_API_KEY=your_actual_demo_api_key_here
BINANCE_TESTNET_API_SECRET=your_actual_demo_secret_key_here
```

---

## 🚀 How to Run Examples

### 1. Execute a MARKET Order

Executes instantly at the current market price.

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
```

### 2. Execute a LIMIT Order

Places an order at a specific price point using Good-Til-Canceled (GTC).

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.005 --price 95000
```

---

## 🧠 Design Decisions & Assumptions

### Testnet Exclusivity

The bot is strictly hardcoded to use the Binance Futures Testnet (`demo.binance.com`). It is designed to fail safely if live API credentials are provided.

### Enhanced CLI User Experience

The CLI combines `argparse` with a custom validation layer (`validators.py`) to provide clear, human-readable error messages for:

* Negative or invalid quantities
* Unsupported order types
* Missing price parameters for limit orders
* Invalid trading symbols or sides

### Security First

* Credentials are loaded securely from a local `.env` file.
* Sensitive information is never hardcoded.
* A comprehensive `.gitignore` prevents accidental commits of:

  * API credentials
  * Virtual environments
  * Log files
  * Cache directories

### Auditability & Logging

Every successful execution:

* Prints a concise, formatted order summary to the terminal.
* Writes detailed timestamped request/response payloads to `trading_bot.log`.
* Provides an auditable trail for debugging, monitoring, and compliance purposes.

---

## 📁 Example Project Structure

```text
binance-futures-bot/
│
├── cli.py
├── requirements.txt
├── .env
├── .gitignore
├── trading_bot.log
│
└── bot/
    ├── __init__.py
    ├── client.py
    ├── orders.py
    ├── validators.py
    └── logging_config.py
```

---

## 📜 License

This project is intended for educational and testing purposes only. Use responsibly and never expose API credentials publicly.

~ Amit Mohanty