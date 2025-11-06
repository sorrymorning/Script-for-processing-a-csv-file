from reports import register_report
import csv
from typing import Dict, Callable, List, Tuple


def aggregate_brand_ratings(files):
    brand_ratings = {}

    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    brand = row['brand']
                    rating = float(row['rating'])
                    
                    # Если бренда еще нет в словаре, создаем пустой список
                    if brand not in brand_ratings:
                        brand_ratings[brand] = []
                    
                    # Добавляем рейтинг в список для этого бренда
                    brand_ratings[brand].append(rating)
                    
        except Exception as e:
            print(f"Ошибка при чтении {filename}: {e}")
            return None
    
    return brand_ratings


@register_report("average-rating")
def average_rating_report(files: List[str]) -> Tuple[List, List]:
    brand_ratings = aggregate_brand_ratings(files)
    if not brand_ratings:
        return [('Error',)], [('Failed to process files',)]
    

    data = []
    for brand, ratings in sorted(brand_ratings.items(), key=lambda item: sum(item[1])/len(item[1]), reverse=True):
        if ratings:
            avg_rating = round(sum(ratings) / len(ratings), 2)
        else:
            avg_rating = 0
        data.append([brand, avg_rating])

    

    return ['brand','rating'], data


