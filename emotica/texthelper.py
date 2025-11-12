import sys
import time
import textwrap

def slow_print(text, delay=0.03, width=70):
    wrapped_text = textwrap.fill(text, width=width)  # wrap lines at `width`
    for line in wrapped_text.split('\n'):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # go to next line after each wrapped line

def wait():
    input("\n(Press Enter to continue...)\n")
    
def slowprint(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def prompt(options):
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        c = input("> ").strip()
        if c.isdigit() and 1 <= int(c) <= len(options):
            return int(c) - 1
        else:
            print("Enter a valid number.")

def clamp(v, lo, hi): 
    return max(lo, min(v, hi))

