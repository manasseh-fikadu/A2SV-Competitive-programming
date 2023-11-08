---
description: >-
  In this first lesson, we will be looking into more advanced transformer
  architectures and see how they are addressing inherent limitations of Bert
  family transformers.
---

# 🎓 Advanced NLP

### Longformers <a href="#longformers" id="longformers"></a>

![](https://i.pinimg.com/originals/bd/15/4f/bd154fdb54f0ff6fa025d86ee3a95841.jpg)Source: https://www.pinterest.es/pin/655203445763107826/

We saw in the previous lessons, that BERT is pretty awesome and can do a variety of tasks. If you still not convinced, this article might change your mind [https://towardsdatascience.com/a-review-of-bert-based-models-4ffdc0f15d58](https://towardsdatascience.com/a-review-of-bert-based-models-4ffdc0f15d58).

So if BERT is that good, what exactly are researchers trying to improve? Well for one, the main limitation of BERT is the max sequence length the model can take - 512 tokens. This means, on really long texts, it is highly likely this transformer will be losing context from early parts of documents, such as legal documents or books. Moreover, the memory requirement for the attention mechanism grows quadratically with sequence length. Thus it makes BERT not a very good choice for documents, where long context dependencies are required.

Meet Longformer 🙌. It is a BERT family model (meaning it is a bi-directional encoder) with a twist! Read the resources below and see how, this technology is addressing the limitations in BERT:

* [https://arxiv.org/abs/2004.05150](https://arxiv.org/abs/2004.05150)\
  and/or
* [https://www.youtube.com/watch?v=\_8KNb5iqblE](https://www.youtube.com/watch?v=\_8KNb5iqblE)

Additional Resources:

* [https://medium.com/dair-ai/longformer-what-bert-should-have-been-78f4cd595be9](https://medium.com/dair-ai/longformer-what-bert-should-have-been-78f4cd595be9)
* [https://www.youtube.com/watch?v=gJR28onlqzs](https://www.youtube.com/watch?v=gJR28onlqzs)

### Question Answering <a href="#question-answering" id="question-answering"></a>

Today exercises later on we will base on the concept of question answering. The task is exactly what it says on the tin - given a text and a reference text a model tries to answer the question. We will check out how BERT and Longformer both perform on this task.

You are probably asking yourself - "But BERT is an encoder. I know it can represent text into a latent space, but how can it actually generate new text? Don't you need a decoder for that? 🤔" Great question. It turns out - not really. For question answering, a new concept of start and end tokens is introduced, which generates probabilities for words from the reference text being part of the answer. So no new text is generated, and the task becomes a classification task.

Check this article to get more intuition on how this works:

* [https://medium.com/saarthi-ai/build-a-smart-question-answering-system-with-fine-tuned-bert-b586e4cfa5f5](https://medium.com/saarthi-ai/build-a-smart-question-answering-system-with-fine-tuned-bert-b586e4cfa5f5)

### Exercise <a href="#exercise" id="exercise"></a>

We know machine learning can do a variety of different tasks. But can it cook?! 🧑‍🍳

Let's play around with HuggingFace transformers library. It offers BERT finetuned on [SQUAD dataset](https://rajpurkar.github.io/SQuAD-explorer/).

Tasks:

* Use the cake recipe below to ask model some questions regarding it.
* Use BERT pre-trained on squad from HuggingFace transformers

Hint: Use `pipeline` method to load model and make predictions

```python
# Reference: https://www.allrecipes.com/recipe/17481/simple-white-cake/ (in case you want to make it...)

recipe =  """
This cake was sent home from our children's school. 
It is the simplest, great tasting cake I've ever made. Great to make with the kids, especially for cupcakes.

Recipe Summary
Prep: 20 mins
Cook: 30 mins
Total: 50 mins
Servings: 12
Yield: 12 cupcakes or 1- 9x9 inch pan

Ingredient Checklist
1 cup white sugar
0.5 cup butter
2 large eggs
2 teaspoons vanilla extract
1.5 cups all-purpose flour
1.75 teaspoons baking powder
0.5 cup milk

Instructions Checklist
Step 1
Preheat oven to 350 degrees F (175 degrees C). Grease and flour a 9x9 inch pan or line a muffin pan with paper liners.

Step 2
In a medium bowl, cream together the sugar and butter. 
Beat in the eggs, one at a time, then stir in the vanilla. 
Combine flour and baking powder, add to the creamed mixture and mix well. 
Finally stir in the milk until batter is smooth. Pour or spoon batter into the prepared pan.

Step 3
Bake for 30 to 40 minutes in the preheated oven. For cupcakes, bake 20 to 25 minutes. 
Cake is done when it springs back to the touch.
"""
```

```python
question = "When is a cake done?"
```

#### Question answering - How it works? <a href="#question-answering---how-it-works" id="question-answering---how-it-works"></a>

You have to admit - it's pretty cool. Let's look deeper into how this works to understand the mechanics

```python
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')
tokenizer = BertTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
```

We will encode the text in our usual way for BERT. The only difference to what we did before when training an MLM, is we will be providing a `text_pair` to the encoder

```python
encoding = tokenizer.encode_plus(text=question, text_pair = recipe, return_tensors='pt')
encoding.keys()
```

Remember, that training BERT is multiobjective learning task, where one of the objectives is to guess, whether one sentence follows the next, i.e. model is trained in pairs of sentences. By providing a `text_pair` we force our `token_type_ids` for question to be zeros and 1 for paragraph. You can read more about token type ids [https://huggingface.co/transformers/glossary.html#token-type-ids](https://huggingface.co/transformers/glossary.html#token-type-ids)

```python
encoding['token_type_ids']
```

When we call a model it returns start and end scores for each word, which simply are probabilities that a word is a start/end of the answer respectively. Note, it's not actually a probability distribution, since the values don't add to 1 but rather a likelihood. We could get probability distribution by applying a softmax over the vector

```python
with torch.no_grad():
    start_scores, end_scores = model(input_ids=encoding['input_ids'], token_type_ids=encoding['token_type_ids'])
```

```python
encoding['input_ids'].shape
```

```python
start_scores.shape
```

```python
end_scores.shape
```

Sometimes it happens, that the model gives importance to some special tokens, like beginning/end of a sentence. We want to avoid this since the importance for stat/end token to a special token is non-sensical. Thus we can manually set the score for these tokens to a very low value, effectively reducing their probability to 0

```python
start_scores[0,0], end_scores[0,0] = -1e10, -1e10
```

Let's take the softmax of all the scores to get the probability distribution and visualize it

```python
import pandas as pd

start_proba = torch.softmax(start_scores, axis=1).detach().numpy()[0]
end_proba = torch.softmax(end_scores, axis=1).detach().numpy()[0]

pd.DataFrame({"start": start_proba, 'end': end_proba}).plot.line(figsize=(15,3))
```

The sequence between max values of start and end, is our answer

```python
start_index = torch.argmax(start_scores)
end_index = torch.argmax(end_scores)
```

```python
start_index.item()
```

```python
end_index.item()
```

```python
answer = tokenizer.decode(encoding['input_ids'][0, start_index:end_index+1])
answer
```

#### Training your own question answering model <a href="#training-your-own-question-answering-model" id="training-your-own-question-answering-model"></a>

If you wanted to train a transformer on your custom dataset, this is pretty easy. You could build a model with pre-trained BERT as a backbone, the output layer having 2 outputs: 1 that predicts an index of start token and another that predicts the end token. Thus, it's a classification problem - classifying start and end tokens from 512 possible. You would use a standard multi-class loss `CrossEntropyLoss`. As input you would pass questions and answers exactly as you have seen above: both tokenized and differentiated by `token_type_ids`.

Check out these links below for a more detailed explanation with code as well as source code for BertForQuestionAnswering. This is an FYI only and we won't build such models ourselves.

* [https://towardsdatascience.com/question-answering-with-bert-xlnet-xlm-and-distilbert-using-simple-transformers-4d8785ee762a](https://towardsdatascience.com/question-answering-with-bert-xlnet-xlm-and-distilbert-using-simple-transformers-4d8785ee762a)
* [https://huggingface.co/transformers/\_modules/transformers/modeling\_bert.html#BertForQuestionAnswering](https://huggingface.co/transformers/\_modules/transformers/modeling\_bert.html#BertForQuestionAnswering)

### Exercise: <a href="#exercise" id="exercise"></a>

So our text was pretty short, with added special tokens - 284.

Use the story and question below and try to use BERT

```python
# reference https://www.nature.com/articles/d41586-020-02187-7

story = """
A Chinese spacecraft is on its way to Mars after launching successfully from Hainan Island in southern China. The mission — named Tianwen-1, which means ‘questions to heaven’ — is the country’s first attempt to land on the red planet.

The 5,000-kilogram spacecraft, which contains a lander, orbiter and rover, blasted off from the Wenchang Satellite Launch Center aboard a Chinese Long March-5 rocket at 12:41 p.m. local time on 23 July. Some 36 minutes later, the craft was successfully put on its trajectory towards Mars.

“This is a really ambitious mission driven by science that represents significant progress in China’s space programme, and they should be proud,” says David Flannery, an astrobiologist at Queensland University of Technology in Brisbane, Australia. “There are a lot of other things that could still go wrong, but so far so good,” he says.


Countdown to Mars: three daring missions take aim at the red planet
Chinese officials have been tight-lipped about many details of Tianwen-1, including the cost and launch preparations. “The Mars mission is very risky, so I understand why managers are keeping quite a low profile,” says Ji Wu, former head of China’s National Space Science Center in Beijing. Ji was chief scientist on China’s earlier attempt to send an orbiter to Mars aboard a Russian spacecraft in 2011, which failed. “It didn’t even depart from Earth’s orbit. That was a very sad story,” he says.

Tianwen-1 is one of three daring missions to the red planet this year. The United Arab Emirates (UAE) launched its Hope orbiter earlier this week, and the United States’ craft — a six-wheeled rover named Perseverance — is likely to launch next week.

Together with the success of the UAE’s orbiter, Tianwen-1 adds weight to a new reality “that Solar System exploration is not the prerogative of the Euro-American world, but a global enterprise”, says geologist Jon Clarke, who is president of the Mars Society Australia based in Canberra. China, India and Japan have previously sent probes into space, including missions to the Moon, Mars, Venus and some asteroids.

Long journey
Tianwen-1 is now coasting through space before it reaches its destination in February. The craft will then spend several months positioning itself for the landing. In April, the orbiter will release the lander and rover into the Martian atmosphere, and these will touch down somewhere on Utopia Planitia — a vast plain littered with volcanic rocks within a large basin, and where NASA’s Viking 2 lander touched down more than three decades ago. If the landing is successful, China will be only the second country after the United States to softly land a rover on Mars, says Flannery. The six-wheeled, solar-powered rover will explore areas of scientific interest.

The orbiter will loop around Mars for an entire Martian year and act as a communication link for the rover, which has a lifetime of around 90 Martian days — the equivalent of some 93 days on Earth.


How China is planning to go to Mars amid the coronavirus outbreak
China’s mission aims to conduct a global survey of the planet, including studying its geological structures, surface characteristics and climate. The orbiter is packed with seven scientific instruments, and the rover has six more. These include several cameras, subsurface radar and a spectrometer.

A magnetic-field detector on the rover could gain valuable insights into Mars’s past magnetic field, which would have shielded the planet from radiation, says Flannery. And its ground-penetrating radar will help discern some of the geological structures just below the surface of the planet, he says.

The designs of the orbiter and rover seem to draw on China’s several successful missions to the Moon, but are significantly larger than previous probes, says Clarke. The mission “promises to be a milestone in Chinese and global exploration of the planet”, he says. “It will mean new and complementary data about Mars from orbit and from a new location on the Mars surface.”

New space powers
Mars has been a major focus of NASA’s space exploration, says Katarina Miljkovic, a planetary scientist at Curtin University in Perth, Australia. “Adding new countries to the mix, like China and UAE, is very exciting,” she says.

Smaller and newer space powers could also create opportunities for science, says Flannery, who helped build NASA’s Perseverance rover. The rover will collect rocks that will one day be brought back to Earth. “Many of the greatest challenges for planetary science in the coming decades will require international cooperation,” he says. The return of samples from Mars will be extremely expensive and technically complex. And the rocks should be studied by experts worldwide, he adds. China has its own plans to bring samples back from Mars by 2030. In some sense, Tianwen-1 is testing all the necessary technology for such a mission, says Flannery.

He hopes the Chinese space agency will share data from Tianwen-1 with the scientific community. China has shared some of its data sets of the Moon, and this should be followed for Mars, he says. “Space belongs to everyone.”
"""
```

```python
question = "Who does the space belong to?"
```

### Exercise <a href="#exercise" id="exercise"></a>

The chances are - you either got an error that the text is too long or completely nonsense answer (if you put a `truncation=True` in your tokenizer). Remember why? Exactly - because 512 is the max length that BERT can handle! Ups! So what should we do?

Two options == two more exercises

1. Split the sentence into chunks of max 512 length, make multiple predictions and join the start/end scores
2. Try this task with a Longformer

If everything went well, the answers should be the same. BERT was able to predict the text even though it was split because the answer did not need the context from the other split of the text. On the other hand, the Longformer should have been much easier to code and quicker to run.

### Exercise <a href="#exercise" id="exercise"></a>

Supposedly, Longformers are much more memory friendly, since they have sliding-window attention. But let's not take that for granted!

* Check what is the difference in run time for Longformer and BERT

Well, this is a surprise! Why is Longformer predicting slower than BERT, when we were promised memory efficiency? If we check the number of parameters for both models, we will see, the Longformer has 50M more parameters.

```python
sum(p.numel() for p in lf_model.parameters()) 
```

```python
sum(p.numel() for p in bert_model.parameters()) 
```

Referring back to the original paper for Longformers, the attention sliding window, which makes it possible to have document length longer than 512 is itself 512 tall. Meaning, if you take a text with less than 512 tokens you will not be taking advantage of Longformer. So the advantage would come from having to predict with BERT multiple times over a very long text, while still being able to keep the global context. Thus, when it comes to deciding whether to use a Longformer or not, see if your text is much longer than that of BERT and if your application requires long context dependencies, as this is the only way to take advantage of this technology.

***

### Summary <a href="#summary" id="summary"></a>

In this lesson, we have learned two new concepts: Longformer and question-answering with NLP. We have learned that Longformers are slower than BERT on short (<512 tokens) text and its real advantage comes from much longer documents. Moreover, we have seen how question-answering works with transformers and how training a transformer in pairs can enable such tasks.

In the next lesson, we will be going back to computer vision paradigm and look into advanced computer vision topics.

```python
```

\
