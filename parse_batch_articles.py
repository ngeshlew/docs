#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import html
import os

def parse_logrocket_article(soup, url):
    """Parse LogRocket article"""
    # Extract title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "LogRocket Article"
    
    # Find main content - LogRocket specific
    main_content = (soup.find('article') or 
                   soup.find('div', class_='post-content') or 
                   soup.find('div', class_='entry-content') or
                   soup.find('div', class_='content') or
                   soup.find('main') or
                   soup.find('div', {'data-testid': 'post-content'}) or
                   soup.find('div', class_='prose'))
    
    if not main_content:
        # Try to find any div with substantial text content
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 1000:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from  
> LogRocket Team, *LogRocket* (2025):  
> [{title}]({url})  
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://blog.logrocket.com')

def parse_nngroup_article(soup, url):
    """Parse Nielsen Norman Group article"""
    # Extract title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "NN/g Article"
    
    # Find main content - NN/g specific
    main_content = (soup.find('article') or 
                   soup.find('div', class_='article-body') or 
                   soup.find('div', class_='content') or
                   soup.find('main') or
                   soup.find('div', class_='post-content') or
                   soup.find('div', class_='entry-content'))
    
    if not main_content:
        # Try to find any div with substantial text content
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 1000:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from  
> Nielsen Norman Group, *NN/g* (2025):  
> [{title}]({url})  
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://www.nngroup.com')

def parse_codecademy_article(soup, url):
    """Parse Codecademy article"""
    # Extract title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Codecademy Article"
    
    # Find main content - Codecademy specific
    main_content = (soup.find('article') or 
                   soup.find('div', class_='article-content') or 
                   soup.find('div', class_='content') or
                   soup.find('main') or
                   soup.find('div', class_='post-content') or
                   soup.find('div', class_='entry-content'))
    
    if not main_content:
        # Try to find any div with substantial text content
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 1000:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from  
> Codecademy Team, *Codecademy* (2025):  
> [{title}]({url})  
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://www.codecademy.com')

def parse_technically_article(soup, url):
    """Parse Technically.dev article"""
    # Extract title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Technically Article"
    
    # Find main content - Technically specific
    main_content = (soup.find('article') or 
                   soup.find('div', class_='post-content') or 
                   soup.find('div', class_='content') or
                   soup.find('main') or
                   soup.find('div', class_='entry-content') or
                   soup.find('div', class_='prose'))
    
    if not main_content:
        # Try to find any div with substantial text content
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 1000:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from  
> Technically Team, *Technically.dev* (2025):  
> [{title}]({url})  
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://technically.dev')

def parse_adamfard_article(soup, url):
    """Parse Adam Fard Studio article"""
    # Extract title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Adam Fard Studio Article"
    
    # Find main content - Adam Fard specific
    main_content = (soup.find('article') or 
                   soup.find('div', class_='post-content') or 
                   soup.find('div', class_='content') or
                   soup.find('main') or
                   soup.find('div', class_='entry-content') or
                   soup.find('div', class_='prose'))
    
    if not main_content:
        # Try to find any div with substantial text content
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 1000:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from  
> Adam Fard Studio, *Adam Fard Studio* (2025):  
> [{title}]({url})  
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://adamfard.com')

