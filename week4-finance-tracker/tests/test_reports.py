"""
Unit tests for ReportGenerator class
"""

import pytest
from datetime import datetime
from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.reports import ReportGenerator


class TestReportGenerator:
    """Test cases for ReportGenerator class"""
    
    def setup_method(self):
        """Setup test data"""
        self.manager = ExpenseManager()
        self.reporter = ReportGenerator(self.manager)
        
        # Add test expenses
        test_expenses = [
            Expense("2024-01-15", 100.00, "Food", "Groceries"),
            Expense("2024-01-16", 50.00, "Transport", "Fuel"),
            Expense("2024-01-17", 200.00, "Food", "Restaurant"),
            Expense("2024-01-18", 120.00, "Bills", "Electricity"),
            Expense("2024-02-01", 75.00, "Entertainment", "Movie"),
            Expense("2024-02-02", 150.00, "Food", "Supermarket"),
            Expense("2024-02-03", 25.00, "Transport", "Bus"),
            Expense("2024-03-01", 300.00, "Shopping", "Clothes"),
            Expense("2024-03-02", 80.00, "Food", "Lunch"),
            Expense("2024-03-03", 45.00, "Healthcare", "Medicine")
        ]
        
        for expense in test_expenses:
            self.manager.add_expense(expense)
    
    def test_generate_monthly_report_valid_month(self):
        """Test monthly report generation for valid month"""
        report = self.reporter.generate_monthly_report(2024, 1)
        
        assert report['year'] == 2024
        assert report['month'] == 1
        assert report['total_expenses'] == 470.00  # 100 + 50 + 200 + 120
        assert report['expense_count'] == 4
        assert report['average_expense'] == 117.50  # 470 / 4
        
        # Check category breakdown
        assert report['category_breakdown']['Food'] == 300.00
        assert report['category_breakdown']['Transport'] == 50.00
        assert report['category_breakdown']['Bills'] == 120.00
        
        # Check percentages
        total = report['total_expenses']
        assert report['category_percentages']['Food'] == pytest.approx((300 / total) * 100, 0.01)
        assert report['category_percentages']['Transport'] == pytest.approx((50 / total) * 100, 0.01)
        assert report['category_percentages']['Bills'] == pytest.approx((120 / total) * 100, 0.01)
    
    def test_generate_monthly_report_empty_month(self):
        """Test monthly report for month with no expenses"""
        report = self.reporter.generate_monthly_report(2024, 12)  # No expenses in December
        
        assert report['year'] == 2024
        assert report['month'] == 12
        assert report['total_expenses'] == 0
        assert report['expense_count'] == 0
        assert report['average_expense'] == 0
        assert report['category_breakdown'] == {}
        assert report['expenses'] == []
    
    def test_generate_monthly_report_february(self):
        """Test monthly report for February"""
        report = self.reporter.generate_monthly_report(2024, 2)
        
        assert report['year'] == 2024
        assert report['month'] == 2
        assert report['total_expenses'] == 250.00  # 75 + 150 + 25
        assert report['expense_count'] == 3
        assert report['average_expense'] == pytest.approx(83.33, 0.01)
    
    def test_generate_category_breakdown(self):
        """Test category breakdown generation"""
        breakdown = self.reporter.generate_category_breakdown()
        
        # Check totals
        total = sum(exp.amount for exp in self.manager.expenses)
        assert breakdown['total'] == total
        
        # Check category totals
        assert breakdown['category_totals']['Food'] == 630.00  # 100 + 200 + 150 + 80
        assert breakdown['category_totals']['Transport'] == 75.00  # 50 + 25
        assert breakdown['category_totals']['Bills'] == 120.00
        assert breakdown['category_totals']['Entertainment'] == 75.00
        assert breakdown['category_totals']['Shopping'] == 300.00
        assert breakdown['category_totals']['Healthcare'] == 45.00
        
        # Check percentages
        assert breakdown['percentages']['Food'] == pytest.approx((630 / total) * 100, 0.01)
        assert breakdown['percentages']['Transport'] == pytest.approx((75 / total) * 100, 0.01)
        assert breakdown['percentages']['Bills'] == pytest.approx((120 / total) * 100, 0.01)
        assert breakdown['percentages']['Entertainment'] == pytest.approx((75 / total) * 100, 0.01)
        assert breakdown['percentages']['Shopping'] == pytest.approx((300 / total) * 100, 0.01)
        assert breakdown['percentages']['Healthcare'] == pytest.approx((45 / total) * 100, 0.01)
    
    def test_generate_category_breakdown_empty(self):
        """Test category breakdown with empty expense manager"""
        empty_manager = ExpenseManager()
        empty_reporter = ReportGenerator(empty_manager)
        
        breakdown = empty_reporter.generate_category_breakdown()
        
        assert breakdown['total'] == 0
        assert breakdown['category_totals'] == {}
        assert breakdown['percentages'] == {}
    
    def test_generate_statistics(self):
        """Test statistics generation"""
        stats = self.reporter.generate_statistics()
        
        # Basic statistics
        assert stats['expense_count'] == 10
        assert stats['total_expenses'] == 1245.00  # Sum of all test expenses
        assert stats['average_expense'] == 124.50  # 1245 / 10
        
        # Largest expense
        assert stats['largest_expense']['amount'] == 300.00
        assert stats['largest_expense']['category'] == "Shopping"
        
        # Smallest expense
        assert stats['smallest_expense']['amount'] == 25.00
        assert stats['smallest_expense']['category'] == "Transport"
        
        # Monthly totals
        assert stats['monthly_totals']['2024-1'] == 470.00
        assert stats['monthly_totals']['2024-2'] == 250.00
        assert stats['monthly_totals']['2024-3'] == 425.00
        
        # Averages
        assert stats['monthly_average'] == pytest.approx((470 + 250 + 425) / 3, 0.01)
        
        # Top category
        assert stats['top_category'] == "Food"
    
    def test_generate_statistics_empty(self):
        """Test statistics with empty expense manager"""
        empty_manager = ExpenseManager()
        empty_reporter = ReportGenerator(empty_manager)
        
        stats = empty_reporter.generate_statistics()
        
        assert stats['expense_count'] == 0
        assert stats['total_expenses'] == 0
        assert stats['average_expense'] == 0
        assert stats['largest_expense'] is None
        assert stats['smallest_expense'] is None
        assert stats['monthly_average'] == 0
        assert stats['daily_average'] == 0
        assert stats['top_category'] is None
    
    def test_generate_text_visualization(self):
        """Test text visualization generation"""
        breakdown = self.reporter.generate_category_breakdown()
        visualization = self.reporter.generate_text_visualization(breakdown, width=20)
        
        # Check that visualization contains expected elements
        assert "Category Breakdown" in visualization
        assert "Food" in visualization
        assert "$630.00" in visualization
        assert "█" in visualization  # Bar characters
        assert "%" in visualization  # Percentage symbols
    
    def test_generate_text_visualization_empty(self):
        """Test text visualization with empty data"""
        empty_manager = ExpenseManager()
        empty_reporter = ReportGenerator(empty_manager)
        
        breakdown = empty_reporter.generate_category_breakdown()
        visualization = empty_reporter.generate_text_visualization(breakdown)
        
        assert visualization == "No data available for visualization."
    
    def test_generate_text_visualization_zero_total(self):
        """Test text visualization with zero total"""
        breakdown = {
            'category_totals': {'Food': 0, 'Transport': 0},
            'total': 0
        }
        visualization = self.reporter.generate_text_visualization(breakdown)
        
        assert visualization == "No expenses recorded."
    
    def test_generate_monthly_summary(self):
        """Test monthly summary generation"""
        summary = self.reporter.generate_monthly_summary(2024)
        
        assert summary['year'] == 2024
        assert summary['yearly_total'] == 1145.00  # Jan + Feb + Mar
        assert summary['yearly_count'] == 10
        assert summary['yearly_average'] == 114.50
        
        # Check monthly data
        assert summary['monthly_data'][1]['total'] == 470.00
        assert summary['monthly_data'][2]['total'] == 250.00
        assert summary['monthly_data'][3]['total'] == 425.00
        
        # Check highest and lowest months
        assert summary['highest_month'] == 1  # January has highest total
        assert summary['lowest_month'] == 2   # February has lowest total
    
    def test_generate_monthly_summary_empty_year(self):
        """Test monthly summary for year with no expenses"""
        summary = self.reporter.generate_monthly_summary(2023)  # No expenses in 2023
        
        assert summary['year'] == 2023
        assert summary['yearly_total'] == 0
        assert summary['yearly_count'] == 0
        assert summary['yearly_average'] == 0
        assert summary['highest_month'] is None
        assert summary['lowest_month'] is None
        
        # All months should have zero totals
        for month in range(1, 13):
            assert summary['monthly_data'][month]['total'] == 0
            assert summary['monthly_data'][month]['count'] == 0
            assert summary['monthly_data'][month]['average'] == 0
    
    def test_single_expense_statistics(self):
        """Test statistics with only one expense"""
        single_manager = ExpenseManager()
        single_reporter = ReportGenerator(single_manager)
        
        single_manager.add_expense(Expense("2024-01-01", 100.00, "Food", "Test"))
        
        stats = single_reporter.generate_statistics()
        
        assert stats['expense_count'] == 1
        assert stats['total_expenses'] == 100.00
        assert stats['average_expense'] == 100.00
        assert stats['largest_expense']['amount'] == 100.00
        assert stats['smallest_expense']['amount'] == 100.00
        assert stats['monthly_average'] == 100.00
        assert stats['daily_average'] == 100.00
    
    def test_expenses_same_category(self):
        """Test with all expenses in same category"""
        same_category_manager = ExpenseManager()
        same_category_reporter = ReportGenerator(same_category_manager)
        
        for i in range(5):
            same_category_manager.add_expense(
                Expense(f"2024-01-{i+1:02d}", (i+1) * 10, "Food", f"Meal {i+1}")
            )
        
        breakdown = same_category_reporter.generate_category_breakdown()
        
        assert breakdown['total'] == 150.00  # 10+20+30+40+50
        assert breakdown['category_totals']['Food'] == 150.00
        assert breakdown['percentages']['Food'] == 100.00
    
    def test_expenses_same_date(self):
        """Test with multiple expenses on same date"""
        same_date_manager = ExpenseManager()
        same_date_reporter = ReportGenerator(same_date_manager)
        
        same_date_manager.add_expense(Expense("2024-01-01", 100.00, "Food", "Breakfast"))
        same_date_manager.add_expense(Expense("2024-01-01", 200.00, "Transport", "Taxi"))
        same_date_manager.add_expense(Expense("2024-01-01", 50.00, "Entertainment", "Movie"))
        
        stats = same_date_reporter.generate_statistics()
        
        assert stats['expense_count'] == 3
        assert stats['total_expenses'] == 350.00
        assert stats['daily_average'] == 350.00  # All on same day
    
    def test_category_percentages_rounding(self):
        """Test that percentages are calculated correctly with rounding"""
        rounding_manager = ExpenseManager()
        rounding_reporter = ReportGenerator(rounding_manager)
        
        # Add expenses that will result in non-integer percentages
        rounding_manager.add_expense(Expense("2024-01-01", 33.33, "Food", "Item 1"))
        rounding_manager.add_expense(Expense("2024-01-02", 33.33, "Transport", "Item 2"))
        rounding_manager.add_expense(Expense("2024-01-03", 33.33, "Entertainment", "Item 3"))
        
        breakdown = rounding_reporter.generate_category_breakdown()
        
        # Each should be approximately 33.33%
        for category in ["Food", "Transport", "Entertainment"]:
            assert breakdown['percentages'][category] == pytest.approx(33.33, 0.01)