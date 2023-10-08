---
description: >-
  You solve a lending automation problem for LendingClub. You will have to apply
  all you have learned about training and deploying machine learning models to
  complete this task.
---

# 👨💻 Unsupervised Learning & Hyperparameter Tuning

### Context <a href="#context" id="context"></a>

Imagine that you are a data scientist who was just hired by the LendingClub. They want to automate their lending decisions fully, and they hired you to lead this project. Your team consists of a product manager to help you understand the business domain and a software engineer who will help you integrate your solution into their product. During the initial investigations, you've found that there was a similar initiative in the past, and luckily for you, they have left a somewhat clean dataset of LendingClub's loan data. The dataset is located in a public bucket here: (although you were wondering if having your client data in a public bucket is such a good idea). In the first meeting with your team, you all have decided to use this dataset because it will allow you to skip months of work of building a dataset from scratch. In addition, you have decided to tackle this problem iteratively so that you can get test your hypothesis that you can automate these decisions and get actual feedback from the users as soon as possible. For that, you have proposed a three-step plan on how to approach this problem. The first step of your plan is to create a machine learning model to classify loans into accepted/rejected so that you can start learning if you have enough data to solve this simple problem adequately. The second step is to predict the grade for the loan, and the third step is to predict the subgrade and the interest rate. Your team likes the plan, especially because after every step, you'll have a fully-working deployed model that your company can use. Excitedly you get to work!

### Requirements <a href="#requirements" id="requirements"></a>

* Download the data from [here](https://www.kaggle.com/datasets/wordsforthewise/lending-club/data).
* Perform exploratory data analysis. This should include creating statistical summaries and charts, testing for anomalies, checking for correlations and other relations between variables, and other EDA elements.
* Perform statistical inference. This should include defining the target population, forming multiple statistical hypotheses and constructing confidence intervals, setting the significance levels, conducting z or t-tests for these hypotheses.
* Apply various machine learning models to predict the target variables based on your proposed plan. You should use hyperparameter tuning, model ensembling, the analysis of model selection, and other methods. The decision where to use and not to use these techniques is up to you, however, they should be aligned with your team's objectives.
* Deploy these machine learning models to Google Cloud Platform. You are free to choose any deployment option you wish as long as it can be called an HTTP request.
* Provide clear explanations in your notebook. Your explanations should inform the reader what you are trying to achieve, what results you got, and what these results mean.
* Provide suggestions about how your analysis and models can be improved.
