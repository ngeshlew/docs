#!/usr/bin/env python3
"""
Script to parse Nielsen Norman Group articles and convert them to markdown format
"""

import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_nng_article(html_file, url):
    """
    Parse the NN/g article HTML and convert to markdown
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the main article content
        # NN/g articles are typically in article tags or specific divs
        article_content = soup.find('article') or soup.find('main')
        
        if not article_content:
            # Look for content in specific divs
            article_content = soup.find('div', class_='article-content') or \
                            soup.find('div', class_='content') or \
                            soup.find('div', class_='post-content') or \
                            soup.find('div', class_='blog-content') or \
                            soup.find('div', class_='entry-content')
        
        if not article_content:
            print("Could not find article content")
            return None
        
        # Extract title
        title = soup.find('h1') or soup.find('title')
        title_text = title.get_text().strip() if title else "NN/g Article"
        
        # Extract text content
        content_parts = []
        images = []
        
        # Process all content elements
        for element in article_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'blockquote', 'pre', 'code', 'figure', 'img']):
            if element.name == 'img':
                # Handle images
                src = element.get('src')
                if src:
                    if not src.startswith('http'):
                        src = urljoin(url, src)
                    alt = element.get('alt', '')
                    caption = element.get('title', '')
                    
                    # Look for figcaption
                    figcaption = element.find_next_sibling('figcaption')
                    if figcaption:
                        caption = figcaption.get_text().strip()
                    
                    images.append({
                        'src': src,
                        'alt': alt,
                        'caption': caption
                    })
                    
                    # Add image markdown
                    content_parts.append(f'![{alt}]({src})')
                    if caption:
                        content_parts.append(f'<sub>{caption}</sub>')
                    else:
                        content_parts.append(f'<sub>Source: *Nielsen Norman Group*, NN/g Team (2025).</sub>')
                    content_parts.append('')
                    
            elif element.name == 'figure':
                # Handle figure elements (which contain images)
                img = element.find('img')
                if img:
                    src = img.get('src')
                    if src:
                        if not src.startswith('http'):
                            src = urljoin(url, src)
                        alt = img.get('alt', '')
                        
                        # Get caption from figcaption
                        figcaption = element.find('figcaption')
                        caption = figcaption.get_text().strip() if figcaption else ''
                        
                        content_parts.append(f'![{alt}]({src})')
                        if caption:
                            content_parts.append(f'<sub>{caption}</sub>')
                        else:
                            content_parts.append(f'<sub>Source: *Nielsen Norman Group*, NN/g Team (2025).</sub>')
                        content_parts.append('')
                        
            elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Handle headings
                level = int(element.name[1])
                heading_text = element.get_text().strip()
                if heading_text:
                    content_parts.append(f'{"#" * level} {heading_text}')
                    content_parts.append('')
                    
            elif element.name == 'p':
                # Handle paragraphs
                text = element.get_text().strip()
                if text:
                    content_parts.append(text)
                    content_parts.append('')
                    
            elif element.name == 'blockquote':
                # Handle blockquotes
                text = element.get_text().strip()
                if text:
                    content_parts.append(f'> {text}')
                    content_parts.append('')
                    
            elif element.name in ['ul', 'ol']:
                # Handle lists
                list_items = element.find_all('li')
                for item in list_items:
                    text = item.get_text().strip()
                    if text:
                        if element.name == 'ul':
                            content_parts.append(f'- {text}')
                        else:
                            content_parts.append(f'1. {text}')
                content_parts.append('')
                
            elif element.name == 'pre':
                # Handle code blocks
                code = element.get_text().strip()
                if code:
                    content_parts.append(f'```')
                    content_parts.append(code)
                    content_parts.append(f'```')
                    content_parts.append('')
                    
            elif element.name == 'code':
                # Handle inline code
                text = element.get_text().strip()
                if text:
                    content_parts.append(f'`{text}`')
        
        # Join all content parts
        content = '\n'.join(content_parts)
        
        return {
            'title': title_text,
            'content': content,
            'images': images
        }
        
    except Exception as e:
        print(f"Error parsing article: {e}")
        return None

def main():
    html_file = "new_article_52.html"
    url = "https://www.productcompass.pm/p/ai-product-management-learning-roadmap?open=false#%C2%A7fine-tuning"
    
    print("Parsing Product Compass article...")
    result = parse_nng_article(html_file, url)
    
    if result:
        print("Article parsed successfully!")
        print(f"Title: {result['title']}")
        print(f"Found {len(result['images'])} images")
        print(f"Content length: {len(result['content'])} characters")
        
        # Save to file
        with open('parsed_new_article_52.md', 'w', encoding='utf-8') as f:
            f.write(result['content'])
        
        print("Article saved to parsed_new_article_52.md")
        
        # Also print first 500 characters for verification
        print("\nFirst 500 characters of content:")
        print(result['content'][:500])
        
    else:
        print("Failed to parse article")

if __name__ == "__main__":
    main()
