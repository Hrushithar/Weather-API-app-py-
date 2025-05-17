# Weather App using PyQt5 and OpenWeatherMap API
# This script creates a simple weather application that allows users to enter a city name
# and fetches the current weather information using the OpenWeatherMap API.
# The application displays the weather information including temperature, humidity, wind speed,
# and a weather emoji based on the weather condition.
# The user can toggle between Celsius and Fahrenheit units for temperature display.
# The application is styled using Qt stylesheets for a modern look and feel.
# Import necessary libraries
# PyQt5 is used for creating the GUI, and requests is used for making HTTP requests to the API.
import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QWidget,
    QPushButton, QLabel, QLineEdit
)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.unit_celsius = True
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")
        self.setFixedSize(400, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #1c1c1c;
                color: #ffffff;
                font-family: Helvetica;
            }
            QLineEdit {
                font-size: 20px;
                padding: 10px;
                border: 1px solid #444;
                border-radius: 6px;
                background-color: #2a2a2a;
                color: #ffffff;
            }
            QPushButton {
                font-size: 18px;
                padding: 10px;
                margin-top: 10px;
                background-color: #3d3d3d;
                color: white;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")

        self.get_weather_button = QPushButton("Get Weather")
        self.toggle_unit_button = QPushButton("Toggle °C/°F")

        self.emoji_label = QLabel("❓")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        # Set emoji font via stylesheet
        self.emoji_label.setStyleSheet("""
            font-family: 'Apple Color Emoji';
            font-size: 70px;
        """)

        self.city_label = QLabel()
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setStyleSheet("font-size: 20px;")

        self.temperature_label = QLabel()
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setStyleSheet("font-size: 40px;")

        self.description_label = QLabel()
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("font-size: 20px;")

        self.extra_label = QLabel()
        self.extra_label.setAlignment(Qt.AlignCenter)
        self.extra_label.setStyleSheet("font-size: 14px;")

        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.toggle_unit_button)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.city_label)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.description_label)
        layout.addWidget(self.extra_label)

        self.setLayout(layout)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.toggle_unit_button.clicked.connect(self.toggle_units)

    def toggle_units(self):
        self.unit_celsius = not self.unit_celsius
        self.get_weather()

    def get_weather(self):
        api_key = "75d9ec13058412d8eea11d8c910300c7"
        city = self.city_input.text()
        if not city:
            self.display_error("Please enter a city name")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
        except Exception:
            self.display_error("City not found or network error")

    def display_weather(self, data):
        temp_k = data["main"]["temp"]
        feels_like_k = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"].capitalize()
        city = data["name"]
        country = data["sys"]["country"]

        if self.unit_celsius:
            temp = round(temp_k - 273.15)
            feels_like = round(feels_like_k - 273.15)
            unit = "°C"
        else:
            temp = round((temp_k - 273.15) * 9/5 + 32)
            feels_like = round((feels_like_k - 273.15) * 9/5 + 32)
            unit = "°F"

        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.city_label.setText(f"{city}, {country}")
        self.temperature_label.setText(f"{temp}{unit}")
        self.description_label.setText(description)
        self.extra_label.setText(f"Feels like: {feels_like}{unit} | Humidity: {humidity}% | Wind: {wind_speed} m/s")

    def display_error(self, message):
        self.emoji_label.setText("⚠️")
        self.city_label.setText("")
        self.temperature_label.setText("")
        self.description_label.setText(message)
        self.extra_label.setText("")

    @staticmethod
    def get_weather_emoji(code):
        if 200 <= code <= 232:
            return "⛈️"
        elif 300 <= code <= 321:
            return "🌦️"
        elif 500 <= code <= 504:
            return "🌧️"
        elif code == 511:
            return "🌨️"
        elif 520 <= code <= 531:
            return "🌧️"
        elif 600 <= code <= 622:
            return "❄️"
        elif 701 <= code <= 771:
            return "🌫️"
        elif code == 781:
            return "🌪️"
        elif code == 800:
            return "☀️"
        elif code == 801:
            return "🌤️"
        elif code == 802:
            return "⛅"
        elif code == 803:
            return "🌥️"
        elif code == 804:
            return "☁️"
        else:
            return "🌈"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())