from os import listdir
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import keras
import keras.backend as K
from keras.models import Sequential
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.regularizers import l2

from PIL import Image
import scipy.misc

from keras import regularizers
from keras.layers import Input, Dense
from keras.models import Model



###############
folders = listdir("../")
folders

cancer_filename = "../CancerMerged.txt"
normal_filename = "../NormalMerged.txt"

cancer_data = pd.read_table(cancer_filename, header=None)
cancer_data_t = cancer_data.T
cancer_data_tmp = cancer_data_t
cancer_data_tmp.columns = cancer_data_tmp.iloc[0]
cData = cancer_data_tmp.drop(0)

normal_data = pd.read_table(normal_filename, header=None)
normal_data_t = normal_data.T
normal_data_tmp = normal_data_t
normal_data_tmp.columns = normal_data_tmp.iloc[0]
nData = normal_data_tmp.drop(0)

allData = pd.concat([cData, nData], ignore_index=True)
dat = allData.values
dat = dat.astype('float32')
dat[np.isnan(dat)] = 0

from sklearn.cross_validation import train_test_split
x_train, x_test = train_test_split(dat,
                                     test_size=0.2,
                                     random_state=0)

################

input_img = Input(shape=(60488,))
encoded = Dense(1000, activation='relu')(input_img)
encoded = Dense(500, activation='relu')(encoded)
encoded = Dense(250, activation='relu')(encoded)

decoded = Dense(250, activation='relu')(encoded)
decoded = Dense(500, activation='relu')(encoded)
decoded = Dense(1000, activation='relu')(decoded)
decoded = Dense(60488, activation='sigmoid')(decoded)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy', metrics=['accuracy', 'mae'])

result3 = autoencoder.fit(x_train, x_train,
                epochs=1000,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))