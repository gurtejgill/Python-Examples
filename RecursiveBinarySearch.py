import math

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = round(l + (r - l)/2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, math.ceil(mid-1), x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, math.floor(mid+1), r, x) 
  
    else: 
        # Element is not present in the array 
        return -1


numbers = []

for num in range(1,51):
    numbers.append(num*2)

numbers.sort()
#print(len(numbers))

user_input= int(input("Enter a number to check if it's present in the list>"))

index = binarySearch(numbers, 0,math.ceil(len(numbers)), user_input)
print("Your number is present at index: ",index)