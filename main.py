import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def count_years_of_work():

    winery_foundation_year = 1920
    curr_year = datetime.date.today().year

    winery_age = curr_year - winery_foundation_year
    return winery_age


def get_drinks_from_excel(excel_path):

    wine_excel_df = pandas.read_excel(excel_path, keep_default_na=False)
    wines_by_category = collections.defaultdict(list)
    wines = wine_excel_df.to_dict('records')

    for wine in wines:
        wines_by_category[wine['Категория']].append(wine)

    return wines_by_category


if __name__ == '__main__':

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    drinks = get_drinks_from_excel('wine3.xlsx')

    rendered_page = template.render(
        years_old=count_years_of_work(),
        drinks=drinks
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
