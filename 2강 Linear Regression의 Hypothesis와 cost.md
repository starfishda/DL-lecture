## 2강 Linear Regression의 Hypothesis와 cost

0~100 사이의 점수를 예측하는 프로그램은 <b>supervised learning</b> 중에서도 <b>regression</b>이다.

학습을 시키는 과정을 <b>training</b><br>
학습 시키는데 필요한 데이터를 <b>training data</b> 라고 한다.<br>
  training 시켜서 나온 regression 모델을 통해 예측을 할 수 있다.<br>
  linear 학습을 한다는 것은 데이터에 알맞은 선을 찾는다는 것<br>

Hypothesis = 가설<br>
H(x) = Wx + b<br>
H(x) = Wx + b -> 가장 데이터와 일치하는 H(x)를 찾는다.<br>

점과 직선사이의 거리가 멀면 좋지 않은 것 점과 직선이 가까울 수록 좋은 것이다.<br>
이것을 판단하는 것이 cost이다.<br>
cost = 우리가 세운 가설이 실제와 얼마나 다른가<br>
cost = (H(x) - y)**2 = 가설로 만든 직선과 실제 y값과의 차이 <br>
