def countWordsFromFile():
    fileName = input("Enter the file name: ")
    numberOfWords = 0
    #to open in read mode
    file = open(fileName,'r')
    #to split the words using whitespace
    for a in file:
        words = a.split()
        #len() in python which will give you the length of the list
        numberOfWords = numberOfWords + len(words)
    print('Number of words: ')
    print(numberOfWords)

#calling the function
countWordsFromFile()
