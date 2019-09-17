import tensorflow as tf
# tf.__version__
print(tf.__version__)

graph1 = tf.Graph()

with graph1.as_default():
    a = tf.constant([2],name="constant_a")
    b = tf.constant([3],name= "constant_b")

# print(a)

ses = tf.Session(graph=graph1)
result = ses.run(a)
print(result)
ses.close()

with graph1.as_default():
    c = tf.add(a,b)

sess = tf.Session(graph=graph1)
result = sess.run(c)
print(result)
sess.close()