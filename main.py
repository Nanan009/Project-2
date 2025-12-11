from evaluation import evaluate, set_dataset
from search import forward_selection, backward_elimination
from data_loader import load_dataset

def main():
    print("Welcome to Our Feature Selection Algorithm.\n")
    
    # ask for dataset file
    filename = input("Enter dataset filename: ").strip()

    if not filename.startswith('data/'):
        filename = 'data/' + filename
    
    # menu
    print("Type the number of the algorithm you want to run.\n")
    print("     1) Forward Selection")
    print("     2) Backward Elimination\n")
    
    choice = input("Your choice: ").strip()

    # load dataset
    try:
        instances, num_features = load_dataset(filename)
        print(f"\nThis dataset has {num_features} features (not including the class attribute), with {len(instances)} instances.\n")
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
    
    # set dataset for evaluation function
    set_dataset(instances)
    
    # show accuracy with no features
    print("Running nearest neighbor with no features (random baseline), using \"leaving-one-out\" evaluation, I get an accuracy of 50.0%\n")
    
    
    all_features = list(range(1, num_features + 1))
    
    if choice == "1":
        forward_selection(all_features)
    elif choice == "2":
        backward_elimination(all_features)
    else:
        print("Invalid choice - running Forward Selection")
        forward_selection(all_features)

if __name__ == "__main__":
    main()
