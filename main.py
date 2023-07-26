from Interpreter import Interpreter
from Space import Space

def parse(file, lines): 
    for line in file:
        line = line.split()
        lines.append(line)
        
if __name__ == "__main__":
    ext = ".boohoo"
    
    fileName = str(input("File name="))
    if not(ext in fileName):
        fileName = fileName+ext

    source = open(fileName, "r")
    
    lines = []
    parse(source, lines)
    
    space = Space([100, 100, 100])
    
    pr = Interpreter(lines, space)
    pr.preScan()
    pr.run()
    pr.getPos()
    
    
