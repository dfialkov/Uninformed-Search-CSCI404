1. Daniel Fialkov, 10825432
2. Python 3
3. Please use Linux
4. The code is in a single file called search.py that takes input from text files. I've created some classes to use as objects to represent cities, objects to represent the graph, and a simple priority queue implementation.
The algorithm is implemented iteratively, first adding the first node to the exploration queue and then adding its connections, and so on until all nodes have been explored. If the target node is explored, it's detected, the program prints the path, and exists.
If the exploration queue is empty, then the program stops the search, prints that there is no path, and exits. 
5. The code is to be run with Python 3 on Linux.
The code is to be run as follows:
python search.py input_file origin_city destination_city
Note that depending on the packages you have installed, you may need to specify that you need to run the code in Python 3 in some other way. Unfortunately, I have no idea what your system is so I can't provide precise instructions. 