import os
import shutil
import pytest
from app import create_theme, create_project, create_page

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