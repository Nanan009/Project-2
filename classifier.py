import math

class NearestNeighborClassifier:
    # initialize the classifier, set training data to empty and set feature subset to None
    def __init__(self):
        self.training_data = []
        self.feature_subset = None

    # create the training data based on the provided feature subset
    def train(self, instances, feature_subset):
        self.feature_subset = [i - 1 for i in feature_subset]
        self.training_data = []

        # build training data with only the selected features
        for class_label, features in instances:
            # select only the features in the subset
            chosen_features = [features[i] for i in self.feature_subset] if self.feature_subset else []
            self.training_data.append((class_label, chosen_features))

    # test every instance against the training data and return the predicted class
    def test(self, instance):
        _, features = instance

        # select only the features in the subset
        test_features = [features[i] for i in self.feature_subset] if self.feature_subset else []

        nearest_class = None
        min_distance = float('inf')

        # compute Euclidean distance to each training instance
        for train_class, train_features in self.training_data:
            squared_sum = 0
            for i in range(len(test_features)):
                a = test_features[i]
                b = train_features[i]
                squared_sum += (a - b) ** 2

            distance = math.sqrt(squared_sum)

            if distance < min_distance:
                min_distance = distance
                nearest_class = train_class

        return nearest_class
