import csv

# Justin DiPietro
# Created 2020-12-02

# Columns:
# review number, brand, variety, style, country, stars, topTen

def main():
    print('starting')
    ramenList = importData()

    question1Results = {} # Dictionary to hold words and their frequency
    question2Results = {} # Dictionary to hold countries and their frequency
    question3Results = {} # Dictionary to hold brands and their frequency
    question4Results = {} # Dictionary to hold stars and their frequency
    question5Results = {} # Dictionary to hold words and their frequency
    question6Results = {} # Dictionary to hold brands and their scores

    for ramen in ramenList:
        words = ramen.variety.split(' ') # break the variety column into words
        for word in words: # iterate thru those words
            if word in question1Results: #if the word is already saved, just increment its frequency
                question1Results[word] += 1
            else:
                #add the uncatalogued word to the list of words and set its count to 1
                question1Results[word] = 1
        if ramen.country in question2Results:
            question2Results[ramen.country] += 1
        else:
            #add the uncatalogued country to the list of country and set its count to 1
            question2Results[ramen.country] = 1
        if ramen.brand in question3Results: # if the brand is already saved, just increment its frequency
            question3Results[ramen.brand] += 1
        else:
            #add the uncatalogued country to the list of country and set its count to 1
            question3Results[ramen.brand] = 1
        if str(ramen.stars) in question4Results:
            question4Results[str(ramen.stars)] += 1 # if the stars is already saved, just increment its frequency
        else:
            #add the uncatalogued stars to the list of stars and set its count to 1
            question4Results[str(ramen.stars)] = 1
        if ramen.stars == "Unrated": # there are 3 datapoints without ratings. Pass over these
            pass
        else:
            if ramen.brand in question6Results: # if the brand is already saved, add new rating
                question6Results[ramen.brand].append(float(ramen.stars))
            else: # add the brand to the dictionary and create list of ratings (to be averaged later)
                question6Results[ramen.brand] = [float(ramen.stars)]

    print('1. What ingredients or flavors are most commonly advertised on ramen package labels?')
    print(getLargestInDict(question1Results, 30))
    print('2. How is ramen manufacturing internationally distributed?')
    print(processQ2(question2Results, len(ramenList)))
    print('3. What are the top 10 most popular ramen brands?')
    print(getLargestInDict(question3Results, 10))
    print('4. What are the top 10 ramen ratings?')
    print(getLargestInDict(question4Results, 10))
    print('5. If you convert the variety column into a set of words, what are the top 20 most popular words in the column?')
    print(getLargestInDict(question1Results, 20))
    print('6. What are the top 10 brands with the best average score?')
    print(processQ6(question6Results))
    

def processQ2(question2Results, totalCount):
    for country in question2Results: # iterate thru the saved countries
        # compare frequency to total to get percentage
        question2Results[country] = round(((question2Results[country]/totalCount)*100), 2) 
    sort = sorted(question2Results.items(), key=lambda x: x[1], reverse=True) # sort it in decreasing order
    for country in sort: #then print in order
        print(country[0] + ": " + str(country[1]) + "%")
    return('')
    

def processQ6(question6Results):
    for brand in question6Results: # iterate thru the saved countries
        # compare frequency to total to get percentage
        ratingCount = len(question6Results[brand])
        question6Results[brand] = sum(question6Results[brand])
        question6Results[brand] = question6Results[brand]/ratingCount
    sort = sorted(question6Results.items(), key=lambda x: x[1], reverse=True) # sort it in decreasing order
    for brand in sort[:10]:
        print(brand[0] + ": " + str(brand[1]) + " stars")
    return('')
    

# Pass in a dictionary and the number of top results requested
def getLargestInDict(inDictionary, count):
    dictionary = inDictionary.copy() # is this what you meant by clone?
    largest = []
    sort = sorted(dictionary.items(), key=lambda x: x[1], reverse=True) # sort it in decreasing order
    for i in range(count):
        largest.append(sort[i]) 
    return largest
    

# Read in the data from the csv file into a list of "Ramen" objects    
def importData():
    ramenList = []
    with open('ramen-ratings.csv', encoding='utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            ramen = Ramen(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            ramenList.append(ramen)
            
    return ramenList


class Ramen:
    def __init__(self, reviewNumber, brand, variety, style, country, stars, topTen):
        self.reviewNumber = reviewNumber
        self.brand = brand
        self.variety = variety
        self.style = style
        self.country = country
        self.stars = stars
        self.topTen = topTen


main() 
