'''
some functions used in notebook
'''

from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, ElasticNetCV,LogisticRegression
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import mean_squared_error,accuracy_score,precision_score,classification_report,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.impute import SimpleImputer
import sklearn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def metric_count(y,y_hat):
    accuracy_score(y,y_hat)
    fpr, tpr, thresh = sklearn.metrics.roc_curve(y, y_hat)
    precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y, y_hat)
    f0=plt.figure()
    f0.add_subplot(2,2,1)
    plt.fill_between(fpr, tpr, 0, color='lightgrey')
    plt.plot(np.linspace(0, 1), np.linspace(0, 1), color='red', linestyle=':')
    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC')
    #plt.show()
    f0.add_subplot(2,2,2)
    #precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y, y_hat)
    plt.plot(recall, precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('P-R')
    #plt.show()
    f0.tight_layout()
    return print(classification_report(y,y_hat))