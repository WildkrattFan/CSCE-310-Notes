from random import randint
import json

# Global variables
exDict = []
word = ""

# Load words from the JSON file into a list
def load_words(filename):
    with open(filename, 'r') as file:
        data = json.load(file)  # Load the JSON data
        return list(data.keys())  # Return the list of words as a list

def firstGuess():
    global word  # Declare word as global to access the chosen word
    wordSoFar = [' ', ' ', ' ', ' ', ' ']  # Use blank spaces consistently
    lettersIn = []
    
    guessWord = "joilt"  # Replace this with user input or your guess logic
    guessPointer = 0

    while guessPointer < 5:
        # Green letter guess (exact match)
        if guessWord[guessPointer] == word[guessPointer]:
            wordSoFar[guessPointer] = guessWord[guessPointer]
        else:
            # Yellow letter guess (letter in word but wrong position)
            if guessWord[guessPointer] in word and guessWord[guessPointer] not in wordSoFar:
                lettersIn.append(guessWord[guessPointer])
        guessPointer += 1

    print("Initial guess result:", lettersIn, " ", wordSoFar)  # Print the result for the first guess
    return lettersIn, wordSoFar

def checkGuess(guessWord):
    global word  # Declare word as global to access the chosen word
    wordSoFar = [' ', ' ', ' ', ' ', ' ']  # Use blank spaces consistently
    lettersIn = []
    
    guessPointer = 0
    print("Checking", guessWord, "for", word)

    while guessPointer < 5:
        # Green letter guess (exact match)
        if guessWord[guessPointer] == word[guessPointer]:
            wordSoFar[guessPointer] = guessWord[guessPointer]
        else:
            # Yellow letter guess (letter in word but wrong position)
            if guessWord[guessPointer] in word and guessWord[guessPointer] not in wordSoFar:
                lettersIn.append(guessWord[guessPointer])
        guessPointer += 1

    print("Check result:", lettersIn, " ", wordSoFar)  # Print the result for the guess
    return lettersIn, wordSoFar  # Return both for further processing

def filter_candidates(candidate_words, lettersIn, wordSoFar):
    filtered_candidates = []

    for currentWord in candidate_words:
        if len(currentWord) != 5:  # Only process 5-letter words
            continue  # Skip invalid word lengths

        # Check if current word has all letters in lettersIn
        hasAllLetters = all(letter in currentWord for letter in lettersIn)

        # Check positions of letters in wordSoFar
        meetsAll = True

        if hasAllLetters:
            for k in range(5):
                if wordSoFar[k] != ' ':  # Compare against blank space now
                    if wordSoFar[k] != currentWord[k]:
                        meetsAll = False  # Set to False if any position does not match
                        break

            if meetsAll:
                filtered_candidates.append(currentWord)

    return filtered_candidates  # Return filtered candidate words

def guess(lettersIn, wordSoFar, candidate_words):
    for currentWord in candidate_words:
        return checkGuess(currentWord)  # Check the first valid candidate word found

    return "No valid word found"  # Return a valid result at the end

def Main():
    global exDict, word  # Declare as global to modify these variables
    exDict = load_words('other/words_dictionary.json')  # Update with the correct path to your JSON file

    # Ensure the selected word is five letters long
    valid_words = [w for w in exDict if len(w) == 5]
    if not valid_words:
        print("No valid 5-letter words found.")
        return

    word = valid_words[randint(0, len(valid_words) - 1)]
    
    print("Selected word:", word)  # Debug: print the chosen word

    lettersIn, wordSoFar = firstGuess()  # Get initial letters and positions
    attempts = 0  # Initialize attempts counter
    max_attempts = 10000  # Set a maximum number of attempts
    candidate_words = valid_words.copy()  # Make a copy of valid words to use as candidates

    last_invalid_index = -1  # Track the last index of the invalid guess

    while attempts < max_attempts:
        # If last_invalid_index is set, filter candidate words to only include those after that index
        if last_invalid_index != -1:
            candidate_words = candidate_words[last_invalid_index + 1:]  # Skip words before last invalid guess

        result = guess(lettersIn, wordSoFar, candidate_words)
        if result == "No valid word found":
            print(result)
            break  # Exit if no valid words are found
        
        lettersIn, wordSoFar = result  # Update lettersIn and wordSoFar for the next guess

        # Store the current guess index for filtering
        last_invalid_index = candidate_words.index(lettersIn) if lettersIn in candidate_words else last_invalid_index
        
        # Filter candidates based on the current guess results
        candidate_words = filter_candidates(candidate_words, lettersIn, wordSoFar)
        attempts += 1

    if attempts == max_attempts:
        print("Reached maximum attempts without finding the word.")

Main()
