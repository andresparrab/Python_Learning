import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import seaborn as sns

stress_df = pd.read_csv(r'stress.csv')
features = stress_df.iloc[:,[0,1]].values
label= stress_df.iloc[:,2].values
#print(stress_df.info())



# 3. Training the model
features_train,features_test,label_train,label_test = train_test_split(features,label,test_size=0.2)

knn = KNeighborsClassifier()
knn.fit(features_train, label_train)

# 4.Testing model and score
stress_predict_knn = knn.predict(features_test)

print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(features_train, label_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(features_test, label_test)))
print(stress_predict_knn)
print(label_test)

label_test_df =pd.array(label_test)
features_test_db = pd.DataFrame(features_test)
print('This is the stress count:\n')
print(label_test_df.value_counts())
cf_matrix = confusion_matrix(label_test, stress_predict_knn)
flat= cf_matrix.flatten()

print('Total not stressed ##############', label_test_df.value_counts().loc[0])
print('Total not stressed guessed correctly //////////////',flat[0])
percent_true = (flat[0]/label_test_df.value_counts().loc[0])
print('percent correct guesses',percent_true)


stress_df.plot.scatter(x='X',
                      y='Y',
                      c='Stress',
                      colormap='viridis')
plt.show()
group_names = ['\n\nTrue Neg','False Pos','False Neg','True Pos']
group_counts = ['{0:0.0f}'.format(value) for value in cf_matrix.flatten()]
group_percentage = ['{0:.2%}'.format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]

labels = [f'{v1}\n{v2}\n{v3}' for v1, v2, v3 in zip(group_names,group_counts,group_percentage)]
labels = np.asanyarray(labels).reshape(2,2)
sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=labels,fmt='',cmap='viridis')
plt.show()

from sklearn.svm import SVC
svm = SVC()
svm.fit(features_train, label_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(features_train, label_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(features_test, label_test)))

stress_predict_svm = svm.predict(features_test)
print(confusion_matrix(label_test, stress_predict_svm))

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, label_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(features_train, label_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(features_test, label_test)))
stress_predict_dt = clf.predict(features_test)
print(confusion_matrix(label_test, stress_predict_dt))




from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(features_train, label_train)
print('Accuracy of GNB classifier on training set: {:.2f}'
     .format(clf.score(features_train, label_train)))
print('Accuracy of GNB classifier on test set: {:.2f}'
     .format(clf.score(features_test, label_test)))
stress_predict_gnb = gnb.predict(features_test)
print(confusion_matrix(label_test, stress_predict_gnb))

