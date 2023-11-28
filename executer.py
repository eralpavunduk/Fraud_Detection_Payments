from data_correlation import correlation
from Config import data_set, downloading_path, reading_path
from Helpers.preparing_data import downloading_data, reading_data
from fraud_detector import detector
from data_visualization import visualization

def download_the_data(our_data_set, our_downloading_path):
    downloader = downloading_data(our_data_set, our_downloading_path)
    return


def correlation_of_fraud_feature(data, name_of_the_feature):
    our_correlation = correlation(data, name_of_the_feature)
    return print(our_correlation)

def fraud_detector(data):
    our_detector = detector(data)
    return print(our_detector)

def visualizing_payments(data):
    our_visualized_graph = visualization(data)
    return print(our_visualized_graph)


our_data = reading_data(reading_path)
download_the_data(data_set, downloading_path)
correlation_of_fraud_feature(our_data, "isFraud")
fraud_detector(our_data)
visualizing_payments(our_data)









