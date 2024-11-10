import os
from flask import Flask, send_from_directory
from livereload import Server
from src.builder import build_site
import logging
logging.basicConfig(level=logging.INFO)

def run_dev_server(project_name):
    if not os.path.exists(os.path.join(os.getcwd(), project_name)):
        logging.error(f'Error: Project {project_name} does not exist.')
        return
    
    app = Flask(__name__)
    app.static_folder = os.path.join(os.getcwd(), project_name, 'public')
    
    @app.route('/')
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/<path:filename>')
    def serve_file(filename):
        return send_from_directory(app.static_folder, filename)

    server = Server(app.wsgi_app)
    server.watch(os.path.join(os.getcwd(), project_name, 'content')), lambda: build_site(project_name, "cc")
    server.watch(os.path.join(os.getcwd(), project_name, 'themes', 'cc')), lambda: build_site(project_name, "cc")

    logging.info("Starting development server with live reload...")
    server.serve(open_url_delay=True)