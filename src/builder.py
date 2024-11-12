import os
from jinja2 import Template
import markdown
import logging
import yaml
import re
logging.basicConfig(level=logging.INFO)

def load_menu_config(project_name):
    menu_path = os.path.join(os.getcwd(), project_name, 'menu.yaml')
    if os.path.exists(menu_path):
        with open(menu_path, 'r') as file:
            return yaml.safe_load(file)
    return []

def build_menu(project_name):
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
                    
    logging.info(f'Site built successfully!')