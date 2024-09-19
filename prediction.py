import pandas as pd
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def make_prediction(data):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return prediction