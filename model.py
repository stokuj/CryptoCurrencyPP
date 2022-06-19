from locale import currency
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

class Model():
    def __init__(self):
        pass
     

    crypto_currency     = 'BTC'
    against_currency    = 'USD'
    data_source         = 'yahoo'
    use_online_db = True
    start = dt.datetime(2016,1,1)
    end = dt.datetime.now()

    data = web.DataReader(f'{crypto_currency}-{against_currency}', data_source, start, end)
    scaler = MinMaxScaler(feature_range=(0,1))

    prediction_days = 30
    future_day = 1

    x_train, y_train = [], []
    
    model_id = 1
    model = Sequential()


    def train(self):

        self.x_train, self.y_train = [], []
        self.model = Sequential()

        if(self.use_online_db):
            print('use_online_db')
            self.data = web.DataReader(f'{self.crypto_currency}-{self.against_currency}', self.data_source, self.start, self.end)
        else:
            print('NOOO')
            filename = "test.csv"
            data = pd.read_csv(filename)


        scaled_data = self.scaler.fit_transform(self.data['Close'].values.reshape(-1,1))

        for x in range(self.prediction_days, len(scaled_data)-self.future_day):

            self.x_train.append(scaled_data[x - self.prediction_days:x, 0])
            self.y_train.append(scaled_data[x + self.future_day, 0])

        self.x_train, self.y_train = np.array(self.x_train), np.array(self.y_train)
        self.x_train = np.reshape(self.x_train, (self.x_train.shape[0], self.x_train.shape[1], 1))

        ### Create Neural Network

        if self.model_id == 1:
            print('Model1')
            self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.x_train.shape[1], 1)))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(units=50, return_sequences=True))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(units=50))
            self.model.add(Dropout(0.2))
            self.model.add(Dense(units=1))

        elif self.model_id == 2:
            print('Model2')    
            self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.x_train.shape[1], 1)))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(units=50, return_sequences=True))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(units=50))
            self.model.add(Dropout(0.2))
            self.model.add(Dense(units=1))
        else:
            print('Model3')
            self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.x_train.shape[1], 1)))
            self.model.add(Dropout(0.30))
            self.model.add(LSTM(units=50, return_sequences=True))
            self.model.add(Dropout(0.30))
            self.model.add(LSTM(units=50))
            self.model.add(Dropout(0.30))
            self.model.add(Dense(units=1))

        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(self.x_train, self.y_train, epochs=5, batch_size=32)

    def plot(self):
        print(self.crypto_currency)
        test_start  = dt.datetime(2022,1,23) #+ dt.timedelta(days=-prediction_days)
        test_end    = dt.datetime.now() + dt.timedelta(days=self.future_day)
        print ("test_start", str(test_start))
        print ("test_end", str(test_end))

        test_data = web.DataReader(f'{self.crypto_currency}-{self.against_currency}', 'yahoo', test_start, test_end)
        actual_prices = test_data['Close'].values

        total_dataset = pd.concat((self.data['Close'], test_data['Close']), axis=0)

        model_inputs = total_dataset[len(total_dataset) - len(test_data) - self.prediction_days:].values
        model_inputs = model_inputs.reshape(-1, 1)
        model_inputs = self.scaler.fit_transform(model_inputs)

        x_test = []

        for x in range(self.prediction_days , len(model_inputs)):
            x_test.append(model_inputs[x - self.prediction_days :x, 0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

        prediction_prices = self.model.predict(x_test)
        prediction_prices = self.scaler.inverse_transform(prediction_prices)

        plt.plot(actual_prices, color='cyan', label='Actual Prices')
        plt.plot(prediction_prices, color='indigo', label='Predicted Prices')
        plt.title(f'CryptoCurrency Price Prediction')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend(loc='upper right')
        plt.show()

    def Alert():
        print('hello')

    def setCurrency(self, i):
        if i == 1:
            self.crypto_currency = 'BTC'
        if i == 2:
            self.crypto_currency = 'ETH'
        if i == 3:
            self.crypto_currency = 'DOGE'
        if i == 4:
            self.crypto_currency = 'LTC'
        print('currency is being set to')
        print(i)
            
    def setDataSource(self,i):
        if i == 1:
            self.data_source    = 'yahoo'
        if i == 2:
            self.data_source    = 'stooq'
        if i == 3:
            self.data_source    = 'naver'
        print('data source is being set to')
        print(i)      

    def setModelId(self,i):
        if i == 1:
            self.model_id   = 1
        if i == 2:
            self.model_id   = 2
        if i == 3:
            self.model_id   = 3
        print('model is being set to')
        print(i)     

    def setFilePath(self, p):
        self.filename = p
        print(p)  

    def setSwitchState(self, i):
        if i == 1:
            self.use_online_db = True
        else:
            self.use_online_db = False
        print('switchstate',i)

    def setPreditionDays(self, i):
        self.prediction_days = i