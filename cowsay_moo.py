##Start from this, merge some of the text of figlet_1 into there so we can finish it off. STOP EPICING ON HOMEWORK
from pyfiglet import Figlet
import random
import sys
import cowsay
def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        x = input("Input: ")
        y = random.choice(figlet.getFonts())
        figlet.setFont(font = y)
        sys.stdout = open('/workspaces/147750595/cs50_python/week_4_class/cow.txt', 'w')
        cowsay.cow(f"{figlet.renderText(x)}")
        sys.stdout.close()
    if len(sys.argv) >= 2 and sys.argv[1] in ["-f","-font"] and sys.argv[2] in figlet.getFonts():
        #w = open("cow.txt", "w")
        a = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        sys.stdout = open('/workspaces/147750595/cs50_python/week_4_class/cow.txt', 'w')
        cowsay.cow(f"{figlet.renderText(a)}")
        sys.stdout.close()
    else: sys.exit("Invalid Usage")


main()
