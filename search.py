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
    print("Beginning Forward Selection...")

    while len(selected) < len(all_features):
        best_feature = None
        best_score = -1

        for f in all_features:
            if f not in selected:
                temp = selected + [f]
                score = evaluate(temp)
                print(f"   Evaluating {temp} → score = {score:.4f}")

                if score > best_score:
                    best_score = score
                    best_feature = f

        selected.append(best_feature)
        print(f">>> Added feature {best_feature} (score = {best_score:.4f})\n")

    print("Forward Selection finished.")
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
    print("Beginning Backward Elimination...")

    while len(selected) > 1:
        best_feature_to_remove = None
        best_score = -1

        for f in selected:
            temp = selected.copy()
            temp.remove(f)
            score = evaluate(temp)
            print(f"   Evaluating {temp} (removed {f}) → score = {score:.4f}")

            if score > best_score:
                best_score = score
                best_feature_to_remove = f

        selected.remove(best_feature_to_remove)
        print(f">>> Removed feature {best_feature_to_remove} (score = {best_score:.4f})\n")

    print("Backward Elimination finished.")
    return selected
