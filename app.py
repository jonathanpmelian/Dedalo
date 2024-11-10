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
    
        with open(os.path.join(project_path, 'index.html'), 'w') as file:
            file.write('<h1>Welcome to your new static site!</h1>')
            
        print(f'Project {name} created successfully!')
        
    except OSError as e:
        print(f'Error: Failed to create directory {name} or index.html. {e}')



def create_theme(project_name, theme_name):
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



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new static site project.')
    parser.add_argument('command', choices=["init", "theme"], help='The command to execute')
    parser.add_argument('name', help='The name of your site.')
    parser.add_argument('theme_name', nargs='?', help='The name of the theme to create. (for theme command)')
    args = parser.parse_args()

    if args.command == 'init':
        create_project(args.name)
    elif args.command == "theme":
        if not args.theme_name:
            print('Error: Missing theme name. Use "theme <site_name> <theme_name>" to add a theme.')
        else:
            create_theme(args.name, args.theme_name)
    else:
        print('Invalid command or missing arguments. Use "init <site_name>" to create a site or "theme <site_name> <theme_name>" to add a theme.')