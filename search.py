from evaluation import evaluate
import time

def forward_selection(all_features):
    """
    Performs greedy forward selection.
    """
    start_time = time.time()
    selected = []
    
    # track the best so far
    current_best_score = 0  
    print("Beginning search.\n")

    while len(selected) < len(all_features):
        best_feature = None
        # best_score = -1
        best_score = 0

        for f in all_features:
            if f not in selected:
                temp = selected + [f]
                score = evaluate(temp)
                
                print(f"Using feature(s) {{{','.join(map(str, temp))}}} accuracy is {score:.1f}%")

                if score > best_score:
                    best_score = score
                    best_feature = f

        # greedy check
        if best_score > current_best_score:
            current_best_score = best_score
            selected.append(best_feature)
            print(f"\nFeature set {{{','.join(map(str, selected))}}} was best, accuracy is {current_best_score:.1f}%\n")
        else:
            print(f"\n(Warning, Accuracy has decreased!)")
            break

    elapsed = time.time() - start_time
    # final report
    print(f"Finished search!! The best feature subset is {{{','.join(map(str, selected))}}}, which has an accuracy of {current_best_score:.1f}%")
    print(f"Time elapsed: {elapsed:.2f} seconds\n")
    return selected


def backward_elimination(all_features):
    """
    Performs greedy backward elimination.
    """
    start_time = time.time()
    selected = all_features.copy()
    
    # track best score (start with full set accuracy)
    current_best_score = evaluate(selected)
    
    print("Beginning search.\n")
    print(f"Using feature(s) {{{','.join(map(str, selected))}}} accuracy is {current_best_score:.1f}%")
    print(f"\nFeature set {{{','.join(map(str, selected))}}} was best, accuracy is {current_best_score:.1f}%\n")

    while len(selected) > 0:
        best_feature_to_remove = None
        # best_score = -1
        best_score = 0

        for f in selected:
            temp = selected.copy()
            temp.remove(f)
            
            # handle empty set just in case
            if len(temp) == 0:
                score = evaluate([])
            else:
                score = evaluate(temp)
                
            print(f"Using feature(s) {{{','.join(map(str, temp))}}} accuracy is {score:.1f}%")

            if score > best_score:
                best_score = score
                best_feature_to_remove = f

        # only remove if accuracy is better (or equal)
        if best_score >= current_best_score:
            current_best_score = best_score
            selected.remove(best_feature_to_remove)
            print(f"\nFeature set {{{','.join(map(str, selected))}}} was best, accuracy is {current_best_score:.1f}%\n")
        else:
            print(f"\n(Warning, Accuracy has decreased!)")
            break

    elapsed = time.time() - start_time
    # final report
    print(f"Finished search!! The best feature subset is {{{','.join(map(str, selected))}}}, which has an accuracy of {current_best_score:.1f}%")
    print(f"Time elapsed: {elapsed:.2f} seconds\n")
    return selected