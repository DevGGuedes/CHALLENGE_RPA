# project main file

import Utilities as DAO

def runAutomation(text):
    try:

        DAO.subjectQuery(text)

    except KeyboardInterrupt:
        print("Execution stopped manually...")

if __name__ == "__main__":

    print("Starting automation")

    while True:
        try:
            text = input("Enter text for search: ")

            break
        except ValueError:
            print("") ## 

    runAutomation(text)