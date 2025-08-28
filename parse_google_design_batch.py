#!/usr/bin/env python3
"""
Parse Google Design and AI-related URLs in batches
"""

import requests
from bs4 import BeautifulSoup
import re
import sys
import time
import os

def parse_google_design_article(soup, url, source_name):
    """Parse Google Design articles"""
    
    # Try to find the title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Google Design Article"
    
    # Try to find main content - Google Design specific selectors
    main_content = (soup.find('div', class_='TextBlock_text__hC8nw') or
                   soup.find('div', class_='--content-wrapper') or
                   soup.find('main') or
                   soup.find('article') or
                   soup.find('div', class_='content'))
    
    if not main_content:
        # Try to find any div with substantial text content as a last resort
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 500:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from
> {source_name}, *Google* (2025):
> [{title}]({url})
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://design.google')

def parse_medium_article(soup, url, source_name):
    """Parse Medium articles"""
    
    # Try to find the title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Medium Article"
    
    # Try to find main content - Medium specific selectors
    main_content = (soup.find('div', class_='postArticle') or
                   soup.find('article') or
                   soup.find('div', class_='content') or
                   soup.find('div', class_='post-content'))
    
    if not main_content:
        # Try to find any div with substantial text content as a last resort
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 500:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from
> {source_name}, *Medium* (2025):
> [{title}]({url})
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://medium.com')

def parse_microsoft_article(soup, url, source_name):
    """Parse Microsoft articles"""
    
    # Try to find the title
    title_elem = soup.find('h1') or soup.find('title')
    title = title_elem.get_text().strip() if title_elem else "Microsoft Article"
    
    # Try to find main content - Microsoft specific selectors
    main_content = (soup.find('div', class_='content') or
                   soup.find('article') or
                   soup.find('main') or
                   soup.find('div', class_='article-content'))
    
    if not main_content:
        # Try to find any div with substantial text content as a last resort
        all_divs = soup.find_all('div')
        for div in all_divs:
            text_content = div.get_text().strip()
            if len(text_content) > 500:  # Substantial content
                main_content = div
                break
    
    if not main_content:
        return None
    
    attribution = f"""> **Note:** The following article is reproduced verbatim from
> {source_name}, *Microsoft* (2025):
> [{title}]({url})
> for internal educational use only (non-profit).

# {title}

"""
    
    return extract_content(main_content, attribution, 'https://www.microsoft.com')

def extract_content(main_content, attribution, base_url):
    """Extract and format content from the main content area"""
    
    # Remove script and style elements
    for script in main_content(["script", "style"]):
        script.decompose()
    
    # Convert to markdown
    markdown_content = attribution
    
    # Process headings
    for heading in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = int(heading.name[1])
        text = heading.get_text().strip()
        if text:
            markdown_content += f"\n{'#' * level} {text}\n"
    
    # Process paragraphs
    for p in main_content.find_all('p'):
        text = p.get_text().strip()
        if text:
            markdown_content += f"\n{text}\n"
    
    # Process lists
    for ul in main_content.find_all('ul'):
        markdown_content += "\n"
        for li in ul.find_all('li'):
            text = li.get_text().strip()
            if text:
                markdown_content += f"- {text}\n"
    
    for ol in main_content.find_all('ol'):
        markdown_content += "\n"
        for i, li in enumerate(ol.find_all('li'), 1):
            text = li.get_text().strip()
            if text:
                markdown_content += f"{i}. {text}\n"
    
    # Process code blocks
    for code in main_content.find_all('code'):
        text = code.get_text().strip()
        if text:
            if code.parent.name == 'pre':
                markdown_content += f"\n```\n{text}\n```\n"
            else:
                markdown_content += f"`{text}`"
    
    # Process tables
    for table in main_content.find_all('table'):
        markdown_content += "\n"
        rows = table.find_all('tr')
        if rows:
            # Header row
            header_cells = rows[0].find_all(['th', 'td'])
            if header_cells:
                markdown_content += "| " + " | ".join([cell.get_text().strip() for cell in header_cells]) + " |\n"
                markdown_content += "| " + " | ".join(["---"] * len(header_cells)) + " |\n"
            
            # Data rows
            for row in rows[1:]:
                cells = row.find_all(['th', 'td'])
                if cells:
                    markdown_content += "| " + " | ".join([cell.get_text().strip() for cell in cells]) + " |\n"
    
    # Process links
    for link in main_content.find_all('a', href=True):
        text = link.get_text().strip()
        href = link['href']
        if not href.startswith('http'):
            href = base_url + href
        if text:
            markdown_content = markdown_content.replace(text, f"[{text}]({href})")
    
    # Clean up extra whitespace
    markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
    markdown_content = markdown_content.strip()
    
    return markdown_content

