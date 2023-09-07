#pip install pytest-timeit
from timeit import default_timer as timer
from Q53 import quickSort #importing quick sort function from Q53.py
from Q52 import mergeSort #importing merge sort function from Q52.py
from Q51 import bubbleSort #importing bubble sort function from Q51.py

with open ("sort.txt","r") as f: #opening the file
    val = f.read().splitlines()  #reading the file and splitting the lines
    f.close() #closing the file

start = timer() #starting the timer
s1 = quickSort(val)     #calling quick sort function
end = timer() #ending the timer
v1 = round((end - start)*1000000,2) #calculating the time taken in microseconds

start = timer()
s2 = bubbleSort(val)
end = timer()
v2 = round((end - start)*1000000,2)

start = timer()
s3 = mergeSort(val)
end = timer()
v3 = round((end - start)*1000000,2)

# showing the time taken by each sort function
print(f"Bubble sort takes {v2} μS.\nQuick Sort takes {v1} μS.\nMerge Sort takes {v3} μS.")

# Test run shows that for short data arranging bubble sort proves good
# But as data input gets bigger it consumes way more time than merge sort which is the fastest.