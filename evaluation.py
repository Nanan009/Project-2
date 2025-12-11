from validator import leave_one_out_validation

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
        return 50.0
    
    accuracy = leave_one_out_validation(dataset, feature_subset)
    return accuracy * 100  # convert to percentage