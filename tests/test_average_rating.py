from reports.average_rating import average_rating_report
from reports.report import get_report


def test_average_rating_report_with_data():
    """Тест отчета с корректными данными"""
    headers, data = average_rating_report(['test_files/products1.csv','test_files/products2.csv'])
    
    # Проверяем заголовки
    assert headers == ['brand', 'rating']
    
    # Проверяем данные
    assert len(data) == 4 
    
    # Проверяем сортировку (по убыванию среднего рейтинга)
    brands = [row[0] for row in data]
    ratings = [row[1] for row in data]
    
    
    assert brands[0] == 'apple'
    assert ratings[0] == 4.55
    
    assert brands[1] == 'samsung' 
    assert ratings[1] == 4.53
    
    assert brands[2] == 'xiaomi'
    assert ratings[2] == 4.37


def test_average_rating_report_empty_files():
    """Тест отчета с пустыми файлами"""
    headers, data = average_rating_report(['test_files/empty.csv'])
    
    # Должны получить сообщение об ошибке
    assert headers == ['Error']
    assert data == ['Failed to process files']
