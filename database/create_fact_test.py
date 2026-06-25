# Tasks P1.4, P4.7
# To Run: pytest database/create_fact_test.py

import pytest
from unittest.mock import patch
import sys

from database.create_fact import create_fact
from fact import Fact


class TestCreateFact:
    """Test the create_fact function"""

    @patch.object(sys.modules['database.create_fact'], 'SQLiteConnectionProvider')
    def test_create_fact_success(self, mock_provider_class, mock_db):
        """Test successful fact creation"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return values
        mock_cursor.fetchone.return_value = (1, "Test fact", "science", 0, 0)

        # ACT
        # TODO: (Task P4.7) Call the create_fact function with fact and category test data as arguments

        # ASSERT
        # TODO: (Task P4.7) Check if returned fact fields, including category, match what we expect 

        # Verify SQL execution
        mock_cursor.execute.assert_called_once()
        mock_provider.commit.assert_called_once()

    @patch.object(sys.modules['database.create_fact'], 'SQLiteConnectionProvider')
    def test_create_fact_with_null_likes_dislikes(self, mock_provider_class, mock_db):
        """Test fact creation when likes/dislikes are NULL in database"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # TODO: Mock database return with NULL values for likes and dislikes

        # ACT
        # TODO: (Task P4.7) Call the create_fact function with fact and category test data as arguments

        # ASSERT
        # TODO: (Task P4.7) Check if returned fact fields, including category, match what we expect 

    @patch.object(sys.modules['database.create_fact'], 'SQLiteConnectionProvider')
    def test_create_fact_empty_strings(self, mock_provider_class, mock_db):
        """Test fact creation with empty strings"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        mock_cursor.fetchone.return_value = (4, "", "", 0, 0)

        # ACT
        # TODO: (Task P4.7) Call the create_fact function with empty string test data as arguments

        # ASSERT
        # TODO: (Task P4.7) Check if returned fact fields, including category, match what we expect 


if __name__ == '__main__':
    pytest.main([__file__])