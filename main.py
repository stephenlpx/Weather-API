import requests
import pandas
from key import key

city = input("Enter the city of choice: ")

#link to API with user to enter a city of their choice and thier API key

# ---- User should get their own API key from Open weather map for this to work (Paste in the key file)
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
res = requests.get(url)
data = res.json()

print("""

Welcome to today's weather

""")
temp = data["main"]["temp"]
desc = data["weather"][0]["description"]
max_temp = data["main"]["temp_max"]

#create dict for dataframe
weather_dict = {
    "Info": ["Current temp", "Max temp", "Desc"],
    "Data": [temp, max_temp, desc]

}
df = pandas.DataFrame(weather_dict)
print(df)


print("""

""")






