import os
import logging
logging.basicConfig(level=logging.INFO)

def create_project(name: str):
  """
  Create a new project directory with the given name
  """
  project_path = os.path.join(os.getcwd(), name)
  if os.path.exists(project_path):
    logging.error(f'Error: Directory {name} already exists.')
    return # Exit the function
  
  try:
      # Create the project directory, folders and content/index.md file
      os.makedirs(project_path)
      os.makedirs(os.path.join(project_path, 'content'))
      os.makedirs(os.path.join(project_path, 'themes'))
      os.makedirs(os.path.join(project_path, 'public'))

      # Add a menu.yaml file with a homepage entry
      with open(os.path.join(project_path, 'menu.yaml'), 'x') as file:
          file.write(
                '# Default menu configuration\n'
                '- label: Home\n'
                '  url: /\n'
                '  order: 1\n'
                )

      # Add a default index.md file
      with open(os.path.join(project_path, 'content', 'index.md'), 'w') as file:
          file.write('# Welcome to your new static site!\n This is the homepage.')
          
      logging.info(f'Project {name} created successfully!')  
  except OSError as e:
      logging.error(f'Error: Failed to create project directory. {e}')


def create_theme(project_name:str, theme_name:str):
  """
  Create a new theme in the project
  """
  if not os.path.exists(os.path.join(os.getcwd(), project_name)):
      logging.error(f'Error: Project {project_name} does not exist.')
      return # Exit the function
  
  theme_path = os.path.join(os.getcwd(), project_name, 'themes', theme_name)
  if os.path.exists(theme_path):
      logging.error(f'Error: Theme {theme_name} already exists.')
      return # Exit the function

  try:
      os.makedirs(theme_path)
      with open(os.path.join(theme_path, 'index.html'), 'x') as file:
          file.write('<!DOCTYPE html><html><head><title>{{ Title }}</title><meta name="description" content="{{ Description }}" /></head><body><nav><ul>{% for item in Menu %}<li><a href="{{item.url}}">{{item.label}}</a></li>{% endfor %}</ul></nav>{{ Content }}</body></html>')

      logging.info(f'Theme {theme_name} created successfully in project {project_name}!')
  except OSError as e:
      logging.error(f'Error: Failed to create theme {theme_name} in project {project_name}. {e}')


def create_page(project_name:str, page_name:str):
  """
  Create a new page in the project content directory
  """
  if not os.path.exists(os.path.join(os.getcwd(), project_name)):
      logging.error(f'Error: Project {project_name} does not exist.')
      return # Exit the function
  
  page_path = os.path.join(os.getcwd(), project_name, 'content', f'{page_name}.md')
  if os.path.exists(page_path):
      logging.error(f"Error: Page {page_name} in {project_name} already exists.")
      return # Exit the function
  
  try:
      with open(page_path, 'x') as file: 
          file.write(f'# {page_name.capitalize()} Page\n This is the {page_name} page.')

      logging.info(f'Page {page_name} created successfully in project {project_name}!')
  except OSError as e:
      logging.error(f'Error: Failed to create page {page_name} in project {project_name}. {e}')