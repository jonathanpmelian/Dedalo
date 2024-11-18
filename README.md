# Dedalo

Dedalo is a Python-based static site generator that allows users to create, manage, and build static websites. It supports project initialization, theme creation, content management using Markdown files with front matter, customizable layouts, and a development server with live reload.

## Features

- **Initialize a New Site**: Quickly set up a new project directory with content and theme folders.
- **Front Matter Support**: Use YAML front matter in Markdown files for dynamic page metadata, such as `title`, `description`, `order`, and `layout`.
- **Custom Layouts**: Assign specific layouts (templates) to individual pages or sections of your site using the `layout` field in front matter.
- **Create Themes**: Easily create and apply themes with customizable HTML templates.
- **Add Pages**: Generate new Markdown pages that integrate seamlessly with existing themes.
- **Build the Site**: Render HTML files from Markdown and templates into a `public` directory for deployment.
- **Development Server**: Preview the site locally with automatic live reloading on content or theme changes.
- **Automatic Sitemap Generation**: Generate a `sitemap.xml` file automatically during the build process to improve SEO.

## Getting Started

### Prerequisites

- **Python 3.6+**
- **Virtual Environment** (optional but recommended)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jonathanpmelian/static-site-generator.git
   cd static-site-generator
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux
   ```

3. **Install the Package**:

   ```bash
   pip install -e .
   ```

   This will install the package in editable mode and make the `ssg` command available globally within the virtual environment.

4. **Verify the Installation**:

   ```bash
   ssg --help
   ```

   You should see a list of available commands.

## Usage

### Initialize a New Project

To start a new project, use the `init` command with a project name:

```bash
ssg init mysite
```

This creates a new directory named `mysite` with the following structure:

```
mysite/
├── content/
│   └── index.md
├── themes/
├── public/
└── menu.yaml
```

### Add Front Matter in Markdown files

Dedalo supports YAML front matter in Markdown files, which allows you to define metadata such as `title` or `description`. Example:

```
---
title: "About Us"
description: "Learn more about our team and mission."
---

# About Us
Welcome to the about page! Here you’ll find information about our team and mission.
```

### Add a Theme

You can add a theme to your project using the `theme` command:

```bash
ssg theme mysite my-theme
```

This creates a `themes/my-theme` directory where you can customize the HTML template.

### Add a New Page

To add a new page, use the `page` command:

```bash
ssg page mysite about
```

This creates a `content/about.md` file. Use Markdown syntax to add content to this file.

### Build the Site

To generate the HTML files from your Markdown and templates, run:

```bash
ssg build mysite my-theme
```

This compiles the site and outputs HTML files to the `public` directory, ready for deployment.

### Run the Development Server

Preview the site locally with the `dev` command:

```bash
ssg dev mysite
```

The server automatically rebuilds and refreshes the site on changes to the content or theme files.

## Directory Structure

A typical project directory structure after initialization might look like this:

```
mysite/
├── content/
│   ├── about.md
│   └── index.md
├── themes/
│   └── my-theme/
│       └── index.html
├── public/
│   ├── about.html
│   └── index.html
└── menu.yaml
```

- **`content/`**: Contains Markdown files that make up the pages of your site.
- **`themes/`**: Stores the HTML templates for your site’s themes.
- **`public/`**: Generated output files that can be deployed to a web server.
- **`menu.yaml`**: Default menu configuration file, where users can define menu structure.

## Custom Layout Support

Dedalo now supports multiple layouts for pages. You can specify which layout (template) to use for each page by adding a `layout` field to the YAML front matter in your Markdown files.

### How to Use Custom Layouts

1. **Specify the Layout in Front Matter**  
   Add a `layout` field in the YAML front matter of your Markdown file. For example:

   **`content/blog_post.md`**:

   ```yaml
   ---
   title: "A Blog Post"
   description: "An example blog post."
   layout: "blog"
   ---
   # A Blog Post
   This is an example of a blog post using a custom layout.
   ```

   **`content/about.md`**:

   ```yaml
   ---
   title: "About Us"
   description: "Learn more about our team."
   layout: "about"
   ---
   # About Us
   Welcome to the about page!
   ```

2. **Add Layout Templates to Your Theme**  
   Create HTML templates in your theme directory that correspond to the specified layouts. Dedalo will look for templates with the same name as the `layout` field.

   **Example Template: `themes/mytheme/blog.html`**:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>{{ Title }} - Blog</title>
       <meta name="description" content="{{ Description }}" />
     </head>
     <body>
       <header>
         <h1>{{ Title }}</h1>
       </header>
       <article>{{ Content }}</article>
       <footer>
         <a href="/">Back to Home</a>
       </footer>
     </body>
   </html>
   ```

   **Example Template: `themes/mytheme/about.html`**:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>{{ Title }} - About</title>
       <meta name="description" content="{{ Description }}" />
     </head>
     <body>
       <header>
         <h1>About Us</h1>
       </header>
       <section>{{ Content }}</section>
     </body>
   </html>
   ```

3. **Default to `index.html` If No Layout Is Specified**  
   If a Markdown file does not include a `layout` field, Dedalo will use the default `index.html` template in the theme directory.

4. **Build the Site**  
   Run the `build` command to compile the site and apply the layouts:

   ```bash
   ssg build myproject mytheme
   ```

5. **Verify the Result**  
   Open the generated HTML files in the `public` directory to ensure that each page uses the specified layout.

### Directory Structure

Here’s what the project might look like after adding custom layouts:

```
mysite/
├── content/
│   ├── blog_post.md
│   └── about.md
├── themes/
│   └── mytheme/
│       ├── index.html
│       ├── blog.html
│       └── about.html
├── public/
│   ├── blog_post.html
│   ├── about.html
│   └── index.html
└── menu.yaml
```

- **`content/`**: Markdown files with optional front matter for each page.
- **`themes/`**: Contains multiple templates (`index.html`, `blog.html`, `about.html`, etc.) for different layouts.
- **`public/`**: Generated output files that reflect the specified layouts.

## Configuration

### Dependencies

Dependencies are listed in `requirements.txt` and are installed automatically when the package is installed. You can also install them manually with:

```bash
pip install -r requirements.txt
```

## Development

### Running Tests

Tests are written with `pytest`. To run tests:

```bash
pytest
```

### Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Next Steps

- **Explore Custom Shortcodes**: Add reusable components (e.g., buttons, alerts) directly within Markdown files.
- **Implement Pagination**: Useful for blogs or sections with many pages.
- **User-Defined Base URL**: Allow users to specify their site’s base URL for generating the sitemap.
