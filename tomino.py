def main():
    import sys,random
    print("Ever seen some of the strange names used for characters in the Gundam franchise? Here's a program that can enerate some Tomino-esque names for you!")
    first=['Char','Paptimus','Allelujah','Bring','Biscuit','Jamiltov','Cinco','Quess','Bright','Philosopher','Haman','Job','Sleggar','Cucuruz','Garma','Ramba','Quattro','Bork','Descartes','Beecha','Madchar','Elpeo','Toraja','Mashymre','Gainer','Timp','Daba','Kacricon','Laraparly','Agrippa','Lockon','Regene','CHibodee','Gym','Yzak']
    last=['Zabi','Karn','Aznable','Scirocco','Haptism','Stabity','Griffon','Hymen','Benis','Paraya','Noa','Holyman','John','Law','Doan','Ral','Bajeena','Cry','Shaman','Oleg','Mucha','Ple','Toraja','Cello','Sanga','Sharon','Myroad','Cacooler','Madorna','Maintainer','Stratos','Regatta','Crocket','Ghingham','Joule']
    while True:
        firstName=random.choice(first)
        lastName=random.choice(last)
        print("\n\n")
        print("{} {}".format(firstName, lastName),file=sys.stderr)
        print("\n\n")
        try_again=input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower()=="n":
            break
    input("\nPress Enter to exit.")
if __name__=="__main__":
    main()
    