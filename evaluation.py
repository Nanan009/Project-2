from validator import leave_one_out_validation
from collections import Counter
# global variable to store dataset
dataset = None

def set_dataset(data):
    global dataset
    dataset = data

def evaluate(feature_subset):
    if dataset is None:
        return 0.0
    
    if not feature_subset:
        # no features selected - return random baseline
        # return 50.0
        labels = [instance[0] for instance in dataset]
        counts = Counter(labels)

        if not counts:
            return 0.0
        
        majority_count = counts.most_common(1)[0][1]

        return (majority_count / len(dataset)) * 100
    
    accuracy = leave_one_out_validation(dataset, feature_subset)
    return accuracy * 100  # convert to percentage