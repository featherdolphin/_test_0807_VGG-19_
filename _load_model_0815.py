import tensorflow as tf
import cv2
from tensorflow.keras.datasets import mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()

new_x_test = x_test.astype("float32")/255.0
model = tf.keras.models.load_model("ngoo's_nn_model_0815_v9.h5")
predictions = model.predict(new_x_test[:5])

for i in range(len(predictions)):
    
    print(predictions[i])
    
    maxValue = 0
    value = 0
    for j in range(len(predictions[i])) :
        if predictions[i][j] > maxValue:
            maxValue = predictions[i][j]
            value = j
    print(value)
    print(y_test[i])
    if value == y_test[i]:
        print("the same")
    else:
        print("not the same")

    cv2.imshow("win", x_test[i])
    print(list[y_test])
    cv2.waitKey(0)