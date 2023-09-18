# TASK 01 Write a recursive function that tests if a string is a palindrome, such as “kayak”, “never odd or even”
# or “Was it a car or a cat I saw?”



def palindrome(mot: str):
    mot = mot.lower()
    mot = mot.replace(" ", "")
    mot_inverse = mot[::-1]

    if mot == mot_inverse:
        print( "Ce mot est un palindrome" )
    else: 
        print("Ce mot n'est PAS un palindrome")

mot = input("Give me a word ")
palindrome(mot)

# TASK °2 
import os

DirPath = r"/home/olivierpakosz/introduction_seminar/"
result = os.walk(DirPath)
print(result)


