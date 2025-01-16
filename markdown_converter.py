#!/usr/bin/env python3

import argparse
import markdown
import sass
import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class MarkdownConverter:
    def __init__(self, template_dir="templates"):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))
        
    def compile_sass(self, sass_file):
        """Compile SASS to CSS"""
        if not os.path.exists(sass_file):
            return ""
        return sass.compile(filename=sass_file)
    
    def convert(self, markdown_file, output_file, sass_file=None, title=None):
        """Convert markdown to HTML with optional styling"""
        # Read markdown content
        with open(markdown_file, 'r') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(
            md_content,
            extensions=['fenced_code', 'tables', 'toc']
        )
        
        # Compile SASS if provided
        css_content = self.compile_sass(sass_file) if sass_file else ""
        
        # Render template
        template = self.env.get_template('base.html')
        output = template.render(
            content=html_content,
            css=css_content,
            title=title or Path(markdown_file).stem
        )
        
        # Write output
        with open(output_file, 'w') as f:
            f.write(output)
        
        return output_file

def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown to styled HTML documents'
    )
    parser.add_argument(
        'input',
        help='Input markdown file'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output HTML file (default: input_file.html)',
        default=None
    )
    parser.add_argument(
        '-s', '--style',
        help='SASS style file to apply',
        default=None
    )
    parser.add_argument(
        '-t', '--title',
        help='Document title',
        default=None
    )
    parser.add_argument(
        '--template-dir',
        help='Directory containing HTML templates',
        default='templates'
    )
    
    args = parser.parse_args()
    
    # Set default output filename if not provided
    if not args.output:
        args.output = str(Path(args.input).with_suffix('.html'))
    
    # Create converter and process file
    converter = MarkdownConverter(template_dir=args.template_dir)
    output_file = converter.convert(
        args.input,
        args.output,
        args.style,
        args.title
    )
    print(f"Created {output_file}")

if __name__ == '__main__':
    main()