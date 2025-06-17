from src import config
from src import data_loader
from sklearn.decomposition import PCA 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import MinMaxScaler , StandardScaler 
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans 
from sklearn.cluster import AgglomerativeClustering
import numpy as np 
import pandas as pd 

def feature_engineering(df : pd.DataFrame) -> pd.DataFrame : 
    df1 = pd.DataFrame()
    df1['Trade'] = (df['imports'] / df['imports'].mean()) + (df['exports'] / df['exports'].mean())
    df1['Health'] = (df['child_mort'] / df['child_mort'].mean()) + (df['health'] / df['health'].mean()) + (df['life_expec'] / df['life_expec'].mean()) + (df['total_fer'] / df['total_fer'].mean())
    df1["Finance"] = (df['income'] /df['income'].mean()) + (df['inflation'] / df['inflation'].mean()) + (df['gdpp'] / df['gdpp'].mean())
    print()
    print("Đã tạo ra các đặc trưng mới")
    return df1 

def apply_pca(df : pd.DataFrame , n_components = None): 
    result_pca = {}
    pca = PCA()
    if 'country' in df.columns:
        df = df.drop('country', axis=1)
    pca_df2 = pd.DataFrame(pca.fit_transform(df))
    result_pca["df"] = pca_df2 
    result_pca["explained_variance_radio"] = pca.explained_variance_ratio_
    
    return result_pca

def use_preprocesing(df : pd.DataFrame ,use_pca: bool = False , n_components = None):
    sds = StandardScaler()
    mms = MinMaxScaler()
    if use_pca : 
        df2 = df.copy(deep = True)
        df2['health'] = sds.fit_transform(df2[['health']])
        df2 = df2.drop('country',axis = 1)
        for i in df2.columns : 
            if i != "health" :
                df2[i] = mms.fit_transform(df2[[i]])
        return apply_pca(df2)

    else : 
        df1 = feature_engineering(df)
        df1_scaled = pd.DataFrame(mms.fit_transform(df1), columns=df1.columns)
        return df1_scaled

# def get_compose(df: pd.DataFrame, std_cols: list = None, mms_cols: list = None,
#                 n_components: int = 3, n_clusters: int = 3,
#                 use_pca: bool = False, use_kmean: bool = False, use_agglomerative: bool = False) -> Pipeline:
    
#     if use_kmean and use_agglomerative:
#         raise ValueError("Chỉ được chọn một trong hai: KMeans hoặc Agglomerative Clustering")

#     steps = []

#     if use_pca:
#         if not std_cols or not mms_cols:
#             raise ValueError("std_cols và mms_cols phải được cung cấp nếu dùng PCA")
#         preprocessor = ColumnTransformer(transformers=[
#             ('std', StandardScaler(), std_cols),
#             ('mms', MinMaxScaler(), mms_cols),
#         ])
#         steps.append(('preprocess', preprocessor))
#         steps.append(('pca', PCA(n_components=n_components)))
#     else:
#         # Lúc này df đã là df_fe nên không cần feature_engineering()
#         preprocessor = ColumnTransformer(transformers=[
#             ('mms', MinMaxScaler(), df.columns.to_list())
#         ])
#         steps.append(('preprocess', preprocessor))

#     if use_kmean:
#         steps.append(('kmean', KMeans(n_clusters=n_clusters, init="k-means++", random_state=config.RANDOM_STATE)))
#     elif use_agglomerative:
#         steps.append(('agglo', AgglomerativeClustering(n_clusters=n_clusters, linkage="ward", metric="euclidean")))

#     return Pipeline(steps=steps)

        
# if __name__ == "__main__":
#     # df = data_loader.load_data()

#     # # Nếu không dùng PCA => feature_engineering
#     # df_fe = feature_engineering(df)

#     # pipe = get_compose(
#     #     df=df_fe,
#     #     use_pca=False,
#     #     use_kmean=True
#     # )

#     # pipe.fit(df_fe)  # fit đúng với dữ liệu đầu vào của pipeline
#     # labels = pipe.named_steps["kmean"].labels_
#     # print(labels)