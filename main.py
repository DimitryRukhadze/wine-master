import datetime
import pandas
import collections


from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def count_years_of_work():

    year_founded = datetime.date(year=1920, month=1, day=1)
    curr_year = datetime.date.today().year

    years_old = curr_year - year_founded.year
    return years_old


def get_drinks_from_excel(excel_path):

    wine_excel_df = pandas.read_excel(excel_path)
    wine_excel_df.fillna(0, inplace=True)
    wine_categories = collections.defaultdict(list)

    for row_num in wine_excel_df.index:
        row = wine_excel_df.iloc[row_num]
        wine_categories[row.Категория].append(row.to_dict())

    return wine_categories


if __name__ == '__main__':

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    drinks = get_drinks_from_excel('wine3.xlsx')

    rendered_page = template.render(
        years_old=count_years_of_work(),
        drink_types=drinks.keys(),
        drinks=drinks
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
