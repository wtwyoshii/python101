def custom_logger(level, *args, **kwargs): 

    message = ' '.join(str(arg) for arg in args) 

    tag_str = ' | '.join(f'{k}={v}' for k, v in kwargs.items()) 

    print(f"[{level.upper()}]: {message}" + (f" [{tag_str}]" if tag_str else '')) 

custom_logger("info", "Server started", port=8080, status="OK") 

custom_logger("error", "Connection failed", reason="Timeout") 