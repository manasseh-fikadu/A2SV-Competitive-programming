---
description: >-
  In this lesson, we will take two fairly simple problems - gender
  classification and age classification from an up-close image of a person.
---

# 👨💻 Project - Practical Deep Learning

The exercise today is to train a multi-objective image classifier using data from [https://www.kaggle.com/jangedoo/utkface-new](https://www.kaggle.com/jangedoo/utkface-new)\
You will train a single model that can predict gender and age.

Find out more about multi-task learning\
[https://ruder.io/multi-task/](https://ruder.io/multi-task/)\
[https://www.youtube.com/watch?v=UdXfsAr4Gjw](https://www.youtube.com/watch?v=UdXfsAr4Gjw)

### Concepts to explore <a href="#concepts-to-explore" id="concepts-to-explore"></a>

* Classification task
* Convolutional neural network
* AI ethics and bias
* Model interpretability

### Requirements <a href="#requirements" id="requirements"></a>

* You should go through the standard cycle of EDA-model-evaluation.
* Create a single model that returns age and gender in a single pass
* Analyze model performance
* Understand, which are the best/worst performing samples.
* Use LIME for model interpretability with images. Understand what you model

Once you are done with these tasks, evaluate any ethical issues with this model

* Identify how this model can be biased and check if the results show signs of these issues.
* Analyze bad predictions. Do you see any patterns in misclassified samples, that can cause ethical concerns?
* Describe in which scenarios your model can be biased. Propose solutions to mitigate it.
* Think of a domain, where this model could/could-not be deployed.

### Evaluation criteria <a href="#evaluation-criteria" id="evaluation-criteria"></a>

* EDA
* A single end-to-end trainable deep learning model is built
* Correctly modeled classification/regression
* Correct selection of loss function(s)
* Model interpretability tools used and insights made
* Model aggregate performance
* Quality of ethical concerns raised
* Code quality

### Sample correction questions <a href="#sample-correction-questions" id="sample-correction-questions"></a>

During a correction, you may get asked questions that test your understanding of covered topics.

* What advantages does building ML model in iterations bring over non-iterative approach.
* You are given 2 million images out of which only 1000 has labels. You are asked to build an image classifier. Explain how would you address the problem with the help of auto-encoders.
* When training ML models, an engineer often has to compromise between inference speed and performance (e.g. accuracy, f1). Explain in what scenarios would you choose performance over speed and vice-versa.
* What is negative feedback loop in ML models. Give an example and explain what (if anything) can be done to avoid it.
