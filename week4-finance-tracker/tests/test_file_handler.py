"""
Unit tests for FileHandler class
"""

import pytest
import os
import json
import tempfile
import shutil
from finance_tracker.expense import Expense
from finance_tracker.file_handler import FileHandler


class TestFileHandler:
    """Test cases for FileHandler class"""
    
    def setup_method(self):
        """Setup test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.data_file = os.path.join(self.test_dir, "expenses.json")
        self.handler = FileHandler(data_dir=self.test_dir, data_file="expenses.json")
    
    def teardown_method(self):
        """Cleanup test environment"""
        shutil.rmtree(self.test_dir)
    
    def test_initialization(self):
        """Test FileHandler initialization"""
        assert self.handler.data_dir == self.test_dir
        assert self.handler.data_file == self.data_file
        assert os.path.exists(os.path.join(self.test_dir, "backup"))
        assert os.path.exists(os.path.join(self.test_dir, "exports"))
    
    def test_save_expenses(self):
        """Test saving expenses to file"""
        expenses = [
            Expense("2024-01-15", 25.50, "Food", "Lunch"),
            Expense("2024-01-16", 15.00, "Transport", "Bus fare")
        ]
        
        # Save expenses
        result = self.handler.save_expenses(expenses)
        assert result == True
        assert os.path.exists(self.data_file)
        
        # Verify file content
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        
        assert len(data) == 2
        assert data[0]['date'] == "2024-01-15"
        assert data[0]['amount'] == 25.50
        assert data[1]['date'] == "2024-01-16"
        assert data[1]['amount'] == 15.00
    
    def test_save_empty_expenses(self):
        """Test saving empty expenses list"""
        result = self.handler.save_expenses([])
        assert result == True
        assert os.path.exists(self.data_file)
        
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        
        assert data == []
    
    def test_load_expenses_file_not_exist(self):
        """Test loading when file doesn't exist"""
        data = self.handler.load_expenses()
        assert data == []
    
    def test_load_expenses(self):
        """Test loading expenses from file"""
        # Create test file
        test_data = [
            {
                'date': '2024-01-15',
                'amount': 25.50,
                'category': 'Food',
                'description': 'Lunch'
            },
            {
                'date': '2024-01-16',
                'amount': 15.00,
                'category': 'Transport',
                'description': 'Bus fare'
            }
        ]
        
        with open(self.data_file, 'w') as f:
            json.dump(test_data, f)
        
        # Load expenses
        data = self.handler.load_expenses()
        assert len(data) == 2
        assert data[0]['date'] == "2024-01-15"
        assert data[0]['amount'] == 25.50
        assert data[1]['date'] == "2024-01-16"
        assert data[1]['amount'] == 15.00
    
    def test_load_corrupted_json(self):
        """Test loading corrupted JSON file"""
        # Create corrupted JSON file
        with open(self.data_file, 'w') as f:
            f.write("This is not valid JSON {")
        
        data = self.handler.load_expenses()
        # Should return empty list or attempt backup restore
        assert data == [] or isinstance(data, list)
    
    def test_backup_creation(self):
        """Test backup creation"""
        expenses = [
            Expense("2024-01-15", 25.50, "Food", "Lunch")
        ]
        
        # Save to create file
        self.handler.save_expenses(expenses)
        
        # Check backup was created
        backup_dir = os.path.join(self.test_dir, "backup")
        backup_files = os.listdir(backup_dir)
        assert len(backup_files) >= 1
        assert backup_files[0].startswith("expenses_backup_")
        assert backup_files[0].endswith(".json")
    
    def test_multiple_backups_limit(self):
        """Test backup cleanup (keep only 5 most recent)"""
        expenses = [Expense("2024-01-15", 25.50, "Food", "Lunch")]
        
        # Save multiple times to create multiple backups
        for i in range(10):
            self.handler.save_expenses(expenses)
        
        backup_dir = os.path.join(self.test_dir, "backup")
        backup_files = os.listdir(backup_dir)
        
        # Should keep only 5 most recent backups
        assert len(backup_files) == 5
    
    def test_csv_export(self):
        """Test CSV export functionality"""
        expenses = [
            Expense("2024-01-15", 25.50, "Food", "Lunch"),
            Expense("2024-01-16", 15.00, "Transport", "Bus fare")
        ]
        
        # Export to CSV
        export_dir = os.path.join(self.test_dir, "exports")
        csv_file = os.path.join(export_dir, "test_export.csv")
        
        result = self.handler.export_to_csv(expenses, csv_file)
        assert result == True
        assert os.path.exists(csv_file)
        
        # Verify CSV content
        with open(csv_file, 'r') as f:
            lines = f.readlines()
        
        assert len(lines) == 3  # Header + 2 data rows
        assert "date,amount,category,description" in lines[0]
        assert "2024-01-15" in lines[1]
        assert "25.5" in lines[1]
    
    def test_csv_export_auto_filename(self):
        """Test CSV export with auto-generated filename"""
        expenses = [
            Expense("2024-01-15", 25.50, "Food", "Lunch")
        ]
        
        result = self.handler.export_to_csv(expenses)
        assert result == True
        
        export_dir = os.path.join(self.test_dir, "exports")
        csv_files = [f for f in os.listdir(export_dir) if f.endswith('.csv')]
        assert len(csv_files) == 1
        assert csv_files[0].startswith("expenses_export_")
    
    def test_list_backups_empty(self):
        """Test listing backups when none exist"""
        backups = self.handler.list_backups()
        assert backups == []
    
    def test_list_backups(self):
        """Test listing available backups"""
        # Create a test backup file
        backup_dir = os.path.join(self.test_dir, "backup")
        test_backup = os.path.join(backup_dir, "expenses_backup_20240101_120000.json")
        
        test_data = [{'date': '2024-01-01', 'amount': 10.0, 'category': 'Test', 'description': 'Test'}]
        with open(test_backup, 'w') as f:
            json.dump(test_data, f)
        
        backups = self.handler.list_backups()
        assert len(backups) == 1
        assert backups[0]['filename'] == "expenses_backup_20240101_120000.json"
    
    def test_restore_backup(self):
        """Test restoring from backup"""
        # Create original file
        original_data = [{'date': '2024-01-01', 'amount': 10.0, 'category': 'Original', 'description': 'Original'}]
        with open(self.data_file, 'w') as f:
            json.dump(original_data, f)
        
        # Create backup file
        backup_dir = os.path.join(self.test_dir, "backup")
        backup_file = os.path.join(backup_dir, "expenses_backup_20240101_120000.json")
        backup_data = [{'date': '2024-01-02', 'amount': 20.0, 'category': 'Backup', 'description': 'Backup'}]
        
        with open(backup_file, 'w') as f:
            json.dump(backup_data, f)
        
        # Restore from backup
        result = self.handler.restore_backup("expenses_backup_20240101_120000.json")
        assert result == True
        
        # Verify data was restored
        with open(self.data_file, 'r') as f:
            restored_data = json.load(f)
        
        assert restored_data[0]['date'] == "2024-01-02"
        assert restored_data[0]['amount'] == 20.0
    
    def test_restore_nonexistent_backup(self):
        """Test restoring from non-existent backup"""
        result = self.handler.restore_backup("nonexistent_backup.json")
        assert result == False
    
    def test_save_permission_error(self):
        """Test handling of permission errors"""
        # Create a read-only directory
        read_only_dir = os.path.join(self.test_dir, "readonly")
        os.makedirs(read_only_dir)
        os.chmod(read_only_dir, 0o444)  # Read-only
        
        handler = FileHandler(data_dir=read_only_dir, data_file="expenses.json")
        expenses = [Expense("2024-01-15", 25.50, "Food", "Lunch")]
        
        result = handler.save_expenses(expenses)
        assert result == False  # Should fail due to permission error
        
        # Clean up permissions for teardown
        os.chmod(read_only_dir, 0o755)
    
    def test_load_permission_error(self):
        """Test handling of permission errors when loading"""
        # Create a file with no read permission
        test_file = os.path.join(self.test_dir, "noread.json")
        with open(test_file, 'w') as f:
            json.dump([], f)
        
        os.chmod(test_file, 0o000)  # No permissions
        
        handler = FileHandler(data_dir=self.test_dir, data_file="noread.json")
        data = handler.load_expenses()
        
        # Should return empty list due to permission error
        assert data == []
        
        # Restore permissions for cleanup
        os.chmod(test_file, 0o644)
    
    def test_ensure_directories_multiple_calls(self):
        """Test that ensure_directories can be called multiple times safely"""
        # This should not raise any errors
        self.handler._ensure_directories()
        self.handler._ensure_directories()
        self.handler._ensure_directories()
        
        # Directories should still exist
        assert os.path.exists(os.path.join(self.test_dir, "backup"))
        assert os.path.exists(os.path.join(self.test_dir, "exports"))