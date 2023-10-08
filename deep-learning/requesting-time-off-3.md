---
description: >-
  In this lesson, we will investigate how to efficiently do transfer learning so
  we are not re-inventing the wheel every time.
---

# 🌐 Transfer Learning

### Transfer Learning <a href="#transfer-learning" id="transfer-learning"></a>

Let's start this lesson by getting to the main topic - transfer learning:

* [https://cs231n.github.io/transfer-learning/](https://cs231n.github.io/transfer-learning/)
* [https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
* [https://www.youtube.com/watch?v=yofjFQddwHE](https://www.youtube.com/watch?v=yofjFQddwHE)

As you learned in the material above, transfer learning is a very simple but very powerful concept. It is a way to infuse a general purpose model with some domain specific knowledge, which can then be used for tasks which will have comparable datasets, e.g. you would want to predict tumors in x-rays shot with a model pretrained for dog/cat classiification.

Let's see how easy it is to do transfer learning in PyTorch.

`torch.vision` module has models pre-trained on [Imagenet](http://www.image-net.org/about). You can [check it out here](https://pytorch.org/vision/stable/models.html). Select one of the available well-known architectures and PyTorch API allows to very simply pull a pre-trained model and use it for our purposes.

#### Matching image sizes <a href="#matching-image-sizes" id="matching-image-sizes"></a>

When you train a neural network, it is common to have images of different sizes. But you must make your images the same size, otherwise, you won't be able to make batches of tensors. In research, the most commonly used image sizes are `224 x 224 x 3` and `299 x 299 x 3`. While internals of some architectures can work with arbitrary sized images, others with fail, if an image is not the size it expects. Moreover, if it is largely different, you will get unpredictable results. So step 1 when using transfer learning is to understand the size of the image that was used with your particular architecture.

For ResNet architectures, it is \[224 x 224 x 3]. Since our image is not a perfect square, we will first resize it to \[224, N] maintaining aspect ratio (where N > 224), and then we will crop the center of it to \[224, 224]. We can do all of that using PyTorch transforms

#### Normalization <a href="#normalization" id="normalization"></a>

One important thing to remember when using pre-trained networks is to always perform the same image normalization that was used when training the net. There is a variety of techniques to normalize images and usually, they vary by framework. For example, for networks pre-trained on ImageNet:

* PyTroch: scale images to have 0 mean and 1 standard deviation
* Tensorflow: normalize pixel values between -1 and 1
* Caffe: scale to 0 mean only

The reason why images are normalized is in order to have the same distributions over different color layers of images. We have learned that filters in a CNN always span the full depth of an image. If we have different data distributions, it is harder for a network to reach the global minimum of a cost function. There are ways to compensate for this, like different learning rates per dimension, but this only adds complexity and more hyper-parameters to track. So by normalizing images, a neural net is able to converge better while keeping the net complexity low.

#### FastAI <a href="#fastai" id="fastai"></a>

For your exercise today you will be using another deep learning framework called FastAI. You already know how to efficiently work with PyTorch and PyTorch-Lightning. It is good for you to also familiarize yourself with FastAI since it could be a good place to start when doing modeling. This library is a very high-level wrapper of PyTorch, meaning the core is still all PyTorch. But it abstracts a lot of the concepts for users, so experimenting with different architectures is a breeze. Moreover, the creators of this framework have put all of the best practices into it, so with default settings, you would be getting optimal results and taking advantage of years of deep learning research.

Learn how to use FastAI [https://docs.fast.ai/tutorial.vision.html](https://docs.fast.ai/tutorial.vision.html)

### Exercise <a href="#exercise" id="exercise"></a>

An AuPair agency for problematic kids has contacted you with a request. They want to install cameras in children's rooms to automatically track how children's behavior is improving and one of the factors is to know how often they clean up a messy room. So your job is to build a model, that can automatically detect if a room is clean or messy from images.

You will use [https://www.kaggle.com/cdawn1/messy-vs-clean-room](https://www.kaggle.com/cdawn1/messy-vs-clean-room) dataset to train and validate your model

Requirements:

* EDA (including visualizing data)
* Use transfer learning. Select your base model from one of the available architectures. Check FastAI documentation for available pre-trained models
* Fine-tune the pre-trained model
* Evaluate training metrics
* Bonus:
  * Build a custom architecture and train it without transfer learning.
  * Compare results with pre-trained model.
