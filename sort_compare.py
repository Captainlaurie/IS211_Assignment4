import random
import time

#Random list function
def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


#Provided algorithms modified 
def insertion_sort(lst):
    a_list = lst.copy()
    start = time.perf_counter()
    for i in range(1, len(a_list)):
        current_value = a_list[i]
        position = i
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    total = time.perf_counter() - start
    return a_list, total



def shell_sort(lst):
    a_list = lst.copy()
    start = time.perf_counter()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for i in range(sublist_count, len(a_list)):
            current_value = a_list[i]
            position = i
            while position >= sublist_count and a_list[position - sublist_count] > current_value:
                a_list[position] = a_list[position - sublist_count]
                position = position - sublist_count
            a_list[position] = current_value
        sublist_count = sublist_count // 2
    total = time.perf_counter() - start
    return a_list, total



def python_sort(lst):
    a_list = lst.copy()
    start = time.perf_counter()
    a_list.sort()
    total = time.perf_counter() - start
    return a_list, total


#Main function that tells the random function how many lists of what length to create
#Sets up variables to store the total times
#Then prints out the time it takes to sort each list
if __name__ == "__main__":
    """Main entry point"""
    
    num_list = 100
    size1 = 500
    size2 = 1000
    size3 = 2000

    total_is1 = 0
    total_is2 = 0
    total_is3 = 0

    total_ss1 = 0
    total_ss2 = 0
    total_ss3 = 0

    total_ps1 = 0
    total_ps2 = 0
    total_ps3 = 0

    for i in range(num_list):
        list1 = get_me_random_list(size1)
        list2 = get_me_random_list(size2)
        list3 = get_me_random_list(size3)

        sorted_list,time_is1 = insertion_sort(list1)
        sorted_list,time_is2 = insertion_sort(list2)
        sorted_list,time_is3 = insertion_sort(list3)

        sorted_list,time_ss1 = shell_sort(list1)
        sorted_list,time_ss2 = shell_sort(list2)
        sorted_list,time_ss3 = shell_sort(list3)

        sorted_list,time_ps1 = python_sort(list1)
        sorted_list,time_ps2 = python_sort(list2)
        sorted_list,time_ps3 = python_sort(list3)

        total_is1 += time_is1
        total_is2 += time_is2
        total_is3 += time_is3

        total_ss1 += time_ss1
        total_ss2 += time_ss2
        total_ss3 += time_ss3

        total_ps1 += time_ps1
        total_ps2 += time_ps2
        total_ps3 += time_ps3

    avg_time_is1 = total_is1 / num_list
    avg_time_is2 = total_is2 / num_list
    avg_time_is3 = total_is3 / num_list

    avg_time_ss1 = total_ss1 / num_list
    avg_time_ss2 = total_ss2 / num_list
    avg_time_ss3 = total_ss3 / num_list

    avg_time_ps1 = total_ps1 / num_list
    avg_time_ps2 = total_ps2 / num_list
    avg_time_ps3 = total_ps3 / num_list


    print(f"Insertion Sort took {avg_time_is1:10.7f} seconds to run, on average for a list of {size1} elements")
    print(f"Shell Sort took {avg_time_ss1:10.7f} seconds to run, on average for a list of {size1} elements")
    print(f"Python Sort took {avg_time_ps1:10.7f} seconds to run, on average for a list of {size1} elements\n")

    print(f"Insertion Sort took {avg_time_is2:10.7f} seconds to run, on average for a list of {size2} elements")
    print(f"Shell Sort took {avg_time_ss2:10.7f} seconds to run, on average for a list of {size2} elements")
    print(f"Python Sort took {avg_time_ps2:10.7f} seconds to run, on average for a list of {size2} elements\n")

    print(f"Insertion Sort took {avg_time_is3:10.7f} seconds to run, on average for a list of {size3} elements")
    print(f"Shell Sort took {avg_time_ss3:10.7f} seconds to run, on average for a list of {size3} elements")
    print(f"Python Sort took {avg_time_ps3:10.7f} seconds to run, on average for a list of {size3} elements")
