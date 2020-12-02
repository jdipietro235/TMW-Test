import csv

# Justin DiPietro
# Created 2020-11-30
# Updated 2020-12-01

# Columns:
# review number, brand, variety, style, country, stars, topTen

# A note on the organization:
# I prioritized readability over efficiency, so there are more lines of code than there needs to be
# and this runs a bit slower than it could.
# For a simple set of problems like this, readability is the important part. Even with this less efficient design,
# the code runs in about one second on my machine.


def main():
    print('Start')
    ramenList = importData()
    question1(ramenList)
    question2(ramenList)
    question3(ramenList)
    question4(ramenList)
    question5(ramenList)
    question6(ramenList)

def question1(ramenList):
    print('1. What ingredients or flavors are most commonly advertised on ramen package labels?')
    uniqueWords = {} # Dictionary to hold words and their frequency
    for ramen in ramenList: # iterate thru list of datapoints from csv file
        words = ramen.variety.split(' ') # break the variety column into words
        for word in words: # iterate thru those words
            if word in uniqueWords: #if the word is already saved, just increment its frequency
                uniqueWords[word] += 1
            else:
                #add the uncatalogued word to the list of words and set its count to 1
                uniqueWords[word] = 1

    print(getLargestInDict(uniqueWords, 30))


def question2(ramenList):
    print('2. How is ramen manufacturing internationally distributed?')
    uniqueCountries = {} # Dictionary to hold countries and their frequency
    ramenCount = len(ramenList) # total number of datapoints, used for getting %
    for ramen in ramenList: # iterate thru list of datapoints from csv file
        if ramen.country in uniqueCountries: # if the country is already saved, just increment its frequency
            uniqueCountries[ramen.country] += 1
        else:
            #add the uncatalogued country to the list of country and set its count to 1
            uniqueCountries[ramen.country] = 1
    for country in uniqueCountries: # iterate thru the saved countries
        # compare frequency to total to get percentage
        uniqueCountries[country] = round(((uniqueCountries[country]/ramenCount)*100), 2) 
    sort = sorted(uniqueCountries.items(), key=lambda x: x[1], reverse=True) # sort it in decreasing order
    for country in sort: #then print in order
        print(country[0] + ": " + str(country[1]) + "%")
    

def question3(ramenList):
    print('3. What are the top 10 most popular ramen brands?')
    uniqueBrands = {} # Dictionary to hold brands and their frequency
    for ramen in ramenList: # iterate thru list of datapoints from csv file
        if ramen.brand in uniqueBrands: # if the brand is already saved, just increment its frequency
            uniqueBrands[ramen.brand] += 1
        else:
            #add the uncatalogued country to the list of country and set its count to 1
            uniqueBrands[ramen.brand] = 1
    sort = sorted(uniqueBrands.items(), key=lambda x: x[1], reverse=True) # sort it in decreasing order
    print(sort[:10]) # Print the top 10
    
def question4(ramenList):
    print('4. What are the top 10 ramen ratings?')
    uniqueStars = {} # Dictionary to hold stars and their frequency
    for ramen in ramenList:
        if str(ramen.stars) in uniqueStars:
            uniqueStars[str(ramen.stars)] += 1 # if the stars is already saved, just increment its frequency
        else:
            #add the uncatalogued stars to the list of stars and set its count to 1
            uniqueStars[str(ramen.stars)] = 1
    sort = sorted(uniqueStars.items(), key=lambda x: x[1], reverse=True)
    print(sort[:10])

def question5(ramenList):
    print('5. If you convert the variety column into a set of words, what are the top 20 most popular words in the column?')
    uniqueWords = {} # Dictionary to hold words and their frequency
    for ramen in ramenList:
        words = ramen.variety.split(' ') # Split variety column into list of words
        for word in words:
            if word in uniqueWords: #if the word is already saved, just increment its frequency
                uniqueWords[word] += 1
            else:
                #add the uncatalogued word to the list of words and set its count to 1
                uniqueWords[word] = 1

    print(getLargestInDict(uniqueWords, 20))

def question6(ramenList):
    print('6. What are the top 10 brands with the best average score?')
    uniqueBrands = {} # Dictionary to hold brands and their frequency
    for ramen in ramenList:
        if ramen.stars == "Unrated": # there are 3 datapoints without ratings. Pass over these
            pass
        else:
            if ramen.brand in uniqueBrands: # if the brand is already saved, just adjust its average
                uniqueBrands[ramen.brand] = (float(uniqueBrands[ramen.brand]) + float(ramen.stars)) / 2
            else: # add the brand to the dictionary and set its average score
                uniqueBrands[ramen.brand] = float(ramen.stars)
    sort = sorted(uniqueBrands.items(), key=lambda x: x[1], reverse=True)
    print(sort)


# Pass in a dictionary and the number of top results requested
def getLargestInDict(dictionary, count):
    largest = []
    for i in range(count):
        big = max(dictionary, key=dictionary.get) #get the key of the max value in the dict
        largest.append(big) 
        dictionary.pop(big) # remove that key value pair
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
    
