# TuringPy
A tiny python module for prototyping Turing Machine logic in python.

## Installing

Just clone / download the module, import it, and go!

## Writing Code for Turing Machines

Obviously, in order to write code that could *"port"* to a turing machine, we have to impose some limits on ourselves.
Here is a rough "rule-of-thumb" type list of *dos* and *don'ts* for writing TM logic,

- ***DO:*** use the `Tape` class for all your data structure needs!
- ***DO:*** write subroutines (functions), each is its own TM that can be called from another TM!
- ***DO:*** write any kind of loop or conditional
- ***DO:*** use variables to reference tapes and symbols
- ***DO:*** declare new objects! As long as they internally follow all these rules, there's no reason you cant!
- ***DO:*** write non-deterministic TMs using threads / subprocesses! (if you're *nasty* nasty)

</br>

- ***DON'T:*** use python primitives other than strings, no arithmetic allowed!
- ***DON'T:*** use python data structures like `list`, `tuple` or `dict`!

</br>

If you're a *true* masochist, looking to write p u r e Turing Machine logic, try using only the `reads` and `writes` methods on the `Tape` class.

## Tape Class

The `Tape` class defines a data structure that imitates the infinite tape of a turing machine and the primitive
operations permitted in a "pure" turing machine implementation.

Each `Tape` object stores its contents and the current position of the read/write head.


### Primitive Operations

```python
tape = Tape("my initial string!") # create a new tape with initial content
tape.read()                       # read a symbol from the tape
tape.write("b")                   # write a symbol from the tape  
tape.step()                       # move to the right on the tape
tape.reads()                      # read symbol at current position, then move to the right
tape.writes()                     # write symbol at current position, then move to the right
```

> [!NOTE]
> All the "traversal" methods (ones that move the current position) accept a `reverse (bool)` argument, allowing you to move to the left instead.

### Extensions 
The following are a collection of methods that aren't strictly part of the theoretical turing machine but are implemented for syntactic sugar / convenience.

### Scanning
Since many TM algorithms involve things like *"Read symbols from tape until **\<CONDITION\>**"*, 
I've implemented a method called `scan()` that returns an infinite generator that yields the tapes contents 
(starting from the current position),

```python
for sym in tape.scan():
    if sym == tape.BLANK: break
    ...
```

which is equivalent to,

```python
while True:
    sym = tape.read()
    if sym == tape.BLANK: break
    ...
    tape.step()
```

> [!IMPORTANT]
> The `scan` method is implemented as an *infinite generator*, meaning that using in a for loop will continue 
> indefinitely unless you specify an explicit `break` condition (like the above example).

### Copying

I've also implemented a `copy()` method that creates a new tape identical to another (including current position).
I've "cheated" by accessing the inner data structure directly, but a fun(?) exercise is to implement this behaviour using only the primitive operations. (Hint: try doing it without preserving positions first, then think about how you'd save/load the position of a tape)

```python
tape = Tape("my tape!")
tape.step()
tape.step()

cp = tape.copy()

print(repr(tape))         # -> Tape("my tape!", 2)
print(repr(cp))           # -> Tape("my tape!", 2)
```

### Resetting

Just a very simple method that returns the head to the position it was in when you initialised the object. 
(another implementation that's "cheating" here, another opportunity for you to implement it yourself!)

```python
tape = Tape("abcdefg")
tape.reads()            # -> "a"
tape.reads()            # -> "b"
tape.reads()            # -> "c"
tape.reads()            # -> "d"
tape.reset()            # RESET POSITION
tape.reads()            # -> "a"
```

## Example Program - Looking for Duplicate Symbols

```python
def no_dupes(tape: Tape) -> bool:
    seen = Tape()

    for sym in tape.scan():
        if sym == tape.BLANK: return True # ACCEPT
        seen.reset()
        for seen_sym in seen.scan():
            if seen_sym == tape.BLANK:
                seen.write(sym)
                break
            if seen_sym == sym: return False # REJECT
```
