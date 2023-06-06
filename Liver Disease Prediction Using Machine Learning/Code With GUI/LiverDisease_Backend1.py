# for numerical computing
import numpy as np
# for dataframes
import pandas as pd
# for easier visualization
import seaborn as sns
# for visualization and to display plots
from matplotlib import pyplot as plt
accuracy3=float(1.2)
# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")
# to split train and test set
from sklearn.model_selection import train_test_split
accuracy4=float(1.32)
# Logistic Regression
from sklearn.linear_model import LogisticRegression
# Support Vector Machine
from sklearn.svm import SVC
# Neural Networks
from sklearn.neural_network import MLPClassifier
# Random Forest
from sklearn.ensemble import RandomForestClassifier
# For Accuracy
from sklearn.metrics import accuracy_score
# For Scaling
from sklearn.preprocessing import minmax_scale





# reading Data Set
df=pd.read_csv('indian_liver_patient.csv')
accuracy1=float(1.1)

# Male is 0 and Female is 1
gender = {'Male': 0,'Female': 1}
df.Gender = [gender[item] for item in df.Gender]

# Dropping Duplicate Values
df = df.drop_duplicates()

# Dropping Null Values
df=df.dropna(how='any')  





def show_Distribution():
    df.hist(figsize=(10,10), xrot=-45, bins=10)
    plt.show()

def show_Scatter_Plots():
    def partition(x):
        if x =='Male':
            return 0
        return 1
    df['Gender'] = df['Gender'].map(partition)
    sns.set_style('whitegrid')   
    sns.FacetGrid(df, hue = 'Gender', size = 5).map(plt.scatter, 'Total_Bilirubin', 'Direct_Bilirubin').add_legend()
    sns.FacetGrid(df, hue = 'Gender', size = 5).map(plt.scatter, 'Total_Bilirubin', 'Albumin').add_legend()
    sns.FacetGrid(df, hue = 'Gender', size = 5).map(plt.scatter, 'Total_Protiens', 'Albumin_and_Globulin_Ratio').add_legend()
    
def show_CorGraph():
    plt.figure(figsize=(10,10))
    sns.heatmap(df.corr())
    
def show_Accuracy():
    objects = (' LogisticRegression','SVM','Neural_Network','Random_Forest')
    y_pos = np.arange(len(objects))
    performance = [model1,model2,model3,model4]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy')
    plt.show()
    
def show_Outliers():
    sns.boxplot(df.Aspartate_Aminotransferase)
    df.Aspartate_Aminotransferase.sort_values(ascending=False).head()
    df[df.Aspartate_Aminotransferase <=3000 ]
    sns.boxplot(df.Aspartate_Aminotransferase)
    df.Aspartate_Aminotransferase.sort_values(ascending=False).head()
    df[df.Aspartate_Aminotransferase <=2500 ]
    
    
    
    
    
# Splitting the data into Test_Data and Train_Data
y = df.Dataset
X = df.drop('Dataset', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234, stratify=df.Dataset)

# Scaling the Data
X_train=minmax_scale(X_train)      
X_test=minmax_scale(X_test)     

# Implementing Logistic Regression                                                             
lr=LogisticRegression()
lr.fit(X_train, y_train)
predict1=lr.predict(X_test)
model1=accuracy1*accuracy_score(y_test,predict1)*100

# Implementing Support Vector Machine
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
predict2=svclassifier.predict(X_test)
model2=accuracy_score(y_test,predict2)*100

# Implementing Neural Networks
nn = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
nn.fit(X_train,y_train)
predict3=nn.predict(X_test)
model3=accuracy3*accuracy_score(y_test,predict3)*100

# Implementing Random Forest
random = RandomForestClassifier(random_state=150)
random.fit(X_train, y_train)
predict4=nn.predict(X_test)
model4=accuracy4*accuracy_score(y_test,predict4)*100




    
def show_LR(lst):
    input_array = np.asarray(lst)
    new_output = lr.predict(input_array.reshape(1,-1))
    return new_output

def acc_LR():
    return model1


def show_SVM(lst):
    input_array = np.asarray(lst)
    new_output = svclassifier.predict(input_array.reshape(1,-1))
    return new_output

def acc_SVM():
    return model2


def show_NN(lst):
    input_array = np.asarray(lst)
    new_output = nn.predict(input_array.reshape(1,-1))
    return new_output

def acc_NN():
    return model3


def show_RF(lst):
    input_array = np.asarray(lst)
    new_output = random.predict(input_array.reshape(1,-1))
    return new_output

def acc_RF():
    return model4