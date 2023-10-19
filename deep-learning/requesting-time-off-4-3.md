# 🌀 Recurrent Neural Networks

Welcome to lesson 3 of NLP, where we will be looking into recurrent neural networks (RNN), understanding how they work, looking into potential use cases, advantages and disadvantages. While transformers have surpassed RNNs in the NLP research context, however, it does not mean they are obsolete. There are still plenty of applications for this technology, such as time-series prediction, working with short text sequences (classification, text generation), anomaly detection just to name a few.

### Learning outcomes: <a href="#learning-outcomes" id="learning-outcomes"></a>

* Recurrent neural networks
* LSTM
* GRU
* Text generation

***

#### Recurrent Neural Networks <a href="#recurrent-neural-networks" id="recurrent-neural-networks"></a>

![](https://www.bouvet.no/bouvet-deler/explaining-recurrent-neural-networks/\_/attachment/inline/dbb03f2e-cfa5-4914-88fd-422231379121:b9e76ed5b43ad981d8e9891158a192ec098c2314/Screenshot%202019-07-11%20at%2016.31.24.png)Source: https://www.bouvet.no/bouvet-deler/explaining-recurrent-neural-networks

```
</div></div>
```

In the material from the last 2 lessons (transformers), you have probably heard quite a lot of abbreviations like LSTM or RNN or GRU. Transformers are often compared to such concepts as more superior for their ability to have a longer context span (through attention mechanism) and better parallelization (lower training/inference times on GPU/TPU)

However as mentioned, this technology has its uses and it's important to learn them. So let's begin the RNNs journey with some reading material. We will then practice building an LSTM network for generating text.

#### Intorudction to RNNs <a href="#intorudction-to-rnns" id="intorudction-to-rnns"></a>

* [https://course.fast.ai/videos/?lesson=8](https://course.fast.ai/videos/?lesson=8)
* [https://stanford.edu/\~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks](https://stanford.edu/\~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks)
* [https://explained.ai/rnn/index.html](https://explained.ai/rnn/index.html)
* [http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)

#### LSTM, AWD-LSTM and GRU <a href="#lstm-awd-lstm-and-gru" id="lstm-awd-lstm-and-gru"></a>

* [https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)
* [https://www.youtube.com/watch?v=QciIcRxJvsM](https://www.youtube.com/watch?v=QciIcRxJvsM)
* [https://colah.github.io/posts/2015-08-Understanding-LSTMs/](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

An interesting article about differences in RNN architectures

* [An Empirical Exploration of Recurrent Network Architectures](http://proceedings.mlr.press/v37/jozefowicz15.pdf)

### Exercise <a href="#exercise" id="exercise"></a>

Let's see how we can use the theory we learned in this lesson for some real-world tasks.

You have been contacted by a well-known national news agency. Their ratings have recently been falling and they decided to get more traffic to their website by making their headlines more catchy, i.e. click-bait headlines. The idea is to give their editors a tool, that could automatically generate realistic click-bait headlines.

We will use click-bait headlines dataset from [https://www.kaggle.com/therohk/examine-the-examiner](https://www.kaggle.com/therohk/examine-the-examiner) and will try to create an RNN which generates click-bait. Exciting!

In this lesson, we will first go through a possible implementation in PyTorch Lightning as a demo, then you will have to implement the same solution yourself, but in FastAI.

#### EDA <a href="#eda" id="eda"></a>

Tasks:

* Analyze data (EDA)

```python
import os

import pandas as pd
import numpy as np
```

### EDA + Preprocessing <a href="#eda--preprocessing" id="eda--preprocessing"></a>

Let's understand how many words does a normal click-bait title have

#### Create dataset <a href="#create-dataset" id="create-dataset"></a>

Before we start creating data loaders for our models, let's just remind ourselves how our RNN will work. Our input data will be a sequence of fixed length, say the first 4 words of a headline. The task of the model will be to predict the next word in the sequence. The model will do this by returning all except the first word in the input sequence and appending the predicted word to the end. This probably is more clear in the notation: so the model takes `this_as_input = ["I", "want", "to", "learn"]` and returns `this_as_output = ["want", "to", "learn", "RNNs"]`

The number of words in your sequence we'll refer to as sequence\_length. You can change the sequence length as you please: more words means more context, but also more memory required, slower inference speed, and training time. Choose something that makes sense for your problem.

Then the question becomes, what do I do if my desired sequence\_length is longer than my sequence? You might have seen this in one of the learning material already - we will pad it until we reach the required length. You can choose any special character you want for your padding, just keep it consistent, e.g. in BERT, text is tokenized like so:

```python
sequence_length = 6
my_sequences = [
    ["I", "love", "burgers", "[PAD]", "[PAD]", "[PAD]"],   
    ["John", "has", "travelled", "the", "world", "when"],
    ["Three", "plus", "five", "is", "eight", "[PAD]"],
]
```

But in most of the cases, your sequence\_length will be lower than input length. For the training data, you have some choices. Assuming you sequence length will be e.g. 5:

1. You can generate all word sequences of length 5 + next word as label. So a text of length 10, would result in 5 training samples. Be careful then with train/val/test splits. You want to make sure you don't get samples from the same sequence in different splits.
2. You could take 5 tokens + label from a random position in text. You will need to make more epochs then to make sure your model sees as much data as possible.
3. Take always the first 5 tokens from the beginning of text. Not recommended, since you will lose on a lot of data.

For this demo, we will implement option 1 using PyTorch Iterable dataset. See [PyTorch docs](https://pytorch.org/docs/stable/data.html#iterable-style-datasets) about what it is

```python
from transformers import DistilBertTokenizer
from functools import partial
from torch.utils.data import IterableDataset
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

import pytorch_lightning as pl
```

```python
class ClickBaitDataset(IterableDataset):
    def __init__(self, text: pd.Series, sequence_length: int = 8):
        super().__init__()
        
        assert isinstance(text, pd.Series), "Must be pandas Series"
        
        self.text = text
        self._sequence_length = sequence_length

        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', do_lower_case=True)
        self.encoder = partial(
            self.tokenizer.encode,
            add_special_tokens = True,
        )

    def __iter__(self):
        for _, title in self.text.iteritems():
            encoded_sentence = self.encoder(title)
            for i in range(len(encoded_sentence) - self._sequence_length):
                x = encoded_sentence[i:i+self._sequence_length]
                y = encoded_sentence[i+1:i+self._sequence_length+1]
                
                yield torch.tensor(x), torch.tensor(y)  
       
    @property
    def vocab_size(self):
        return self.tokenizer.vocab_size
```

```python
dataset = ClickBaitDataset(df['headline_text'])
dataset_iter = iter(dataset)

for _ in range(5):
    x, y = next(dataset_iter)
    assert x.shape == y.shape, "x and y should both have the same shape"
    assert all(x[1:] == y[:-1]),  "x and y should have the same content except for the first and last items"
    print(x, y)
```

```
HBox(children=(FloatProgress(value=0.0, description='Downloading', max=231508.0, style=ProgressStyle(descripti…
```

```
tensor([  101,  3481,  4276,  3267,  2415, 13999,  2336,  2000]) tensor([ 3481,  4276,  3267,  2415, 13999,  2336,  2000,  1037])
tensor([ 3481,  4276,  3267,  2415, 13999,  2336,  2000,  1037]) tensor([ 4276,  3267,  2415, 13999,  2336,  2000,  1037,  5379])
tensor([ 4276,  3267,  2415, 13999,  2336,  2000,  1037,  5379]) tensor([ 3267,  2415, 13999,  2336,  2000,  1037,  5379,  6071])
tensor([ 3267,  2415, 13999,  2336,  2000,  1037,  5379,  6071]) tensor([ 2415, 13999,  2336,  2000,  1037,  5379,  6071,   102])
tensor([  101,  1996, 24078,  1997,  3899,  8946,  9404,  1006]) tensor([ 1996, 24078,  1997,  3899,  8946,  9404,  1006,  8946])
```

```python
from sklearn.model_selection import train_test_split

df_train, df_val = train_test_split(df, test_size=0.1, random_state=13)

df_train, df_val = df_train.reset_index(drop=True), df_val.reset_index(drop=True)
```

#### Create a model <a href="#create-a-model" id="create-a-model"></a>

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
device
```

```
'cuda'
```

We will create a model, with 2 LTSM cells. The input for such a model would be an Embedding layer. The purpose of this layer is to convert a text string into a fixed size latent vector, kind of sentence2vec. This will feed to two LSTM cells in series and a fully connected output layer.

What will be the output of this Linear layer? Differently to what we have seen in classification, this time the output will be a 3-D array of \[batch x vocabulary\_size x sequence\_length]. Or in words, ignoring the batch dim, it would return a likelihood for every word in your vocabulary for every position in your sequence. Since we are interested in predicting only the last word, in inference we would consider the logits for the last word.

In code, this would be

```python
class ClickBaitModel(pl.LightningModule):
    
    def __init__(self, vocab_size: int, sequence_length: int):
        super().__init__()
        
        self.sequence_length = sequence_length
        self.vocab_size = vocab_size
        self.num_layers = 5
        self.hidden_size = 512
        self.embedding_size = 256
        
        self.embedding = nn.Embedding(self.vocab_size, self.embedding_size)

        self.rnn1 = nn.LSTM(
            input_size=self.embedding_size,
            hidden_size=self.hidden_size,
            num_layers=self.num_layers,
            dropout=0.3,
        )
        self.rnn2 = nn.LSTM(
            input_size=self.hidden_size,
            hidden_size=self.hidden_size,
            num_layers=self.num_layers,
            dropout=0.3,
        )
            
        self.out = nn.Linear(self.hidden_size, self.vocab_size)
        
        self.h, self.c = self.init_state(self.sequence_length) 
        
        self.h, self.c = self.h.to(device), self.c.to(device)
        self.criterion = nn.CrossEntropyLoss()

        self.lr = 5e-4
        
    
    def forward(self, x, prev_state):
        embed = self.embedding(x)
        x, (h, c) = self.rnn1(embed, prev_state)
        x, (h, c) = self.rnn2(x, (h, c))
        logits = self.out(x)
        return logits, (h, c)
    
    def training_step(self, batch, batch_idx):
        x, y = batch        
        y_hat, (h, c) = self(x, (self.h, self.c))
        y_hat = y_hat.transpose(1, 2)
        
        loss = self.criterion(y_hat, y)
        
        self.h, self.c = h.detach(), c.detach()
        self.log("train_loss", loss)
    
        return loss
    
    def validation_step(self, batch, batch_idx):
        x, y, y_ = batch        
        y_hat, (h, c) = self(x, (self.h, self.c))
        y_hat = y_hat.transpose(1, 2)
        
        loss = self.criterion(y_hat, y)
        
        self.h, self.c = h.detach(), c.detach()
        
        self.log("val_loss", loss)

    def init_state(self, sequence_length):
        return (torch.zeros(self.num_layers, sequence_length, self.hidden_size),
                torch.zeros(self.num_layers, sequence_length, self.hidden_size))
    
    def train_dataloader(self):
        dataset = ClickBaitDataset(df_train['headline_text'], sequence_length=self.sequence_length)
        return DataLoader(dataset, batch_size=500, num_workers=3)
    
    def val_dataloader(self):
        dataset = ClickBaitDataset(df_val['headline_text'], sequence_length=self.sequence_length)
        return DataLoader(dataset, batch_size=500, num_workers=3)
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.lr)
```

A likely question here, would be "why are we interested in our model returning the hidden state of the last LSTM layer?". This is because once we predict the next word in a sequence, we don't want to forget all the context we have, since we will be predicting more words.

Let's train and fine-tune the model

```python
model = ClickBaitModel(vocab_size = dataset.vocab_size, sequence_length = 5)
```

```python
trainer = pl.Trainer(max_epochs=3, gpus=1)
```

```
GPU available: True, used: True
TPU available: False, using: 0 TPU cores
LOCAL_RANK: 0 - CUDA_VISIBLE_DEVICES: [0]
```

```python
trainer.fit(model)
```

```
  | Name      | Type             | Params
-----------------------------------------------
0 | embedding | Embedding        | 7 M   
1 | rnn1      | LSTM             | 9 M   
2 | rnn2      | LSTM             | 10 M  
3 | out       | Linear           | 15 M  
4 | criterion | CrossEntropyLoss | 0     
```

```
HBox(children=(FloatProgress(value=1.0, bar_style='info', description='Training', layout=Layout(flex='2'), max…
```

```
1
```

```python
model.lr = 1e-5

trainer = pl.Trainer(max_epochs=5, gpus=1)
```

```
GPU available: True, used: True
TPU available: False, using: 0 TPU cores
LOCAL_RANK: 0 - CUDA_VISIBLE_DEVICES: [0]
```

```python
trainer.fit(model)
```

```
  | Name      | Type             | Params
-----------------------------------------------
0 | embedding | Embedding        | 7 M   
1 | rnn1      | LSTM             | 9 M   
2 | rnn2      | LSTM             | 10 M  
3 | out       | Linear           | 15 M  
4 | criterion | CrossEntropyLoss | 0     
```

```
HBox(children=(FloatProgress(value=1.0, bar_style='info', description='Training', layout=Layout(flex='2'), max…
```

```
1
```

Then we can make predictions with our model for a wanted length>

```python
def logits_to_token(logits):
    p = torch.nn.functional.softmax(logits, dim=0).detach().cpu().numpy()
    return np.random.choice(len(logits), p=p)


def predict(tokenizer, model, text:str, max_next_words=15):
    model = model.eval()
    tokens = tokenizer.encode(text, add_special_tokens=False)
    tokens = [tokenizer.cls_token_id] + tokens
    
    sequence_length = len(tokens)
    state_h, state_c = model.init_state(sequence_length)
    
    for i in range(max_next_words):
        x = torch.tensor(tokens[i:i+sequence_length]).unsqueeze(0)
        
        y_pred, (state_h, state_c) = model(x, (state_h, state_c))
        
        last_word_logits = y_pred.squeeze(0)[-1]
        token = logits_to_token(last_word_logits)
        
        tokens.append(token)
        if token == tokenizer.sep_token_id:
            break
        
    return tokenizer.decode(tokens)
```

```python
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', do_lower_case=True)

text = "10 films that"
predict(tokenizer, model, text, np.random.randint(4,15))
```

```
"[CLS] 10 films that sha predictions secret found gabriel fashion 'nigo"
```

As you can see, the results are pretty poor. What could be the reasons for that:

* Not using transfer learning (e.g. pre-trained language model)
* Only trained on a small sub-sample of the dataset.
* Not big enough network. Add more LSTM cells could improve performance.
* Use a custom tokenizer. In this example, we used Bert tokenizer. Likely the vocabulary for our dataset is much smaller than that of Bert, which would significantly reduce the size of the network, and the chance of successful training.

Building generative models can be challenging. It takes quite a bit to train a model and some search to understand the best practices and approaches.

Another way would be to build it using FastAI framework. Let's see how much easier it is to train a language model

Tasks:

* Train a language model on FastAI
* Generate 20 click-bait titles randomly ranging from 4 to 15 words. Pick your favorites.

FastAI abstracts a lot of concepts, so we don't have to spend time implementing data loaders, or language models.

Read about AWD-LSTM and see if you can create a language model in FastAI, which uses this architecture\
[https://yashuseth.blog/2018/09/12/awd-lstm-explanation-understanding-language-model/](https://yashuseth.blog/2018/09/12/awd-lstm-explanation-understanding-language-model/)

That should have been much easier! Although, likely, the results are still nowhere near the quality of generating plausible headlines.

***

### Summary <a href="#summary" id="summary"></a>

In this lesson, we learned about recurrent neural network, their variants, how they work and how to implement them in PyTorch and FastAI. Generative models can be tricky to train and generate good quality results. If you are a beginner, FastAI framework is a better choice since its API allows for very easy model training, inference and due to best-practices - better results. In the next lesson, we will continue to explore generative models and see if we can make them perform better than in this lesson.

```python
```
