import tensorflow as tf 
import numpy as np 

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('./MNIST', one_hot=True)

#input_layer
x = tf.placeholder(dtype=tf.float32, shape=[None,784], name='x')
#labels
y = tf.placeholder(dtype=tf.float32, shape=[None,10], name='y')

def add_layer(input_data, input_num, output_num, activation_function=None):
	#output = input_data * weight + bias
	w = tf.Variable(initial_value = tf.random_normal(shape=[input_num, output_num]))
	b = tf.Variable(initial_value = tf.random_normal(shape=[1, output_num]))
	output = tf.add(tf.matul(input_data, w), b)
	#activation? output = activation_function(output) : output
	if activation_function:
		output = activation_function(output)
	return output
	

def build_nn(data):
	hidden_layer1 = add_layer(data, 784, 100, activation_function=tf.nn.sigmoid)
	hidden_layer2 = add_layer(hidden_layer1, 100, 50, activation_function=tf.nn.sigmoid)
	output_layer = add_layer(hidden_layer2, 50, 10)
	return output_layer

def train_nn(data):
	# output of NN
	output = build_nn(data)

	loss = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=output)
	optimizer = tf.train.GradientDescentOptimizer(learning_rate=1).minimize(loss)

	for _ in range(50):
		



train_nn(x)


