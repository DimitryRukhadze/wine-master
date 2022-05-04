import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from os import environ

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv

def count_years_of_work():

    winery_foundation_year = 1920
    curr_year = datetime.date.today().year

    winery_age = curr_year - winery_foundation_year
    return winery_age


def get_drinks_from_excel(excel_path):

    wine_excel_df = pandas.read_excel(excel_path, keep_default_na=False)
    wines_from_excel = wine_excel_df.to_dict('records')
    wines_by_category = collections.defaultdict(list)

    for wine in wines_from_excel:
        wines_by_category[wine['Категория']].append(wine)

    return wines_by_category


if __name__ == '__main__':

    load_dotenv()
    excel_file_path = environ.get('EXCEL_FILE_PATH')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    drinks = get_drinks_from_excel(excel_file_path)

    rendered_page = template.render(
        years_old=count_years_of_work(),
        drinks=drinks
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
