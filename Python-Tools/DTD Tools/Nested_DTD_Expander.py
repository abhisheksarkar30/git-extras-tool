def main():
    mainFile = input("Enter main DTD name: ")
    try:
        originalFile = open(mainFile + ".dtd", "r")
        expandedFile = open(mainFile + "_expanded.dtd", "w+")
        linkNestedDtd(originalFile, expandedFile)
        expandedFile.close()
        print("Expanded dtd file generated: " + expandedFile.name)
    except Exception as e:
        print(e)
        input("Exception! Halt...")

def linkNestedDtd(originalFile, expandedFile):
    content = originalFile.readlines()
    for line in content:
        if "ENTITY" in line:
            linkedFile = open(line[line.find('\"')+1:line.rfind('\"')], "r")
            linkNestedDtd(linkedFile, expandedFile)
            expandedFile.write('\n')
        else:
            expandedFile.write(line)

if __name__ == "__main__":
    main()
