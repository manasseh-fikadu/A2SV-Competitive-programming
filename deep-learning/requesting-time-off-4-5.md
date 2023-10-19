# 👨💻 Project - Natural Language Processing

### Toxic comment challenge <a href="#toxic-comment-challenge" id="toxic-comment-challenge"></a>

### Background <a href="#background" id="background"></a>

The time has come again to put together all we learned in the previous lessons and try to tackle a real-life issue.

In this project, we will try to put ourselves into the shoes of content moderators. Every online platform which has an open forum faces an issue of people posting inappropriate comments, which if uncontrolled, can lead to loss of users, reputation and revenue. However, it is impractical and expensive for humans to keep track of all the messages other people post. Luckily, ML is here to help. We can train a model to automatically analyze all the messages users write and flag toxic users/comments so that appropriate actions can be taken.

We will use Kaggle toxic comment dataset [https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

Your task today is to build a **multi-label** classifier, to assign forum posts to one or more of the 6 classes.

***

### Multi-label classification <a href="#multi-label-classification" id="multi-label-classification"></a>

Up until now all, of the classification exercises we have seen were _multi-class_ (e.g. dog, cat, plane) or binary (e.g. yes/no). Both methods are used when there is only 1 right answer, e.g. an animal cannot be both a dog and a plane. In _multi-label_ classification, each input can result in many possible answers, e.g. articles could have a mixture of tags: news, sports, politics.

![](https://i0.wp.com/theailearner.com/wp-content/uploads/2019/07/multilabel.png?fit=625%2C339\&ssl=1)Source: https://theailearner.com/2019/07/15/multi-label-classification/

So what are the implications for the neural network, that you are going to build?

1. You cannot use softmax any more, since it makes a probability distribution over all of the classes. This time we need each output to have its own and independent probability. A good way to do it is to apply a Sigmoid activation to the output layer, which will squash your output between 0 and 1, thus you can treat the output as a probability to a sample belonging to a class
2. We need to change our loss function. Cross-entropy loss is used for multi-class problems, so you will have to change it to Binary Cross-entropy since we want each output considered individually.
3. Your labels will now have to be 1-hot-encoded. Since each output can have various labels, it is a good way to represent it. So a label, that belongs to class 1 and 4 out of possible 5, will be represented as `[0, 1, 0, 0, 1, 0]`. You can use sklearn [one-hot-encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) to easily convert your labels
4. When using model outputs (e.g. predictions in prod, evaluation), you will need to threshold the output. Why? Consider how a multi-label output with sigmoid activation from your model will look. For a 5 label problem, it will be a vector with 5 values, each from 0 to 1, e.g. `[0.01, 0.99, 0.68, 0.89, 0.32]`. How do you convert this into yes/no for each label? By applying a threshold of some value, such as 0.5. Meaning if the probability is less than 50%, we say it does not belong to this class. If more than 50% then it does, which will convert the above output to `[0, 1, 1, 1, 0]`

You can use HuggingFace transformers library and adapt a \*{TRANSFORMER}\*ForSequenceClassification method. I recommend using [DistilBERT](https://huggingface.co/transformers/model\_doc/distilbert.html#distilbertforsequenceclassification) or [RoBERTa](https://huggingface.co/transformers/model\_doc/roberta.html#robertaforsequenceclassification). You will have to make sure you don't pass labels to the classifier and calculate it yourself in the model.

### EDA <a href="#eda" id="eda"></a>

Since your time is very limited and the task is not trivial, do not spend time doing extensive EDA. It is a very important step in every project and you will have to do some, in order to understand how many classes you have, what the text data looks like, potentially the class distribution. But avoid spending more than an hour on this, since you want to leave the maximum time for building a model and preprocessing data.

### Concepts to explore <a href="#concepts-to-explore" id="concepts-to-explore"></a>

* Multi-label classification
* Binary cross-entropy loss

### Requirements <a href="#requirements" id="requirements"></a>

* EDA
* Preprocess your data correctly, including converting labels to one-hot-encoding
* Split data into train/validation/test sets
* Visualize model performance
* Ensure your work has written conclusions and insights about
  * Main details about the data
  * Model considerations and implementation
  * Results
  * Recommendations for improvements

### Evaluation criteria <a href="#evaluation-criteria" id="evaluation-criteria"></a>

When solving this problem, ensure that you plan your time carefully. The most important part is to show your NLP and deep learning knowledge. Meaning, ensure you build a model with correct output, loss, and activations as well as do the correct data preprocessing pipeline (e.g. text tokenization, one-hot-encoding of labels). Model performance

* Correctly preprocessed labels
* Correctly built model
* End-to-end trainable model
* Model performance
* Code quality

### Bonus challenges <a href="#bonus-challenges" id="bonus-challenges"></a>

* Add class weights to BCE loss. To calculate those weights refer to [here](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class\_weight.compute\_sample\_weight.html)
* Use tanh activation for the output layer and compare results with sigmoid. Note, you will have to change your data preprocessing pipeline since tanh has a different activation range. Investigate what it is and adapt your solution.

### Sample correction questions <a href="#sample-correction-questions" id="sample-correction-questions"></a>

During a correction, you may get asked questions that test your understanding of covered topics.

* What is tokenization in NLP context and why is it important?
* What is attention mechanism in transformers and what are its main advantage(s)
* What are the differences between GPT and BERT transformers
* Explain in a high level - how does a character-based generative model work?

```python
trainer.fit(model)
```

```
  | Name       | Type                                | Params
-------------------------------------------------------------------
0 | classifier | DistilBertForSequenceClassification | 66 M  
1 | criterion  | BCEWithLogitsLoss                   | 0     
```

```
HBox(children=(FloatProgress(value=1.0, bar_style='info', description='Validation sanity check', layout=Layout…
```

```
HBox(children=(FloatProgress(value=1.0, bar_style='info', description='Training', layout=Layout(flex='2'), max…
```

```
1
```

\
