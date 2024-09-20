
class Symbol:
    """Class representing a symbol on the tape of a turing machine.
    - Wraps a single character string that can be obtained by casting to string
    - Implements __eq__ with other symbols and strings (so can be compared with literals)
    """

    __slots__ = ('_sym',)

    def __init__(self, sym: str):
        if not isinstance(sym, str) or len(sym) != 1:
            raise ValueError("Symbol must be a single character")
        self._sym = sym

    @classmethod
    def create(cls, sym):
        if isinstance(sym, Symbol):
            return sym
        elif sym is None:
            return BlankType()
        else:
            return cls(sym)

    def is_blank(self):
        return False

    def __repr__(self): 
        return f"Symbol('{self._sym}')"
    
    def __str__(self):
        return self._sym

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self._sym == other._sym
        elif isinstance(other, str) and len(other) == 1:
            return self._sym == other
        else:
            return False

class BlankType(Symbol):
    """Special-case singleton instance of Symbol class. 
    - Represents a blank spot on the tape.
    - __str__ method returns a space " " for printing.
    - Implemented as a singleton for memory efficiency.
    """

    __slots__ = ()

    _instance = None # Singleton instance

    def __new__(cls):
        if cls._instance is None:

            instance = super().__new__(cls)
            cls._instance = instance

            super(Symbol, instance).__setattr__("_sym", None)
        return cls._instance

    def __init__(self): pass

    def is_blank(self):
        return True

    def __repr__(self):
        return "Symbol(<blank>)"
    
    def __str__(self):
        return " "
    
    def __eq__(self, other):
        if isinstance(other, BlankType):
            return True
        elif isinstance(other, Symbol):
            return other._sym is None
        else:
            return False
        
Blank = BlankType()
        

if __name__ == "__main__":
    def bf(s): return f"\033[1m{s}\033[0m"

    title = "+" + " Symbol Module ".center(25, "=") + "+"
    print("\n"+bf(title)+"\n")

    print(f" {bf('__repr__'):<23} | {bf('__str__')}")
    print("-"*17 + "+" + "-"*9)
    for i in ('a', 'A', '1', None):
        s = Symbol.create(i)
        print(f" {repr(s):<15} | {repr(str(s)):^7}")

    print()