# Encyclopedia

This program create html site with **devman_encyclopedia** wiki about Python by markdown articles
 and json config file, where stored structure of site.

# How to install
1. Recomended use venv or virtualenv for better isolation.
   Venv setup example:
   `python venv ENV`
   `source ENV/bin/activate`
2. Install requirements: 
   `pip install -r requirements.txt` (alternatively try add `sudo` before command)

# How to use
If it's needed edit `config.json` and put .md files to dir `site` in necessary folder.
Then run program: `python create_site.py`.

Example of final result: [devman_encyclopedia](https://Djapy.github.io/19_site_generator/)
Example structure:
```
├── index.html
├── sites
│   ├── 0_tutorial
│   │   ├── 14_google.md
│   │   ├── 27_devman.md
│   │   ├── 29_english.md
│   │   ├── 7_codenvy.md
│   │   ├── 8_cli.md
│   │   └── 9_git.md
│   ├── 1_python_basics
│   │   ├── 10_pep8.md
│   │   ├── 18_comments.md
│   │   ├── 1_intro.md
│   │   ├── 2_base_types.md
│   │   ├── 3_base_constructions.md
│   │   ├── 4_types.md
│   │   ├── 5_modules.md
│   │   └── 6_tips_and_tricks.md
│   ├── 2_html
│   │   ├── html_injection.md
│   │   └── special &amp; symbol.md
│   └── 4_git
│       └── 22_git_history.md
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
