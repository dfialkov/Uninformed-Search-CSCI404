import sys
import argparse

class City:
#Using strings like pointers is not a good idea. I'm doing it anyway.

    name = ""
    connections = dict()
    predecessor = ""

    def __init__(self, newName):
        self.name = newName
        self.connections = dict()

    def addConnection(self, newName, newLength):
        self.connections[newName] = newLength

class Graph:
    graph = dict()
    def __init__(self):
        self.graph = dict()

    #If the city already exists in the database, ignore it. Else, add an entry for it in the database
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
        returnedCity = self.toExplore[0]
        minPath = returnedCity[1]
        #If there's a closer city, that city becomes the new returned city and its distance becomes the closest
        for i in self.toExplore:
            if i[1] < minPath:
                returnedCity = i
                minPath = returnedCity[1]
        #Remove the returned city from the queue
        self.toExplore.remove(returnedCity)
        return returnedCity

    def push(self, cityName, totalDistance):
        self.toExplore.append((cityName, totalDistance))

    def isEmpty(self):
        if len(self.toExplore) == 0:
            return True
        else:
            return False
#True if the city is already in the queue. False if not
    def contains(self, cityName):
        for i in self.toExplore:
            if i[0] == cityName:
                return True
        return False
    def getDistance(self, cityName):
        for i in self.toExplore:
            if i[0] == cityName:
                return i[1]
        return None
#Configuring the parser and parsing args
parser = argparse.ArgumentParser()
parser.add_argument("inputFile", help="The file containing connection data")
parser.add_argument("startCity", help="The root node of the graph")
parser.add_argument("endCity", help="The city to search for")
args = parser.parse_args()

inFile = args.inputFile
startCity = args.startCity
endCity = args.endCity

f = open(inFile, 'r')
cities = Graph()
#Read file
while(True):
    currLine = f.readline()
    if(currLine == "END OF INPUT\n"):
        break
    else:
        #Load and connect the cities
        lineContents = currLine.split(' ')
        cities.addCityIfAbsent(lineContents[0])
        cities.addCityIfAbsent(lineContents[1])
        cities.connectCities(lineContents[0], lineContents[1], int(lineContents[2]))


exploredList = []

explorationQueue = ExploreQueue()
#Get the start node, push it into the queue
explorationQueue.push(cities.graph[startCity].name, 0)
#If queue not empty
while not explorationQueue.isEmpty():
    currNode = explorationQueue.pop()
    currCityName = currNode[0]
    currCityDistance = currNode[1]
    #If the node is not in the explored list
    if not currCityName in exploredList:
        #Mark the current node as explored
        exploredList.append(currCityName)
        #For every node connected to the current node(iterating through the entire dictionary by going through the key list)
        for i in cities.graph[currCityName].connections.keys():
            #If the node has already been explored or if the current path to the node is shorter than the current shortest path to the node
            if (not i in exploredList) or (explorationQueue.contains(i) and explorationQueue.getDistance(i) > currCityDistance + cities.graph[currCityName].connections[i]):
                #Add the node to the exploration queue, with its travel cost being the total travel cost up to the predecessor + the cost to the node itself
                explorationQueue.push(i, cities.graph[currCityName].connections[i] + currCityDistance)
                #The node's precedessor is the node currently being explored, so set that too
                cities.graph[i].predecessor = currCityName
            
            #If the node is the goal node
            if i == endCity:
                #Calculate the final distance

                distanceTotal = cities.graph[currCityName].connections[i] + currCityDistance
                print("distance: " + str(distanceTotal) +" km")
                print("route: ")
                
                routeList = []
                
                lastCity = i
                
                while(cities.graph[lastCity].predecessor != ""):
                    
                    lastPredecessor = cities.graph[lastCity].predecessor
                    routeList.append(str(lastPredecessor) +" to " + str(lastCity)   + ", " + str(cities.graph[lastPredecessor].connections[lastCity]) + " km")
                    lastCity = lastPredecessor
                for i in reversed(routeList):
                    print(i)
                sys.exit()
print("distance: infinity")
print("route:")
print("none")