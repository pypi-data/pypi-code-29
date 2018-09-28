import tensorflow as tf

con_a = tf.constant(3.0)
con_b = tf.constant(4.0)

sum_c = tf.add(con_a,con_b)

print(con_b,con_a,sum_c)

print(tf.get_default_graph())
print(con_b.graph)
print(con_a.graph)
print(sum_c.graph)

with tf.Session() as sess:
    print(sess.run(con_a))
    print(sess.run(con_b))
    print(sess.run(sum_c))
    print(sess.graph)

new_g = tf.Graph()

with new_g.as_default():
    con_d = tf.constant(30.0)

    print(con_d.graph)

with tf.Session(graph=new_g) as new_sess:
    print(new_sess.run(con_d))
    print(new_sess.graph)

