# 🕵 Generative models

In the previous lesson, we saw how RNNs can generate text. Given some fixed-length sequence, we gave the model the task of predicting the next word in that sequence. Even though the window of words visible to a model was shorter than the whole sentence, by storing a hidden state of an RNN, we were able to predict words without losing the bigger context. In the first part of a lesson, we will look into another type of generative approach - character-based text generation. Later, we will spend the major part of the lesson by talking about GPT, we will compare it to BERT family transformers and see its applications

### Learning outcomes: <a href="#learning-outcomes" id="learning-outcomes"></a>

* Character-based text generation
* GPT-2/3
* GPT vs BERT

***

### Character-based text generation <a href="#character-based-text-generation" id="character-based-text-generation"></a>

![](https://miro.medium.com/max/1644/1\*-4Y\_FY9Zz5cvA3T3KS6nBQ.jpeg)Source: https://towardsdatascience.com/text-generation-with-bi-lstm-in-pytorch-5fda6e7cc22c

In the previous lesson, we have already done word-level generation. The concept of character-level generation is almost identical, except that instead of words, it will predict characters. This has advantages as well as disadvantages: firstly let's consider the vocabulary size. A BERT tokenizer has a vocabulary size of \~30k. If we used char-level generation, the vocabulary size would be limited to the number of characters in a language, which in most cases (including letters, numbers, punctuation) will likely be under 100. This is great news if we want to reduce complexity. On the contrary, to train a model to predict the next character of a word requires not only to understand word structures of a language, but also while doing it, keep the semantics of the language. Usually, char-level generative models are rare in the wild, and would most likely benefit such applications where language semantics is easy or not necessary (e.g. predictive typing).

Read this great blog about char-level vs word-level NLP, which explains more in-depth of advantages and caveats of this approach.

* [https://www.lighttag.io/blog/character-level-NLP/](https://www.lighttag.io/blog/character-level-NLP/)
* [https://towardsdatascience.com/text-generation-with-bi-lstm-in-pytorch-5fda6e7cc22c](https://towardsdatascience.com/text-generation-with-bi-lstm-in-pytorch-5fda6e7cc22c)

\[OPTIONAL]\
By the way, did you know you can do NLP using convolutional neural networks!? If you are interested, check this out:

* [https://www.youtube.com/watch?v=CNY8VjJt-iQ](https://www.youtube.com/watch?v=CNY8VjJt-iQ)
* [https://arxiv.org/pdf/1808.04444.pdf](https://arxiv.org/pdf/1808.04444.pdf)

#### Exercise <a href="#exercise" id="exercise"></a>

What if neural networks could be funny? Could we teach a neural network to tell jokes? We will use [https://www.kaggle.com/abhinavmoudgil95/short-jokes](https://www.kaggle.com/abhinavmoudgil95/short-jokes) and try to build a char-level generative model, that can generate humor 1 character at a time.

We can refactor the solution we had in the previous lesson to work generating characters instead of words. The only difference in our data loaders is that they will now return a sequence of letters rather than words.

Firstly, we will have to preprocess our data. The good thing about char-level models is that we don't need dedicated tokenizers as our vocabulary size is much smaller.

There are no pre-trained tokenizers, since for char-level models it would always be the same for every task (in English). Therefore, we will have to do the text cleaning ourselves.

Tasks:

* Remove non ascii characters
* Split texts into arrays of letters
* Tokenize. Use `string.printable` for tokenization

Great. Now that we have each letter tokenized, we continue by building a data pipeline. Before we do this, let's agree on what to expect as outputs of our data pipeline. As with word-level model, our char-level generator will do a sliding window over all of the tokens and return a fixed sequence as train data and this sequence offset by 1 token as label.

Let's try building it:

* Make a dataset for your neural net to return fixed sequence length input and label

How are the results...? Depending on the number and depth of RNN cells and the amount of time you spent training, your result quality might vary. But chances are, they are not so good. Why? For the same reason GPT-3 is so good - it's size and amount of data.

### GPT <a href="#gpt" id="gpt"></a>

Let's continue our journey with generative models by getting to know another heavy-weight of NLP from OpenAI - GPT

![](https://cdn.vox-cdn.com/thumbor/ATtGiyo1fvJx5yFraBe\_zJvFxaI=/1400x0/filters:no\_upscale\(\)/cdn.vox-cdn.com/uploads/chorus\_asset/file/14125439/Screen\_Shot\_2019\_02\_21\_at\_2.04.39\_PM.png)Source: https://www.theverge.com/

GPT and all its successors (GPT2 and GPT3) also has a transformer-based architecture, the only difference compared to the BERT family is that it is made of stacks of transformer decoders, rather than encoders. It is a self-supervised algorithm, which means it can train on huge corpora of data, without the need for a human to label it. GPTs are _causal language models_ which means it tries to predict next words in a sequence. Remember, BERT is a masked-language model as it tries to predict masked out words in a sentence.

Another difference to BERT, GPT uses transformer decoders, which have masked attention heads. This ensures, that during training GPT cannot peek into the next words in a sentence. While in BERT this is allowed (it uses non-masked attention heads) in GPT this would be considered cheating. This makes sense, since decoders are by nature generators, and it should not look into next words in sequence as they are yet to be generated.

OpenAI has made headlines in June 2020 with their GPT-3. It is not yet open-sourced, however the company has made an API to query it for research/leisure purposes. While from an architecture perspective it is not novel, it still has beaten most of the SOTA for NLP tasks. So if it's not novel, why is it so good? Because it's big! Check out these resources below to understand better what goes on under the hood and see how big it is... (spoiler alert: it's HUGE!)

* [https://openai.com/blog/language-unsupervised/](https://openai.com/blog/language-unsupervised/)
* [https://openai.com/blog/better-language-models/](https://openai.com/blog/better-language-models/)
* [http://jalammar.github.io/illustrated-gpt2/](http://jalammar.github.io/illustrated-gpt2/)
* [https://medium.com/@dronh.to/gpt-3-paper-summary-462eda87952d](https://medium.com/@dronh.to/gpt-3-paper-summary-462eda87952d)
* [https://www.youtube.com/watch?v=UULqu7LQoHs](https://www.youtube.com/watch?v=UULqu7LQoHs)

#### Exercise <a href="#exercise" id="exercise"></a>

The good people of HuggingFace transformers have made available GPT and GPT-2 for us to use. We can thus use this library to build something exciting using this technology.

Let's take a pre-trained GPT-2 model from hugging face and fine-tune it on our humor data to see if it can be any better at generating jokes. This time we will use Transformers API to fine-tune our model. Follow links below for help on how to fine-tune a GPT-2 model

* [https://huggingface.co/transformers/custom\_datasets.html](https://huggingface.co/transformers/custom\_datasets.html)
* [https://towardsdatascience.com/fine-tune-a-non-english-gpt-2-model-with-huggingface-9acc2dc7635b](https://towardsdatascience.com/fine-tune-a-non-english-gpt-2-model-with-huggingface-9acc2dc7635b)

Tasks:

* Fine-tune a pre-trained GPT-2 language model

The chances are, that the jokes generated much more resemble to ones we have actually used to train our model. You could also think, that the network due to its size, might just have remembered the jokes (overfit on our dataset). We can easily validate this by seeing items in the original dataset that have the same cue

Double check if there are jokes generated by GPT-2 which resemble those in your training data. If not, you can be sure, that new humor is being created. Let's just hope it is funny...

#### GPT vs BERT <a href="#gpt-vs-bert" id="gpt-vs-bert"></a>

GPTs and BERTs are both heavyweights (both in terms of performance and # parameters) in NLP. Let's see, what are their major differences and similarities. You have already learned about both of them, but it's always useful to compare them side-by-side. So firstly, let's read some articles doing just that, then we will try to evaluate their performance

* [https://www.kaggle.com/residentmario/notes-on-gpt-2-and-bert-models](https://www.kaggle.com/residentmario/notes-on-gpt-2-and-bert-models)
* [https://analyticsindiamag.com/gpt-3-vs-bert-for-nlp-tasks/](https://analyticsindiamag.com/gpt-3-vs-bert-for-nlp-tasks/)

So as you have read in the articles above, both architectures are transformers-based. GPT series are decoders and BERT are encoders. Both variants have a lot of parameters and trained on GB and GB of data.

### Exercise <a href="#exercise" id="exercise"></a>

One question still remains though. Which one is faster?

Your last task of the lesson:

* Compare inference speeds of GPT-2 and BERT. Use the texts below

```python
text_gpt = f"""
One day, a fox became very hungry as he went to search for some food. He searched high and low, but couldn’t find something that he could eat.
Finally, as his stomach rumbled, he stumbled upon a farmer’s wall. At the top of the wall, he saw the biggest, juiciest grapes he’d ever seen. They had a rich, purple color, telling the fox they were ready to be eaten.
To reach the grapes, the fox had to jump high in the"""


text_bert = """
One day, a fox became very hungry as he went to search for some food. He searched high and low, but couldn’t find something that he could eat.
Finally, as his stomach rumbled, he stumbled upon a farmer’s wall. At the top of the wall, he saw the biggest, juiciest grapes he’d ever seen. They had a rich, purple color, telling the fox they were ready to be eaten.
To reach the grapes, the fox had to jump high in the [MASK]."""
```

Why will we need two different texts to test the two models? Remember, that BERT is a masked language model, meaning it tries to predict masked out words. While GPT is a causal language model, which tries to predict next in sequence.

***

### Summary <a href="#summary" id="summary"></a>

In this lesson, we learned how to make a character-level generative model based on RNNs. We saw, that the performance of such a model was not very good and we discussed what factors of such an approach could be limiting this performance. Later we looked into the GPT family, what they are and how they work at a very high level. Then we compared it BERT in terms of functionality as well as speed. Such understanding of different types of technologies is very important as it will allow you to make informed decisions when choosing the best approach for your problem

```python
```
