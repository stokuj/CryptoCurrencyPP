# 📚 Cryptocurrency Price Prediction using Neural Networks

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
Be in IMPL folder
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
