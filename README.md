# 📚 Cryptocurrency Price Prediction using Neural Networks

## 📈Project Overview

This project predicts cryptocurrency prices using advanced neural network architectures — LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit), and a hybrid LSTM-GRU model. It includes a graphical user interface (GUI) built with Tkinter, allowing users to easily select parameters, visualize results, and interact with the prediction system.

## 🚀 Features

- Multiple Cryptocurrencies: Supports Bitcoin (BTC), Ethereum (ETH), Dogecoin (DOGE), and Litecoin (LTC)
- Flexible Data Sources: Fetches historical data from:
- Yahoo Finance
  - Stooq
  - Local CSV files
- Neural Network Models:
  - LSTM
  - GRU
  - Hybrid LSTM-GRU
- Interactive GUI:
  - Built with Tkinter
  - Model and data source selection
  - Parameter input controls
- Visualization:
  - Matplotlib charts showing predicted vs. actual prices
- Customizable Parameters:
  - Prediction days (default: 50)
  - Future days (default: 1)
  - Test range (default: 100)
  - Epochs and batch size

## 🛠️ Installation
1. Clone the Repository
<pre><code>git clone https://github.com/yourusername/cryptocurrency-prediction.git cd cryptocurrency-prediction </code></pre>
2. Install Required Packages
<pre><code>pip install tensorflow keras pandas numpy matplotlib pandas_datareader </code></pre>
## ▶️ Usage
Run the Application
<pre><code>python app.py </code></pre>
In the GUI:
Select the cryptocurrency and data source.
Choose the neural network model type (LSTM, GRU, or Hybrid).
Set parameters:
 - Prediction Days
 - Future Days
 - Test Range

Click Train to train the model.

Click Plot to visualize actual vs. predicted prices.

Click Gain to calculate the percentage change between the last predicted and real value.

## 📁 Project Structure
```
/cryptocurrency-prediction/
│
├── app.py                   # Main application entry point
├── model.py                 # Neural network architecture and training
├── view.py                  # Tkinter GUI implementation
├── controller.py            # Handles logic and user interactions
├── dane/                    # Katalog na wygenerowane dane
│   └── books.csv            # Plik wynikowy z danymi książek
└── requirements.txt         # List of dependencies
```

## 📊 Key Findings

 - GRU models train faster than LSTM, but LSTM provides smoother and more stable predictions.
 - Increasing epochs improves accuracy but also increases training time.
 - Increasing future days tends to decrease prediction precision.
 - Using more historical data generally improves the model's performance.

## 🧠 Code Architecture (MVC Pattern)
 - Model (model.py):
  - Loads and preprocesses data
  - Defines and trains LSTM, GRU, and hybrid models
 - View (view.py):
  -  GUI built with Tkinter
  -  Handles parameter input and result display
 - Controller (controller.py):
  - Connects the View with the Model
  - Manages application logic and state

## 📦 Dependencies
Project was tested 5.05.2025 with python 3.11.9 and tensorflow 2.19.
pandas_datareader had to be raplaced with yfinance module.
 - Python 3.11
 - TensorFlow
 - Keras
 - Pandas
 - NumPy
 - Matplotlib
 - yfinance

## 📄 License

This project is licensed under the MIT License.

## 📬 Contact

For questions, suggestions, or contributions, please open an issue or contact the project maintainer via GitHub.
