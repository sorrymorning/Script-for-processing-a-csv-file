from typing import Callable, Dict, List, Tuple

from reports.utils import aggregate_brand_ratings

from .report import register_report


@register_report("average-rating")
def average_rating_report(files: List[str]) -> Tuple[List, List]:
    brand_ratings = aggregate_brand_ratings(files)
    if not brand_ratings:
        return [("Error",)], [("Failed to process files",)]

    data = []
    for brand, ratings in sorted(
        brand_ratings.items(), key=lambda item: sum(item[1]) / len(item[1]), reverse=True
    ):
        if ratings:
            avg_rating = round(sum(ratings) / len(ratings), 2)
        else:
            avg_rating = 0
        data.append([brand, avg_rating])

    return ["brand", "rating"], data
