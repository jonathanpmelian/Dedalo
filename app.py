import argparse
import os


def create_project(name):
    project_path = os.path.join(os.getcwd(), name)
    try:
        if os.path.exists(project_path):
            print(f'Error: Directory {name} already exists.')
            return # Exit the function

        # Create the project directory and index.html file
        os.makedirs(project_path)
        os.makedirs(os.path.join(project_path, 'content'))
        os.makedirs(os.path.join(project_path, 'themes'))
        with open(os.path.join(project_path, 'content', 'index.md'), 'w') as file:
            file.write('# Welcome to your new static site!\n This is the homepage.')
            
        print(f'Project {name} created successfully!')
        
    except OSError as e:
        print(f'Error: Failed to create project directory. {e}')


def create_theme(project_name, theme_name):
    if not os.path.exists(os.path.join(os.getcwd(), project_name)):
        print(f'Error: Project {project_name} does not exist.')
        return
    
    theme_path = os.path.join(os.getcwd(), project_name, 'themes', theme_name)
    try:
        if os.path.exists(theme_path):
            print(f'Error: Theme {theme_name} already exists.')
            return
        
        os.makedirs(theme_path, exist_ok=True)

        with open(os.path.join(theme_path, 'index.html'), 'w') as file:
            file.write('<h1>Theme Template</h1>')

        print(f'Theme {theme_name} created successfully in project {project_name}!')
    except OSError as e:
        print(f'Error: Failed to create theme {theme_name} in project {project_name}. {e}')


def create_page(project_name, page_name):
    if not os.path.exists(os.path.join(os.getcwd(), project_name)):
        print(f'Error: Project {project_name} does not exist.')
        return
    
    page_path = os.path.join(os.getcwd(), project_name, 'content', f'{page_name}.md')

    try:
        if os.path.exists(page_path):
            print(f"Error: Page {page_name} in {project_name} already exists.")
            return
        
        with open(page_path, 'w') as file:
            file.write(f'# {page_name.capitalize()} Page\n This is the {page_name} page.')

        print(f'Page {page_name} created successfully in project {project_name}!')
    except OSError as e:
        print(f'Error: Failed to create page {page_name} in project {project_name}. {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new static site project.')
    subparsers = parser.add_subparsers(dest='command', help='The command to execute')

    # Subparser for "init" command
    init_parser = subparsers.add_parser('init', help='Initialize a new static site project')
    init_parser.add_argument('name', help='The name of your')

    # Subparser for "theme" command
    theme_parser = subparsers.add_parser('theme', help='Create a new theme for your site')
    theme_parser.add_argument('name', help='The name of your site.')
    theme_parser.add_argument('theme_name', help='The name of the theme to create.')

    # Subparser for "page" command
    page_parser = subparsers.add_parser('page', help='Create a new page for your site')
    page_parser.add_argument('name', help='The name of your site.')
    page_parser.add_argument('page_name', help='The name of the page to create.')

    args = parser.parse_args()

    if args.command == 'init':
        create_project(args.name)
    elif args.command == "theme":
        create_theme(args.name, args.theme_name)
    elif args.command == "page":
        create_page(args.name, args.page_name)
    else:
        print('Invalid command or missing arguments. Use "init <site_name>", "theme <site_name> <theme_name>", or "page <site_name> <page_name>"')
