import numpy as np

class NearestNeighborClassifier:
    """
    NN classifier using Euclidean distance.
    """
    
    def __init__(self):
        self.training_data = []
    
    def train(self, instances, feature_subset):
        """
        we train the classifier by storing training instances.
        
        arguments:
            instances: list of tuples (class_label, feature_vector)
            feature_subset: list of feature indices to use 
        """
        self.training_data = []
        self.feature_subset = [f - 1 for f in feature_subset]  # Convert to 0-indexed
        
        for class_label, features in instances:
            # only keep selected features
            selected_features = features[self.feature_subset] if self.feature_subset else np.array([])
            self.training_data.append((class_label, selected_features))
    
    def test(self, test_instance):

        test_class, test_features = test_instance
        
        # only use selected features
        test_selected = test_features[self.feature_subset] if self.feature_subset else np.array([])
        
        min_distance = float('inf')
        nearest_class = None
        
        for train_class, train_features in self.training_data:
            # euclidean distance
            distance = np.sqrt(np.sum((test_selected - train_features) ** 2))
            
            if distance < min_distance:
                min_distance = distance
                nearest_class = train_class
        
        return nearest_class