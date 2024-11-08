from tda import auth, client
import json
import config

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path = 'e:/OneDrive/Documents/GitHub/notes/python/libs_and_topics/finance/part_time_larry/ameritrade/chromedriver.exe') as driver:
        c = auth.client_from_login_flow(driver, config.api_key, config.redirect_uri, config.token_path)

# r = c.get_price_history(
#     'APPL',
#     period_type = client.Client.PriceHistory,PeriodType.YEAR,
#     period = client.Client.PriceHistory,PeriodType.TWENTY_YEARS,
#     frequency_type = client.Client.PriceHistory,FrequencyType.DAILY,
#     frequency = client.Client.PriceHistory,Frequency.DAILY)

# assert r.ok, r.raise_for_status()
# print(json.dumps(r.json(), indent = 4))



# https://auth.tdameritrade.com/oauth?client_id=O6VMDXJD0GMBYTMOUYBSF6JNAAA3DEHW%40AMER.OAUTHAP&response_type=code&redirect_uri=https%3A%2F%2Flocalhost&state=Rujw4V7lTzSSuXuARfsDeyiieO6ZsD

# https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https%3A%2F%2F127.0.0.1&client_id=O6VMDXJD0GMBYTMOUYBSF6JNAAA3DEHW%40AMER.OAUTHAP

# https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https%3A%2F%2Flocalhost&state=Rujw4V7lTzSSuXuARfsDeyiieO6ZsD&client_id=O6VMDXJD0GMBYTMOUYBSF6JNAAA3DEHW%40AMER.OAUTHAP

# https://auth.tdameritrade.com/oauth?client_id=O6VMDXJD0GMBYTMOUYBSF6JNAAA3DEHW%40AMER.OAUTHAP&response_type=code&redirect_uri=https%3A%2F%2Flocalhost&state=Rujw4V7lTzSSuXuARfsDeyiieO6ZsD

# https://auth.tdameritrade.com/oauth?client_id=O6VMDXJD0GMBYTMOUYBSF6JNAAA3DEHW%40AMER.OAUTHAP&response_type=code&redirect_uri=https%3A%2F%2F127.0.0.1

# https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https%3A%2F%2Flocalhost&client_id=O6VMDXJD0GMBYTMOUYBSF6JNAAA3DEHW%40AMER.OAUTHAP