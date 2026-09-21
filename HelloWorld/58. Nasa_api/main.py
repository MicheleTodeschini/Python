import requests
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout

api_key = ""
apod_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key="

url = f"{apod_url}{api_key}"

try:
    res = requests.get(url)

    data = res.json()

    print(data[0]["title"])
    print(data[0]["date"])
except:
    print(f"Error when fetching the data {res.status_code}")
