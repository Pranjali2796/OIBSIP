import requests

API_KEY = "693c8c618be7bd9bb7dbacb3105fd91f"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Information")
    print("-------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

else:
    print("Error: City not found or API issue.")
