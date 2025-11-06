import argparse
import csv
from tabulate import tabulate
from reports import get_report,list_reports



def main():
    parser = argparse.ArgumentParser(
        description='Скрипт для обработки csv-файла',
    )
    parser.add_argument('--files', type=str, nargs='+',help='Подробный вывод')
    parser.add_argument('--report', type=str, help=f"Available: {', '.join(list_reports())}")


    args = parser.parse_args()
    
    report_func = get_report(args.report)
    if not report_func:
        print(f"Unknown report: {args.report}")
        return
    
    results = report_func(args.files)
    
    print(tabulate(results[1], 
        headers=results[0], 
        tablefmt='pretty',
        showindex=range(1, len(results[1])+1),
        colalign=("center", "left", "right")
        ))







if __name__ == '__main__':
    main()