from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
print("---")


print(np.argmax(y_train[1, :])) 


%matplotlib inline

first_train_img = np.reshape(x_train[1, :], (28, 28))
plt.matshow(first_train_img, cmap = plt.get_cmap('gray'))
plt.show()