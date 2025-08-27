#!/usr/bin/env python3
import os
import re
import glob

def fix_frontmatter(file_path):
    """Fix frontmatter issues in markdown files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        return False
    
    # Find the end of frontmatter
    frontmatter_end = content.find('---', 3)
    if frontmatter_end == -1:
        return False
    
    frontmatter = content[:frontmatter_end + 3]
    body = content[frontmatter_end + 3:]
    
    # Fix the figures array issue
    if 'figures: []' in frontmatter and '- path:' in frontmatter:
        # Replace the malformed figures section
        pattern = r'figures: \[\].*- path:.*?license: "internal-copy"\n'
        replacement = '''figures:
  - path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-collaboration/71bc45159c09.webp"
    caption: "light logo"
    credit_name: "docs.crewai.com"
    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
    license: "internal-copy"
  - path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-collaboration/71bc45159c09.webp"
    caption: "dark logo"
    credit_name: "docs.crewai.com"
    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
    license: "internal-copy"
'''
        
        # Use a more specific pattern to match the entire malformed section
        lines = frontmatter.split('\n')
        new_lines = []
        in_figures = False
        skip_until_updatedAt = False
        
        for line in lines:
            if line.strip() == 'figures: []':
                in_figures = True
                new_lines.append('figures:')
                continue
            
            if in_figures and line.strip().startswith('- path:'):
                if not skip_until_updatedAt:
                    new_lines.append('  - path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-collaboration/71bc45159c09.webp"')
                    new_lines.append('    caption: "light logo"')
                    new_lines.append('    credit_name: "docs.crewai.com"')
                    new_lines.append('    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"')
                    new_lines.append('    license: "internal-copy"')
                    new_lines.append('  - path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-collaboration/71bc45159c09.webp"')
                    new_lines.append('    caption: "dark logo"')
                    new_lines.append('    credit_name: "docs.crewai.com"')
                    new_lines.append('    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"')
                    new_lines.append('    license: "internal-copy"')
                    skip_until_updatedAt = True
                continue
            
            if skip_until_updatedAt and line.strip().startswith('updatedAt:'):
                skip_until_updatedAt = False
                new_lines.append(line)
            elif not skip_until_updatedAt:
                new_lines.append(line)
        
        fixed_frontmatter = '\n'.join(new_lines)
        fixed_content = fixed_frontmatter + body
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        return True
    
    return False

def main():
    """Fix all markdown files in the sources directory"""
    source_files = glob.glob('sources/**/*.md', recursive=True)
    fixed_count = 0
    
    for file_path in source_files:
        if fix_frontmatter(file_path):
            print(f"Fixed: {file_path}")
            fixed_count += 1
    
    print(f"Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
