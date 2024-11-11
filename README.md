# Static Site Generator

A Python-based static site generator that allows users to create, manage, and build static websites with a development server featuring live reload. This tool supports project initialization, theme creation, content management using Markdown files, and customizable templates.

## Features

- **Initialize a New Site**: Quickly set up a new project directory with a content structure.
- **Create Themes**: Easily create and apply themes with customizable HTML templates.
- **Add Pages**: Generate new Markdown pages that integrate seamlessly with existing themes.
- **Build the Site**: Render HTML files from Markdown and templates into a `public` directory for deployment.
- **Development Server**: Preview the site locally with automatic live reloading on content or theme changes.

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
└── public/
```

### Add a Theme

You can add a theme to your project using the `theme` command:

```bash
ssg theme mysite mytheme
```

This creates a `themes/mytheme` directory where you can customize the HTML template.

### Add a New Page

To add a new page, use the `page` command:

```bash
ssg page mysite about
```

This creates a `content/about.md` file. Use Markdown syntax to add content to this file.

### Build the Site

To generate the HTML files from your Markdown and templates, run:

```bash
ssg build mysite mytheme
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
│   └── mytheme/
│       └── index.html
├── public/
│   ├── about.html
│   └── index.html
```

- **`content/`**: Contains Markdown files that make up the pages of your site.
- **`themes/`**: Stores the HTML templates for your site’s themes.
- **`public/`**: Generated output files that can be deployed to a web server.

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
pytest test_app.py
```

### Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
