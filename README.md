# 📚 Prognozowanie Cen Kryptowalut przy użyciu Sieci Neuronowych

---

## 📈 Przegląd Projektu

Ten projekt prognozuje ceny kryptowalut przy użyciu zaawansowanych architektur sieci neuronowych — LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit) oraz hybrydowego modelu LSTM-GRU. Zawiera graficzny interfejs użytkownika (GUI) zbudowany przy użyciu Tkinter, umożliwiający użytkownikom łatwy wybór parametrów, wizualizację wyników i interakcję z systemem prognozowania.

## 🚀 Funkcje

- Wiele Kryptowalut: Obsługuje Bitcoin (BTC), Ethereum (ETH), Dogecoin (DOGE) i Litecoin (LTC)
- Elastyczne Źródła Danych: Pobiera dane historyczne z:
  - Yahoo Finance
  - Stooq
  - Naver
  - Lokalnych plików CSV
- Modele Sieci Neuronowych:
  - LSTM
  - GRU
  - Hybrydowy LSTM-GRU
- Interaktywny GUI:
  - Zbudowany z Tkinter z motywem Azure
  - Wybór modelu i źródła danych
  - Kontrolki wprowadzania parametrów
- Wizualizacja:
  - Wykresy Matplotlib pokazujące przewidywane vs. rzeczywiste ceny
- Konfigurowalne Parametry:
  - Dni predykcji (domyślnie: 30)
  - Dni przyszłe (domyślnie: 1)
  - Zakres wykresu (domyślnie: 20)
  - Epoki (domyślnie: 100) i rozmiar partii (domyślnie: 32)

## 🛠️ Instalacja
1. Sklonuj Repozytorium
<pre><code>git clone https://github.com/yourusername/cryptocurrency-prediction.git
cd cryptocurrency-prediction</code></pre>
2. Zainstaluj Wymagane Pakiety
<pre><code>pip install -r IMPL/requirements.txt</code></pre>

## ▶️ Użytkowanie
Uruchom Aplikację
Bądź w folderze IMPL
<pre><code>python app.py</code></pre>
W interfejsie GUI:
1. Wybierz kryptowalutę (BTC, ETH, Doge, LTC)
2. Wybierz źródło danych (Yahoo, Stooq, Naver)
3. Wybierz typ modelu sieci neuronowej (LSTM, GRU lub LSTM+GRU)
4. Ustaw parametry:
   - Dni Predykcji (1-100): Liczba minionych dni, na których opiera się prognoza
   - Dni Przyszłe (1-10): Ile dni w przyszłość przewidywać
   - Zakres Wykresu (20-600): Zakres dni do wyświetlenia na wykresie

5. Kliknij "Train", aby wytrenować model
6. Kliknij "Plot", aby zwizualizować rzeczywiste vs. przewidywane ceny
7. Kliknij "Gain", aby obliczyć procentową zmianę między ostatnią przewidywaną a rzeczywistą wartością
8. Użyj przycisku "Help", aby uzyskać dodatkowe informacje

## 📁 Struktura Projektu
```
/CryptoCurrencyPP/
│
├── DATA/                    # Historyczne dane kryptowalut
│   ├── BTC.csv              # Dane historyczne Bitcoin
│   ├── DOGE.csv             # Dane historyczne Dogecoin
│   ├── ETH.csv              # Dane historyczne Ethereum
│   ├── LTC.csv              # Dane historyczne Litecoin
│   └── download.py          # Skrypt do pobierania danych
│
├── DOC/                     # Dokumentacja projektu
│   ├── Assumptions.pdf      # Założenia projektu
│   ├── GUI_DEMO.png         # Zrzut ekranu interfejsu GUI
│   ├── Presentation.pdf     # Prezentacja projektu
│   ├── Report.pdf           # Szczegółowy raport projektu
│   └── Experiments/         # Wyniki eksperymentów
│
├── IMPL/                    # Pliki implementacyjne
│   ├── app.py               # Główny punkt wejścia aplikacji z klasą Controller
│   ├── model.py             # Architektura sieci neuronowej i trening
│   ├── view.py              # Implementacja GUI w Tkinter
│   ├── azure.tcl            # Plik motywu Tkinter
│   ├── requirements.txt     # Lista zależności
│   ├── test.csv             # Plik testowy
│   ├── assets/              # Dodatkowe zasoby
│   └── images/              # Obrazy używane w aplikacji
│
└── README.md                # Dokumentacja projektu
```

## 📊 Kluczowe Wnioski

- Modele GRU trenują szybciej niż LSTM, ale LSTM zapewnia bardziej płynne i stabilne prognozy
- Zwiększanie liczby epok poprawia dokładność, ale wydłuża czas treningu
- Zwiększanie liczby dni przyszłych zwykle zmniejsza precyzję prognoz
- Wykorzystanie większej ilości danych historycznych generalnie poprawia wydajność modelu

## 🧠 Architektura Kodu (Wzorzec MVC)
- Model (model.py):
  - Ładuje i przetwarza dane
  - Definiuje i trenuje modele LSTM, GRU i hybrydowe
  - Obsługuje wizualizację danych i obliczanie zysków
- Widok (view.py):
  - GUI zbudowane z Tkinter z motywem Azure
  - Obsługuje wprowadzanie parametrów i wyświetlanie wyników
  - Zapewnia elementy interakcji z użytkownikiem
- Kontroler (app.py):
  - Łączy Widok z Modelem
  - Zarządza logiką i stanem aplikacji
  - Obsługuje interakcje użytkownika

