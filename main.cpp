#include <iostream>
using namespace std;

// Function prototypes
void greet();

int main() {
    cout << "Welcome to Bertie Woosters (change this to your name) Feature Selection Algorithm. \n \n Please enter total number of features:";

    int totalFeatures;
    cin >> totalFeatures;

    cout << "Type the number of the algorithm you want to run." << endl << endl;
    cout << "     Forward Selection" << endl;
    cout << "     Backward Elimination" << endl;
    cout << "     Bertie's Special Algorithm." << endl;
    
    return 0;
}

void greet() {
    cout << "Hello from a function!" << endl;
}
