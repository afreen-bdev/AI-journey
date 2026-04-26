from sklearn.linear_model import LinearRegression
import pickle

model = LinearRegression()

X = [[1], [2], [3]]
y = [2, 4, 6]

model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model saved!")