import os
import shutil
import pytest
from src.file_manager import create_theme, create_project, create_page
from src.builder import build_site

@pytest.fixture
def setup_and_teardown():
  # Set up
  if os.path.exists("mysite"):
        shutil.rmtree("mysite")

  yield
   
  # Clean up
  if os.path.exists("mysite"):
        shutil.rmtree("mysite")

def test_create_theme(setup_and_teardown):
   create_project("mysite")
   create_theme("mysite", "cc")

   theme_path = os.path.join("mysite", "themes", "cc", "index.html")
   assert os.path.exists(theme_path), "Theme was not created correctly"

def test_project_initialization_with_content(setup_and_teardown):
    create_project("mysite")

    content_path = os.path.join("mysite", "content", "index.md")
    assert os.path.exists(content_path), "Content was not created correctly"

def test_create_new_page(setup_and_teardown):
    create_project("mysite")
    create_page("mysite", "about")

    page_path = os.path.join("mysite", "content", "about.md")
    assert os.path.exists(page_path), "Page was not created correctly"

def test_build_site_creates_html_from_markdown(setup_and_teardown):
    create_project("mysite")
    create_theme("mysite", "cc")

    # Check if HTML is created correctly
    build_site("mysite", "cc")
    output_path = os.path.join("mysite", "public", "index.html")
    assert os.path.exists(output_path), "HTML was not created correctly"

    # Check if Markdown content is rendered correctly
    with open(output_path, "r") as f:
        contents = f.read()
        assert "<h1>Welcome to your new static site!</h1>" in contents, "Markdown title was not rendered correctly"
        assert "<p>This is the homepage.</p>" in contents, "Markdown content was not rendered correctly"