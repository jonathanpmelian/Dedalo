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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new static site project.')
    parser.add_argument('command', choices=["init"], help='The command to execute')
    parser.add_argument('name', help='The name of your site.')
    args = parser.parse_args()

    if args.command == 'init':
        create_project(args.name)
    