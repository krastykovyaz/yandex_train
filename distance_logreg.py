import numpy as np


# euclidian distance between two points
def distance(color1, color2):
    return np.sqrt(np.sum([(x - y) ** 2 for x, y in zip(color1, color2)]))

# orthogonal projection between 2 vectors
def projection(vec, normal):
    return normal * ((normal @ vec) / (normal @ normal))

def projection_on_plane(normal, vec):
    return vec - projection(vec, normal)

# euclidian norm and cosine distance
def euclidian_norm(color):
    return np.sqrt(np.sum([x ** 2 for x in color]))


# implement a function that computed Euclidian norm between two colors in the RGB
def dot_prod(color1, color2):
    return np.sum([x * y for x, y in zip(color1, color2)])


# cosine betwee 2 vectors
def cosine(color1, color2):
    enum = dot_prod(color1, color2)
    color1_norm = euclidian_norm(color1)
    color2_norm = euclidian_norm(color2)
    denom = color1_norm *color2_norm
    return  enum / denom

# sigmoid function for log reg
def sigmoid(w,x,b):
    linear = w @ x + b
    return 1 / (1 + np.exp(-linear))

# binary cross entropy
def loss(y_hat, y):
    return -np.mean((y * np.log(y_hat)) + ((1 - y) * np.log(1 - y_hat)))

def gradient(y_hat, X, y):
    m = X.shape[0]
    dw = (X.T @ (y_hat - y)) / m
    db = (np.sum(y_hat - y)) / m
    return dw, db

def normalize(X):
    f = lambda x: (x - np.mean(X)) / X.std(axis=0)
    return [f(val) for val in X]

def learning_cycle(w, X, b, y, epochs=100, lr=0.01):
    X = normalize(X)
    losses = []
    for epoch in epochs:
        y_hat = sigmoid(w, X, b)
        l = loss(y_hat, y)
        dw, db = gradient(X, y_hat, y)
        w -= lr * dw
        b -= lr * db
        losses.append(loss)





