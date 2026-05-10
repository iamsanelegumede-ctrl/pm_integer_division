#1.1 - Provide python 3 code for a function distribute_n() that takes in an integer number n, and an integer number k as arguments,then returns a list with k-elements such that the sum of the elements in the list is equal to n. If n is not greater than or equal to k, the function must return None. The elements of the list are required to be at least 1. (5 marks)

def distribute_n(n, k):
    # Check if n is at least k (since each element must be >= 1)
    if n < k:
        return None
    
    # Start with a list of k ones (minimum requirement)
    result = [1] * k
    
    # We already used up k, so distribute the remaining (n - k)
    remaining = n - k
    
    # Add the remaining value to the first element
    result[0] += remaining
    
    # Return the final list
    return result

# Example:
print(distribute_n(10, 3))  # [8, 1, 1] → sum = 10
print(distribute_n(2, 5))   # None (since 2 < 5)


#1.2 - Provide python 3 code for a function pie_chart() that takes in a list (“percentages[]”) of real numbers between 0 and 100, and uses the numbers in the list as percentages and return a list of tuples (p, share) where p is the number in the list, and share is a percentage of out 360. If the numbers in percentages[] do not add up to 100 exactly, return None. (5 marks)

def pie_chart(percentages):
    # Check if percentages add up to exactly 100
    if sum(percentages) != 100:
        return None
    
    result = []
    for p in percentages:
        # share = percentage of 360 degrees
        share = (p / 100) * 360
        result.append((p, share))
    
    return result

# Example:
print(pie_chart([50, 30, 20]))
# [(50, 180.0), (30, 108.0), (20, 72.0)]
print(pie_chart([40, 40, 30]))  # None (sum ≠ 100)


#1.3 - Provide python 3 code for a function school_trip() that takes a number n, which represents the number of students going on a trip, and returns a list of tuples (“taxi n:”, k) where “taxi n:” is the taxi number, and k is the number of students in that taxi. (5 marks)
def school_trip(n):
    # Assume each taxi can carry 4 students
    capacity = 4
    
    result = []
    taxi_number = 1
    
    # While there are students left
    while n > 0:
        # Put up to 4 students in the current taxi
        if n >= capacity:
            result.append((f"taxi {taxi_number}:", capacity))
            n -= capacity
        else:
            # Last taxi with fewer than 4 students
            result.append((f"taxi {taxi_number}:", n))
            n = 0
        
        taxi_number += 1
    
    return result

# Example:
print(school_trip(10))
# [('taxi 1:', 4), ('taxi 2:', 4), ('taxi 3:', 2)]
