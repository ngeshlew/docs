#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import html
import os

def find_main_content(soup):
    """Try multiple strategies to find main content"""
    # Try common content selectors
    selectors = [
        'article',
        'main',
        {'tag': 'div', 'class': 'content'},
        {'tag': 'div', 'class': 'post-content'},
        {'tag': 'div', 'class': 'entry-content'},
        {'tag': 'div', 'class': 'article-content'},
        {'tag': 'div', 'class': 'prose'},
        {'tag': 'div', 'class': 'markdown'},
        {'tag': 'div', 'class': 'blog-post'},
        {'tag': 'div', 'class': 'post-body'},
        {'tag': 'div', 'class': 'article-body'},
        {'tag': 'div', 'class': 'blog-content'},
        {'tag': 'div', 'class': 'post'},
        {'tag': 'div', 'class': 'page-content'},
        {'tag': 'section', 'class': 'content'},
    ]
    
    for selector in selectors:
        if isinstance(selector, str):
            content = soup.find(selector)
        else:
            content = soup.find(selector['tag'], class_=selector['class'])
        
        if content:
            return content
    
    # If no specific content area found, try to find divs with substantial text
    all_divs = soup.find_all('div')
    for div in all_divs:
        text_content = div.get_text().strip()
        if len(text_content) > 1500:  # Substantial content
            return div
    
    return None

def extract_content(main_content, attribution, base_url):
    """Extract and convert content to markdown"""
    if not main_content:
        return None
        
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
        if text and len(text) < 200:  # Avoid very long headings
            markdown_content += f"{'#' * level} {text}\n\n"
    
    # Process paragraphs
    for p in main_content.find_all('p'):
        text = p.get_text().strip()
        if text and len(text) > 10:  # Avoid very short paragraphs
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

def parse_article(html_file, url, source_name):
    """Parse article from any source"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_elem = soup.find('h1') or soup.find('title')
        title = title_elem.get_text().strip() if title_elem else f"{source_name} Article"
        
        # Clean up title
        if '|' in title:
            title = title.split('|')[0].strip()
        if '–' in title:
            title = title.split('–')[0].strip()
        if '-' in title and len(title.split('-')) > 1:
            title = title.split('-')[0].strip()
        
        # Find main content
        main_content = find_main_content(soup)
        
        if not main_content:
            return None
        
        # Determine base URL
        if 'anthropic' in url:
            base_url = 'https://anthropic.com'
        elif 'openai' in url:
            base_url = 'https://openai.com'
        elif 'deepmind' in url:
            base_url = 'https://www.deepmind.com'
        elif 'cohere' in url:
            base_url = 'https://cohere.com'
        elif 'langchain' in url:
            base_url = 'https://blog.langchain.dev'
        elif 'pinecone' in url:
            base_url = 'https://www.pinecone.io'
        else:
            base_url = url.split('/')[0] + '//' + url.split('/')[2]
        
        # Create attribution
        attribution = f"""> **Note:** The following article is reproduced verbatim from  
> {source_name}, *{source_name}* (2025):  
> [{title}]({url})  
> for internal educational use only (non-profit).

# {title}

"""
        
        return extract_content(main_content, attribution, base_url)
        
    except Exception as e:
        print(f"Error parsing {html_file}: {str(e)}")
        return None

def main():
    # Define articles to process with source names
    articles = [
        ("anthropic_computer_use.html", "https://www.anthropic.com/news/introducing-computer-use", "Anthropic"),
        ("openai_reasoning.html", "https://openai.com/index/reasoning/", "OpenAI"),
        ("deepmind_alphafold.html", "https://www.deepmind.com/research/highlighted-research/alphafold", "DeepMind"),
        ("deepmind_gemini.html", "https://www.deepmind.com/research/highlighted-research/gemini", "DeepMind"),
        ("cohere_aya.html", "https://cohere.com/blog/aya-expanse", "Cohere"),
        ("langchain_studio.html", "https://blog.langchain.dev/langgraph-studio/", "LangChain"),
        ("langchain_agents.html", "https://blog.langchain.dev/controllable-agents/", "LangChain"),
        ("pinecone_rag.html", "https://www.pinecone.io/blog/retrieval-augmented-generation/", "Pinecone"),
        ("pinecone_evaluation.html", "https://www.pinecone.io/blog/llm-evaluation/", "Pinecone"),
    ]
    
    results = []
    
    for html_file, url, source_name in articles:
        if os.path.exists(html_file):
            print(f"Processing {html_file} from {source_name}...")
            result = parse_article(html_file, url, source_name)
            if result and len(result['content']) > 500:  # Only save substantial content
                title = result['content'].split('\n')[4].replace('# ', '') if '# ' in result['content'] else "Unknown Title"
                print(f"  ✓ Parsed: {title}")
                print(f"  ✓ Content length: {len(result['content'])} characters")
                print(f"  ✓ Images found: {len(result['images'])}")
                results.append({
                    'file': html_file,
                    'url': url,
                    'title': title,
                    'content': result['content'],
                    'images': result['images'],
                    'source': source_name
                })
                
                # Save individual file
                output_file = f"parsed_{html_file.replace('.html', '.md')}"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result['content'])
                print(f"  ✓ Saved to: {output_file}")
            else:
                print(f"  ✗ Failed to parse {html_file} or content too short")
        else:
            print(f"  ✗ File not found: {html_file}")
        print()
    
    print(f"Successfully processed {len(results)} articles!")
    return results

if __name__ == "__main__":
    main()