def extract_content(main_content, attribution, base_url):
    """Extract and convert content to markdown"""
    # Extract images
    images = []
    for img in main_content.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', '')
        if src:
            # Handle relative URLs
            if src.startswith('/'):
                src = base_url + src
            elif src.startswith('./'):
                src = base_url + src[1:]
            images.append({'src': src, 'alt': alt})
    
    # Convert to markdown
    markdown_content = ""
    
    # Process headings
    for heading in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = int(heading.name[1])
        text = heading.get_text().strip()
        if text:
            markdown_content += f"{'#' * level} {text}\n\n"
    
    # Process paragraphs
    for p in main_content.find_all('p'):
        text = p.get_text().strip()
        if text:
            markdown_content += f"{text}\n\n"
    
    # Process lists
    for ul in main_content.find_all('ul'):
        for li in ul.find_all('li'):
            text = li.get_text().strip()
            if text:
                markdown_content += f"- {text}\n"
        markdown_content += "\n"
    
    for ol in main_content.find_all('ol'):
        for i, li in enumerate(ol.find_all('li'), 1):
            text = li.get_text().strip()
            if text:
                markdown_content += f"{i}. {text}\n"
        markdown_content += "\n"
    
    # Process code blocks
    for code in main_content.find_all('code'):
        text = code.get_text().strip()
        if text:
            # Check if it's a block or inline
            if '\n' in text or len(text) > 50:
                markdown_content += f"```\n{text}\n```\n\n"
            else:
                markdown_content += f"`{text}` "
    
    # Process pre blocks
    for pre in main_content.find_all('pre'):
        text = pre.get_text().strip()
        if text:
            markdown_content += f"```\n{text}\n```\n\n"
    
    # Process blockquotes
    for blockquote in main_content.find_all('blockquote'):
        text = blockquote.get_text().strip()
        if text:
            markdown_content += f"> {text}\n\n"
    
    # Add images
    for img in images:
        markdown_content += f"![{img['alt']}]({img['src']})\n\n"
    
    return {
        'content': attribution + markdown_content,
        'images': images
    }

def parse_article(html_file, url):
    """Parse article based on the domain"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Determine parser based on URL
    if 'logrocket.com' in url:
        return parse_logrocket_article(soup, url)
    elif 'nngroup.com' in url:
        return parse_nngroup_article(soup, url)
    elif 'codecademy.com' in url:
        return parse_codecademy_article(soup, url)
    elif 'technically.dev' in url:
        return parse_technically_article(soup, url)
    elif 'adamfard.com' in url:
        return parse_adamfard_article(soup, url)
    else:
        return None

def main():
    # Define articles to process
    articles = [
        ("logrocket_1.html", "https://blog.logrocket.com/ux-design/ai-chatbot-design-best-practices/"),
        ("nngroup_1.html", "https://www.nngroup.com/articles/ai-paradigm-change/"),
        ("nngroup_2.html", "https://www.nngroup.com/articles/neurodiversity-ai-guidelines/"),
        ("nngroup_3.html", "https://www.nngroup.com/articles/ai-usability-testing/"),
        ("nngroup_4.html", "https://www.nngroup.com/articles/ai-inclusive-tool-building/"),
        ("nngroup_5.html", "https://www.nngroup.com/articles/beyond-conversational-ai/"),
        ("codecademy_1.html", "https://www.codecademy.com/article/how-to-develop-chatbots"),
        ("codecademy_2.html", "https://www.codecademy.com/article/chatbot-development-python"),
        ("technically_1.html", "https://technically.dev/posts/ai-augmented-design-workflow"),
        ("technically_2.html", "https://technically.dev/posts/ui-animations-with-manim"),
        ("adamfard_1.html", "https://adamfard.com/blog/ai-information-seeking"),
    ]
    
    results = []
    
    for html_file, url in articles:
        if os.path.exists(html_file):
            print(f"Processing {html_file}...")
            result = parse_article(html_file, url)
            if result:
                title = result['content'].split('\n')[2].replace('# ', '') if '# ' in result['content'] else "Unknown Title"
                print(f"  ✓ Parsed: {title}")
                print(f"  ✓ Content length: {len(result['content'])} characters")
                print(f"  ✓ Images found: {len(result['images'])}")
                results.append({
                    'file': html_file,
                    'url': url,
                    'title': title,
                    'content': result['content'],
                    'images': result['images']
                })
                
                # Save individual file
                output_file = f"parsed_{html_file.replace('.html', '.md')}"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result['content'])
                print(f"  ✓ Saved to: {output_file}")
            else:
                print(f"  ✗ Failed to parse {html_file}")
        else:
            print(f"  ✗ File not found: {html_file}")
        print()
    
    print(f"Successfully processed {len(results)} articles!")
    return results

if __name__ == "__main__":
    main()
