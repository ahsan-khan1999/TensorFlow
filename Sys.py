import sys
for i in sys.argv[::-1]:
		print('hello',i)

import tensorflow as tf

a = tf.constant([2])
b= tf.constant([3])

c= tf.add(a,b)
# tf.device()
# session = tf.Session()
# result = session.run(c)
# print(result)
# session.close()

#due to this with block tf will automatically close the session
with tf.Session() as session:
	result = session.run(c)
	print(result)
