import joblib

def predict_data(X):
    """
    Predict the wine class labels for the input data.
    Args:
        X (numpy.ndarray): Input data for which predictions are to be made.
    Returns:
        y_pred (numpy.ndarray): Predicted wine class labels.
    """
    model = joblib.load("../model/wine_model.pkl")
    y_pred = model.predict(X)
    return y_pred
