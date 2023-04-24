/* Binary Seach Algorithm 
 * e.g. input can be strings and ints */

#include <stdio.h>

int binary_search(int element, int startIndex, int endIndex, int arr[])
{
  int middleIndex;
  int result=-1;
  
  if (startIndex <= endIndex) {
    middleIndex = (startIndex + endIndex)/2;
    if (arr[middleIndex] == element)
      return middleIndex;
    if (element > arr[middleIndex])
      result = binary_search(element, middleIndex, endIndex, arr);
    else 
      result = binary_search(element, startIndex, middleIndex, arr);
  }
  return result;
}

int main(int argc, char *argv)
{
  int test_array[] = {1,2,3,4,5,6,7,8,9,10};
  int startIndex = 0;
  int endIndex = sizeof(test_array)/sizeof(int) - 1;
  int element = 4;
  int result = binary_search(element, startIndex, endIndex, test_array);
  
  if (result > -1)
    printf("Found element %d, found at position %d\n", element, result);
  else
    printf("No element found in array\n");

  return 0;
}
    
