import tensorflow as tf

def create_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(64, input_shape=(6, 1)))
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def predict_values(model, data):
    val = data.get('high')
    predict = model.predict(val)
    return predict[0][0]