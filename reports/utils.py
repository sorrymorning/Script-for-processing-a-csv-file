import csv


def aggregate_brand_ratings(files):
    brand_ratings = {}
    processed_files = 0
    for filename in files:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                if "brand" not in reader.fieldnames or "rating" not in reader.fieldnames:
                    print(
                        f"Ошибка: в файле {filename} отсутствуют необходимые колонки 'brand' или 'rating'"
                    )
                    continue

                for row in reader:
                    try:
                        brand = row["brand"]
                        rating = float(row["rating"])

                        if brand not in brand_ratings:
                            brand_ratings[brand] = []

                        brand_ratings[brand].append(rating)
                    except (ValueError, KeyError) as e:
                        print(f"Ошибка в строке файла {filename}: {e}")
                        continue

                processed_files += 1

        except Exception as e:
            print(f"Ошибка при чтении {filename}: {e}")
            return None

    if processed_files == 0:
        print("Не удалось обработать ни один файл")
        return None

    return brand_ratings
