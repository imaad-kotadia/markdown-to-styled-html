import modules.md_css_linker as link
import modules.parser as parse

if __name__ == "__main__":
    print("markdown-to-styled-html v1.0.0\n" + "=" * 30)

    # 1. Parse inputs
    args, keyword_flags = parse.getInput()

    # 2. Process and merge files
    link.md_to_html(
        md_path=args.mandatory, css_path=args.optional, out_file=args.output
    )

    # 3. Print Execution Summary
    print("\n--- Execution Summary ---")
    print(f"Markdown File: {args.mandatory}")
    print(f"CSS Style:     {args.optional}")
    print(f"Output File:   {args.output}")
    if keyword_flags:
        print(f"Custom Flags:  {keyword_flags}")