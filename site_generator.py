import os
from jinja2 import FileSystemLoader, Environment
import json
import markdown


INDEX_TEMPLATE_HTML = 'index.html'
ARTICLE_TEMPLATE_HTML = 'article.html'
CONFIG_FILE = 'config.json'
INDEX_CSS_PATHWAY = 'static/bootstrap-3.3.7/css'
ARTICLE_CSS_PATHWAY = '../../static/bootstrap-3.3.7/css'


def get_json_config(path_json):
    with open(path_json, mode='r',encoding='utf-8') as config_content:
        return json.load(config_content)


def get_structure_site(config_tree):
    if not os.path.exists('site'):
        os.mkdir('site')
    for path_to_folder in config_tree['articles']:
        article = path_to_folder['source']
        folder_name_tuple = os.path.split(article)[0]
        if not os.path.exists('site/{}'.format(folder_name_tuple)):
            os.mkdir('site/{}'.format(folder_name_tuple))


def get_templates(INDEX_TEMPLATE_HTML, ARTICLE_TEMPLATE_HTML):
    loader = FileSystemLoader('templates', encoding='utf-8',followlinks=True)
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    index_template = env.get_template(INDEX_TEMPLATE_HTML)
    article_template = env.get_template(ARTICLE_TEMPLATE_HTML)
    return index_template, article_template


def get_index_page_content(config_tree, INDEX_CSS_PATHWAY):
    topics = config_tree['topics']
    articles = config_tree['articles']
    content = {'links': topics,
               'articles': articles,
               'index_css': INDEX_CSS_PATHWAY}
    return content


def create_index(template, content):
    with open('index.html', mode='w') as content_index:
        content_index.write(template.render(content))


def get_article_in_md(article):
    article = 'articles/{}'.format(article['source'])
    with open(article, mode='r', encoding='utf-8') as article:
        article_in_md = article.read()
        return article_in_md


def get_article_content(article_in_md, article, ARTICLE_CSS_PATHWAY):
    content = markdown.markdown(article_in_md)
    title = article['title']
    content = {'title': title,
               'content': content,
               'article_css': ARTICLE_CSS_PATHWAY}
    root, extension = os.path.splitext(article['source'])
    return content, root


def create_article(template, content, path):
    site = 'site/{}.html'.format(path)
    with open(site, mode='w') as content_article:
        content_article.write(template.render(content))


if __name__ == '__main__':
    try:
        config_tree = get_json_config(CONFIG_FILE)
    except(FileNotFoundError):
        print('Ops! You should check the file for correctness.')
    else:
        get_structure_site(config_tree)
        index_content = get_index_page_content(config_tree, INDEX_CSS_PATHWAY)
        index_template, article_template = get_templates(INDEX_TEMPLATE_HTML,
                                                         ARTICLE_TEMPLATE_HTML)
        create_index(index_template, index_content)

        articles = config_tree['articles']
        for article in articles:
            content_in_md = get_article_in_md(article)
            article_content, pathway = get_article_content(content_in_md,
                                                           article,
                                                           ARTICLE_CSS_PATHWAY)
            create_article(article_template, article_content, pathway)