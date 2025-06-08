import sys # For command-line argument handling
import markdown # For converting markdown into HTML
import os # For file existence checks

# Help message shown with -help flag
HELP_TEXT = """
Usage:
  python3 file_converter.py markdown <input_file.md> <output_file.html>
  python3 file_converter.py -help

Options:
  markdown   Convert Markdown file to HTML.
  -help      Show this help message.
"""

# CSS styling for the HTML output
CSS_STYLE = """
body {
  font-family: Arial, sans-serif;
  margin: 2em;
  background: #f9f9f9;
  color: #222;
}

h1, h2, h3, h4, h5, h6 {
  color: #2a5d9f;
}

pre {
  background: #eee;
  padding: 1em;
  border-radius: 5px;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #ccc;
  padding: 0.5em;
}
"""

def print_help():
  """Print the help message."""
  print(HELP_TEXT)

def is_valid_command(args):
  """
  Validate command-line arguments
  Returns True if valid, otherwise prints error/help and returns False.
  """
  if len(args) == 2 and args[1] == '-help':
    print_help()
    return False
  
  if len(args) != 4:
    print("Invalid number of arguments.")
    print_help()
    return False
  
  if args[1] != 'markdown':
    print("Invalid command. Supported command: markdown")
    print_help()
    return False
  
  if not args[2].endswith('.md'):
    print("Input file must be an markdown file with .md extension.")
    return False
  
  if not args[3].endswith('.html'):
    print("Output file must be an HTML file with .html extension.")
    return False
  
  if not os.path.exists(args[2]):
    print(f"Input file '{args[2]}' does not exist.")
    return False
  return True

def convert_markdown_to_html(md_path, html_path):
  """
  Convert a markdown file to a styled HTML file.
  Wraps the HTML in a full <html><head><body> block and applies CSS.
  """
  try:
    with open(md_path, "r") as md_file:
      markdown_content = md_file.read()
      # Convert markdown to HTML with extra features
      html_body = markdown.markdown(
        markdown_content, 
        extensions=['extra', 'tables', 'fenced_code']
      )
      # Compose the full HTML document
      full_html = f"""
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="utf-8">
          <title>Converted markdown</title>
          <style>{CSS_STYLE}</style>
        </head>
        <body>
        {html_body}
        </body>
      </html>
      """
      with open(html_path, "w") as html_file:
        html_file.write(full_html)
      print(f'Converted {md_path} to {html_path} successfully.')
  except Exception as e:
    print(f"Error during conversion: {e}")

if __name__ == "__main__":
  # Only proceed if arguments are valid
  if not is_valid_command(sys.argv):
    sys.exit(1)
  if sys.argv[1] == 'markdown':
    convert_markdown_to_html(sys.argv[2], sys.argv[3])