import tensorflow as tf


# 1. Hello TensorFlow 출력시키기

# "Hello"라는 형태의 costant를 만든다. 이 constant의 이름은 hello로 지정
hello = tf.constant("Hello, TensorFlow!") #constant 라는 노드를 만들어주는것.

# 그래프의 노드를 실행시키기 위해 sess라는 변수를 만들어준다.
sess = tf.Session()

# hello라는 노드를 출력시킨다.
print(sess.run(hello))


# 2. node 값 출력시키기

# 그래프를 만들어서 계산할 때 노드에 미리 값을 넣어주는 형식
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) #자동적으로 float32 변수
node3 = tf.add(node1, node2) # node3 = node1 + node2

# 아래와 같이 출력시키면 node의 Tensor 타입이 출력되는 것을 볼 수 있다.
print("node1 :", node1, "node2 :", node2)
print("node3 :", node3)

# 노드 값을 출력시키기 위해서는 session이 필요하다.
print(sess.run([node1, node2]))
print(sess.run([node3])) # 값이 하나 일때는 [] 괄호가 필요없다.


# 3. Placeholder - 그래프는 미리 만들어두고 노드 안의 값은 나중에 넣어주는 방식
a = tf.placeholder(tf.float32) #placeholder 형식의 노드를 만들어 준다.
b = tf.placeholder(tf.float32)
adder_node = a + b # tf.add(a,b)

# feed_dict => 비어 있는 노드에 값을 채워준다.
print(sess.run(adder_node, feed_dict={a : 3, b : 4.5}))
print(sess.run(adder_node, feed_dict={a : [1,3], b : [2,4]})) # a와 b에 2개 이상의 값을 넘겨준 때 사용
