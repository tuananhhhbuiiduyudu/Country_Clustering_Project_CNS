from src import config
from src import data_loader
from sklearn.decomposition import PCA 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import MinMaxScaler , StandardScaler , FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans 
from sklearn.cluster import AgglomerativeClustering
import numpy as np 
import pandas as pd 
from src.data_preprocessing import feature_engineering

def get_compose(df: pd.DataFrame = None, std_cols: list = None, mms_cols: list = None,
                n_components: int = 3, n_clusters: int = 3,
                use_pca: bool = False, use_kmean: bool = False, use_agglomerative: bool = False) -> Pipeline:
    
    if use_kmean and use_agglomerative:
        raise ValueError("Chỉ được chọn một trong hai: KMeans hoặc Agglomerative Clustering")

    steps = []

    if use_pca:
        if not std_cols or not mms_cols:
            raise ValueError("std_cols và mms_cols phải được cung cấp nếu dùng PCA")
        preprocessor = ColumnTransformer(transformers=[
            ('std', StandardScaler(), std_cols),
            ('mms', MinMaxScaler(), mms_cols),
        ])
        steps.append(('preprocess', preprocessor))
        steps.append(('pca', PCA(n_components=n_components)))
    else:
        if df is None:
            raise ValueError("Vì bạn đã đặt use_pca=False, hãy truyền vào DataFrame gốc")

        required_cols = ['country', 'child_mort', 'exports', 'health', 'imports', 'income', 'inflation', 'life_expec', 'total_fer', 'gdpp']
        if not set(required_cols).issubset(df.columns):
            raise ValueError(f"Thiếu cột cần thiết cho feature_engineering: {set(required_cols) - set(df.columns)}")
        # Lúc này df đã là df_fe nên không cần feature_engineering()
        feature_step = ('feature_engineering', FunctionTransformer(feature_engineering))
        preprocessor = ColumnTransformer(transformers=[
            ('mms', MinMaxScaler(), ['Trade', 'Finance', 'Health'])
        ])
        steps.append(feature_step)
        steps.append(('preprocess', preprocessor))
    if use_kmean:
        steps.append(('kmean', KMeans(n_clusters=n_clusters, init="k-means++", random_state=config.RANDOM_STATE)))
    elif use_agglomerative:
        steps.append(('agglo', AgglomerativeClustering(n_clusters=n_clusters, linkage="ward", metric="euclidean")))

    return Pipeline(steps=steps)
