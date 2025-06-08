# Write a test that checks if the output file contains expected HTML
import subprocess
import os

def test_markdown_to_html():
  md_file = "test.md"
  html_file = "test.html"
  with open(md_file, "w") as f:
    f.write("# Hello\n\nThis is **bold** text.")
  subprocess.run(["python3", "file_converter.py", "markdown", md_file, html_file])
  assert os.path.exists(html_file)
  with open(html_file) as f:
    html = f.read()
    assert "<h1>Hello</h1>" in html
    assert "<strong>bold</strong>" in html
  os.remove(md_file)
  os.remove(html_file)

if __name__ == "__main__":
  test_markdown_to_html()
  print("Test passed!") 