from mnist import MNIST
from skimage.feature import hog
from sklearn.decomposition import PCA
import numpy as np

class MNISTFeatures:
    def load_mnist_data(self):
        mndata = MNIST('minist/mnist_data')
        X_train, y_train = mndata.load_training()
        X_test, y_test = mndata.load_testing()
        return X_train[:6000], y_train[:6000], X_test[:2000], y_test[:2000]
    
    def pixel_intensity_feature(self, image):
        return [x/255.0 for x in image]
    
    def hog_feature(self, image):
        image = np.array(image).reshape(28, 28)
        feature_vector, _ = hog(image, orientations=8, pixels_per_cell=(4, 4), cells_per_block=(1, 1), visualize=True)
        return feature_vector
    
    def pca_feature(self, images, n_components=100):
        pca = PCA(n_components)
        pca.fit(images)
        return pca 
    
    
    
    def extract_features(self, image, pca):
       
        pca_feat = pca.transform([image]).flatten()
        
        return pca_feat