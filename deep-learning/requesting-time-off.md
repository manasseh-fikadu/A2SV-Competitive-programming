---
description: >-
  The plan for this lesson is to take a very low-level look into classical
  neural networks and try to understand what is a neuron and how the network of
  them can reach superhuman predictive power.
---

# 🕸 Deep Learning Fundamentals

Let's start the journey into deep learning by understanding what is a neuron, what is a neural network and get an idea of what happens inside vanilla neural networks (aka multilayer perceptrons)

What is neural network\
[https://www.youtube.com/watch?v=n1l-9lIMW7E\&list=PLkDaE6sCZn6Ec-XTbcX1uRg2\_u4xOEky0\&index=2](https://www.youtube.com/watch?v=n1l-9lIMW7E\&list=PLkDaE6sCZn6Ec-XTbcX1uRg2\_u4xOEky0\&index=2)

Supervised learning with neural networks\
[https://www.youtube.com/watch?v=BYGpKPY9pO0\&list=PLkDaE6sCZn6Ec-XTbcX1uRg2\_u4xOEky0\&index=3](https://www.youtube.com/watch?v=BYGpKPY9pO0\&list=PLkDaE6sCZn6Ec-XTbcX1uRg2\_u4xOEky0\&index=3)

Why is deep learning taking off\
[https://www.youtube.com/watch?v=xflCLdJh0n0\&list=PLkDaE6sCZn6Ec-XTbcX1uRg2\_u4xOEky0\&index=4](https://www.youtube.com/watch?v=xflCLdJh0n0\&list=PLkDaE6sCZn6Ec-XTbcX1uRg2\_u4xOEky0\&index=4)

But what is a Neural Network? | Deep learning, chapter 1\
[https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk)

If the theory makes sense, let's go straight into practice. Let's try to implement a neuron to get a better intuition of how these concepts transfer into code.

We will try to implement a neuron that has only one connection (input), something like Andrew Ng drew in his video.

![](https://miro.medium.com/max/1826/1\*L9xLcwKhuZ2cuS8fF0ZjwA.png)

"OpenAI recently published GPT-3, the largest language model ever trained. GPT-3 has 175 billion parameters and would require 355 years and $4,600,000 to train - even with the lowest priced GPU cloud on the market"\[[quote](https://lambdalabs.com/blog/demystifying-gpt-3/)]

What are neural networks, gradient descent, how neural networks learn

* [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk)
* [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w)
* [https://www.youtube.com/watch?v=Ilg3gGewQ5U](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
* [https://www.youtube.com/watch?v=tIeHLnjs5U8](https://www.youtube.com/watch?v=tIeHLnjs5U8)

Resources for a more in-depth back propagation calculus

* [https://cs231n.github.io/optimization-2/](https://cs231n.github.io/optimization-2/)
* [https://alexander-schiendorfer.github.io/2020/02/24/a-worked-example-of-backprop.html](https://alexander-schiendorfer.github.io/2020/02/24/a-worked-example-of-backprop.html)

Let's see how these concepts implement in practice

There are a couple of things our neuron is missing:

* Loss function.
* Activation function

Let's start with the latter. An important part of a neuron is to use some activation function to bound the output values, introduce non-linearity (since we saw that neurons are basically linear functions) as well as normalize them. There is a variety of different activation functions, but the most popular are Sigmoid, Tanh and ReLU.

* [https://www.analyticsvidhya.com/blog/2020/01/fundamentals-deep-learning-activation-functions-when-to-use-them/](https://www.analyticsvidhya.com/blog/2020/01/fundamentals-deep-learning-activation-functions-when-to-use-them/)
* [https://ml-cheatsheet.readthedocs.io/en/latest/activation\_functions.html](https://ml-cheatsheet.readthedocs.io/en/latest/activation\_functions.html)

Next, a crucial ingredient for any network is cost and loss functions. A lot of the times these terms are used interchangeably and both represent how well your model is doing. Loss function represents how far your prediction is from the actual value, e.g. euclidean distance between vectors. Cost function is more general and it represents loss on multiple samples (batches or whole dataset). It also sometimes contain additional parameters, e.g. regularization. By finding the weights of a NN which has the lowest cost, we optimize the network.

* [https://medium.com/@zeeshanmulla/cost-activation-loss-function-neural-network-deep-learning-what-are-these-91167825a4de](https://medium.com/@zeeshanmulla/cost-activation-loss-function-neural-network-deep-learning-what-are-these-91167825a4de)
* [https://www.youtube.com/watch?v=QBbC3Cjsnjg](https://www.youtube.com/watch?v=QBbC3Cjsnjg)

Great! We are just missing the last crucial part in our neuron - optimization

#### Optimizers <a href="#optimizers" id="optimizers"></a>

Last part of the lesson is to learn about optimizers, what they are, different types and what features each bring into the training process of our network.

* [https://d2l.ai/chapter\_optimization/](https://d2l.ai/chapter\_optimization/)
* [https://towardsdatascience.com/deep-learning-optimizers-hard-not-3f5c4f7b4e96](https://towardsdatascience.com/deep-learning-optimizers-hard-not-3f5c4f7b4e96)
* [https://medium.com/datadriveninvestor/overview-of-different-optimizers-for-neural-networks-e0ed119440c3](https://medium.com/datadriveninvestor/overview-of-different-optimizers-for-neural-networks-e0ed119440c3)
* [https://www.youtube.com/watch?v=mdKjMPmcWjY](https://www.youtube.com/watch?v=mdKjMPmcWjY)

