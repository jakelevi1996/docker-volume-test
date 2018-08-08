# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:55:54 2018

@author: Jake
"""

#Imports
print("Starting imports...")
import tensorflow as tf
import numpy as np
# Before importing pyplot, set the matplotlib backend to allow usage in Docker container
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("Creating model...")

#Parameters
num_epochs = int(3000)
learning_rate = 0.01
print_every = 1000
logdir = "./Summaries/Classification"
savedir = "./models/classification_model.ckpt"


# Create training data set
x_data = np.random.randn(1000,2)
y_true = np.array(1 * (x_data[:,0]**2 + x_data[:,1]**2) < 1).reshape(-1, 1)

# Create grid for evaluation
x_array = np.linspace(-4, 4, 100)
xx0, xx1 = np.meshgrid(x_array, x_array)
x_grid_eval_vec = np.concatenate((xx0.reshape(-1,1),
                                  xx1.reshape(-1,1)),
                                 axis=1)

##Create tf.data.Dataset object
##TODO: split into training and test sets
#sliced_dataset = tf.data.Dataset.from_tensor_slices(x_data)
#next_item = sliced_dataset.make_one_shot_iterator().get_next()

# Define network
# Regulariser ??
x = tf.placeholder(dtype=tf.float32, shape=(None,2))
hidden_layer = tf.layers.dense(inputs=x, units=4, activation=tf.tanh)
logits = tf.layers.dense(inputs=hidden_layer, units=1,)
y = tf.sigmoid(logits)


# Define loss and optimiser
loss = tf.losses.sigmoid_cross_entropy(y_true, logits)
accuracy = tf.reduce_mean(tf.cast(tf.equal(y, y_true), tf.float32)) # need y>.5
adam = tf.train.AdamOptimizer(learning_rate)
train_op = adam.minimize(loss)

# Create Saver object for saving
saver = tf.train.Saver()

# Create op for initialising variables
init_op = tf.global_variables_initializer()

# Create summaries, for visualising in Tensorboard
tf.summary.scalar("Loss", loss)
tf.summary.scalar("Accuracy", accuracy)
tf.summary.histogram("Hidden_layer_activations", hidden_layer)
tf.summary.histogram("Logits", logits)
# tf.summary.histogram("Gradients", adam.compute_gradients(loss))
summary_op = tf.summary.merge_all()

# Train and save the model
with tf.Session() as sess:
    print("Opening FileWriter...")
    writer = tf.summary.FileWriter(logdir, sess.graph)
    print("Initialising variables...")
    sess.run(init_op)
    print("Starting loop...\n{}".format("-"*15))
    # Training loop:
    for epoch in range(num_epochs):
        # Run the graph, summaries and training op
        loss_val, summary_val, _ = sess.run((loss, summary_op, train_op),
                                            feed_dict={x: x_data})
        # Add summary to Tensorboard
        writer.add_summary(summary_val, epoch)
        # Display progress every few epochs
        if epoch % print_every == 0:
            print("Epoch: {:<8} | Loss: {:<.6f}".format(epoch, loss_val))
    # Evaluate final loss and summary
    loss_val, sum_val, _ = sess.run((loss, summary_op, train_op),
                                    feed_dict={x: x_data})
    print("Epoch: {:<8} | Loss: {:<.6f}".format(num_epochs, loss_val))
    
    # Save model
    save_path = saver.save(sess, savedir)



# Restore and evaluate the model
with tf.Session() as eval_sess:
    saver.restore(eval_sess, save_path)
    print("Model restored")
    y_grid_eval = y.eval(feed_dict={x: x_grid_eval_vec}).reshape(xx0.shape)
    

# Plot results
plt.plot(x_data[y_true[:,0]==0, 0], x_data[y_true[:,0]==0, 1], 'bo',
         x_data[y_true[:,0]==1, 0], x_data[y_true[:,0]==1, 1], 'ro',
         alpha=.1)
# plt.pcolor(xx0, xx1, y_grid_eval, cmap='bwr')
# plt.colorbar()
plt.contour(xx0, xx1, y_grid_eval, [.2, .4, .6, .8], cmap='bwr')
plt.grid(True)
plt.axis('equal')
plt.savefig("classification results.png")
print("Graph saved")
# plt.show()