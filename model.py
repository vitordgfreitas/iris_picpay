from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
iris_dict = load_iris()
X = iris_dict['data']
y = iris_dict['target']
from sklearn.utils import shuffle
X_new, y_new = shuffle(X, y, random_state=0)
n_samples_train = 120 
X_train = X_new[:n_samples_train, :]
y_train = y_new[:n_samples_train]

X_test = X_new[n_samples_train:, :]
y_test = y_new[n_samples_train:]
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
import pickle
with open('iris_trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)