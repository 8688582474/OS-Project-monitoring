import pandas as pd
import random

def generate_random_usage_data(max_intervals: int = 50):
    data = []
    for _ in range(max_intervals):
        row = {
            'CPU': round(random.uniform(10, 95), 2),
            'RAM': round(random.uniform(20, 90), 2),
            'Disk': round(random.uniform(30, 85), 2)
        }
        data.append(row)
    return pd.DataFrame(data)

def save_to_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
