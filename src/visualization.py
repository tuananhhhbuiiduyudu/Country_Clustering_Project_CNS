import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from src import data_preprocessing
from src import data_loader
from src import config
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score
def select_components_pca(df : pd.DataFrame) : 
    result = data_preprocessing.use_preprocesing(df, use_pca=True)
    plt.step(list(range(1,10)) , np.cumsum(result['explained_variance_radio']))
    plt.plot(np.cumsum(result['explained_variance_radio']))
    plt.xlabel('Số lượng chiều')
    plt.ylabel("Tỷ lệ phương sai theo số lượng chiều")
    plt.tight_layout()
    plt.show()

def select_k_for_kmeans(x : np.array):
    kmax = 10 
    sse = [0] * kmax 
    sil = []
    fig , ax =plt.subplots(1,2 , figsize = (20,5))
    plt.subplot(1,2,1)
    for k in range(1 , kmax+1):
        kmeans = KMeans(n_clusters= k , init= "k-means++" , random_state= config.RANDOM_STATE)
        kmeans.fit(x)
        sse[k-1] = kmeans.inertia_
    sns.lineplot(x = range(1 , kmax+1) , y = sse[:])
    plt.title("Elbow Method")
    plt.xlabel("Số lượng k")
    plt.ylabel("Tổng bình phương khoảng cách")
    plt.grid()
    plt.subplot(1,2,2)
    for k in range(2 , kmax+1):
        kmeans = KMeans(n_clusters=k , init= "k-means++" , random_state=config.RANDOM_STATE)
        kmeans.fit(x)
        labels = kmeans.labels_
        sil.append(silhouette_score(x , labels , metric="euclidean")) 
    sns.lineplot(x = range(2 , kmax+1) , y = sil)
    plt.title("Silhouette Score Method")
    plt.xlabel("k : Số lượng K")
    plt.ylabel("Silhouette Score")
    plt.grid()
    plt.show()

def plot_boxplot_by_class(df: pd.DataFrame ):
    fig , ax = plt.subplots(nrows=1 , ncols= 2 , figsize = (15,5))
    plt.subplot(1,2,1)
    sns.boxplot(x = "Class" , y = 'child_mort' , data = df , color = 'b')
    plt.title("child_mort vs Class")
    
    plt.subplot(1,2,2)
    sns.boxplot(x = "Class" , y = "income" , data = df , color = 'g')
    plt.title("income vs Class")
    plt.show()  
if __name__ == '__main__':
    select_components_pca(df = data_loader.load_data())
    x = data_preprocessing.use_preprocesing(df = data_loader.load_data() , use_pca= True)
    select_k_for_kmeans(x["df_values"])
    
    