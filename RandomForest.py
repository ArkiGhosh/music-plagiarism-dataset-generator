import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def extractFeatures(filePath):
    y, sr = librosa.load(filePath)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    features = np.mean(mfcc.T, axis=0)  
    return features

def loadDataset(originalDir, plagiarizedDir):
    X = []
    y = []

    for filename in os.listdir(originalDir):
        if filename.endswith(".mp3"):
            filePath = os.path.join(originalDir, filename)
            features = extractFeatures(filePath)
            X.append(features)
            y.append(0)  

    for filename in os.listdir(plagiarizedDir):
        if filename.endswith(".mp3"):
            filePath = os.path.join(plagiarizedDir, filename)
            features = extractFeatures(filePath)
            X.append(features)
            y.append(1)  

    return X, y

originalDir = "./original"
plagiarizedDir = "./plagiarized"

X, y = loadDataset(originalDir, plagiarizedDir)

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(xTrain, yTrain)

yPred = clf.predict(xTest)

accuracy = accuracy_score(yTest, yPred)
print("Accuracy:", accuracy)
