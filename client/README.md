# Chest X-Ray & CT-Scan Project

* To Show Code And More details about Chest X-Ray  <a href='https://colab.research.google.com/drive/1eYQQsR0HMrLFk15JR8Z1cDuRuagxb8XA?usp=sharing'>Go to Colab</a>
* To Show Code And More details about CT-Scan images  <a href='https://colab.research.google.com/drive/1f3YYVBiSMF40Ddm0sMo2Na2HqFLA5r2x?usp=sharing'>Go to Colab</a>

* To Download Chest X-Ray Dataset <a href='https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia'>Go to Kaggle</a>
* To Download CT-Scan images Dataset <a href='https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images'>Go to Kaggle</a>

 **About Chest X-Ray  dataset**
---


*   The dataset provide 6000 images to classify.

---



# > **Unzipping files**
```python
import zipfile

# returns 'Select files'
zip_files = ['test1', 'train']

for zip_file in zip_files:
    with zipfile.ZipFile("/x-ray.zip".format(zip_file),"r") as z:
        z.extractall(".")
        print("{} unzipped".format(zip_file))

```

# > **importing library**
```python
import numpy as np
import pandas as pd
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras import regularizers
from keras.layers.core import Dropout

```

 > **ScreenShot**
> 
 <img src='/chrome-capture-2022-11-25.gif' alt="Sample"   />
 <img src='https://www.mdpi.com/diagnostics/diagnostics-10-00417/article_deploy/html/images/diagnostics-10-00417-g001.png'   />
 <img src='https://www.mdpi.com/diagnostics/diagnostics-10-00417/article_deploy/html/images/diagnostics-10-00417-g001.png'   />



 > **Build Model**

 <img src='https://www.mdpi.com/diagnostics/diagnostics-10-00417/article_deploy/html/images/diagnostics-10-00417-g001.png'   />
 
> **Front-End**
* React Js
> **Back-End**
* Flask Framwork

>Library
* pandas
* numpy
* os
* keras
* tensorflow
* matplotlib
* pandas