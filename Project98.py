print("Data Swapper")
file1 = input("Enter the name of the first file : ")
file2 = input("Enter the name of the second file : ")


def swapFileData() :
    with open(file1,"r") as openFile1:
        file1Data = openFile1.read()
    with open(file2,"r") as openFile2:
        file2Data = openFile2.read()
    with open(file1,"w") as openFile1:
        openFile1.write(file2Data)
    with open(file2,"w") as openFile2:
        openFile2.write(file1Data)
    print("Data Swapped Successfully")

swapFileData()