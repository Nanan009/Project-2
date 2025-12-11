from data_loader import load_dataset
from evaluation import set_dataset, evaluate

# test small dataset
instances, num_features = load_dataset('data/small-test-dataset.txt')
set_dataset(instances)

# test features {3, 5, 7}
accuracy = evaluate([3, 5, 7])
print(f"Small dataset with features {{3, 5, 7}}: {accuracy:.1f}%")
print("Expected: ~89.0%\n")

# test large dataset
instances, num_features = load_dataset('data/large-test-dataset.txt')
set_dataset(instances)

# test features {1, 15, 27}
accuracy = evaluate([1, 15, 27])
print(f"Large dataset with features {{1, 15, 27}}: {accuracy:.1f}%")
print("Expected: ~94.9%")