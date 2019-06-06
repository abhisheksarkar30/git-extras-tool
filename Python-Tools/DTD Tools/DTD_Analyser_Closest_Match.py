from Levenshtein import distance
def main():
    dtd1 = input("Enter 1st DTD name: ")
    dtd2 = input("Enter 2nd DTD name: ")
    try:
        dtdFile1 = open(dtd1 + ".dtd", "r")
        dtdFile2 = open(dtd2 + ".dtd", "r")
        outFile = open(dtd1 + " vs " + dtd2 + ".txt", "w+")
        dtd1Elements = collectElements(dtdFile1)
        dtd2Elements = collectElements(dtdFile2)
        extrasInDtd1 = [x for x in dtd1Elements if x not in dtd2Elements]  # set(dtd1Elements) - set(dtd2Elements)
        extrasInDtd2 = [x for x in dtd2Elements if x not in dtd1Elements]  # set(dtd2Elements) - set(dtd1Elements)
        printList(outFile, extrasInDtd1, extrasInDtd2, dtd1)
        printList(outFile, extrasInDtd2, extrasInDtd1, dtd2)
        outFile.close()
        print("Dtd analysis file generated: " + outFile.name)
    except Exception as e:
        print(e)
        input("Exception! Halt...")

def collectElements(dtdFile):
    content = dtdFile.readlines()
    elements = []
    for line in content:
        if "ELEMENT" in line:
            elements.append(line[line.find(' ')+1:line.rfind('(')-1])
    elements.sort()
    return elements

def printList(outFile, content1, content2, dtd):
    outFile.write("==========================Extras in " + dtd + "=============================\n")
    for i in content1:
        exists = False
        for j in content2:
            dist = distance(i, j)
            if dist <= 2:
                outFile.write("%30s matches with %30s having distance %d\n" % (i, j, dist))
                exists = True
        if exists is False:
            outFile.write("%30s doesn't significantly match with any element\n" % i)
    outFile.write("\n\n")

if __name__ == "__main__":
    main()
