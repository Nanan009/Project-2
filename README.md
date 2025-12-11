# CS 170 Project 2 - Feature Selection

## Requirements

- Python 3.x
- NumPy

Install NumPy:
```bash
pip install numpy
```

## How to Run

1. Place dataset files in `data/` folder
2. Run the program:
```bash
python3 main.py
```
3. Enter dataset filename when prompted (e.g., `small-test-dataset.txt`)
4. Choose algorithm:
   - `1` for Forward Selection
   - `2` for Backward Elimination

## Files

- `classifier.py` - Nearest neighbor classifier
- `validator.py` - Leave-one-out cross validation
- `data_loader.py` - Load and normalize data
- `evaluation.py` - Evaluate feature subsets
- `search.py` - Forward selection and backward elimination algorithms
- `main.py` - Main program

## Test Files

Included in `data/`:
- `small-test-dataset.txt` (100 instances, 10 features)
- `large-test-dataset.txt` (1000 instances, 40 features)
- `titanic-clean.txt` (Titanic dataset)

## Example Run

```bash
$ python3 main.py
Welcome to Siyuan's Feature Selection Algorithm.

Enter dataset filename: small-test-dataset.txt

This dataset has 10 features (not including the class attribute), with 100 instances.

Running nearest neighbor with no features (random baseline), using "leaving-one-out" evaluation, I get an accuracy of 50.0%

Type the number of the algorithm you want to run.

     1) Forward Selection
     2) Backward Elimination

Your choice: 1
```

## Notes

- Large dataset experiments take 10-20 minutes
- Results are printed to console
- Timing information included if enabled in code