word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Convert both words to lowercase
word1 = word1.lower()
word2 = word2.lower()

# Remove spaces
word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

# Sort the characters
word1 = sorted(word1)
word2 = sorted(word2)

# Compare the sorted characters
if word1 == word2:
    print("Both words are anagrams")
else:
    print("Both words are not anagrams")