class City:
#Using strings like pointers
    name = ""
    connections = []

    def __init__(self, newName):
        self.name = newName
    
    def addConnection(self, newName, newLength):
        self.connections += (newName, newLength)

class Graph:
    graph = []
    def __init__(self):
        self.graph = dict()
    
    def addCityIfAbsent(self, newCity):
        if newCity in self.graph.keys():
            pass
        else:
            self.graph[newCity] = City(newCity)
    #Cities add each other to their connections simultaneously
    def connectCities(self, startCity, endCity, pathLength):
        self.graph[startCity].addConnection(endCity, pathLength)
        self.graph[endCity].addConnection(startCity, pathLength)

#A truly hideous queue implementation. 
class ExploreQueue:
    toExplore = []
    def __init(self):
        self.toExplore = []
    
    def pop(self):
        #Get some initial values for the city and minimum path to serve as defaults
        returnedCity = toExplore[0]
        minPath = self.toExplore[0][1]
        #If there's a closer city, that city becomes the new returned city and its distance becomes the closest
        for i in self.toExplore:
            if i[1] < minPath:
                minPath = i[1]
                returnedCity = i
        return returnedCity

    def push(self, cityName, totalDistance):
        self.toExplore += (cityName, totalDistance)

f = open("input1.txt", 'r')
cities = Graph()
#Read file
while(True):
    currLine = f.readline()
    if(currLine == "END OF INPUT"):
        break
    else:
        #Load and connect the cities
        lineContents = currLine.split()
        cities.addCityIfAbsent(lineContents[0])
        cities.addCityIfAbsent(lineContents[1])
        cities.connectCities(lineContents[0], lineContents[1], lineContents[2])

#Get the start node, push it into the queue
startCity = "Munich"
endCity = "Berlin"


explorationQueue = ExploreQueue()
explorationQuque.push(cities[startCity])