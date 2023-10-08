# 👨💻 Project - Computer Vision

### Background <a href="#background" id="background"></a>

In US alone, around 7500 yearly cases of mushrooms poisoning are reported [(Source)](https://www.tandfonline.com/doi/full/10.1080/00275514.2018.1479561). According to the source, "misidentification of edible mushroom species appears to be the most common cause and may be preventable through education". To avoid expenses for hospitalization and in some cases pointless deaths, you have been hired by US National Health Service to create a machine learning model, that can recognize mushroom types. They want to install this on hand-held devices and to help people make the right choice when mushroom picking.

***

### Concepts to explore <a href="#concepts-to-explore" id="concepts-to-explore"></a>

Today, we will put everything we learned in this module and use it to solve a classification problem. The idea of this project is to use transfer learning on an architecture of your choice and fine-tune to predict mushroom types.

You will use this Kaggle dataset [https://www.kaggle.com/maysee/mushrooms-classification-common-genuss-images](https://www.kaggle.com/maysee/mushrooms-classification-common-genuss-images)

### How to start? <a href="#how-to-start" id="how-to-start"></a>

#### Data <a href="#data" id="data"></a>

Well, the obvious first steps will be getting the data from Kaggle. There are a number of choices on how to do it, such as downloading images to your machine and then uploading to Drive or using [Kaggle API](https://github.com/Kaggle/kaggle-api). Once you get your data, start with an EDA, as this will directly feed into design choices for your architecture.

#### Modeling <a href="#modeling" id="modeling"></a>

My suggestion is that you start with a simple pre-trained architecture, like ResNet18. This will allow you to fine-tune your net faster and if results are not too good, you can try switching to a larger model later. It is recommended that you use PyTorch Lightning or FastAI. Both are equally good for simple problems like this, but PyTorch Lightning will give you more control, better customization ability, and better understanding of your network.

### Requirements: <a href="#requirements" id="requirements"></a>

* Choose whichever framework you prefer from FastAI, PyTorch Lightning or PyTorch.
* As always - EDA
* Use a pre-trained neural net as a backbone of your class
* Train a classifier. Don't forget to fine-tune
* Evaluate inference time
* Visualize results

### Bonus challenges <a href="#bonus-challenges" id="bonus-challenges"></a>

* Repeat the process with modifications to your network and see how the results vary.
  * Try a different optimizer
  * Add an intermediate layer between the backbone and output layer

