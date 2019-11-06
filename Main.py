import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


print("Running tensor flow version =", tf.__version__)

hello = tf.constant('Hello, TensorFlow!')
print(hello)
mnist = tf.keras.datasets.mnist
print(mnist)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train,y_train,x_test,y_test)

print(type(x_train))
print(type(x_test))
x_train, x_test = x_train / 255.0, x_test / 255.0