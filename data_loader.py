import numpy as np

def load_dataset(filename):

    instances = []

    with open(filename, 'r') as f:
        for line in f:
            values = list(map(float, line.strip().split()))
            class_label = int(values[0])
            features = np.array(values[1:])
            instances.append((class_label, features))
    
    num_features = len(instances[0][1]) if instances else 0
    
    # normalize features
    instances = normalize_features(instances)
    
    return instances, num_features


def normalize_features(instances):
    """
    normalize features using z-score normalization.
    """
    if not instances:
        return instances
    
    num_features = len(instances[0][1])
    
    # extract all feature vectors
    all_features = np.array([inst[1] for inst in instances])
    
    # calculate mean and std for each feature
    means = np.mean(all_features, axis=0)
    stds = np.std(all_features, axis=0)
    
    # avoid division by zero
    stds[stds == 0] = 1.0
    
    # normalize
    normalized_instances = []
    for class_label, features in instances:
        normalized = (features - means) / stds
        normalized_instances.append((class_label, normalized))
    
    return normalized_instances