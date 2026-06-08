import argparse
import os
import sys
from dotenv import load_dotenv
from bot.logging_config import setup_logger
from bot.client import BinanceTestnetClient
from bot.orders import place_order
from bot.validators import validate_inputs

def main():
    load_dotenv() # loads data fron env files

    # Initialize our unified logging system
    logger = setup_logger()
    
    # Setup of the Command Line Argument Parser
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument('--symbol', type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL', 'buy', 'sell'], help="BUY or SELL")
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT', 'market', 'limit'], help="MARKET or LIMIT")
    parser.add_argument('--quantity', type=float, required=True, help="Amount to trade")
    parser.add_argument('--price', type=float, help="Price (Required if type is LIMIT)")

    args = parser.parse_args()

    api_key = os.getenv('BINANCE_TESTNET_API_KEY')
    api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')

    if not api_key or not api_secret:
        logger.error("Missing Credentials! Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET in your terminal.")
        print("\n FAILURE: Missing API credentials. Check trading_bot.log for instructions.")
        sys.exit(1)

    try:
        # clean the data
        symbol, side, order_type = validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        client_wrapper = BinanceTestnetClient(api_key, api_secret)
        
        # to make sure that the API call send correct parameters to the binance server (caused error while development)
        response = place_order(
            client_wrapper=client_wrapper,
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )
        
        # Print summary 
        if response:
            print("\n" + "="*45)
            print("BINANCE FUTURES ORDER RESPONSE SUMMARY")
            print("="*45)
            print(f"Status:        {response.get('status')}")
            print(f"Order ID:      {response.get('orderId')}")
            print(f"Symbol:        {response.get('symbol')}")
            print(f"Executed Qty:  {response.get('executedQty')}")
            print(f"Average Price: {response.get('avgPrice', 'N/A')}")
            print("="*45 + "\n")
            print("SUCCESS: Order placed and saved to log.")
        else:
            print("\n FAILURE: Order execution failed. See trading_bot.log for details.")
            sys.exit(1)

    except ValueError as ve:
        logger.error(f"Input Validation Error: {ve}")
        print(f"\n  INPUT ERROR: {ve}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Application Error: {e}")
        print(f"\n CRITICAL SYSTEM ERROR: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()