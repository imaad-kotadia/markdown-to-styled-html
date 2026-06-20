import argparse
import sys

def createParser():
    return argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

def parserInput(parser):    
    user_mandatory = input("Enter .md file: ").strip()
    user_optional = input("Enter css styling (Press Enter to skip): ").strip()
    keyword_flags = {}
    
    # If they skipped the optional one, don't pass it to the list
    if user_optional:
        simulated_args = [user_mandatory, user_optional]
    else:
        simulated_args = [user_mandatory]
        
    # Overwrite the empty system arguments with our manual list
    args, _ = parser.parse_known_args(simulated_args)

    print("\n--- Add Custom Flags (Optional) ---")
    while True:
        key = input("Enter flag name (or press Enter to finish): ").strip().lstrip("-")
        if not key:
            break
        val = input(f"Enter value for '{key}': ").strip()
        keyword_flags[key] = val if val else True  # Store True if value is skipped
    return args, keyword_flags
    
def scriptInput(parser):
    args, unknown_flags = parser.parse_known_args()

    # 3. Convert remaining arbitrary flags into a clean dictionary
    keyword_flags = {}
    for i in range(0, len(unknown_flags), 2):
        flag = unknown_flags[i].lstrip("-")  # Remove the dashes
        value = unknown_flags[i+1] if i+1 < len(unknown_flags) else True
        keyword_flags[flag] = value
    return args, keyword_flags

def getInput():
    parser = createParser()
    parser.add_argument("mandatory", type=str, help="This argument is required")
    parser.add_argument("optional", type=str, nargs="?", default="default_value", help="This argument is optional")

    keyword_flags = {}

    if len(sys.argv) == 1:
        args, keyword_flags = parserInput(parser)
    else: 
        args, keyword_flags = scriptInput(parser)
    return args, keyword_flags