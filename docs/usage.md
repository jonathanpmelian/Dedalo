## Usage

To summarize this are the steps to follow to run your website:

1. Initialize a new project
2. Add pages, themes, from matter and custom layouts to customize your website
3. Build the site
4. Run the development server

Now, let's check in deep each one of them.

## Initialize a New Project

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

### Directory Structure

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

## Add Front Matter in Markdown files

Dedalo supports YAML front matter in Markdown files, which allows you to define metadata such as `title` or `description`. Example:

```
---
title: "About Us"
description: "Learn more about our team and mission."
---

# About Us
Welcome to the about page! Here you’ll find information about our team and mission.
```

## Add a Theme

You can add a theme to your project using the `theme` command:

```bash
ssg theme mysite my-theme
```

This creates a `themes/my-theme` directory where you can customize the HTML template.

## Add a New Page

To add a new page, use the `page` command:

```bash
ssg page mysite about
```

This creates a `content/about.md` file. Use Markdown syntax to add content to this file.

## Build the Site

To generate the HTML files from your Markdown and templates, run:

```bash
ssg build mysite my-theme
```

This compiles the site and outputs HTML files to the `public` directory, ready for deployment.

## Run the Development Server

Preview the site locally with the `dev` command:

```bash
ssg dev mysite
```

The server automatically rebuilds and refreshes the site on changes to the content or theme files.

## How to Use Custom Layouts

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