## 📦 Zależności
Projekt został przetestowany 5.05.2025 z Python 3.11.9 i TensorFlow 2.19.
Kluczowe zależności obejmują:
- Python 3.11
- TensorFlow 2.19.0
- Keras 3.9.2
- Pandas 2.2.3
- NumPy 2.1.3
- Matplotlib 3.10.1
- scikit-learn 1.6.1
- yfinance 0.2.58 (zastąpił pandas_datareader)

Pełna lista zależności znajduje się w pliku IMPL/requirements.txt

## 📄 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT.

## 📬 Kontakt

W przypadku pytań, sugestii lub wkładu, proszę otworzyć zgłoszenie lub skontaktować się z opiekunem projektu przez GitHub.

---

# 📚 Cryptocurrency Price Prediction using Neural Networks

---
## 📈 Project Overview

This project predicts cryptocurrency prices using advanced neural network architectures — LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit), and a hybrid LSTM-GRU model. It includes a graphical user interface (GUI) built with Tkinter, allowing users to easily select parameters, visualize results, and interact with the prediction system.

## 🚀 Features

- Multiple Cryptocurrencies: Supports Bitcoin (BTC), Ethereum (ETH), Dogecoin (DOGE), and Litecoin (LTC)
- Flexible Data Sources: Fetches historical data from:
  - Yahoo Finance
  - Stooq
  - Naver
  - Local CSV files
- Neural Network Models:
  - LSTM
  - GRU
  - Hybrid LSTM-GRU
- Interactive GUI:
  - Built with Tkinter with Azure theme
  - Model and data source selection
  - Parameter input controls
- Visualization:
  - Matplotlib charts showing predicted vs. actual prices
- Customizable Parameters:
  - Prediction days (default: 30)
  - Future days (default: 1)
  - Plot range (default: 20)
  - Epochs (default: 100) and batch size (default: 32)

## 🛠️ Installation
1. Clone the Repository
<pre><code>git clone https://github.com/yourusername/cryptocurrency-prediction.git
cd cryptocurrency-prediction</code></pre>
2. Install Required Packages
<pre><code>pip install -r IMPL/requirements.txt</code></pre>

## ▶️ Usage
Run the Application
Be in the IMPL folder
<pre><code>python app.py</code></pre>
In the GUI:
1. Select the cryptocurrency (BTC, ETH, Doge, LTC)
2. Choose the data source (Yahoo, Stooq, Naver)
3. Select the neural network model type (LSTM, GRU, or LSTM+GRU)
4. Set parameters:
   - Prediction Days (1-100): Number of past days to base prediction on
   - Future Days (1-10): How many days into the future to predict
   - Plot Range (20-600): Range of days to display on the chart

5. Click "Train" to train the model
6. Click "Plot" to visualize actual vs. predicted prices
7. Click "Gain" to calculate the percentage change between the last predicted and real value
8. Use "Help" button for additional information

## 📁 Project Structure
```
/CryptoCurrencyPP/
│
├── DATA/                    # Historical cryptocurrency data
│   ├── BTC.csv              # Bitcoin historical data
│   ├── DOGE.csv             # Dogecoin historical data
│   ├── ETH.csv              # Ethereum historical data
│   ├── LTC.csv              # Litecoin historical data
│   └── download.py          # Script for downloading data
│
├── DOC/                     # Project documentation
│   ├── Assumptions.pdf      # Project assumptions
│   ├── GUI_DEMO.png         # Screenshot of the GUI
│   ├── Presentation.pdf     # Project presentation
│   ├── Report.pdf           # Detailed project report
│   └── Experiments/         # Experimental results
│
├── IMPL/                    # Implementation files
│   ├── app.py               # Main application entry point with Controller class
│   ├── model.py             # Neural network architecture and training
│   ├── view.py              # Tkinter GUI implementation
│   ├── azure.tcl            # Tkinter theme file
│   ├── requirements.txt     # List of dependencies
│   ├── test.csv             # Test data file
│   ├── assets/              # Additional assets
│   └── images/              # Images used in the application
│
└── README.md                # Project documentation
```

## 📊 Key Findings

- GRU models train faster than LSTM, but LSTM provides smoother and more stable predictions
- Increasing epochs improves accuracy but also increases training time
- Increasing future days tends to decrease prediction precision
- Using more historical data generally improves the model's performance

## 🧠 Code Architecture (MVC Pattern)
- Model (model.py):
  - Loads and preprocesses data
  - Defines and trains LSTM, GRU, and hybrid models
  - Handles data visualization and gain calculation
- View (view.py):
  - GUI built with Tkinter using Azure theme
  - Handles parameter input and result display
  - Provides user interaction elements
- Controller (app.py):
  - Connects the View with the Model
  - Manages application logic and state
  - Handles user interactions

## 📦 Dependencies
Project was tested on 5.05.2025 with Python 3.11.9 and TensorFlow 2.19.
Key dependencies include:
- Python 3.11
- TensorFlow 2.19.0
- Keras 3.9.2
- Pandas 2.2.3
- NumPy 2.1.3
- Matplotlib 3.10.1
- scikit-learn 1.6.1
- yfinance 0.2.58 (replaced pandas_datareader)

For a complete list of dependencies, see IMPL/requirements.txt

## 📄 License

This project is licensed under the MIT License.

## 📬 Contact

For questions, suggestions, or contributions, please open an issue or contact the project maintainer via GitHub.
