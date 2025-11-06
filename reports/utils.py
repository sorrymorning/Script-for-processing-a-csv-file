import csv


def aggregate_brand_ratings(files):
    brand_ratings = {}

    for filename in files:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    brand = row["brand"]
                    rating = float(row["rating"])

                    # Если бренда еще нет в словаре, создаем пустой список
                    if brand not in brand_ratings:
                        brand_ratings[brand] = []

                    # Добавляем рейтинг в список для этого бренда
                    brand_ratings[brand].append(rating)

        except Exception as e:
            print(f"Ошибка при чтении {filename}: {e}")
            return None

    return brand_ratings
