import argparse
from src.file_manager import create_project, create_theme, create_page
from src.builder import build_site
from src.server import run_dev_server

def main():
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

    # Subparser for "build" command
    build_parser = subparsers.add_parser('build', help='Build your site')
    build_parser.add_argument('name', help='The name of your site.')
    build_parser.add_argument('theme_name', help='The name of the theme to use.')

    # Subparser for "dev" command
    dev_parser = subparsers.add_parser('dev', help='Run the development server')
    dev_parser.add_argument('name', help='The name of your site.')

    args = parser.parse_args()

    if args.command == 'init':
        create_project(args.name)
    elif args.command == "theme":
        create_theme(args.name, args.theme_name)
    elif args.command == "page":
        create_page(args.name, args.page_name)
    elif args.command == "build":
        build_site(args.name, args.theme_name)
    elif args.command == "dev":
        run_dev_server(args.name)
    else:
        print('Invalid command or missing arguments. Use "init <site_name>", "theme <site_name> <theme_name>", or "page <site_name> <page_name>"')
