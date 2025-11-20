import pandas as pd
import psutil
import time
import numpy as np

def get_past_system_metrics(samples: int = 10, interval: float = 1.0):
    data = []
    for _ in range(samples):
        cpu = psutil.cpu_percent(interval=interval)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        data.append({'CPU': cpu, 'RAM': ram, 'Disk': disk})
    df = pd.DataFrame(data)
    return df, 'minutes'

def predict_future_trends(data: pd.DataFrame, hours: float, interval: int):
    from sklearn.linear_model import LinearRegression

    num_points = int((hours * 60) / interval)
    predictions = []

    for column in data.columns:
        X = np.arange(len(data)).reshape(-1, 1)
        y = data[column].values
        model = LinearRegression()
        model.fit(X, y)
        X_future = np.arange(len(data), len(data) + num_points).reshape(-1, 1)
        y_pred = model.predict(X_future)
        predictions.append(pd.Series(y_pred, name=column))

    future_df = pd.concat(predictions, axis=1)
    return future_df

def load_user_data_from_csv(path: str):
    return pd.read_csv(path)
