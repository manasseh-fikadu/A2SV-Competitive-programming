---
description: >-
  Today we will learn how to use PyTorch - probably one of the most versatile
  (subjective opinion) and widely used framework.
---

# 🖼 Convolutional Neural Networks

In today's lesson, we are going to take a deep dive into convolutional neural networks (CNN). We will learn what they are, how they work, and how they are different from the fully connected neural networks we saw in the previous lesson. CNNs have revolutionized the computer vision field as they brought spatial invariance (it does not matter in which part of an image a dog is, as long as it is there, is what matters) as well as computational efficiency. In this lesson, we will start by understanding what is convolution is CNN, then you will build your first neural network using PyTorch.

Get's get started with listening to lecture on this topic from Stanford university

* [https://youtu.be/bNb2fEVKeEo](https://youtu.be/bNb2fEVKeEo)

Also below are course notes from Stanford University for a course on CNNs. Bookmark this resource as this is the holy grail for computer vision

* [https://cs231n.github.io/convolutional-networks/](https://cs231n.github.io/convolutional-networks/)

Additional

* [https://www.youtube.com/watch?v=m8pOnJxOcqY](https://www.youtube.com/watch?v=m8pOnJxOcqY)
* [https://towardsdatascience.com/applied-deep-learning-part-4-convolutional-neural-networks-584bc134c1e2](https://towardsdatascience.com/applied-deep-learning-part-4-convolutional-neural-networks-584bc134c1e2)

So as you have seen in the material above, CNNs traverse a number of small filters on an image (apply convolution). Let's see how this looks in code

#### Exercise <a href="#exercise" id="exercise"></a>

To get a better understanding of convolutional layers, let's implement the first one ourselves.

Tasks:

* Make function, which given an image and a filter calculates their convolution. Refer to material above for guidance
* Load a random image from MNIST dataset. PyTorch has an easy access to this.
* Display the image and its shape
* Convert the image to a tensor. Use [PyTorch transforms](https://pytorch.org/vision/stable/transforms.html) for this operation
* Convert convolved tensor back to image and display it. Again, use PyTorch transforms

#### Exercise <a href="#exercise" id="exercise"></a>

This was probably the only time in your life where you implemented a convolutional operation manually. You won't have to worry about this since frameworks like PyTorch have implemented this for us. So let's check it out if our implementation does what PyTorch is doing. You should see [https://pytorch.org/docs/stable/nn.functional.html#conv2d](https://pytorch.org/docs/stable/nn.functional.html#conv2d) for guidance

* Implement the same functionality using PyTorch
* Visualize activation

### Building a Fashion-MNIST classifier <a href="#building-a-fashion-mnist-classifier" id="building-a-fashion-mnist-classifier"></a>

And that really is all the knowledge you were missing in order to start solving computer vision problems. We will practice by building a classifier for [FashionMNIST](https://github.com/zalandoresearch/fashion-mnist)

#### PyTorch-Lightning <a href="#pytorch-lightning" id="pytorch-lightning"></a>

Before we dive into the exercise, let's learn about a new tool, that will help us with a lot of the boilerplate code we saw in the previous lesson. We will be using PyTorch Lightning library, which is a wrapper for PyTorch, which takes out all the boring bits (e.g. training/validation loops, logging, automatic `.train()` and `.eval()` on a model, etc) and leaves us all the good stuff from PyTorch, plus has a lot of helpful functionality (e.g. automatically send data and model tensors to CPU, GPU or TPU, distributed training, etc.)

Familiarize yourself with this library, as we will use it in later modules\
[https://github.com/PyTorchLightning/pytorch-lightning](https://github.com/PyTorchLightning/pytorch-lightning)

#### Exercise <a href="#exercise" id="exercise"></a>

Tasks:

* Get the FashionMNIST dataset. You will need to get train, val and test splits.
* Do EDA
* Build data loader and model

Follow [https://pytorch-lightning.readthedocs.io/en/latest/starter/new-project.html](https://pytorch-lightning.readthedocs.io/en/latest/starter/new-project.html) and adapt to your problem

If you need more guidance, feel free to use this tutorial\
[https://www.kaggle.com/pankajj/fashion-mnist-with-pytorch-93-accuracy](https://www.kaggle.com/pankajj/fashion-mnist-with-pytorch-93-accuracy)

When building a model it is sometimes useful to understand how the data will be passed from one layer to another and its transformations. Keras framework has a built-in function `.summary()` which makes a neat table for you. In PyTorch however, you would have to use additional library `torchsummary`.

Below is a table describing the internal of your model:

* What type of layers you have
* What is the output shape of a layer. This is useful when you want to double-check that your model is doing the transformations you expected. E.g. take the first layer of your net`[-1, 32, 28, 28]` (I assume it is Conv2D layer): the first parameter is batch parameter, the second shows the depth of your output. In this example it is 32, because I selected 32 filters in my Conv2D layer. 28, 28 is the height and width of the output. In the case of the first layer, it matches the image dimensions (if you have put padding)
* Number of parameters. Could help you identify which layers are the largest ones, so you can consider reducing them.
* Total parameters and more importantly total trainable parameters. We will talk in later lessons about transfer learning and fine-tuning, in which cases freezing and unfreezing layers (making them non-trainable or trainable) is necessary.

