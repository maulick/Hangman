import random

word_list = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")

random_words = random.choice(word_list)

a = set()
b = set()
lives = 0

while lives < 8:

    for i in range(0,8):
        print("\n",end = "")
        for j in random_words:
            if j in a:
                print(j,end = "")
                #word = j.append()
            else:
                print('-',end = "")

        letter = input("\nInput a  letter :")

        if letter not in random_words:
            print("No such letter in the word")
            lives += 1
        else:
            a.add(letter)
            print("No improvements")
            lives += 1
        
        
print(word)
