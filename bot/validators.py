def validate_inputs(symbol,side,order_type,quantity,price):
    """Validate CLI inputs before sending them to the API layer"""
    
    # Making sure that all the input is iin upper case so the case sensitivity errors don't occur.
     
    side_upper = side.upper()
    type_upper = order_type.upper()
    symbol_upper = symbol.upper()

    # Checks side
    if side_upper not in ['BUY','SELL']:
        raise ValueError(f"invalid side '{side}'.Side must be strictly 'BUY' or 'SELL'.")
    
    # checks types
    if type_upper not in ['MARKET','LIMIT']:
        raise ValueError(f"Invalid type '{type}'.Type must be strictly 'MARKET' or 'LIMIT'.")
    
    # checks quantity
    if quantity <= 0 :
        raise ValueError("Quantity must be a positive number greater than 0")
    
    if type_upper == 'LIMIT':
        if price is None or price <= 0:
            raise ValueError("Limit order requires a valid price greater than 0")
        
    return symbol_upper,type_upper,side_upper