import pandas as pd
import pickle
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder


def getData(data):
    model = load_model()
    print("GOT MODEL")
    print(data)
    df = dictToDf(data)
    # print("Data Type", df.head())
    labelEncode = LabelEncoder()
    for i in df:
        df[i] = labelEncode.fit_transform(df[i])
    print("DataFrame",df.dtypes)
    result = model.predict(df)
    return result[0]
    


def load_model():
    return joblib.load(
        "/home/andrew/ML/data_science/Is_Project/revised_attrition_model/attrition_model.pkl"
    )


def dictToDf(data):
    return pd.DataFrame(data, index=[0])
    # return type(data)