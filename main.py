import argparse
import csv
from calculations import average
from tabulate import tabulate



def main():
    parser = argparse.ArgumentParser(
        description='Скрипт для обработки csv-файла',
    )
    parser.add_argument('--files', type=str, nargs='+',help='Подробный вывод')
    parser.add_argument('--report', type=str, help='Название')


    args = parser.parse_args()

    results = average(args.files)


    if args.report:
        with open(args.report + ".csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(results[0])
            writer.writerows(results[1:])
    
    print(tabulate(results[1:], 
        headers=results[:1][0], 
        tablefmt='pretty',
        showindex=range(1, len(results)),
        colalign=("center", "left", "right")
        ))







if __name__ == '__main__':
    main()