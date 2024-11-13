import os
from jinja2 import Template
import markdown
import logging
import yaml
import re
import datetime

logging.basicConfig(level=logging.INFO)

def generate_sitemap(output_dir):
    """
    Generate a sitemap.xml file for the site
    """
    sitemap_path = os.path.join(output_dir, 'sitemap.xml')
    base_url="http://127.0.0.1:5500"
    
    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for filename in os.listdir(output_dir):
        if filename.endswith('.html'):
            page_url = f"{base_url}/{filename if filename != 'index.html' else ''}"
            lastmod = datetime.datetime.now().strftime("%Y-%m-%d")
            sitemap_content.append("  <url>")
            sitemap_content.append(f"    <loc>{page_url}</loc>")
            sitemap_content.append(f"    <lastmod>{lastmod}</lastmod>")
            sitemap_content.append("  </url>")

    sitemap_content.append('</urlset>')

    with open(sitemap_path, 'w') as file:
        file.write("\n".join(sitemap_content))

    logging.info(f"Sitemap generated at '{sitemap_path}'")

def load_menu_config(project_name):
    """
    Load the menu.yaml file from the project directory
    """
    menu_path = os.path.join(os.getcwd(), project_name, 'menu.yaml')
    if os.path.exists(menu_path):
        with open(menu_path, 'r') as file:
            return yaml.safe_load(file)
    return []

def build_menu(project_name):
    """
    Build the menu items for the site ordered by the menu.yaml file or 
    by the order of the files in the content directory
    """
    menu_items = load_menu_config(project_name)
    existing_urls = {item['url'] for item in menu_items}
    content_path = os.path.join(os.getcwd(), project_name, 'content')
    
    for filename in os.listdir(content_path):
        if filename.endswith('.md'):
            page_name = filename.replace(".md", "")
            url = f"/{page_name}.html" if page_name != "index" else "/"

            if url not in existing_urls:
                menu_items.append({
                    'label': page_name.capitalize(),
                    'url': url,
                    'order': len(menu_items)+1
                })
    

    menu_items.sort(key=lambda x: x['order'])
    return menu_items

def parse_front_matter(file):
    """
    Split the front matter and markdown content from a file
    """
    content = file.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)

    if match:
        front_matter = yaml.safe_load(match.group(1))
        markdown_content = match.group(2)
    else:
        front_matter = {}
        markdown_content = content
    
    return front_matter, markdown_content

def build_site(project_name, theme_name):
    """
    Build the site using the content and theme provided
    """
    if not os.path.exists(os.path.join(os.getcwd(), project_name)):
        logging.error(f'Error: Project {project_name} does not exist.')
        return # Exit the function
    
    if not os.path.exists(os.path.join(os.getcwd(), project_name, 'themes', theme_name)):
        logging.error(f'Error: Theme {theme_name} does not exist.')
        return # Exit the function
    
    menu = build_menu(project_name)
    content_dir = os.path.join(os.getcwd(), project_name, 'content')
    theme_dir = os.path.join(os.getcwd(), project_name, 'themes', theme_name, 'index.html')
    output_dir = os.path.join(os.getcwd(), project_name, 'public')

    with open(theme_dir, 'r') as file:
        template_content = file.read()
        template = Template(template_content)

    for md_file in os.listdir(content_dir):
        if md_file.endswith('.md'):
            with open(os.path.join(content_dir, md_file), 'r') as file:
                front_matter, markdown_content = parse_front_matter(file)
                html_content = markdown.markdown(markdown_content)
                title = front_matter.get('title') or markdown_content.splitlines()[0].lstrip('# ')
                description = front_matter.get('description', '')

                rendered_html = template.render(Description=description, Title=title, Content=html_content, Menu=menu)

                output_path = os.path.join(output_dir, md_file.replace('.md', '.html'))

                with open(output_path, 'w') as file:
                    file.write(rendered_html)
    
    generate_sitemap(output_dir)
    logging.info(f'Site built successfully!')