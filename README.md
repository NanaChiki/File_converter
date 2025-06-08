# File Converter 
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)

A Python command-line tool that converts Markdown files to beautifully styled HTML documents. Perfect for quickly creating web-ready content from your markdown files.

## Features
- 🧩 Help flag: `-help` flag for usage instructions.
- 🖼️ Full HTML output: Auto-wraps converted content in a complete HTML document.
- 🎨 CSS Styling: Adds clean, readable CSS to the HTML output.
- 🧪 Testing: Includes a test script to check conversion correctness.

## Requirements
- Python 3.7+
- [markdown](https://pypi.org/project/Markdown/) library

## Installation
1. Clone the repository:
```bash
git clone https://github.com/NanaChiki/File_converter.git
cd file_converter
```

2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip3 install markdown
```

## Usage
Convert a Markdown file to HTML:
```bash
python3 file_converter.py markdown input.md output.html
```

- input.md: Path to your Markdown file.
- output.html: Desired output HTML file name.

Show help message:
```bash
python3 file_converter.py -help
```

## Example 
Suppose you have a file called `sample.md`:
```markdown
# Hello world

This is **bold** and *italic* text.
```

Convert it to HTML:
```bash
python3 file_converter.py markdown sample.md sample.html
```

Open `sample.html` in your browser to see the styled result.

## Testing
A test script is included to verify the conversion process.

Run the test:
```bash
python3 test_file_converter.py
```

If successful, you will see:
```
Converted test.md to test.html successfully.
Test passed!
```

## Project Structure
```
file_converter/
├── examples/                 # Example files
│   ├── sample.md             # Example markdown file
│   └── sample.html           # Example HTML output
├── file_converter.py         # Main script
├── test_file_converter.py    # Test script
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Pull requests and issues are welcome! Please open an issue to discuss ideas or report bugs.

## Author
[Daito](https://github.com/NanaChiki)

## Acknowledgements
- [Python-Markdown](https://python-markdown.github.io/)
- Inspired by the need for quick Markdown-to-HTML conversion with style.
