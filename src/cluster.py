from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import OPTICS
import numpy as np



class kmean_cluster():
    def __init__(self,dataset,k=10, pcaValue = 60):
       self.k=k
       self.dataset=dataset
       self.pcaValue = pcaValue

    def pca(self,dataset):
        # now we call the sklearn library to train and fit.
        # pca = PCA(0.95) # we want 95% variance to be explained
        pca = PCA(self.pcaValue)
        self.dataset=pca.fit_transform(dataset)

    def kmean(self):
        kmeans = KMeans(n_clusters=self.k, random_state=0).fit(self.dataset)
        return kmeans
    
    def classification(self,model):
        # return model.predict(self.dataset)
        return model.labels_
    
    def clusterCenter(self,model):
        # return model.predict(self.dataset)
        return model.cluster_centers_
    
    def clusterPredict(self,model,predictList):
        return model.predict(predictList)
        # return model.cluster_centers_



class Dbscan_cluster():
    def __init__(self,dataset,epsilon=1):
       self.epsilon=epsilon
       self.dataset=dataset

    def pca(self,dataset):
        # now we call the sklearn library to train and fit.
        pca = PCA(0.95) # we want 95% variance to be explained
        self.dataset=pca.fit_transform(dataset)

    def Dbscan(self):
        Dbscan_model = DBSCAN(eps=self.epsilon, min_samples=2).fit(self.dataset)
        return Dbscan_model
    
    def classification(self,model):
        return model.labels_

class OPTICS_cluster():
    def __init__(self,dataset,min_samples=2):
       self.min_samples=min_samples
       self.dataset=dataset

    def pca(self,dataset):
        # now we call the sklearn library to train and fit.
        pca = PCA(0.95) # we want 95% variance to be explained
        self.dataset=pca.fit_transform(dataset)

    def OPTICS(self):
        OPTICS_model = OPTICS(min_samples=self.min_samples).fit(self.dataset)
        return OPTICS_model
    
    def classification(self,model):
        return model.labels_