import math

'''
Author: Jackson Jacobs & Jorge Soto-Ventura

Gets the cover of each of the data sets.
'''
def main(file, outputFileName):
    file= open(file, "r")
    xList=[]
    yList=[]
    currentNeighborhood=[] #all the points in the current point's neighborhood
    allNeighborhoods=set()
    distances=[]
    cover=[]

    #Creates two seperate lists for X and Y variables
    for line in file:
        word=line.split()
        x= int(word[0])
        y= int(word[1])
        xList.append(x)
        yList.append(y)
    file.close()

    points=list(zip(xList, yList))
    # Global Variables used to compare the points against one another
    compareIndex=0
    currentIndex=0

    #For loop for the current point in order to find the cover
    for current in points:
        currentPoint= points[currentIndex]
        for point in points:
            nextPoint= points[compareIndex]
            # Used to check if the next point is a neighbor of the current points
            if math.sqrt(((nextPoint[0]- currentPoint[0])**2) + ((nextPoint[1] - currentPoint[1]))**2) <=25:
                currentNeighborhood.append(nextPoint)
            compareIndex+=1
    
        check= all(item in allNeighborhoods for item in currentNeighborhood) #Checks to see if the current point and its neighbors are already apart of the spread
        # If check is false then it adds the point to the cover.
        if check is False:
            cover.append(currentPoint)
            allNeighborhoods.update(currentNeighborhood)
        currentNeighborhood.clear()
        currentIndex+=1
        compareIndex= 0

    with open(outputFileName, "w") as outputFile:
        outputFile.write('\n'.join(str(x) for x in cover))

    
if __name__ == "__main__":
    main("numbers1.txt", "cover_1.txt")
    main("numbers2.txt", "cover_2.txt")