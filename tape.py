class Tape:
    """
    A data structure representing a (theoretically) infinite tape for a Turing machine or similar computational model.
    """

    BLANK = " "

    def __init__(self, tape_string = ""):
        """Initialise the tape with an optional initial string"""
        self._pos = 0
        self._tape = dict((enumerate(tape_string)))

    def _read_idx(self, idx) -> str:
        """PROTECTED function to read from specific index on the tape."""
        return self._tape.get(idx, self.BLANK)
    
    def reset(self):
        """Reset position of tape head to starting index (0)."""
        self._pos = 0
    
    def step(self, reverse=False):
        """Move the tape head one position to the right or left."""
        if reverse:
            self._pos -= 1
        else:
            self._pos += 1
    
    def read(self) -> str:
        """Read the character at the current position."""
        return self._read_idx(self._pos)
    
    def reads(self, reverse=False) -> str:
        """Read the character at the current position, then move the tape head.
        - READ equivalent of `writes()`. 
        - To read without moving, use `read()`.
        """
        val = self.read()
        self.step(reverse)
        return val
    
    def write(self, char: str):
        """Write a character to the current position."""
        self._tape[self._pos] = char

    def writes(self, char: str, reverse=False):
        """Write a character at current position, then move the tape head.
        - WRITE equivalent of `reads()`. 
        - To write without moving, use `write()`.
        """
        self.write(char)
        self.step(reverse)

    def scan(self, reverse=False):
        """Scan over tape, yielding each symbol as it goes (**Infinite** generator).

        - If you use it in a for loop, you must include a break/return to break the loop explicitly.
        """
        while True: 
            yield self.read()
            self.step(reverse)

    def copy(self) -> 'Tape':
        """ Return a copy of this tape, preserving position """
        cp = Tape()
        cp._pos = self._pos
        cp._tape = {k:v for k,v in self._tape.items()}
        return cp

    def pprint(self):
        """ Print a nice representation of the tape contents along with the current head position (as a ^). """
        if self._tape:
            min_idx = min(min(self._tape.keys()), self._pos)
            max_idx = max(max(self._tape.keys()), self._pos)
        else:
            min_idx = self._pos
            max_idx = self._pos

        tape_str = "".join(self._read_idx(i) for i in range(min_idx, max_idx+1))

        offset = self._pos - min_idx
        print(tape_str)
        print(" " * offset + "^")

    def __repr__(self):
        """ Return a string representing the tape object in the form: `Tape(tape, pos)`. """
        return f"Tape({self}, {self._pos})"

    def __str__(self):
        if not self._tape: return "<empty tape>"
        min_idx = min(self._tape.keys())
        max_idx = max(self._tape.keys())
        return "".join(self._read_idx(i) for i in range(min_idx, max_idx + 1))
    