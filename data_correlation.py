import numpy as np

def correlation(data, checking_feature):
    numeric_data = data.select_dtypes(include=[np.number])
    correlation = numeric_data.corr()

    correlation_table=correlation[checking_feature].sort_values(ascending=False)
    return correlation_table

