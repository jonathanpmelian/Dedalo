import os
from jinja2 import Template
import markdown

def build_site(project_name, theme_name):
    if not os.path.exists(os.path.join(os.getcwd(), project_name)):
        print(f'Error: Project {project_name} does not exist.')
        return

    content_dir = os.path.join(os.getcwd(), project_name, 'content')
    theme_dir = os.path.join(os.getcwd(), project_name, 'themes', theme_name, 'index.html')
    output_dir = os.path.join(os.getcwd(), project_name, 'public')

    with open(theme_dir, 'r') as file:
        template_content = file.read()
        template = Template(template_content)

    for md_file in os.listdir(content_dir):
        if md_file.endswith('.md'):
            with open(os.path.join(content_dir, md_file), 'r') as file:
                md_content = file.read()
                html_content = markdown.markdown(md_content)

                title = md_content.splitlines()[0].lstrip('# ')
                rendered_html = template.render(Title=title, Content=html_content)

                output_path = os.path.join(output_dir, md_file.replace('.md', '.html'))
                with open(output_path, 'w') as file:
                    file.write(rendered_html)
                    
    print(f'Site built successfully!')