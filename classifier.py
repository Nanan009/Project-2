import math

class NearestNeighborClassifier:

    def __init__(self):
        self.training_data = []
        self.feature_subset = None

    def train(self, instances, feature_subset):
        self.feature_subset = [i - 1 for i in feature_subset]
        self.training_data = []

        for class_label, features in instances:
            chosen_features = [features[i] for i in self.feature_subset] if self.feature_subset else []
            self.training_data.append((class_label, chosen_features))

    def test(self, instance):
        _, features = instance

        test_features = [features[i] for i in self.feature_subset] if self.feature_subset else []

        nearest_class = None
        min_distance = float('inf')

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
