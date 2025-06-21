import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
gemini_api_model = os.getenv("GEMINI_API_MODEL")
weather_api_key = os.getenv("WEATHER_API_KEY") 
weather_api_url = os.getenv("WEATHER_API_URL")

if gemini_api_key is None:
    print("Api key is not set in Environment varibales")
    exit(1)
if gemini_base_url is None:
    print("Base url is not set in Environment varibales")
    exit(1)
if gemini_api_model is None:
    print("api model is not set in Environment varibales")
    exit(1)
if weather_api_key is None:
   print("Weather Api key is not set in Environment varibales")
   exit(1)

if weather_api_url is None:
   print("Weather Api URL is not set in Environment varibales")
   exit(1)

class Secrets:
    def __init__(self):
     self.gemini_api_key = gemini_api_key
     self.gemini_base_url = gemini_base_url
     self.gemini_api_model = gemini_api_model
     self.weather_api_key = weather_api_key
     self.weather_api_url = weather_api_url
    

