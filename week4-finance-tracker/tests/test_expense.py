"""
Unit tests for Expense class
"""

import pytest
from finance_tracker.expense import Expense


class TestExpense:
    """Test cases for Expense class"""
    
    def test_valid_expense_creation(self):
        """Test creating a valid expense"""
        exp = Expense("2024-01-15", 25.50, "Food", "Lunch at cafe")
        assert exp.date == "2024-01-15"
        assert exp.amount == 25.50
        assert exp.category == "Food"
        assert exp.description == "Lunch at cafe"
    
    def test_invalid_date_format(self):
        """Test invalid date format raises error"""
        with pytest.raises(ValueError, match="Invalid date format"):
            Expense("2024/01/15", 25.50, "Food", "Lunch")
    
    def test_invalid_date_future(self):
        """Test future date raises error"""
        with pytest.raises(ValueError, match="Date cannot be in the future"):
            Expense("2030-01-01", 25.50, "Food", "Lunch")
    
    def test_invalid_amount_negative(self):
        """Test negative amount raises error"""
        with pytest.raises(ValueError, match="Amount must be greater than 0"):
            Expense("2024-01-15", -10, "Food", "Lunch")
    
    def test_invalid_amount_zero(self):
        """Test zero amount raises error"""
        with pytest.raises(ValueError, match="Amount must be greater than 0"):
            Expense("2024-01-15", 0, "Food", "Lunch")
    
    def test_invalid_amount_string(self):
        """Test string amount raises error"""
        with pytest.raises(ValueError, match="Invalid amount"):
            Expense("2024-01-15", "twenty", "Food", "Lunch")
    
    def test_valid_amount_rounding(self):
        """Test amount rounding to 2 decimal places"""
        exp = Expense("2024-01-15", 25.555, "Food", "Lunch")
        assert exp.amount == 25.56
    
    def test_custom_category(self):
        """Test custom category (not in VALID_CATEGORIES)"""
        exp = Expense("2024-01-15", 25.50, "Gaming", "New game")
        assert exp.category == "Gaming"
        assert "Gaming" in Expense.VALID_CATEGORIES
    
    def test_empty_description(self):
        """Test empty description raises error"""
        with pytest.raises(ValueError, match="Description cannot be empty"):
            Expense("2024-01-15", 25.50, "Food", "")
    
    def test_to_dict_method(self):
        """Test serialization to dictionary"""
        exp = Expense("2024-01-15", 25.50, "Food", "Lunch at cafe")
        result = exp.to_dict()
        expected = {
            'date': '2024-01-15',
            'amount': 25.50,
            'category': 'Food',
            'description': 'Lunch at cafe'
        }
        assert result == expected
    
    def test_from_dict_method(self):
        """Test deserialization from dictionary"""
        data = {
            'date': '2024-01-15',
            'amount': 25.50,
            'category': 'Food',
            'description': 'Lunch at cafe'
        }
        exp = Expense.from_dict(data)
        assert exp.date == "2024-01-15"
        assert exp.amount == 25.50
        assert exp.category == "Food"
        assert exp.description == "Lunch at cafe"
    
    def test_string_representation(self):
        """Test string representation"""
        exp = Expense("2024-01-15", 25.50, "Food", "Lunch")
        str_repr = str(exp)
        assert "2024-01-15" in str_repr
        assert "Food" in str_repr
        assert "25.50" in str_repr
    
    def test_repr_representation(self):
        """Test detailed representation"""
        exp = Expense("2024-01-15", 25.50, "Food", "Lunch")
        repr_str = repr(exp)
        assert "Expense(" in repr_str
        assert "date='2024-01-15'" in repr_str
        assert "amount=25.5" in repr_str
    
    def test_amount_large_number(self):
        """Test with large amount"""
        exp = Expense("2024-01-15", 1000000.50, "Real Estate", "Property")
        assert exp.amount == 1000000.50
    
    def test_amount_small_number(self):
        """Test with very small amount"""
        exp = Expense("2024-01-15", 0.01, "Misc", "Small item")
        assert exp.amount == 0.01
    
    def test_category_case_sensitive(self):
        """Test category is case-sensitive"""
        exp1 = Expense("2024-01-15", 25.50, "FOOD", "Lunch")
        exp2 = Expense("2024-01-15", 25.50, "food", "Lunch")
        exp3 = Expense("2024-01-15", 25.50, "Food", "Lunch")
        
        assert exp1.category == "FOOD"
        assert exp2.category == "food"
        assert exp3.category == "Food"
        assert "FOOD" in Expense.VALID_CATEGORIES
        assert "food" in Expense.VALID_CATEGORIES
    
    def test_description_whitespace_stripping(self):
        """Test description whitespace is stripped"""
        exp = Expense("2024-01-15", 25.50, "Food", "  Lunch at cafe  ")
        assert exp.description == "Lunch at cafe"
    
    def test_invalid_data_missing_fields(self):
        """Test from_dict with missing fields"""
        with pytest.raises(KeyError):
            Expense.from_dict({
                'date': '2024-01-15',
                'amount': 25.50
                # Missing category and description
            })
    
    def test_edge_case_last_day_of_month(self):
        """Test expense on last day of month"""
        exp = Expense("2024-01-31", 25.50, "Food", "Dinner")
        assert exp.date == "2024-01-31"
    
    def test_edge_case_first_day_of_year(self):
        """Test expense on first day of year"""
        exp = Expense("2024-01-01", 25.50, "Food", "New Year lunch")
        assert exp.date == "2024-01-01"