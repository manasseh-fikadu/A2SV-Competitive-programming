void countSwaps(vector<int> a) {
    int n, numSwaps = 0, firstElement, lastElement, temp;
    for (int i = 0; i < a.size(); i++) {
    
        for (int j = 0; j < a.size() - 1; j++) {
            if (a[j] > a[j + 1]) {
                //swap(a[j], a[j + 1]);
                temp = a[j];
                a[j] = a[j+1];
                a[j + 1] = temp;
                 
                numSwaps++;
            }
        }
    }
    cout << "Array is sorted in " << numSwaps << " swaps." << endl;
    cout << "First Element: " << a.at(0) << endl;
    cout << "Last Element: " << a.at(a.size() - 1);
}
