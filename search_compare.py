import time
import random

#Function to generate random list
def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

#Provided algorithm functions for searching lists
#time added using Python built in time.perf_counter() module

def sequential_search(a_list, item):
    start = time.perf_counter()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    total = time.perf_counter() - start
    return found, total


def ordered_sequential_search(a_list, item):
    start = time.perf_counter()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    total = time.perf_counter() - start
    return found, total


def binary_search_iterative(a_list,item):
    
    start = time.perf_counter()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    total = time.perf_counter() - start
    return found, total

def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False, 0
    else:
        start_time = time.perf_counter()
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end_time = time.perf_counter()
            total_time = end_time - start_time
            return True, total_time
        else:
            if item < a_list[midpoint]:
                result, total_time = binary_search_recursive(a_list[:midpoint], item)
            else:
                result, total_time = binary_search_recursive(a_list[midpoint + 1:], item)
            end_time = time.perf_counter()
            total_time += end_time - start_time
            return result, total_time

#Main function to tell the random function what lists to create, then print results
if __name__ == "__main__":
    """Main entry point"""
    
    num_list = 100
    size1 = 500
    size2 = 1000
    size3 = 2000

#Set up sequential search time variables
    total_seq1 = 0
    total_seq2 = 0
    total_seq3 = 0

#Set up ordered sequential search time variables
    total_oseq1 = 0
    total_oseq2 = 0
    total_oseq3 = 0

#Set up binary search time variables
    total_ibin1 = 0
    total_ibin2 = 0
    total_ibin3 = 0

#Set up recursive binary search time variables
    total_rbin1 = 0
    total_rbin2 = 0
    total_rbin3 = 0

#For loop to iterate through lists and save the time it takes for each algorithm to run
#Use a large humber instead of -1 to search as noted in the weekly office hours
 
    for i in range(num_list):
        list1 = get_me_random_list(size1)
        list2 = get_me_random_list(size2)
        list3 = get_me_random_list(size3)

        check,time_seq1 = sequential_search(list1, 99999999)
        check,time_seq2 = sequential_search(list2, 99999999)
        check,time_seq3 = sequential_search(list3, 99999999)

        list1.sort()
        list2.sort()
        list3.sort()

        check,time_oseq1 = ordered_sequential_search(list1, 99999999)
        check,time_oseq2 = ordered_sequential_search(list2, 99999999)
        check,time_oseq3 = ordered_sequential_search(list3, 99999999)

        check,time_ibin1 = binary_search_iterative(list1, 99999999)
        check,time_ibin2 = binary_search_iterative(list2, 99999999)
        check,time_ibin3 = binary_search_iterative(list3, 99999999)

        check,time_rbin1 = binary_search_recursive(list1, 99999999)
        check,time_rbin2 = binary_search_recursive(list2, 99999999)
        check,time_rbin3 = binary_search_recursive(list3, 99999999)

        total_seq1 += time_seq1
        total_seq2 += time_seq2
        total_seq3 += time_seq3

        total_oseq1 += time_oseq1
        total_oseq2 += time_oseq2
        total_oseq3 += time_oseq3

        total_ibin1 += time_ibin1
        total_ibin2 += time_ibin2
        total_ibin3 += time_ibin3

        total_rbin1 += time_rbin1
        total_rbin2 += time_rbin2
        total_rbin3 += time_rbin3
        
        
    #Find average time for each list size and search type and print
    avg_time_seq1 = total_seq1 / num_list
    avg_time_seq2 = total_seq2 / num_list
    avg_time_seq3 = total_seq3 / num_list

    avg_time_oseq1 = total_oseq1 / num_list
    avg_time_oseq2 = total_oseq2 / num_list
    avg_time_oseq3 = total_oseq3 / num_list

    avg_time_ibin1 = total_ibin1 / num_list
    avg_time_ibin2 = total_ibin2 / num_list
    avg_time_ibin3 = total_ibin3 / num_list

    avg_time_rbin1 = total_rbin1 / num_list
    avg_time_rbin2 = total_rbin2 / num_list
    avg_time_rbin3 = total_rbin3 / num_list

    print(f"Sequential Search took {avg_time_seq1:10.7f} seconds to run, on average for a list of {size1} elements")
    print(f"Ordered Sequential Search took {avg_time_oseq1:10.7f} seconds to run, on average for a list of {size1} elements")
    print(f"Binary Search Iterative took {avg_time_ibin1:10.7f} seconds to run, on average for a list of {size1} elements")
    print(f"Binary Search Recursive took {avg_time_rbin1:10.7f} seconds to run, on average for a list of {size1} elements\n")

    print(f"Sequential Search took {avg_time_seq2:10.7f} seconds to run, on average for a list of {size2} elements")
    print(f"Ordered Sequential Search took {avg_time_oseq2:10.7f} seconds to run, on average for a list of {size2} elements")
    print(f"Binary Search Iterative took {avg_time_ibin2:10.7f} seconds to run, on average for a list of {size2} elements")
    print(f"Binary Search Recursive took {avg_time_rbin2:10.7f} seconds to run, on average for a list of {size2} elements\n")

    print(f"Sequential Search took {avg_time_seq3:10.7f} seconds to run, on average for a list of {size3} elements")
    print(f"Ordered Sequential Search took {avg_time_oseq3:10.7f} seconds to run, on average for a list of {size3} elements")
    print(f"Binary Search Iterative took {avg_time_ibin3:10.7f} seconds to run, on average for a list of {size3} elements")
    print(f"Binary Search Recursive took {avg_time_rbin3:10.7f} seconds to run, on average for a list of {size3} elements")