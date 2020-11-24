import base64
import codecs

telegram_token = 'YOUR_TELEGRAM_TOKEN'
BASE_PATH = '{$YOUR_PATH}blockchain-oracle-telegram/'


def load_resource(resource):
    d = []
    with open(resource) as f:
        for line in f:
            d.append(line.replace('\n', ''))

    return d


def update_resource(col, file):
    f = open(file, 'w')
    for ele in col:
        f.write(ele + '\n')

    f.close()


def convert_from_b64_url_to_hex(input):
    input = input.replace('-', '+').replace('_', '/').replace('.', '==')
    x = base64.b64decode(input)
    b_string = codecs.encode(x, 'hex')

    return b_string.decode('utf-8')


def clean_string(input):
    return input.replace('"', '').replace('}', '').replace(']', '')