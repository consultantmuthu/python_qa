import re

if __name__ == '__main__':
    expression = r"[,.]"
    print(re.split(expression, '100,000,000.000'))

    