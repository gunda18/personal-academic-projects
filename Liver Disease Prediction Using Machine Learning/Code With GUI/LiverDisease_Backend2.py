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
    accuracy2=float(1.1)
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