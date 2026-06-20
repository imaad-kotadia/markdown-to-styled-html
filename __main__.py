import modules.parser as parse

if __name__ == "__main__":
    print("markdown-to-styled-html v1.0.0")

    args, keyword_flags = parse.getInput()

    # 4. Print results
    print(f"Mandatory: {args.mandatory}")
    print(f"Optional:  {args.optional}")
    print(f"Custom Flags: {keyword_flags}")