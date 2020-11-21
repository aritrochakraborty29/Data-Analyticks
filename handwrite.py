import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
digits = datasets.load_digits()


plt.imshow(digits.images[1791],cmap=plt.cm.gray_r, interpolation='nearest')


svc = svm.SVC(gamma=0.001, C=100.)
svc.fit(digits.data[1:1791], digits.target[1:1791])
svc.predict(digits.data[1791:1791])