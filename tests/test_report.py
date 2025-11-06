import pytest

from reports.report import _report_registry, get_report, list_reports, register_report


def test_register_and_get_report():
    """Тест регистрации и получения отчета"""

    _report_registry.clear()

    @register_report("test-report")
    def test_func(files):
        return ["header"], [["data"]]

    assert "test-report" in list_reports()
    assert get_report("test-report") == test_func


def test_get_nonexistent_report():
    """Тест получения несуществующего отчета"""
    _report_registry.clear()

    result = get_report("nonexistent")
    assert result is None


def test_list_reports():
    """Тест получения списка отчетов"""
    _report_registry.clear()

    # Регистрируем несколько отчетов
    @register_report("report1")
    def func1(files):
        pass

    @register_report("report2")
    def func2(files):
        pass

    reports = list_reports()
    assert "report1" in reports
    assert "report2" in reports
    assert len(reports) == 2
