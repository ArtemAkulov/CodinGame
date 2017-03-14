#########################################
#                                       #
#  CodinGame Machine Learning Problems  #
#              Tensorflow               #
#                                       #
#########################################

# Not a problem, per se. And due to the time constraints,
# there's no way to train a more sophisticated neural network
# on their website. 
# My personal best on the MNIST dataset is 0.965 
# which I consider good enough for 15 minutes on a VM
# running on two threads

import tensorflow as tf
import input_data

mnist = input_data.read_data_sets(input(), input(), input())
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()

tf.initialize_all_variables().run()

for _ in range(1500):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

result = sess.run(tf.argmax(y,1), feed_dict={x: mnist.validation.images})

print(' '.join(map(str, result)))