def download_and_parse_url(url, filename, source_name):
    """Download and parse a single URL"""
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Determine parser based on URL
        if 'design.google' in url:
            content = parse_google_design_article(soup, url, source_name)
        elif 'medium.com' in url:
            content = parse_medium_article(soup, url, source_name)
        elif 'microsoft.com' in url:
            content = parse_microsoft_article(soup, url, source_name)
        else:
            content = parse_google_design_article(soup, url, source_name)  # Default
        
        if content:
            # Save to file
            with open(f'{filename}_content.md', 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully parsed {source_name} article")
            print(f"📄 Content saved to: {filename}_content.md")
            return content
        else:
            print(f"❌ Could not extract content from {source_name} article")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading {source_name}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error parsing {source_name}: {e}")
        return None

def main():
    """Main function to process all URLs"""
    
    # Define the URLs with their source names and filenames
    urls_to_process = [
        # Google Design Library
        ("https://design.google/library/ux-ai", "Google Design", "google_ux_ai"),
        ("https://design.google/library/control-and-simplicity", "Google Design", "google_control_simplicity"),
        ("https://design.google/library/design-is-smart", "Google Design", "google_design_smart"),
        ("https://design.google/library/six-ai-terms", "Google Design", "google_six_ai_terms"),
        ("https://design.google/library/ai-design-roundtable-discussion", "Google Design", "google_ai_roundtable"),
        ("https://design.google/library/a-new-interaction-design-paradigm", "Google Design", "google_interaction_paradigm"),
        ("https://design.google/library/why-google-needs-ux-engineers", "Google Design", "google_ux_engineers"),
        ("https://design.google/library/six-ways-to-develop-your-ux-design-career", "Google Design", "google_ux_career"),
        ("https://design.google/library/first-raters", "Google Design", "google_first_raters"),
        ("https://design.google/library/ux-design-system-dance", "Google Design", "google_ux_design_system"),
        ("https://design.google/library/figma-comments-material-ux-euphrates-dahout", "Google Design", "google_figma_comments"),
        ("https://design.google/library/ai-sparkle-icon-research-pozos-schmidt", "Google Design", "google_ai_sparkle_icon"),
        ("https://design.google/library/adrian-secord-material-engineering-ai", "Google Design", "google_adrian_secord"),
        ("https://design.google/library/people-ai-research", "Google Design", "google_people_ai_research"),
        ("https://design.google/library/simulating-intelligence", "Google Design", "google_simulating_intelligence"),
        ("https://design.google/library/fast-real-time-and-fully-interactive-emoji", "Google Design", "google_interactive_emoji"),
        ("https://design.google/library/towards-resilient-systems", "Google Design", "google_resilient_systems"),
        
        # Medium Articles
        ("https://medium.com/google-design/human-centered-machine-learning-a770d10562cd", "Google Design", "medium_human_centered_ml"),
        ("https://medium.com/people-ai-research/participatory-machine-learning-69b77f1e5e23", "People + AI Research", "medium_participatory_ml"),
        ("https://medium.datadriveninvestor.com/putting-people-first-a-look-at-google-pair-and-human-centric-ai-0546a97e616b", "DataDrivenInvestor", "medium_people_first"),
        
        # Microsoft Research
        ("https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/", "Microsoft Research", "microsoft_hai_guidelines"),
        ("https://www.microsoft.com/en-us/research/publication/planning-for-natural-language-failures-with-the-ai-playbook/", "Microsoft Research", "microsoft_nl_failures"),
        ("https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/", "Microsoft Research", "microsoft_hai_design"),
        ("https://www.microsoft.com/en-us/research/blog/how-to-better-design-ai-from-ideation-to-user-perception-and-acceptance/", "Microsoft Research", "microsoft_ai_design_process"),
        
        # Other Sources
        ("https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming", "Mustafa Suleyman", "suleyman_conscious_ai"),
        ("https://www.buildo.com/blog-posts/what-we-learned-from-googles-people-ai-guidebook", "Buildo", "buildo_people_ai_guidebook"),
        ("https://adamfard.com/blog/ai-ux-design", "Adam Fard", "adamfard_ai_ux_design"),
        ("https://www.interaction-design.org/master-classes/how-to-design-with-and-for-artificial-intelligence", "Interaction Design Foundation", "idf_design_with_ai"),
        ("https://www.interaction-design.org/master-classes/ux-design-and-ai", "Interaction Design Foundation", "idf_ux_design_ai"),
        ("https://www.nngroup.com/articles/ai-hallucinations/", "Nielsen Norman Group", "nng_ai_hallucinations"),
        ("https://www.reloade.com/blog/2019/05/designing-human-centered-ai-products-a-peopleai-guidebook.php", "Reloade", "reloade_human_centered_ai"),
        ("https://www.reloade.com/blog/2017/06/human-centered-machine-learning.php", "Reloade", "reloade_human_centered_ml"),
        ("https://www.smashingmagazine.com/2016/11/does-conversation-hurt-or-help-the-chatbot-ux/", "Smashing Magazine", "smashing_chatbot_ux"),
    ]
    
    print(f"🚀 Starting to process {len(urls_to_process)} URLs...")
    
    successful_parses = []
    failed_parses = []
    
    for i, (url, source_name, filename) in enumerate(urls_to_process, 1):
        print(f"\n📝 Processing {i}/{len(urls_to_process)}: {source_name}")
        print(f"🔗 URL: {url}")
        
        content = download_and_parse_url(url, filename, source_name)
        
        if content:
            successful_parses.append((source_name, filename))
        else:
            failed_parses.append((source_name, url))
        
        # Add a small delay to be respectful to servers
        time.sleep(1)
    
    # Summary
    print(f"\n📊 Processing Complete!")
    print(f"✅ Successfully parsed: {len(successful_parses)} articles")
    print(f"❌ Failed to parse: {len(failed_parses)} articles")
    
    if successful_parses:
        print(f"\n✅ Successfully parsed articles:")
        for source_name, filename in successful_parses:
            print(f"  - {source_name}: {filename}_content.md")
    
    if failed_parses:
        print(f"\n❌ Failed to parse articles:")
        for source_name, url in failed_parses:
            print(f"  - {source_name}: {url}")

if __name__ == "__main__":
    main()
