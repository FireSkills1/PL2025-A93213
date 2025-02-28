import sys
import os
import re

# Patterns and their replacements
patterns = [
    # Headers (e.g., # Header 1, ## Header 2, ...)
    (r'^(#{1,6}) (.+)$',
     lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>',
     re.MULTILINE),

    # Numbered lists (e.g., 1. Item)
    (r'((?:^\\d\\.\\s(.+)(?:\\n|$))+)',
     lambda m: '<ol>\\n' + ''.join(f'<li>{item.strip()}</li>\\n' for item in re.findall(r'^\\d\\.\\s(.+)', m.group(1), re.MULTILINE)) + '</ol>\\n',
     re.MULTILINE),

    # Bullet lists (e.g., - Item)
    (r'((?:^-\\s(.+)(?:\\n|$))+)',
     lambda m: '<ul>\\n' + ''.join(f'<li>{item.strip()}</li>\\n' for item in re.findall(r'^-\\s(.+)', m.group(1), re.MULTILINE)) + '</ul>\\n',
     re.MULTILINE),

    # Images (e.g., ![alt](url))
    (r'!\\[(.+)\\]\\((.+)\\)',
     lambda m: f'<img src=\"{m.group(2)}\" alt=\"{m.group(1)}\">',
     0),

    # Links (e.g., [text](url))
    (r'\\[(.+)\\]\\((.+)\\)',
     lambda m: f'<a href=\"{m.group(2)}\">{m.group(1)}</a>',
     0),

    # Horizontal rules (e.g., ---)
    (r'^(?:-{3,}|_{3,}|\\*{3,})$',
     lambda m: '<hr>',
     re.MULTILINE),

    # Bold text (e.g., **bold**)
    (r'\\*\\*(.+?)\\*\\*',
     lambda m: f'<b>{m.group(1)}</b>',
     0),

    # Italic text (e.g., *italic*)
    (r'\\*(.+?)\\*',
     lambda m: f'<i>{m.group(1)}</i>',
     0),

    # Inline code (e.g., `code`)
    (r'`(.+?)`',
     lambda m: f'<code>{m.group(1)}</code>',
     0),

    # Paragraphs
    (r'((?:^(?!\\s*$)(?!<\\/\\?\\w).+$\\n?)+)',
     lambda m: f'<p>{m.group(1).rstrip()}</p>',
     re.MULTILINE)
]


def convert_markdown_to_html(input_file: str) -> None:
    # Read markdown content
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Escape HTML tags
    content = content.replace('<', '&lt;').replace('>', '&gt;')

    # Apply patterns
    for pattern, replacement, flags in patterns:
        content = re.sub(pattern, replacement, content, flags=flags)

    # Prepare the output file path
    output_file = os.path.splitext(input_file)[0] + '.html'
    output_path = os.path.join(os.getcwd(), os.path.basename(output_file))

    # Write to HTML file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write('<!DOCTYPE html>\\n<html>\\n<body>\\n')
        file.write(content)
        file.write('\\n</body>\\n</html>\\n')

    print(f'Converted {input_file} to {output_path}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python markdown_to_html_converter.py <input.md>')
        sys.exit(1)
    convert_markdown_to_html(sys.argv[1])
