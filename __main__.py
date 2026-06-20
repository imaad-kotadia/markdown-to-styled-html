import sys
import modules.parser as parse

if __name__ == "__main__":
    print("markdown-to-styled-html v1.0.0")

    parser = parse.createParser()
    parser.add_argument("mandatory", type=str, help="This argument is required")
    parser.add_argument("optional", type=str, nargs="?", default="default_value", help="This argument is optional")

    keyword_flags = {}

    if len(sys.argv) == 1:
        args, keyword_flags = parse.parserInput()
    else: 
        args, keyword_flags = parse.scriptInput()

    # 4. Print results
    print(f"Mandatory: {args.mandatory}")
    print(f"Optional:  {args.optional}")
    print(f"Custom Flags: {keyword_flags}")