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
    
    try:
        num_str = input("Please enter total number of features: ")
        total_features = int(num_str)
    except ValueError:
        print("Invalid number. Exiting.")
        return
    
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
        forward_selection(all_features)
    elif choice == "2":
        backward_elimination(all_features)
    elif choice == "3":
        print("Not implemented yet — running Forward Selection instead!\n")
        forward_selection(all_features)
    else:
        print("Invalid choice — running Forward Selection")
        forward_selection(all_features)
    
if __name__ == "__main__":
    main()

