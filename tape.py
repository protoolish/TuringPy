class Tape:
    BLANK=" "

    def __init__(self, tape_string = ""):
        self.__pos = 0
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        if not len(self.__tape): return " "
        min_idx = min(self.__tape.keys())
        max_idx = max(self.__tape.keys())
        return "".join(self.__readi(i) for i in range(min_idx, max_idx + 1))
    
    def __readi(self, idx):
        return self.__tape.get(idx, self.BLANK)
    
    def reset(self): 
        self.__pos = 0
    
    def step(self, reverse=False):
        if reverse:
            self.__pos -= 1
        else:
            self.__pos += 1
        # print("STEPPED to:", self.__pos)
    
    def read(self):
        return self.__readi(self.__pos)
    
    def reads(self, reverse=False) -> str:
        ''' read value from the tape and step (by default, to the right) '''
        val = self.read()
        self.step(reverse)
        return val
    
    def write(self, char):
        self.__tape[self.__pos] = char

    def writes(self, char: str, reverse=False):
        ''' write a string to the tape and step (by default, to the right) '''
        self.write(char)
        self.step(reverse)

    def scan(self, reverse=False):
        while True: 
            yield self.read()
            self.step(reverse)

    def print(self):
        print(self)
        print(" "*self.__pos+"^")

    def debug(self, verbose=False):
        if verbose: return self.__repr__()
        return str(self), self.__pos

    def __repr__(self):
        return {
            "tape": self.__tape,
            "pos": self.__pos
        }
    
    def __eq__(self, other):
        assert isinstance(other, Tape)
        return str(self).strip() == str(other).strip()

