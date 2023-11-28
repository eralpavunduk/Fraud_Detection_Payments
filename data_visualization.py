import plotly.express as px

def visualization(data):
    print(data.type.value_counts())

    type = data["type"].value_counts()
    transactions = type.index
    quantity = type.values

    figure = px.pie(data,
                 values=quantity,
                 names=transactions,hole = 0.5,
                 title="Distribution of Transaction Type")
    return figure.show()