import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)  # text input field where user types the city
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # setObjectName() gives each widget a unique CSS id
        # allows targeting specific widgets in the stylesheet like #city_label
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # stylesheet uses CSS id selectors (#name) to style specific widgets
        # shared styles go in the combined QLabel, QPushButton block
        # Segoe UI emoji is used for the emoji label so emojis render correctly on Windows
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "91ad8632867c42b27bde3164f85bb8df"  # get a free key from openweathermap.org
        city = self.city_input.text()       # reads whatever the user typed in the input field

        # openweathermap free API endpoint, returns JSON weather data for the city
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)

            # raise_for_status() throws an HTTPError if status code is 4xx or 5xx
            # without this, a 404 or 401 would silently pass through
            response.raise_for_status()

            data = response.json()  # parse the JSON response into a Python dict

            # cod 200 means the API returned valid weather data
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            # match statement checks the exact HTTP status code and shows a specific message
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")  # fallback for any other code

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            # base class for all requests exceptions, catches anything not caught above
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        # shrink font size so longer error messages fit in the label
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)

        # clear emoji and description so old weather data doesnt show alongside the error
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        # restore original font size in case it was shrunk by display_error
        self.temperature_label.setStyleSheet("font-size: 75px;")

        # openweathermap returns temperature in Kelvin by default
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15                  # Kelvin to Celsius
        temperature_f = (temperature_k * 9/5) - 459.67         # Kelvin to Fahrenheit

        # weather id is a numeric code that represents the weather condition
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]  # e.g. "light rain"

        self.temperature_label.setText(f"{temperature_f:.0f}°F")  # :.0f = no decimal places
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        # openweathermap groups weather conditions into id ranges
        # full list at openweathermap.org/weather-conditions
        # @staticmethod used because this method doesnt need self or any instance data
        if 200 <= weather_id <= 232:
            return "⛈"   # thunderstorm
        elif 300 <= weather_id <= 321:
            return "🌦"   # drizzle
        elif 500 <= weather_id <= 531:
            return "🌧"   # rain
        elif 600 <= weather_id <= 622:
            return "❄"    # snow
        elif 701 <= weather_id <= 741:
            return "🌫"   # mist/fog
        elif weather_id == 762:
            return "🌋"   # volcanic ash
        elif weather_id == 771:
            return "💨"   # squall
        elif weather_id == 781:
            return "🌪"   # tornado
        elif weather_id == 800:
            return "☀"    # clear sky
        elif 801 <= weather_id <= 804:
            return "☁"    # cloudy
        else:
            return ""      # unknown condition, show nothing


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())