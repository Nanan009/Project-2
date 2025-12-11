from classifier import NearestNeighborClassifier

def leave_one_out_validation(instances, feature_subset):
    """
    Leave-one-out cross validation.
    For each instance: train on all others, test on it.
    """
    if not instances:
        return 0.0
    
    correct = 0
    total = len(instances)
    
    for i in range(total):
        # leave out one instance for testing
        training_set = instances[:i] + instances[i+1:]
        test_instance = instances[i]
        
        # train on the rest
        classifier = NearestNeighborClassifier()
        classifier.train(training_set, feature_subset)
        
        # test on the left-out instance
        predicted_class = classifier.test(test_instance)
        actual_class = test_instance[0]
        
        if predicted_class == actual_class:
            correct += 1
    
    return correct / total