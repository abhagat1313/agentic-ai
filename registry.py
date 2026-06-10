from tools.weather import get_weather
from tools.time_tool import get_time
from tools.stock import get_stock_price

TOOLS = {
    "weather":{
        "description": "Get the current weather",
        "function": get_weather
    },
    "time":{
        "description": "Get the current time",
        "function": get_time    
    },
    "stock":{
        "description": "Get the current stock price",
        "function": get_stock_price    
    }
}