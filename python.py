score=0

def quiz():
    print(" Which company manufactures the “Mustang” car?")
print("A. Ford")
print("B. BMW")
print("C. Toyota")
print("D. Honda")

answer=input("enter your answer").strip()
if (answer=="Ford"or answer=="A"):
    print("congrasulation you get 1 point sir")
    score += 1
else:
    print("you lose 1 point good luck for next question")

print(" What is used to color the eyelids?")

print("A. Eyeshadow")
print("B. Blush")
print("C. Concealer")
print("D. Primer")

answer_2=input("enter your 2nd answer").strip()
if(answer_2=="Eyeshadow" or answer_2=="A"):
    print("you get 1 point")
    score += 1
else:
    print("you lose it")



print("Which country is known as the Land of the Rising Sun?")

print("A. China")
print("B. Japan")
print("C. Korea")
print("D. Thailand")
answer_3=input("enter your answer").strip()
if(answer_3=="Japan" or answer_3=="B"):
    print("you get 1 point")
    score += 1
else:
    print("you lose it")

print("final score= ",score,"/3")
import sys
sys.exit()

quiz()