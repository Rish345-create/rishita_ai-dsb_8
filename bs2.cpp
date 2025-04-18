#include <stdio.h>

// Function to perform Bubble Sort (iterative)
void bubbleSort(int arr[], int size) {
    // Loop through the array
    for (int i = 0; i < size - 1; i++) {
        // Compare each pair of adjacent elements
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap if the element is greater than the next one
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Function to perform Binary Search using recursion
int binarySearch(int arr[], int low, int high, int target) {
    // Base case: if the range is invalid, return -1 (not found)
    if (low > high) {
        return -1;
    }

    // Find the middle index
    int mid = low + (high - low) / 2;

    // Check if the target is at the middle
    if (arr[mid] == target) {
        return mid; // Target found
    }
    
    // If the target is smaller than the middle element, search in the left half
    if (arr[mid] > target) {
        return binarySearch(arr, low, mid - 1, target);
    }
    
    // If the target is greater than the middle element, search in the right half
    return binarySearch(arr, mid + 1, high, target);
}

int main() {
    int arr[100], size, target, result;

    // Step 1: Get the array size and elements from the user
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    printf("Enter %d elements:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    // Step 2: Sort the array using Bubble Sort
    bubbleSort(arr, size);
    printf("Array has been sorted.\n");

    // Step 3: Ask the user for the target element to search
    printf("Enter the target element to search: ");
    scanf("%d", &target);

    // Step 4: Perform Binary Search
    result = binarySearch(arr, 0, size - 1, target);
    
    // Step 5: Display the result
    if (result != -1) {
        printf("Element %d found at index %d.\n", target, result);
    } else {
        printf("Element %d not found in the array.\n", target);
    }

    return 0;
}
