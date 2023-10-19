# 👨🌾 Transformers Part 2

In the previous lesson, we have learned a lot about transformers. You must have the basic concepts about how transformers work. In this lesson, we will continue the journey with this technology. We will look more in-depth into the foundational part of transformers, which made them so efficient and well-performing - attention.

Start by refreshing your mind with the original paper about attention, then we will continue familiarizing with one of the most famous transformer architectures BERT and its progeny RoBERTa

### Learning outcomes: <a href="#learning-outcomes" id="learning-outcomes"></a>

* Self-attention
* Bert and Roberta
* Sentiment analysis

***

### Attention <a href="#attention" id="attention"></a>

![](https://images7.memedroid.com/images/UPLOADED702/5e398f634526a.jpeg)Source: https://www.memedroid.com/

#### Roberta <a href="#roberta" id="roberta"></a>

In this lesson, the most important concepts to understand will be the attention and self-attention mechanisms. But before that, familiarize yourself with RoBERTa and how the authors' approach squeezed the maximum performance out of BERT. Below there is the original paper as well as the paper review. Choose the best format for you

* [https://arxiv.org/abs/1907.11692](https://arxiv.org/abs/1907.11692)\
  and/or
* [https://www.youtube.com/watch?v=-MCYbmU9kfg](https://www.youtube.com/watch?v=-MCYbmU9kfg)

#### Attention is all you need <a href="#attention-is-all-you-need" id="attention-is-all-you-need"></a>

Let's continue to the main topic of the lesson - attention and self-attention.

Refresh your mind with the original paper, Part 3.2 - Attention

* [https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)

Additional material:

* [https://www.saama.com/attention-mechanism-benefits-and-applications/](https://www.saama.com/attention-mechanism-benefits-and-applications/)
* [https://medium.com/data-from-the-trenches/decoding-nlp-attention-mechanisms-38f108929ab7](https://medium.com/data-from-the-trenches/decoding-nlp-attention-mechanisms-38f108929ab7)
* [https://www.youtube.com/watch?v=W2rWgXJBZhU](https://www.youtube.com/watch?v=W2rWgXJBZhU)
* [https://medium.com/syncedreview/a-brief-overview-of-attention-mechanism-13c578ba9129](https://medium.com/syncedreview/a-brief-overview-of-attention-mechanism-13c578ba9129)

#### Self-attention <a href="#self-attention" id="self-attention"></a>

* [https://medium.com/lsc-psd/introduction-of-self-attention-layer-in-transformer-fc7bff63f3bc](https://medium.com/lsc-psd/introduction-of-self-attention-layer-in-transformer-fc7bff63f3bc)
* [https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a](https://towardsdatascience.com/illustrated-self-attention-2d627e33b20a)
* [https://www.youtube.com/watch?v=OYygPG4d9H0](https://www.youtube.com/watch?v=OYygPG4d9H0)

\[OPTIONAL]\
These are the tutorials and notebook on how to code a transformer from scratch. Feel free to try this out in your notebook.

* [https://www.youtube.com/watch?v=U0s0f995w14](https://www.youtube.com/watch?v=U0s0f995w14)
* [https://atcold.github.io/pytorch-Deep-Learning/en/week12/12-3/](https://atcold.github.io/pytorch-Deep-Learning/en/week12/12-3/)
* [https://github.com/Atcold/pytorch-Deep-Learning/blob/master/15-transformer.ipynb](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/15-transformer.ipynb)

#### BERT and RoBERTa <a href="#bert-and-roberta" id="bert-and-roberta"></a>

* [http://jalammar.github.io/illustrated-bert/](http://jalammar.github.io/illustrated-bert/)
* [https://towardsdatascience.com/bert-roberta-distilbert-xlnet-which-one-to-use-3d5ab82ba5f8](https://towardsdatascience.com/bert-roberta-distilbert-xlnet-which-one-to-use-3d5ab82ba5f8)

#### Recap <a href="#recap" id="recap"></a>

Phew! There is a lot of theory and a lot of concepts to understand. Let's recap on the most important things:

**Attention**

* Transformers don't use recurrent architectures nor convolutions to represent attention
* Positional encoders use sinusoidal patterns to represent position, as it helps with texts of unseen length
* Attention is represented by query, key, and value and their linear combination
* Transformers use multiple attention heads which improves learning
* Layer normalization and residual connections are used in transformers to aid optimization
* Scaling is used in attention layers to avoid vanishing gradient problem

**RoBERTa**

* Still uses BERT architecture
* Trains BERT model in a more optimized way
* Amount of data is increased by 10x
* Introduced dynamic masking to improve generalization
* Increased training batch size

### Exercise <a href="#exercise" id="exercise"></a>

Let's try to put into practice what we learned by doing a classic problem of understanding the sentiment of user reviews.

For everything you need to know about sentiment analysis - [http://nlpprogress.com/english/sentiment\_analysis.html](http://nlpprogress.com/english/sentiment\_analysis.html)

For this task, you are free to choose your own dataset. You can use any of the popular datasets for sentiment analysis. Check out [this link](http://nlpprogress.com/english/sentiment\_analysis.html) for a comprehensive list of resources.\
_Suggestion:_ use Kaggle (e.g. [IMDB](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)) or [TorchText](https://torchtext.readthedocs.io/en/latest/datasets.html) as your data sources

#### EDA <a href="#eda" id="eda"></a>

Tasks:

* Data preprocessing (if any)
* EDA

```python
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
```

```
/kaggle/input/imdb-dataset-of-50k-movie-reviews/IMDB Dataset.csv
```

#### Dataset <a href="#dataset" id="dataset"></a>

Before we go and start building our dataloaders, as in the previous lesson, let's recap on how our models will behave in terms of data input/output.

So BERT and RoBERTA are both [masked language models](https://demo.allennlp.org/masked-lm). This means when we train them, we randomly mask out words in the sentence and ask the model to fill in those gaps with the most probable words (self-supervised learning). As you already have seen in the material above, this way a model learns the semantics of a language (dataset you train on). Then during inference time, the models will encode your sequence to a fixed size latent space, just as we did with encoding image to latent space. Then we can use those vectors to make predictions about our data.

Luckily for us, we don't have to train neither of these models from scratch. Good people from HuggingFace made this available for us to use

* BERT - [https://huggingface.co/transformers/model\_doc/bert.html](https://huggingface.co/transformers/model\_doc/bert.html)
* RoBERTa - [https://huggingface.co/transformers/model\_doc/roberta.html](https://huggingface.co/transformers/model\_doc/roberta.html)

Tasks:

* Create a data pipeline. As in the previous lesson, use PyTorch dataset
* Create train/val/test data splits

```python
class IMDBDataset(Dataset):
    archs = {
        "bert": (BertTokenizer, "bert-base-uncased"),
        "roberta": (RobertaTokenizer, "roberta-base"),
    }
    def __init__(self, df: pd.DataFrame, arch: str = "bert", max_sequence_length: int = 256):
        tokenizer, version = self.archs[arch]
        
        self.tokenizer = tokenizer.from_pretrained(version, do_lower_case=True)
        self.df = df
        self.max_sequence_length = max_sequence_length

    def __len__(self): ...

    def __getitem__(self, idx): ...
```

```python
sample = IMDBDataset(df, max_sequence_length=10)[0]
assert "input_ids" in sample.keys()
assert "token_type_ids" in sample.keys()
assert "attention_mask" in sample.keys()
assert "labels" in sample.keys()
assert isinstance(sample['input_ids'], torch.Tensor)
assert len(sample['input_ids'].shape) == 1, "The sample output should be 1-dimensional vector. When dataloader creates a batch, it will automatically create a 2-D array"
```

```
Downloading:   0%|          | 0.00/232k [00:00<?, ?B/s]
```

#### Model <a href="#model" id="model"></a>

As in the previous lesson, you should be using PyTorch-Lightning to build your model

Tasks:

* Train two models: BERT and RoBERTa from HuggingFace Transformers library
* Evaluate both of the models. As a minimum:
  * Confusion matrix
  * Classification report
* Compare their performance
* ⚠️ **Do not** use HuggingFace transformers [pipeline](https://huggingface.co/transformers/main\_classes/pipelines.html#transformers.pipeline) (but you can take inspiration from there)
* Get output of any of the attention heads from any layer in BERT for some sample input
* Create a heat map from this attention head output, investigate what do the different strengths of values represent. See [bertviz](https://github.com/jessevig/bertviz) for ideas

***

### Summary <a href="#summary" id="summary"></a>

In this lesson, we have gained a more in-depth understanding of what are transformers in NLP and managed to train two different transformer architectures on a sentiment classification dataset. We have seen, that using transfer learning, with very little fine-tuning we can train a model to understand the sentiment - a task that requires a very good understanding of a language and its semantics. Similarly, we can utilize transformers for many different purposes, like question answering, which we will discuss in the next sprint. For the next lesson, we will learn about recurrent neural networks, their types, and how to use them for language generation.

```python
```
