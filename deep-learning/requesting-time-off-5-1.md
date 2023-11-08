---
description: >-
  Deep learning is quite an extensive topic and its application reach much more
  than just text or image classification.
---

# 🎓 Advanced Deep Learning

### Object detection <a href="#object-detection" id="object-detection"></a>

![](https://pjreddie.com/media/image/Screen\_Shot\_2018-03-24\_at\_10.48.42\_PM.png)Source: https://pjreddie.com/darknet/yolo/

For some tasks, it's not enough to know that there is a dog or a bicycle in a picture. We also want to know where exactly in the image they are. While for humans this task is trivial, for computers not so much. There has been a ton of research over the last \~8 years for this problem. Most notable are the RCNN family (Region Proposal Networks) and Yolo family ("You only look once")

RCNN and its successors Fast-RCNN and Faster-RCNN have a lottery-style detection approach, when a network generates thousands of regions in an image of different shapes and sizes, then it classifies all of them, and the ones with a probability higher than some threshold are considered as positives.

Yolo on the other hand, divides an image into a grid, (e.g. 7x7 or 13x13 depending on Yolo version) and it predicts some number of bounding boxes in each grid. Yolo is a multi-objective learning algorithm as it models bounding boxes as regression (top-left and bottom-right corners) and class score for each grid as classification. Each grid can only contain 1 class.

There are some intricate details between the versions, so let's do some reading to understand more in-depth how these algorithms works, and then we will jump into exercises.

**Intro to object detection**

* [https://machinelearningmastery.com/object-recognition-with-deep-learning/](https://machinelearningmastery.com/object-recognition-with-deep-learning/)

**RCNN**

* [https://arxiv.org/abs/1506.01497](https://arxiv.org/abs/1506.01497)
* [https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html](https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html)

**Yolo**

* [https://arxiv.org/abs/1506.02640](https://arxiv.org/abs/1506.02640) and [https://arxiv.org/abs/1612.08242](https://arxiv.org/abs/1612.08242)
* [https://www.youtube.com/watch?v=NM6lrxy0bxs](https://www.youtube.com/watch?v=NM6lrxy0bxs)
* [https://medium.com/@ODSC/overview-of-the-yolo-object-detection-algorithm-7b52a745d3e0](https://medium.com/@ODSC/overview-of-the-yolo-object-detection-algorithm-7b52a745d3e0)
* [https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)

### Exercise <a href="#exercise" id="exercise"></a>

As with classification and NLP models, there is a variety of pre-trained object detection models

* Use a torchvision pre-trained RCNN model and classify some images of your choice
* Display images with bounding boxes superimposed and label above bounding box, something similar to what you see in the image above.

```python
# Use these images or find your own.

image_urls = [
    "https://thebogotapost.com/wp-content/uploads/2018/07/soccer-1457988_1920-1280x720.jpg",
    "https://i.ytimg.com/vi/SZF1LbmyH6E/maxresdefault.jpg"
]
```

```python
images = []
for url in image_urls:
    response = requests.get(url)
    im = Image.open(BytesIO(response.content))
    images.append(im)
```

```python
coco_labels = ["background", "person","bicycle","car","motorcycle","airplane","bus","train","truck","boat","traffic light","fire hydrant","street sign","stop sign","parking meter","bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","hat","backpack","umbrella","shoe","eye glasses","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard","tennis racket","bottle","plate","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake","chair","couch","potted plant","bed","mirror","dining table","window","desk","toilet","door","tv","laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator","blender","book","clock","vase","scissors","teddy bear","hair drier","toothbrush","hair brush"]
```

### Image segmentation <a href="#image-segmentation" id="image-segmentation"></a>

Very similar task to object detection is semantic object segmentation, with additional complexity: assigning every pixel in an image belonging to a particular class/object. Although there is a variety of methods, which try to solve this task, a good starting point is to use one of these 2 methods when it comes to object segmentation:

* Mask-RCNN
* U-Net

Mask RCNN is an extension of RCNN we saw in the section earlier. For this reason, it can segment different instances of the same object class (instance segmentation). While U-Net, although much simpler in design than Mask-RCNN, is limited to a single instance per class (semantic segmentation)

![](https://miro.medium.com/max/800/1\*SNvD04dEFIDwNAqSXLQC\_g.jpeg)Source: https://towardsdatascience.com/detection-and-segmentation-through-convnets-47aa42de27ea

Let's learn more about Mask-RCNN and U-Net, and then we will try to

* [https://arxiv.org/pdf/1703.06870.pdf](https://arxiv.org/pdf/1703.06870.pdf)
* [https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46](https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46)
* [https://www.youtube.com/watch?v=4tkgOzQ9yyo](https://www.youtube.com/watch?v=4tkgOzQ9yyo)

...and U-Net:

* [https://arxiv.org/abs/1505.04597](https://arxiv.org/abs/1505.04597)
* [https://towardsdatascience.com/understanding-semantic-segmentation-with-unet-6be4f42d4b47](https://towardsdatascience.com/understanding-semantic-segmentation-with-unet-6be4f42d4b47)

### Exercise <a href="#exercise" id="exercise"></a>

Let's look more into the U-Net architecture and see if we can create architecture for training such a model. We will not do the actual training, just implement the modules based on the paper.

For more intuition on segmentation check [this resource](https://www.jeremyjordan.me/semantic-segmentation/)

Tasks:

* Create a PyTorch module `UnetUpsample` for the upsampling units described in the paper. You can also use [this resource](https://towardsdatascience.com/learn-ai-today-05-image-segmentation-with-u-net-models-800105e400d1) for ideas.
* The UnetUpsample modules should work with already implemented UNet architecture. Although, feel free to change this as required.

```python
def batchnorm_unit(input_dim, hidden_dim):
    return nn.Sequential(
        nn.Conv2d(input_dim, hidden_dim, kernel_size=3, bias=False),
        nn.BatchNorm2d(hidden_dim),
        nn.ReLU(inplace=True),
    )
                        
def double_conv_block(input_dim, hidden_dim):
    return nn.Sequential(
        batchnorm_unit(input_dim, hidden_dim),
        batchnorm_unit(hidden_dim, hidden_dim)
    )
```

```python
class UnetUpsample(nn.Module):
    ...
```

```python
class UNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.down_block1 = double_conv_block(3, 64)
        self.down_block2 = double_conv_block(64, 128)
        self.down_block3 = double_conv_block(128, 256)
        self.down_block4 = double_conv_block(256, 512)

        self.bottleneck = nn.Sequential(
            double_conv_block(512, 1024),
            nn.Dropout(0.5)
        )
        
        self.upsample1 = UnetUpsample(1536, 512)
        self.upsample2 = UnetUpsample(768, 256)
        self.upsample3 = UnetUpsample(384, 128)
        self.upsample4 = UnetUpsample(192, 64)
        
        self.out = nn.Conv2d(64, 1, kernel_size=1)

    def forward(self, x):
        b1_out = self.down_block1(x)        
        b2_out = self.down_block2(F.max_pool2d(b1_out, kernel_size=2))        
        b3_out = self.down_block3(F.max_pool2d(b2_out, kernel_size=2))        
        b4_out = self.down_block4(F.max_pool2d(b3_out, kernel_size=2))
        
        bottleneck_out = self.bottleneck(F.max_pool2d(b4_out, kernel_size=2))
        
        up1_out = self.upsample1(bottleneck_out, b4_out)
        up2_out = self.upsample2(up1_out, b3_out)   
        up3_out = self.upsample3(up2_out, b2_out)   
        up4_out = self.upsample4(up3_out, b1_out)   

        out = self.out(up4_out)
        
        return out
```

```python
unet = UNet()
```

```python
response = requests.get("https://thebogotapost.com/wp-content/uploads/2018/07/soccer-1457988_1920-1280x720.jpg")
test_image = Image.open(BytesIO(response.content))
```

```python
tfms = transforms.Compose([
    transforms.Resize(600),
    transforms.CenterCrop(572),
    transforms.ToTensor()
])

test_batch = tfms(test_image).unsqueeze(0)

result = unet(test_batch)
```

```python
assert result.shape == torch.Size([1, 1, 388, 388])
```

### GANs <a href="#gans" id="gans"></a>

Another exciting topic - Generative Adversarial Networks, or GANs.

GANs emerged in 2014 and has since been used in a variety of applications: from entertainment to generating artificial datasets for training neural nets (sounds a bit of a Skynet scenario...). Check out [this list](https://machinelearningmastery.com/impressive-applications-of-generative-adversarial-networks/) of amazing GAN applications

Let's understand better what GANs are and how they work under the hood:\
Read the original paper of GANs [https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)\
Alternatively watch the video of Ian Goodfellow (creator of the paper above) about GANs [https://www.youtube.com/watch?v=9JpdAg6uMXs](https://www.youtube.com/watch?v=9JpdAg6uMXs)

### Exercise <a href="#exercise" id="exercise"></a>

Do this great intro to GANs, with questions

* [https://developers.google.com/machine-learning/gan](https://developers.google.com/machine-learning/gan)

The tutorial is in Tensorflow, therefore it is optional. But since you don't need to write your code, I recommend following it through, as you will find a lot of similarities in code and should be able to understand what is going on.

### Autoencoders <a href="#autoencoders" id="autoencoders"></a>

The last topic of the day - Autoencoders. As you learn about autoencoders, you will find that they have a lot of similarities to U-Net and transformers as well as some similarities to GANs. It's a really powerful and simple technology, which has some exciting use-cases.

Let's dive straight into autoencoders and then try to build a simple model ourselves.

* [http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/](http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/)
* [https://www.jeremyjordan.me/autoencoders/](https://www.jeremyjordan.me/autoencoders/)
* [https://www.youtube.com/watch?v=7mRfwaGGAPg](https://www.youtube.com/watch?v=7mRfwaGGAPg)
* Check out [https://blog.keras.io/building-autoencoders-in-keras.html](https://blog.keras.io/building-autoencoders-in-keras.html) for building autoencoders in Keras

Let's summarize what we have learned about autoencoders. First of all - autoencoders are made of two parts: encoder and decoder. The encoder's job is to represent and input into a latent space, while the decoder's job is to convert into a necessary output. Sounds a lot like transformers, right? The problem is that autoencoders are not very good with sequences (you can [read more about this here](https://machinelearningmastery.com/lstm-autoencoders/), see "A Problem with Sequences").

You could train an autoencoder to take an image as input and return the same image as output. How is that useful? Well, autoencoder learns how to represent images into a latent space, so you could extract the encoder part and use it for other tasks as a pre-trained network (transfer learning). Except this time, compared to training a classification task from scratch (Imagenet), you don't need labeled images. You could scrape the internet for all the images you can find and train your autoencoder on it. Pretty powerful, right?! So autoencoders are unsupervised learners since the expected output of an autoencoder is the original input. Sometimes the input is randomly perturbed, depending on the application as we will see in the next exercise.

#### Exercise <a href="#exercise" id="exercise"></a>

Let's try building an autoencoder ourselves. The task for this exercise is to de-noise images. We will use a sign language dataset as the images are quite small and grayscale, so they are good for experimentation. In the data pipeline, we will add noise randomly to each image and use it as input. Then, we will ask our decoder to output the same image, but with noise removed, i.e. our label will be the original image and we will use [mean squared error](https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/loss-functions/mean-squared-error) loss as objective.

First let's start by building a data pipeline. Since the type of images does not make much difference here, you can either use the [proposed dataset from Kaggle](https://www.kaggle.com/datamunge/sign-language-mnist) or any other image dataset of your choice.

Tasks:

* You will need to add some random noise to your dataset.
* Your dataloader(databunch) will have to return 2 images: a noisy image and the original

```python
class HandSignDataset(Dataset):
    def __init__(self, image_data):
        super().__init__()
        
        self.images = image_data
        self.noisy_tfms = transforms.Compose([
            GausianNoise(0, 0.1),
        ])
        
        
    def __len__(self):
        return self.images.shape[0]
    
    def __getitem__(self, idx):
        
        image_clean = torch.from_numpy(self.images[idx]).unsqueeze(0)
        
        image_noisy = self.noisy_tfms(image_clean)
                
        return image_noisy, image_clean
        
```

```python
def hand_vectors_to_image(*images):
    imgs = []
    for im in images:
        imgs.append(im)
    
    return transforms.ToPILImage()(
        torch.cat(imgs, dim=2)
    )
```

```python
hand_vectors_to_image(
    dataset[0][0], dataset[0][1],
    dataset[1][0], dataset[1][1],
    dataset[2][0], dataset[2][1],
)
```

Now, let's create the model and train it.

Remember the architecture of autoencoders: encoder and decoder. Encoder reduces the size of an image and decoder restores it to the original dimensions. For this exercise, to save time you should not use convolutional layers, only fully connected ones, since restoring image to the original dimensions with convolutional layers is a bit more complicated.

Tasks:

* Build autoencoder model
* Train model
* Evaluate results

```python
hand_vectors_to_image(*sample_to_display)
```

How are your results? They are likely something like the above. As we see, the autoencoder has learned somewhat how to remove noise, however, the reconstruction ability of the network still needs to improve. You likely have found some easy variants of this exercise on the internet, like removing noise from MNIST (black and white) images. In such cases, the decoder needs to get the values somewhere above 0.5 for white pixels and below 0.5 for black. This encoder, apart from removing noise, needs to be much more precise on each pixel value to get a meaningful image. Thus additional work needs to be done on enlarging the architecture with longer training regimes.

***

### Summary <a href="#summary" id="summary"></a>

In this lesson, you have learned a crash course on 4 different advanced deep learning topics. As you noticed, even though some concepts are advanced, the basic building blocks of each technology are very similar. Choosing correct loss, defining metrics, building data pipelines, evaluating models, etc. - are all foundational parts of any ML task. With this lesson, we will finish learning about new technologies and for the remainder of the course, focus on practical issues for deep learning practitioners, how to work in an agile way with deep learning and be a successful machine learning engineer in a company.

### Further research <a href="#further-research" id="further-research"></a>

* RetinaNet. RetinaNet is another object detection algorithm which at the time of release has beaten SOTA in this task. Investigate how it works. You can start here:
  * [https://developers.arcgis.com/python/guide/how-retinanet-works/](https://developers.arcgis.com/python/guide/how-retinanet-works/)
  * [https://arxiv.org/abs/1708.02002](https://arxiv.org/abs/1708.02002)
