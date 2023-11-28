import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

#This function downloads the data from Kaggle
def downloading_data(name_of_dataset, download_path):

    dataset_name = name_of_dataset
    api = KaggleApi()
    api.authenticate()

    our_path = download_path

    try:
        api.dataset_download_files(dataset_name, path=our_path, unzip=True)
        return print(f"Dataset '{dataset_name}' başarıyla indirildi ve kullanıma hazır.")
    except Exception as e:
        return print(f"Hata oluştu: {e}")

#Reading of data
def reading_data(path):
    data = pd.read_csv(path)
    return data

#This function checks if there any null values in the data and convert the null data to mean value of related column
def checker_and_converter_of_nulldata(data):

    print(data.isnull().sum())
    null_check = data.isnull().any()
    if null_check.any():
        for column in data.columns:
            if data[column].isnull().any():
                mean_value = data[column].mean()
                data[column].fillna(mean_value, inplace=True)
                print(f"{column} has null values and changed with mean in related column which is {mean_value} ")
    else:
        print("Data hasn't any null values at any column")



