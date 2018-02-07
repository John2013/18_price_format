import re
import argparse


def format_price(price) -> str:
    if isinstance(price, (int, float)) or (
        isinstance(price, str) and re.match(r'^\d+\.?\d*$', price)
    ):
        price = float(price)
        if price.is_integer():
            format_string = ',.0f'
        else:
            format_string = ',.2f'
        return format(price, format_string).replace(',', ' ')

    else:
        raise ValueError(
            'Некорректное значение, ожидалось число, дано: {}'.format(
                price
            )
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Форматирование числа в цену')
    parser.add_argument('--price', '-p', help='Входящая цена', required=True)
    args = parser.parse_args()
    print(format_price(args.price))
