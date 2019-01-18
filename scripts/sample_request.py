import requests
import json

import numpy as np
import pandas as pd
from sklearn.datasets import load_wine


# load data
wine = load_wine()
data = pd.DataFrame(data=np.c_[wine['data'], wine['target']],
                    columns=wine['feature_names'] + ['target'])
data = data.sample(frac=1)   # to shuffle rows
X_train = data[:-20]
X_test = data[-20:]
y_train = X_train.target
y_test = X_test.target
X_train = X_train.drop('target', 1)
X_test = X_test.drop('target', 1)

# send one to API
url = 'http://a08datasc003.cdbdx.biz:5000/api/'

for i in range(10):
    data = [X_test.iloc[i].values.tolist()]
    j_data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    print('truth:', y_test.iloc[i], 'predicted:', r.text)
