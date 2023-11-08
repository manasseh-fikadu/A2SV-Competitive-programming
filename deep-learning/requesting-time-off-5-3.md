---
description: In this lesson, we will talk about 4 topics non-technical topics regarding AI.
---

# 🩺 Practical AI Ethics

### ML Engineer = 5% ML / 95% Engineering <a href="#ml-engineer--5-ml--95-engineering" id="ml-engineer--5-ml--95-engineering"></a>

Over the past few months, you have been building various ML models for numerous domains. Unfortunately what you have seen so far is not even half of the story. ML engineering is a much more complicated domain, where building an ML model is actually the easy part. As this diagram below shows, it also a very small part of the whole process

![](https://mk0caiblog1h3pefaf7c.kinstacdn.com/wp-content/uploads/2019/11/hidden-technical-debt-in-machine-learning-systems.png)Source: https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf

All the exercises you solved so far had well-defined datasets, which is a very rare commodity in real life. Moreover, we didn't take the time to properly investigate all possible alternatives to a problem but instead dived straight into deep learning (well, it is the theme of the module after all...). What about the deployment part? What do you do when your model is in production? When are you actually finished with an ML project? We will try to find answers to all these questions and more as we learn about the process of delivering an ML project.

As you go through the learning material, take time to reflect on how would have solved differently the problems from the past few modules.

* [https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)
* [https://blog.insightdatascience.com/how-to-deliver-on-machine-learning-projects-c8d82ce642b0](https://blog.insightdatascience.com/how-to-deliver-on-machine-learning-projects-c8d82ce642b0)
* [https://www.jeremyjordan.me/ml-projects-guide/](https://www.jeremyjordan.me/ml-projects-guide/)
* [https://martinfowler.com/articles/cd4ml.html](https://martinfowler.com/articles/cd4ml.html)
* [https://towardsdatascience.com/structuring-machine-learning-projects-be473775a1b6](https://towardsdatascience.com/structuring-machine-learning-projects-be473775a1b6)

So the main takeaways from all of the material that you read are:

1. Get a good test set
2. Set you baseline (e.g. human evaluation)
3. Don't use ML if you don't really have to.
4. Make simple models first to get results as fast as possible.
5. Iterate models: start simple, then increase complexity
6. Understand in which cases your model underperforms

As we go through the practical exercise, we try to use the points above as guidelines for the modeling process.

#### Exercise <a href="#exercise" id="exercise"></a>

You have been approached by the United States Aviation Consumer Protection department. They are looking for a contractor to create a versatile model (ML or not) for **sentiment classification** from consumer reviews. The system should be versatile enough to apply for all currently active airlines in the US ([>100 active airlines](https://en.wikipedia.org/wiki/List\_of\_airlines\_of\_the\_United\_States)). They have provided you with [this dataset](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)

Model requirements:

* Predicts sentiment of a review with 85% accuracy
* Extendable to all airlines

You will see that the dataset actually contains only 6 unique airlines, so you talk with the agency and express your deep concerns about the data. This is a red flag for you and you argue that you need more data to ensure it works for all airlines. Since they are quite strict on the resources your request is rejected and you have to continue with what you have.

Let's follow the steps above 1 by 1 and try to see how real-life restrictions affect how we make decisions.

#### Load data <a href="#load-data" id="load-data"></a>

#### EDA and data clean up <a href="#eda-and-data-clean-up" id="eda-and-data-clean-up"></a>

Investigate data and see if there is noise in data. If so, perform data clean up.

```python
df['airline_sentiment'].value_counts(normalize=True).plot.bar(title="Label proportions")
```

```python
df['airline'].value_counts().plot.bar(title="Amount of reviews by airlines")
```

```python
df['tweet_id'].duplicated().sum()
```

```
155
```

```python
df[df['tweet_id'].duplicated(keep=False)].sort_values(by="tweet_id").head(10)
```

There are some duplicated tweet id, so let's just keep the one with the higher confidence score.

```python
df = (
    df
    .sort_values(by="airline_sentiment_confidence", ascending=False)
    .drop_duplicates(subset=['tweet_id'], ignore_index=True)
)

df['tweet_id'].duplicated().sum()
```

```
0
```

```python
df[df['tweet_id'] == 569600137296633856]
```

|      | tweet\_id          | airline\_sentiment | airline\_sentiment\_confidence | negativereason | negativereason\_confidence | airline  | airline\_sentiment\_gold | name           | negativereason\_gold | retweet\_count | text                                         | tweet\_coord | tweet\_created            | tweet\_location                | user\_timezone |
| ---- | ------------------ | ------------------ | ------------------------------ | -------------- | -------------------------- | -------- | ------------------------ | -------------- | -------------------- | -------------- | -------------------------------------------- | ------------ | ------------------------- | ------------------------------ | -------------- |
| 7371 | 569600137296633856 | positive           | 1.0                            | NaN            | NaN                        | American | NaN                      | douglaskgordon | NaN                  | 0              | @AmericanAir Thank you.....you do the same!! | NaN          | 2015-02-22 12:50:30 -0800 | Caribbean, New York and Miami. | Indiana (East) |

```python
df['tweet_location'].value_counts(dropna=False)
```

```
NaN                           4687
Boston, MA                     156
New York, NY                   155
Washington, DC                 145
New York                       125
                              ... 
Glendale, Arizona                1
Roseville, CA                    1
Dallas, TX Memphis, TN, MS       1
Atlanta Ga && Traveling          1
Eternity|GOMAB                   1
Name: tweet_location, Length: 3082, dtype: int64
```

#### Get a good test set <a href="#get-a-good-test-set" id="get-a-good-test-set"></a>

Although it seems like a trivial task, getting a good test set is not always just a `train_test_split` from sklearn. Let's see why?

Let's do a random split and analyze our splits

```python
from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df, test_size=0.25, random_state=14)
```

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)


df_train['airline_sentiment'].value_counts(normalize=True).plot.bar(ax=ax1, title="Train")
df_test['airline_sentiment'].value_counts(normalize=True).plot.bar(ax=ax2, title="Test")
```

```python
len(df_train[['tweet_id']].merge(df_test[['tweet_id']], how="inner"))
```

```
0
```

The label distribution is the same for both splits and there are no duplicated ids. But is this a good test split? Not really! Let's see why.

You are probably wondering, "we did such train/test splits all the course and they are suddenly wrong?" And the answer is "it depends on the situation". Consider the following:

Test sets are supposed to be disjoint from your train set. Based on your problem, dataset, and constraints, the amount of separation could be differernt. For example, does your train/test split contain reviews from the same user? Users can have a unique style of writing and if we do training and testing with reviews from the same person, this indicates train data leakage into your test set. We could go even one step further and say, that people in a specific location have a similar style of language and thus we should exclude people from the same location from our test set.

```python
unique_train_users = df_train['name'].drop_duplicates().to_frame()
unique_test_users = df_test['name'].drop_duplicates().to_frame()

unique_train_users.merge(unique_test_users, on="name", how='inner').count()
```

```
name    1524
dtype: int64
```

We see that indeed we do have the same users in both train and test splits

Moreover, let's look into our problem: we have 6 unique airlines when modeling - and potentially > 100 airlines when in production. How can we be sure that the model will perform well on a new airline if both train and test sets have all 6 airlines?

```python
fig, (ax1, ax2) = plt.subplots(1, 2)

df_train['airline'].value_counts(normalize=True).plot.bar(ax=ax1, title="Train")
df_test['airline'].value_counts(normalize=True).plot.bar(ax=ax2, title="Test")
```

The more you think about your data and modeling, the more of such questions you will have. It's ok to draw a line at some point where it makes sense to you, as you can easily get into a rabbit hole. The important thing is to have these considerations.

#### Exercise <a href="#exercise" id="exercise"></a>

So for this specific application we decided that location of users does not matter, but

* users who wrote the review must not be present in both splits
* same airline should not be in both splits

Your task is to create a test set which satisfies those conditions

```python
train_unique_airlines = set(df_train['airline'])
test_unique_airlines = set(df_test['airline'])
assert len(train_unique_airlines) > 0
assert len(test_unique_airlines) > 0
assert len(train_unique_airlines - test_unique_airlines) == len(train_unique_airlines), "Train and test sets must have unique values"
```

```python
train_unique_name = set(df_train['name'])
test_unique_name = set(df_test['name'])
assert len(train_unique_name) > 0
assert len(test_unique_name) > 0
assert len(train_unique_name - test_unique_name) == len(train_unique_name), "Train and test sets must have unique usernames"
```

#### Set your baseline / Don't use ML if you don't really have to / Get results fast <a href="#set-your-baseline----dont-use-ml-if-you-dont-really-have-to---get-results-fast" id="set-your-baseline----dont-use-ml-if-you-dont-really-have-to---get-results-fast"></a>

We now have a reliable test set and we can be **more** certain that the model will perform well in prod. The emphasis on _more_ is because you are never sure that it performs well until you deploy it to prod and see the live performance metrics.

"You are never sure the model performs well until you deploy it to prod"

Let's move on to the next step - setting your baseline. For this, you want to use something simple - human performance (if feasible) or maybe some heuristic model. Let's try to make a heuristic implementation of sentiment analysis. Maybe we won't need ML at all...

We can look into our data and find if there are any indicative features in text that tells us about the sentiment.

```python
df_train[df_train['airline_sentiment'] == 'positive']['text']
```

```
2        @JetBlue They just came out. Thanks for the fo...
3                           @JetBlue Thanks! See you soon!
12       @JetBlue great flight on a brand new jet. Grea...
15       @JetBlue thank you! I know the weather in #Bos...
21       @JetBlue okay thank you! I'll check with them ...
                               ...                        
14471    @united not just refunded, but for those of us...
14475    @JetBlue Crisis averted! Flight #69 from BOS t...
14476    @SouthwestAir can anyone help me upgrade to bu...
14477    @united Thank you but the person in Houston co...
14480    .@united Thanks. Hopefully this is easily reso...
Name: text, Length: 1625, dtype: object
```

**Plotting word counts per sentiment**

Let's plot word counts for the reviews

```python
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,4), sharey=True)

df_train[df_train['airline_sentiment'] == 'positive']['text'].str.split().str.len().plot.hist(ax=ax1, title="Word count positive")
df_train[df_train['airline_sentiment'] == 'neutral']['text'].str.split().str.len().plot.hist(ax=ax2, title="Word count neutral")
df_train[df_train['airline_sentiment'] == 'negative']['text'].str.split().str.len().plot.hist(ax=ax3, title="Word count negative")

plt.subplots_adjust(wspace=0.2)
```

So first of all, it seems that negative reviews seem to be much longer than positive and neutral. That could be a good feature

Are there any specific words phrases, that might also indicate sentiment? I will use TfidfVectorizer which will count all the words in the dataset and will return 15 most frequent while ignoring English stop words, e.g. "and", "the", "her", etc.

```python
from sklearn.feature_extraction.text import TfidfVectorizer


positive_vecz = TfidfVectorizer(ngram_range=(1, 4), max_features=15, stop_words="english")
positive_vecz.fit(df_train[df_train['airline_sentiment'] == 'positive']['text'])
positive_vecz.get_feature_names()
```

```
['best',
 'flight',
 'great',
 'guys',
 'http',
 'jetblue',
 'just',
 'love',
 'service',
 'southwestair',
 'thank',
 'thanks',
 'united',
 'usairways',
 'virginamerica']
```

```python
neutral_vecz = TfidfVectorizer(ngram_range=(1, 4), max_features=15, stop_words="english")
neutral_vecz.fit(df_train[df_train['airline_sentiment'] == 'neutral']['text'])
neutral_vecz.get_feature_names()
```

```
['dm',
 'fleek',
 'fleet fleek',
 'flight',
 'flights',
 'help',
 'http',
 'jetblue',
 'just',
 'need',
 'southwestair',
 'thanks',
 'united',
 'usairways',
 'virginamerica']
```

```python
negative_vecz = TfidfVectorizer(ngram_range=(1, 4), max_features=15, stop_words="english")
negative_vecz.fit(df_train[df_train['airline_sentiment'] == 'negative']['text'])
negative_vecz.get_feature_names()
```

```
['cancelled',
 'customer',
 'delayed',
 'flight',
 'help',
 'hold',
 'hours',
 'jetblue',
 'just',
 'plane',
 'service',
 'southwestair',
 'time',
 'united',
 'usairways']
```

So for neutral we see no obvious words, that would indicate sentiment. We can see all 3 categories contain airline names as top-15 most common words in reviews. In fact, we should consider removing all `@name` mentions from text, as our model can later start associating sentiment with an airline name (talking about data bias...)

But for the positive, some obvious choices are variations of `thank you`, `best`, `great`, `love`, which makes sense to be part of positive experiences.

For negative, obvious contenders are `canceled` and `delayed` which indicate negative experience.

So let's create our baseline model with just these few rules and see how it performs. It might seem weird, as to why are we wasting our time with this, this will never work in prod. And it is true, we will need much more than hardcoded rules, but this gives a baseline to compare our models to AND look at how much you learned about your data. This is called 'being the model' and it's one of the best ways to really become an expert on your particular dataset.

#### Exercise <a href="#exercise" id="exercise"></a>

* Make a function which classifies reviews into negative neutral and positive (\[0, 1, 2] respectively) based on review length and presence sentiment keywords from above.
* make prediction using your function on the test set
* evaluate predictions: precision, recall, f1 and confusion matrix

```python
label_map = {
    "negative": 0,
    "neutral": 1,
    "positive": 2,
}
```

So just based on the two very simple features we were able to get some decent results. Performance for neutral is the worst and I am kind of surprised how well `finding keywords` worked for classifying positive reviews - f1 for positive is 0.6. Also as it was pretty obvious from the [graph before](https://intra.turingcollege.com/hardskills/delivering-ml-projects#Plotting-word-counts-per-sentiment), the review length was a significant factor. Hopefully future ML model will easily pick up on this too.

At this point, you could continue investigating your data and finding other heuristic features. For the sake of the exercise, we will continue to the next step.

#### Iterate models <a href="#iterate-models" id="iterate-models"></a>

Let's move onto iterating to more complex models. Having a heuristic baseline, we can move on to building classical machine learning solutions and only then deep learning.

Do you remember Module 3? Let's build a simple linear regression to classify our text and see if we can get better results than a rule-based system

#### Exercise <a href="#exercise" id="exercise"></a>

* Remove @ mentions from text
* Build a linear model (logistic regression) to predict sentiment
* Compare performance to heuristic model
* ❗️Save this model as we will need it for the next lesson

Hopefully you seeing an increase in performance, which you should. If not, baseline is serving its purpose and telling you that you are doing something wrong. Review your code for the logistic regression

So far so good! Next natural step - decision trees. You should remember them from the previous module. If not, go back to refresh your memory.

Let's build a random forest classifier and see if we can improve our score even more.

#### Exercise <a href="#exercise" id="exercise"></a>

* Build a random forest classifier
* Compare results with previous versions

Depending on your results for the log reg, you likely found out that it's actually not that easy with simple text features to get better results than LogReg. Read [this article](https://towardsdatascience.com/is-random-forest-better-than-logistic-regression-a-comparison-7a0f068963e4) to get more insights for why that might be.

#### Understand in which cases your model underperforms <a href="#understand-in-which-cases-your-model-underperforms" id="understand-in-which-cases-your-model-underperforms"></a>

> When you sort your dataset descending by loss you are guaranteed to find something unexpected, strange and helpful.
>
> — Andrej Karpathy (@karpathy) [October 2, 2020](https://twitter.com/karpathy/status/1311884485676294151?ref\_src=twsrc%5Etfw)

When we get aggregate model performance (accuracy, f1-score), this tells us very little about what we can do to make it better. Take our random forest model, for instance, we can keep tuning hyper-parameters of the model and see what give us that extra few % difference. But it's not the way to go if the model is nowhere near optimal.

In such case, we should try to understand in what cases is our model performing best/worst. This should give us a lot of insights.

#### Exercise <a href="#exercise" id="exercise"></a>

* Instead of class predictions, get probabilities for each test sample
* Get top-10 best performing samples for each class label (e.g. model says negative sentiment and it actually is negative)
* Get top-10 worst-performing samples for each class label (e.g. model says negative sentiment but it actually is not)
* See if you can draw some conclusions from observations

```python
y_pred.shape
```

```
(540,)
```

**Correct predictions**

**Incorrect predictions**

So just by looking into best and worst examples you should have been able to make some interesting insights.

Mine were:

* The model could not distinguish sarcarsm (e.g. "@AmericanAir thanks for the canned reply.")
* Data contains `&amp;` symbols, which should just be `&`
* There are mislabelled samples (e.g. "@AmericanAir thank you" is labelled as neutral)
* Any others?

Your model performance will always be limited by the data correctness. I guess this famous quote sums it all up:

![](https://www.accutrend.com/wp-content/uploads/2018/07/GiGo-570x315.jpg)Source: https://www.accutrend.com/wp-content/uploads/2018/07/GiGo-570x315.jpg

Again, for the sake of exercise, let's continue

At this moment it might be a good time to start thinking about model deployment. It's not a perfect model, but we are not aiming for that. We have some decent results and we will have even better insights once our model is live.

Now we will talk about some model deployment considerations and monitoring

#### Deploying the model <a href="#deploying-the-model" id="deploying-the-model"></a>

When it comes to model deployment in production, there are lots of things to consider. Let's start with how your model will be used.

You have built a sentiment analyzer. But how will it be used? Is this going to be some background job in a company's data warehouse (server-side deployment), that runs every night for large batches of data and you will have access to 20 GPUs? Or will you want to use it on a company's mobile app (client-side deployment) to provide users with appropriate responses, based on reviews they just wrote? This will have different implications, such as

* Inference speed - for app or client-facing deployment, model inference speed is usually crucial. You don't want a user waiting for 2s for your application to respond (especially after just having written a negative review). This will degrade the usability of your product and you will start seeing an impact on business metrics, such as user retention, new user acquisition, time spent on the app, and eventually revenue.

"What is the impact of X happening?"

* Network latency - Let's say you deploy the quickest model you can get. Then your bottleneck might become the network latency, or even network availability. Obviously, it is not something you can control, so you should always make considerations what is the impact of this happening. If it makes your app unusable, you should probably redesign it.
*   Monitoring - there are various quotes around the internet saying something like "ML models have restricted view of reality". This refers to the fact that a limited training dataset can seldom represent true reality. Moreover, since our reality is dynamic, sooner or later they will become wrong. This is the harsh truth and there is nothing you can do to stop this from happening, but you can make sure your model gets constantly updated. The only issue - how do you know when? Monitoring is an integral part of any software system and machine learning is not an exception.

    Some of the metrics you could consider tracking can be your usual performance metrics, like 'response time', 'number of errors', or business metrics like 'request count', 'no of returning users', 'requests per user', etc. If you are running a website with a single ML functionality (e.g. a service to remove background from images, like [this one](https://www.remove.bg/)), you could get a good indication of you model performance by tracking e.g. # of returning users.

    But since ML models are usually part of some bigger functionality, such metrics might not give you a full picture. Your business metrics might not degrade over time, but it's not because the model is still awesome. It might be the case that your marketing team has to work harder to get new/returning users and your model is not helping at all. Check out the resources below about what to monitor in ML and when.
* [https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/)

\[OPTIONAL]

* [https://mlinproduction.com/why-is-it-important-to-monitor-machine-learning-models/](https://mlinproduction.com/why-is-it-important-to-monitor-machine-learning-models/)
* [https://towardsdatascience.com/monitoring-machine-learning-models-62d5833c7ecc](https://towardsdatascience.com/monitoring-machine-learning-models-62d5833c7ecc)

![](https://i.imgflip.com/4kdrww.jpg)Source: https://imgflip.com/i/4kdrww

*   We are just scratching the surface. There are other important issues, such as A/B testing and roll-out strategies. Read the links below to learn more about each of these points. There is a great series of blogs in [http://mlinproduction.com/](http://mlinproduction.com/) which exclusively talks about the challenges of ML model deployment. Bookmark this website, as I am sure you will be coming back to it.

    Also, if you have access to O'Reilly, check out this book [_Building Machine Learning Powered Applications_](https://learning.oreilly.com/library/view/building-machine-learning/9781492045106/) by Emmanuel Ameisen as an alternative to the links below. It is a really great practical guide to ML.

    * [https://mlinproduction.com/what-does-it-mean-to-deploy-a-machine-learning-model-deployment-series-01/](https://mlinproduction.com/what-does-it-mean-to-deploy-a-machine-learning-model-deployment-series-01/)
    * [https://mlinproduction.com/the-challenges-of-online-inference-deployment-series-04/](https://mlinproduction.com/the-challenges-of-online-inference-deployment-series-04/)
    * [https://mlinproduction.com/online-inference-for-ml-deployment-deployment-series-05/](https://mlinproduction.com/online-inference-for-ml-deployment-deployment-series-05/)
    * [https://mlinproduction.com/ab-test-ml-models-deployment-series-08/](https://mlinproduction.com/ab-test-ml-models-deployment-series-08/)
    * [https://www.kdnuggets.com/2019/06/approaches-deploying-machine-learning-production.html](https://www.kdnuggets.com/2019/06/approaches-deploying-machine-learning-production.html)

#### Exercise: <a href="#exercise" id="exercise"></a>

So we have deployed our model to prod and realized that the model performance is too low for it to be useful in the long term. You are asked to improve the model. Last exercise of the lesson - use deep learning for sentiment analysis model. We have already done an exercise of sentiment analysis in the previous sprint. Use the knowledge you learned to solve this problem.

* Implement deep learning solution with transformers
* Compare results with baseline and other ML models
* Get best/worst performing samples from DL model

```python
def remove_mentions(text: str) -> str:
    words = text.split()
    words = [w for w in words if '@' not in w]
    return ' '.join(words)
```

How are the results. It is likely, that the deep learning model performance was not actually better than logreg. If it is - well done!

***

### Summary <a href="#summary" id="summary"></a>

In this lesson, you have gone through the process of ML model development. It is not a straightforward approach and it always is use-case specific. All the decisions we made in this lesson were specific to our problem, data, client, and potential users. There is no standard way of what is best, but instead of what makes most sense. How do you know what makes sense? Unfortunately, the only answer I can give you - experience. But what is pretty standard in any ML model development process are the main points of the lesson:

1. Get a good test set
2. Set you baseline (e.g. human evaluation)
3. Don't use ML if you don't really have to.
4. Make simple models first to get results as fast as possible.
5. Iterate models: start simple, then increase complexity
6. Understand in which cases your model underperforms

Develop your models iteratively and understand why your model is underperforming at every iteration. Don't wait for the perfect model - deploy as early as possible. You will be surprised the value evaluation in production brings.
