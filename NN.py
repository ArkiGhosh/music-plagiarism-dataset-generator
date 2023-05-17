import os
import librosa
import numpy as np
from pydub import AudioSegment
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout

original_songs = []
plagiarized_songs = []

originalDir = "./original"
plagiarizedDir = "./plagiarized"

def extractFeatures(filePath):
    y, sr = librosa.load(filePath)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    features = np.mean(mfcc.T, axis=0)  
    return features

for filename in os.listdir(originalDir):
    filePath = os.path.join(originalDir, filename)
    features = extractFeatures(filePath)
    original_songs.append(features)

for filename in os.listdir(plagiarizedDir):
    filePath = os.path.join(plagiarizedDir, filename)
    features = extractFeatures(filePath)
    plagiarized_songs.append(features)

labels = np.zeros(len(original_songs) + len(plagiarized_songs))
labels[len(original_songs):] = 1

songs = original_songs + plagiarized_songs
xTrain, xTest, yTrain, yTest = train_test_split(songs, labels, test_size=0.2, random_state=42)


xTrain = np.array(xTrain)
xTest = np.array(xTest)
yTrain = np.array(yTrain)
yTest = np.array(yTest)

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=xTrain.shape[1]))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(xTrain, yTrain, epochs=10, batch_size=32)

loss, accuracy = model.evaluate(xTest, yTest)
print('Test Loss:', loss)
print('Test Accuracy:', accuracy)
