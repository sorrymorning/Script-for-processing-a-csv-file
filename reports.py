from typing import Dict, Callable, List, Tuple

_report_registry: Dict[str, Callable] = {}

def register_report(name: str):
    def decorator(func):
        _report_registry[name] = func
        return func
    return decorator

def get_report(name: str):
    return _report_registry.get(name)

def list_reports():
    return list(_report_registry.keys())



# reports/price_by_brand.py  
# @register_report("price_by_brand")
# def price_by_brand_report(files: List[str]) -> Tuple[List, List]:
#     # новый отчёт средней цены по брендам
#     pass