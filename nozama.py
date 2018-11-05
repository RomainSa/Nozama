import urllib.request
import re
import configparser

from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

config = configparser.ConfigParser()
config.read('conf.cfg')


class NozamaPrice(Resource):

    def get(self, asin):

        # basic response
        response = {'asin': asin, 'price': None}

        # get html
        with urllib.request.urlopen(config['patterns']['search'].format(asin)) as r:
            html = r.read()

        # parse it to get price text
        soup = BeautifulSoup(html, "html.parser")
        price_match = soup.find(class_="a-size-base a-color-price s-price a-text-bold")
        if price_match is not None:

            price_text = price_match.text
            # convert it to float
            match = re.search(config['patterns']['price'], price_text)

            if match is not None:
                price = float(match.group(0).replace(',', '.'))
                response['price'] = price

        return response


api.add_resource(NozamaPrice, '/<asin>')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
