# def main():
#     print("Welcome to Bertie Woosters (change this to your name) Feature Selection Algorithm.\n")
#     total_features = int(input("Please enter total number of features: "))

#     print("\nType the number of the algorithm you want to run.\n")
#     print("     1) Forward Selection")
#     print("     2) Backward Elimination")
#     print("     3) Bertie's Special Algorithm.")

#     # You can add logic later to call each algorithm


# if __name__ == "__main__":
#     main()

import random
from evaluation import evaluate
from search import forward_selection, backward_elimination

def main():
    print("Welcome to [Your Name] and [Partner Name]'s Feature Selection Algorithm.\n")
    
    total_features = int(input("Please enter total number of features: "))
    all_features = list(range(1, total_features + 1))

    # show accuracy with zero features
    zero_accuracy = evaluate([])
    print(f"\nUsing no features and \"random\" evaluation, I get an accuracy of {zero_accuracy:.1f}%\n")
    
    print("Type the number of the algorithm you want to run.\n")
    print("     1) Forward Selection")
    print("     2) Backward Elimination")
    print("     3) Bertie's Special Algorithm (not implemented yet)\n")
    
    choice = input("Your choice: ").strip()
    
    if choice == "1":
        print("Beginning search.\n")
        best_set = forward_selection(all_features)
    elif choice == "2":
        print("Beginning search.\n")
        best_set = backward_elimination(all_features)
    elif choice == "3":
        print("Not implemented yet — running Forward Selection instead!\n")
        best_set = forward_selection(all_features)
    else:
        print("Invalid choice — running Forward Selection")
        best_set = forward_selection(all_features)
    
    # final result
    final_accuracy = evaluate(best_set)
    print(f"\nFinished search!! The best feature subset is {best_set}, which has an accuracy of {final_accuracy:.1f}%")   

if __name__ == "__main__":
    main()

