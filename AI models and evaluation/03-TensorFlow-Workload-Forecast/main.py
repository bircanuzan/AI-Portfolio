"""TensorFlow/Keras synthetic demand regression with separate validation set."""
import numpy as np
import tensorflow as tf

tf.keras.utils.set_random_seed(17)
rng = np.random.default_rng(17)
features = rng.random((320, 3)).astype("float32")
target = (8 + 10 * features[:, 0] + 4 * features[:, 1]
          - 3 * features[:, 2] + rng.normal(0, .3, 320)).astype("float32")
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1),
])
model.compile(optimizer=tf.keras.optimizers.Adam(0.02), loss="mse", metrics=["mae"])
model.fit(features[:250], target[:250], epochs=35, verbose=0)
loss, mae = model.evaluate(features[250:], target[250:], verbose=0)
print({"holdout_MAE": round(float(mae), 3), "n_test": len(target[250:])})
print("All measurements are synthetic, not operational forecasts.")
