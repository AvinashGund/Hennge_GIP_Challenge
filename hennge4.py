#MISSION 1
import array as arr
import sys

def calc_sum_of_sq_recur(case_int_list, index, result):
    if index == len(case_int_list):
        return result

    num = case_int_list[index]

    if num>=0:
        result += num**2

    return calc_sum_of_sq_recur(case_int_list, index + 1, result)

def calculate_sum_of_squares(num_list):
    return calc_sum_of_sq_recur(num_list, 0, 0)

def validate_integers(int_arr, index=0):
    if index < len(int_arr):
        if  int_arr[index] < -100 or int_arr[index] > 100:
            print("Please enter integers as per following format: -100 <= numbers >=100")
            sys.exit()
        
        validate_integers(int_arr, index + 1)


def read_test_case(n, results, index=0):
    if n==0:
        return results

    x = int(input())  # Input number of integers to be processed, as X (0 < X <= 100)
    if x>0 and x<=100:
        yn = arr.array('i', map(int, input().split()))  # Input space seperated integers to be processed. Yn (-100 <= Yn <= 100)   
        validate_integers(yn)   # Validate entered integers to be processed as: -100 <= Yn >=100
        if len(yn) == x:
            case_res = calculate_sum_of_squares(yn)  # Calculate sum of square of integers excluding negative      
            results.append(case_res)
        else:
            print("Enter {} integer numbers." .format(x))
            sys.exit()       
    else:
        print("Please enter integer numbers as i.e. greater than 0 and less that or equal to 100. ")
        sys.exit()
    

    return read_test_case(n-1, results, index+1)

def print_results(results, index=0):
    if index < len(results):
        print(results[index])
        print_results(results, index + 1)

def main():
    n = int(input())  #Input number of test cases to follow,  as N (1 <= N <= 100)
    if 1<=n<=100:
        results = read_test_case(n, arr.array('i', []))  #Calculate sum of square.
        print_results(results) 
    else:
        print("Enter a valid test cases number, i.e., 1 to 100")
        sys.exit()

if __name__ == "__main__":
    main()
