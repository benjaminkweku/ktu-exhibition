import tensorflow as tf
tf.enable_eager_excution()
print(tf.reduce_sum(tf.random_normal([1000,1000])))