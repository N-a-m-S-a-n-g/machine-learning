
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn import svm 

fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish.head()

fish_input = fish[['Weight', 'Length','Diagonal','Height','Width']].to_numpy()
fish_target = fish['Species'].to_numpy()
#훈련셋, 테스트셋 분류
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target)
#데이터셋 스케일링
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
#SVM
s = svm.SVC(C = 20, gamma = 0.001)
s.fit(train_scaled,train_target)

print("train set 정답률: %.1f"%(100*s.score(train_scaled, train_target)),"%") 
print("test set 정답률: %.1f"%(100*s.score(test_scaled, test_target)),"%")

