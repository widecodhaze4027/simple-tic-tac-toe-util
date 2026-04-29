"""
Tic Tac Toe - Main module.
"""
import sys

VERSION = "0.2.0"

def run(args):
    """Main entry point."""
    print(f"Tic Tac Toe v{VERSION}")
    if args:
        print(f"Processing: {', '.join(args)}")
        process(args)
    else:
        print("Usage: python tic.py [arguments]")
        print("Try: python tic.py --help")

def process(args):
    """Process input arguments."""
    items = []
    for arg in args:
        result = arg.strip()
        if result:
            items.append(result)
            print(f"  Processed: {result}")
    print(f"\nTotal: {len(items)} items processed")
    return items

def main():
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
