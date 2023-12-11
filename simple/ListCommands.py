class ListFunctions:
    def __init__(self):
        self.ListValue = []
        
    def insert(self, index, value):
        self.ListValue.insert(index, value)

    def append(self, value):
        self.ListValue.append(value)
        
    def remove(self, value):
        self.ListValue.remove(value)

    def pop(self):
        self.ListValue.pop()

    def reverse(self):
        self.ListValue.reverse()

    def sort(self):
        self.ListValue.sort()

    def print(self):
        print(self.ListValue)

    def parseCommand(self, command, values):
        match command:
            case 'append':
                for value in values:
                    self.append(int(value))
            case 'insert':
                index = values[0]
                value = values[1]
                self.insert(int(index),int(value))
            case 'remove':
                for value in values:
                    self.remove(int(value))
            case 'pop':
                self.pop()
            case 'reverse':
                self.reverse()
            case 'sort':
                self.sort()
            case 'print':
                self.print()

if __name__ == '__main__':
    lf = ListFunctions()
    N = int(input())
    for _ in range(N):
        command, *line = input().split()
        lf.parseCommand(command, line)