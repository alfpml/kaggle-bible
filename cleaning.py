#importing libraries
import pandas as pd
from sklearn import datasets, svm, metrics
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

avila =  pd.read_csv('./input/training_dataset.csv')
avila = pd.DataFrame(avila)
print(avila.head())
print(avila.dtypes)
print(avila.describe)
X = avila[["F1","F2","F3","F4","F8","F10"]]