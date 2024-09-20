from turingpy.tape import Tape
from turingpy.symbol import Blank

def no_dupes(tape: Tape) -> bool:
    seen = Tape()

    for sym in tape.scan():
        if sym is Blank: 
            break # ACCEPT
        seen.reset()

        for seen_sym in seen.scan():
            if seen_sym is Blank:
                seen.write(sym)
                break
            if seen_sym == sym:
                return False # REJECT
            
    return True

if __name__ == "__main__":
    rich_loaded = True
    try: from rich import print
    except ImportError: rich_loaded = False

    cases = [
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstavwxyz",
        "thequickbrownfxjmpdvlazyg",
        "the quick brown blah blah",
    ]

    for case in cases:
        tape = Tape(case)
        res = no_dupes(tape)
        msg = "" if res else f"(found duplicate '{tape.read()}')"
        for key, val in {
            "String:": f"{tape}",
            "No Dupes?:": f"{res} {msg}"
        }.items():

            if rich_loaded:
                print(f"[b]{key}[/] [i]{val}[/]")
            else:
                print(f"{key} {val}")