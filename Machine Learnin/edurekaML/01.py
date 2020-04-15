import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

url = "iris.data"
names = ['sepal-length','sepal-with','petal-length','petal-with','class']
dataset = pandas.read_csv(url,names=names)

# Get the basic idea of the dataset
print(dataset.shape)
print(dataset.head(60))
print(dataset.describe())
print(dataset.groupby('class').size())

# Visualization of the data
    # 1.fisrt we create the univariate plot. to better understand each attribute
    #2. then we create multivariate plot to understand the relationships between the attributes

# 1. univariate plot
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex= False,sharey= False)
plt.show()
dataset.hist()
plt.show()

# 2. create multivariate plot
cmap = cm.get_cmap('hot')
scatter_matrix((dataset),cmap = cmap)
plt.show()
print(cm.cmap_d.keys())

# Create a model of the data and estimate the accuracy on the basisof unseen data
# 1. Create a validation dataset
array = dataset.values
print(array)
X = array[:,0:4]
print(X)
Y = array[:,4]
print(Y)
validation_size =0.2
# the seed keeps the same randomness in the train and test set
seed = 6
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,test_size=validation_size, random_state=seed)

seed = 6
scoring = 'accuracy'

# 2. Building the model
# Witch modelwill give the best accuracy

models =[]
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART',DecisionTreeClassifier))
models.append(('NB', GaussianNB()))
models.append(('SVM',SVC()))

# Evaluate each model in turn
results= []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10)
    cv_results = model_selection.cross_val_score(model,X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg ='%s: %f (%f)' % (name, cv_results.mean(), cv_results.std())
    print(msg)

# It seems that LDA algorithm had the most accuracy
# Now we want an accuracy Idea on our validation set, the testing set
# this will give us independent final check on the accuracy of the best model

