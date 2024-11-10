import os
import shutil
from app import create_theme

def teardown_module():
    shutil.rmtree("mysite")
    
def setup_module():
  if os.path.exists("mysite"):
    teardown_module()  

  os.makedirs("mysite")

def test_create_theme():
   create_theme("mysite", "cc")

   theme_path = os.path.join("mysite", "themes", "cc", "index.html")
   assert os.path.exists(theme_path), "Theme was not created correctly"