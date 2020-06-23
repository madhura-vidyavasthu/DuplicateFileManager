class ConsoleWrite:

    def showDuplicates(filecontent_grp):
        print("Duplicate Files")
        for _, files in filecontent_grp.items():
            for file in files:
                print(file)
            print()