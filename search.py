from evaluation import evaluate

def forward_selection(all_features):
    
    """
    Performs greedy forward selection.
    
    Parameters:
        all_features (list): list of all feature identifiers (e.g., [1, 2, 3, ...])
    
    Returns:
        list: the selected features in the order they were added
    """

    selected = []
    current_best_accuracy = 0

    print("Beginning search.\n")

    while len(selected) < len(all_features):
        best_feature = None
        best_score = -1

        for f in all_features:
            if f not in selected:
                temp = selected + [f]
                score = evaluate(temp)
                print(f"Using feature(s) {temp} accuracy is {score:.1f}%")

                if score > best_score:
                    best_score = score
                    best_feature = f

        selected.append(best_feature)
        print(f"\nFeature set {selected} was best, accuracy is {best_score:.1f}%\n")

    # print("Forward Selection finished.")

    final_acc = evaluate(selected)
    if final_acc < best_score:  # best_score is the highest seen
        print("(Warning, Accuracy has decreased!)")
    print(f"Finished search!! The best feature subset is {selected}, which has an accuracy of {final_acc:.1f}%")
    return selected


def backward_elimination(all_features):
    """
    Performs greedy backward elimination.
    
    Parameters:
        all_features (list): list of all feature identifiers (e.g., [1, 2, 3, ...])
    
    Returns:
        list: the remaining features after elimination
    """
    selected = all_features.copy()
    best_ever = evaluate(selected)
    print("Beginning search.\n")

    while len(selected) > 1:
        best_feature_to_remove = None
        best_score = -1

        for f in selected:
            temp = selected.copy()
            temp.remove(f)
            score = evaluate(temp)
            print(f"Using feature(s) {temp} accuracy is {score:.1f}%")

            if score > best_score:
                best_score = score
                best_feature_to_remove = f

        selected.remove(best_feature_to_remove)
        print(f"\nFeature set {selected} was best, accuracy is {best_score:.1f}%\n")

    final_acc = evaluate(selected)
    if final_acc < best_score:  
        print("(Warning, Accuracy has decreased!)")
    print(f"Finished search!! The best feature subset is {selected}, which has an accuracy of {final_acc:.1f}%")
    return selected
