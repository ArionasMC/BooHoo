class Interpreter:
    def __init__(self, lines, space):
        self.lines = lines
        self.pos = [0, 0, 0]
        self.space = space
        self.stack = []
        self.loopMap = {} # key: position of '{', value: position of '}'

    def preScan(self):
        i = 0
        j = 0
        while i < len(self.lines):
            line = self.lines[i]
            for cmd in line:
                if cmd[0] == "#":
                    break

                if cmd == "bOo":
                    self.stack.append((i, j))
                    
                elif cmd == "HoO":
                    self.loopMap[self.stack[-1]] = (i, j)
                    self.stack.pop()

                j += 1

            i += 1
            j = 0
        print(self.loopMap)

    def run(self):
        i = 0 # line number
        j = 0 # command number in line
        jump = False # force change reading position
        jGoal = 0

        while i < len(self.lines):
            line = self.lines[i]

            for cmd in line:
                if jGoal >= len(line):
                    jGoal = 0
                    break
                if j < jGoal:
                    j += 1
                    continue
                jGoal = 0 

                # if a command string starts with # then it's a comment
                if cmd[0] == '#':
                    break

                #print((i,j),"executing",cmd, self.pos, self.space.read(self.pos))

                if cmd == "bOo":
                    if self.isLoopable():
                        j += 1
                        continue
                    else:
                        jump = True
                        pos = self.loopMap[(i, j)]
                        i = pos[0]
                        jGoal = pos[1] + 1
                        break
                elif cmd == "HoO":
                    jump = True
                    pos = list(self.loopMap.keys())[list(self.loopMap.values()).index((i, j))]
                    i = pos[0]
                    jGoal = pos[1]
                    break
                else:
                    self.executeCommand(cmd)
                
                j += 1
 
            j = 0
            if not jump:
                i += 1
            jump = False

    def executeCommand(self, cmd):

        if cmd == "pos":
            print("pos=",self.pos,"value=",self.space.read(self.pos))
            return

        if cmd == "BOO":
            print(self.space.read(self.pos))
            return
        elif cmd == "HOO":
            x = int(input())
            self.space.insert(self.pos, x)
            return
        
        match cmd[0]:
            case 'h':
                self.pos[0] += self.getCmdLen(cmd)
            case 'b':
                if cmd[1].islower():
                    self.pos[2] += self.getCmdLen(cmd)
                else:
                    self.space.increase(self.pos, self.getCmdLen(cmd))
            case 'B':
                self.pos[1] += self.getCmdLen(cmd)
            case 'H':
                if cmd[1].isupper() and cmd[2:].islower():
                    self.space.increase(self.pos, -self.getCmdLen(cmd))
                elif cmd[1:].islower():
                    self.pos[1] -= self.getCmdLen(cmd)
            case 'o':
                if cmd[-1] == 'h':
                    self.pos[0] -= self.getCmdLen(cmd)
                elif cmd[-1] == 'b':
                    self.pos[2] -= self.getCmdLen(cmd)
            case _:
                print(cmd, "is not a valid command!")
    
    def executeList(self, l):
        for cmd in l:
            self.executeCommand(cmd)

    def getCmdLen(self, cmd):
        return max(len(cmd)-2, 1)
    
    def getPos(self):
        print(self.pos, self.space.read(self.pos))

    def isLoopable(self):
        return self.space.read(self.pos) > 0
