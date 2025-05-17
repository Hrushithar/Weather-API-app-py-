# 🌤️ PyQt5 Weather App

A simple desktop weather application built with Python and PyQt5. It fetches real-time weather using the OpenWeatherMap API and displays temperature, conditions, wind, and humidity in a dark-themed UI with emoji-based weather visuals. Designed to work best on macOS (M1/M2), with notes for Windows users too.

## ⚙️ Features

- Live weather for any city
- Celsius and Fahrenheit toggle
- Displays temperature, weather description, feels like temp, humidity, and wind speed
- Emoji-based weather icons ☁️🌧️☀️
- Dark-mode UI (modern and minimal)
- Fast and optimized for macOS

## 🧑‍💻 How to Run

1. Clone the Repo

git clone https://github.com/your-username/Weather-API-app-py-.git
cd Weather-API-app-py-

2. Create and Activate a Virtual Environment

(macOS / Linux)

python3 -m venv venv
source venv/bin/activate

(Windows)

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install PyQt5 requests

4. Run the App

python main.py

## 🔑 Get Your API Key

This app uses OpenWeatherMap.  
Sign up and get your free API key here: https://openweathermap.org/api  
Then, replace the `api_key` variable in `main.py` with your key:

api_key = "your_api_key_here"

## 🪟 Windows Users Note

- Emojis might not render properly on some Windows systems.
  - Option 1: Replace emoji with plain text or icons.
  - Option 2: Use "Segoe UI Emoji" as the font in code instead of "Apple Color Emoji".
- If it still doesn't work, switch to weather PNG icons for guaranteed support.

## 📦 Requirements

- Python 3.9 or higher
- PyQt5
- requests

If you don't have a requirements.txt file, just run:

pip install PyQt5 requests

## 📄 License

MIT License — free for personal and commercial use.

## 🙌 Author

Made with 💻 by Hrushith AR  
Built using Python, OpenWeatherMap API, and PyQt5.
