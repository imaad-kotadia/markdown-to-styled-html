import argparse
import sys


def createParser():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("mandatory", type=str, help="Path to the Markdown file")
    parser.add_argument(
        "optional",
        type=str,
        nargs="?",
        default="default_value",
        help="Path to the CSS file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.html",
        help="Path to the output HTML file",
    )
    return parser


def parserInput(parser):
    md_file = input("Enter .md file: ").strip()
    css_file = input("Enter css styling (Press Enter to skip): ").strip()
    out_file = input("Enter output file name (Press Enter to skip): ").strip()

    simulated_args = [md_file]
    if css_file:
        simulated_args.append(css_file)
    if out_file:
        simulated_args.extend(["--output", out_file])

    args, _ = parser.parse_known_args(simulated_args)

    keyword_flags = {}
    print("\n--- Add Custom Flags (Optional) ---")
    while True:
        key = input("Enter flag name (or press Enter to finish): ").strip().lstrip("-")
        if not key:
            break
        val = input(f"Enter value for '{key}': ").strip()
        keyword_flags[key] = val if val else True

    return args, keyword_flags


def scriptInput(parser):
    args, unknown_flags = parser.parse_known_args()

    keyword_flags = {}
    for i in range(0, len(unknown_flags), 2):
        flag = unknown_flags[i].lstrip("-")
        value = (
            unknown_flags[i + 1]
            if (i + 1 < len(unknown_flags) and not unknown_flags[i + 1].startswith("-"))
            else True
        )
        keyword_flags[flag] = value

    return args, keyword_flags


def getInput():
    parser = createParser()
    if len(sys.argv) == 1:
        return parserInput(parser)
    return scriptInput(parser)