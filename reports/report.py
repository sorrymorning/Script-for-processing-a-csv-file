from typing import Callable, Dict

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
