---
description: >-
  Today we will learn how to use PyTorch - probably one of the most versatile
  (subjective opinion) and widely used framework.
---

# 🔥 PyTorch

We will start the lesson by understanding what is a tensor. Tensorflow as well as PyTorch both operate on this concept, so it's crucial to know what it is. So tensors are simply multi-dimensional data objects. Tensor of dimensionality=0 is a number, dim=1 - vector, dim=2 - 2D array, dim=3 - 3D array (e.g. image) and so on. I am sure you get the idea. On top of that, PyTorch tensor holds additional gradient information, so it is very efficient when applying backward step.

But essentially, it is very closely related to numpy array and you will find you can do, in most cases, identical operations in PyTorch as in Numpy.

* [https://pytorch.org/tutorials/beginner/deep\_learning\_60min\_blitz.html](https://pytorch.org/tutorials/beginner/deep\_learning\_60min\_blitz.html)
* [https://pytorch.org/tutorials/beginner/blitz/tensor\_tutorial.html#what-is-pytorch](https://pytorch.org/tutorials/beginner/blitz/tensor\_tutorial.html#what-is-pytorch)

#### How PyTorch works <a href="#how-pytorch-works" id="how-pytorch-works"></a>

PyTorch is not only a really powerful framework, but also very efficient. If you have millions of parameters and perform millions of calculations in your neural network at every pass, it is crucial to get the code as efficient as possible. Let's learn what happens behind the scenes of PyTorch

* [https://pytorch.org/tutorials/beginner/blitz/autograd\_tutorial.html#autograd-automatic-differentiation](https://pytorch.org/tutorials/beginner/blitz/autograd\_tutorial.html#autograd-automatic-differentiation)
* [https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95](https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95)

As you can see in the articles above, PyTorch optimizes the gradient calculations by keeping track of all of your operations with tensors in a graph. And once you call a `backward()` function, it simply replays the graph to apply changes to weights and biases.

#### Building neural nets with PyTorch <a href="#building-neural-nets-with-pytorch" id="building-neural-nets-with-pytorch"></a>

Let's look into how PyTorch allows you to easily build neural networks. When going through the below practical example, keep in mind the Neuron you manually implemented yesterday and see if you find similarities in the PyTorch API.

* [https://pytorch.org/tutorials/beginner/blitz/neural\_networks\_tutorial.html#neural-networks](https://pytorch.org/tutorials/beginner/blitz/neural\_networks\_tutorial.html#neural-networks)

#### Exercise <a href="#exercise" id="exercise"></a>

Let's build our first neural net using PyTorch. Just to emphasize the concepts you have seen in the previous tutorial: whether you are building a custom layer or full neural net, you will simply need to create a class that inherits from `torch.nn.Module`. This will force you to implement a forward method, exactly as in your Neuron in the previous lesson. You can then plug it into another Module or train it.

See [https://pytorch.org/tutorials/beginner/pytorch\_with\_examples.html#pytorch-custom-nn-modules](https://pytorch.org/tutorials/beginner/pytorch\_with\_examples.html#pytorch-custom-nn-modules) for more details

Requirements:

* Use sklearn iris dataset
* Create a neural network of 2 fully connected layers.
  * First layer can have an arbitrary number of neurons. Let's say - 1024
  * The second layer is the output layer. Iris is a classification task, so check how many labels does the data have and set the output layer to have that many neurons (1 for each label)
* Create a train function, which given a model, data and labels, trains the model for n epochs
* Train your model for 3000 epochs, lr=1e-4 with optimizer of your choice (remember the last lesson) and ensure the loss is reducing
* Record and plot training loss
* Calculate the time it takes to train the model. You can [see here](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) how to efficiently do it in Jupyter

Don't worry about the results. They are likely to be horrible. We are only making sure at this moment we can build a trainable end-to-end network.

Congrats! You just build and trained your first neural network with PyTorch.

#### Overfitting / Underfitting <a href="#overfitting--underfitting" id="overfitting--underfitting"></a>

Given enough epochs and neurons in the network, you can train your model to get to close to zero training loss. But does that really mean that the model is performing well?

Let's understand a bit more about over/underfitting in ML/DL

* [https://towardsdatascience.com/what-are-overfitting-and-underfitting-in-machine-learning-a96b30864690](https://towardsdatascience.com/what-are-overfitting-and-underfitting-in-machine-learning-a96b30864690)
* [https://www.coursera.org/lecture/machine-learning/the-problem-of-overfitting-ACpTQ](https://www.coursera.org/lecture/machine-learning/the-problem-of-overfitting-ACpTQ)

As an ML engineer, you don't care that training loss is getting smaller. You are not interested that the model, as Andrew Ng put it "tries too hard to fit the data" and gets perfect training metrics but fails miserably when in prod. What you want to ensure is that the model performs well on unseen data. This is where the validation set comes into action.

#### Exercise <a href="#exercise" id="exercise"></a>

Create an `evaluate()` function which will validate if the model is performing well on unseen data.

Tasks:

* Split data into training/validation data
* Modify train function to accept validation data as inputs
* Put the `evaluate()` function inside the training loop
* Record validation loss,
* Plot both train/val losses on the same graph
* Time your training procedure

That is pretty good. The validation loss is smaller than training loss, which suggests underfitting. You should train your model for some epochs more, until train and val losses are similar.

Well done so far!

#### Dataloaders <a href="#dataloaders" id="dataloaders"></a>

The data you have been working with so far is pretty basic: it probably did not have many samples or many features. When training we were able to make calculations for all of the data in a single pass in the forward function. However, when dealing with larger tensors, higher-dimensional data, and larger quantities, it will be unfeasible to make calculations for all the samples in a single operation. Iris sample has 1 row and 4 features, and the whole training dataset is a 2D tensor of `112 * 4 = 448` values. Consider a single RGB image of size 224x244 will have `224 * 224 * 3 = ~150k` values. Trying to calculate gradients for a dataset of 1k images will quickly flood memory of any GPU.

An obvious solution is to make small batch calculations. But even then, the bottleneck of your pipeline might be when loading data. Imagine if you had to load 128 images into memory, then do calculations, free up the memory, then repeat the process. Your model running on a GPU would be waiting for data most of the time.

This is where the PyTorch Dataloaders come into play. They are parallel procedures that help you easily load data and ensure your model never has to wait for data. And the best part - they are fully customizable, so you can write your own for any problem you have at hand.

**Some more motivation:**

Even though the computers and GPUs are becoming bigger and more powerful, so are the datasets. For many state-of-the-art models you will find in research and industry, the datasets are really big, in the 100s of GBs or even TBs ([GPT-3 used 45TB](https://in.springboard.com/blog/openai-gpt-3/) of data for training). For this reason, it is very important to ensure that your process of data loading, pre-processing, passing to model, and then removing from memory for the next batch of data is efficient. You don't want this to become a bottleneck in the (already long) model training process. You will find that all the major DL frameworks have data loaders, that provide multi-process parallelized data loaders, which ensure you can train a neural network without worrying your model trains faster than data is being loaded.

Let's look into the theory of DataLoaders and then we will try to build one ourselves.

* [https://stanford.edu/\~shervine/blog/pytorch-how-to-generate-data-parallel](https://stanford.edu/\~shervine/blog/pytorch-how-to-generate-data-parallel)
* [https://pytorch.org/docs/stable/data.html](https://pytorch.org/docs/stable/data.html)
* [https://pytorch.org/tutorials/beginner/data\_loading\_tutorial.html](https://pytorch.org/tutorials/beginner/data\_loading\_tutorial.html)

#### Exercise <a href="#exercise" id="exercise"></a>

Tasks:

* Build a map-style dataset for the training and validation data we made earlier
* Get a single item from your dataset
* Create a dataloader for train and validation datasets and visualize one batch of data
* Update our training routine to incorporate the train and validation dataloaders
* Visualize training loss
* Time your training routine

Depending on the batch\_size you selected, you probably noticed, that it's taking much longer to train than just passing all the data. It is because we are calculating gradients and updating weights much more frequently now.

But at the same time, it is taking us much less iterations to get the same results.
