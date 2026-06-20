import markdown

def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: file at {file_path} not found.")
        raise
    
def compile_html(md_content: str, css_content: str) -> str:
    html_body = markdown.markdown(md_content, extensions=["extra", "codehilite"])

    html_document = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Document</title>
    <style>
        {css_content}
    </style>
    </head>
    <body>
    <div class="markdown-body">
        {html_body}
    </div>
    </body>
    </html>"""
    return html_document

def write_file(content: str, out_path: str) -> None:
    """Writes the string content to the specified output file."""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

def md_to_html(md_path: str, css_path: str, out_file: str) -> None:
    """Merges a markdown file and a CSS file into a single standalone HTML file."""
    md_content = read_file(md_path)
    css_content = read_file(css_path)

    if not out_file: 
        out_file = "output.html"

    final_html = compile_html(md_content, css_content)

    write_file(final_html, out_file)
    print(f"Generated HTML at: {out_file}")