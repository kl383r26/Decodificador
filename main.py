import sys
import pandas

def main(url):

    tabela = pandas.read_html(url, encoding='utf-8', header=0)[0]

    x = tabela['x-coordinate'].astype(int).tolist()
    caracteres = tabela['Character'].tolist()
    y = tabela['y-coordinate'].astype(int).tolist()

    for i in range(max(y), -1, -1):
        for j in range(max(x) + 1):
            c = ' '
            for k in range(len(x)):          
                if x[k] == j and y[k] == i:
                    c = caracteres[k]
            print(c, end='')
        print()

main(sys.argv[1])