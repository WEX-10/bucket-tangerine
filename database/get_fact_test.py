# Tasks P0.4, P4.7, P5.9

import pytest
from unittest.mock import patch
import sys

from database.get_fact import get_fact, get_facts_by_category
from fact import Fact


class TestGetFact:
    """Test the get_fact function"""

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_success(self, mock_provider_class, mock_db):
        """Test successful fact retrieval"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return values
        mock_cursor.fetchone.return_value = (1, "Random test fact", "science", 5, 2)

        # ACT
        result = get_fact()

        # ASSERT
        assert isinstance(result, Fact)
        assert result.id == 1
        assert result.fact == "Random test fact"
        assert result.category == "science"
        assert result.likes == 5
        assert result.dislikes == 2

        # Verify SQL execution
        mock_cursor.execute.assert_called_once_with(
            "SELECT id, fact, category, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;"
        )

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_with_null_likes_dislikes(self, mock_provider_class, mock_db):
        """Test fact retrieval when likes/dislikes are NULL in database"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return with NULL values
        mock_cursor.fetchone.return_value = (2, "Another random fact", "history", None, None)

        # ACT
        # TODO: Call the get_fact function

        # ASSERT
        # TODO: Verify that the Fact object is created with default values for likes/dislikes

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_no_results_found(self, mock_provider_class, mock_db):
        """Test behavior when no facts are found in database"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock no result returned
        mock_cursor.fetchone.return_value = None

        # ACT
       # TODO: Call the get_fact function

        # ASSERT
        # TODO: Verify that the Fact object is created with default values for likes/dislikes

        # Verify SQL execution
        mock_cursor.execute.assert_called_once()

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_fact_database_error(self, mock_provider_class, mock_db):
        """Test handling of database errors during fact retrieval"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database error
        mock_cursor.execute.side_effect = Exception("Database connection failed")

        # ACT & ASSERT
        # TODO: (Task P0.4) Call get_fact and verify it raises an exception with the correct message


class TestGetFactsByCategory:
    """Test the get_facts_by_category function for Task P5.9"""

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_facts_by_category_success(self, mock_provider_class, mock_db):
        """Test successful retrieval of categories"""
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return values
        mock_cursor.fetchall.return_value = [
            ("science",),
            ("history",),
            ("math",)
        ]

        result = get_facts_by_category()
        assert result == ["science", "history", "math"]
        mock_cursor.execute.assert_called_once()

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_facts_by_category_empty(self, mock_provider_class, mock_db):
        """Test retrieval when no categories exist"""
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return with empty list
        mock_cursor.fetchall.return_value = []

        # ACT
        # TODO: (Task P5.9) Call the get_facts_by_category function

        # ASSERT
        # TODO: (Task P5.9) Verify the result is an empty list

    @patch.object(sys.modules['database.get_fact'], 'SQLiteConnectionProvider')
    def test_get_facts_by_category_database_error(self, mock_provider_class, mock_db):
        """Test handling of database errors during category retrieval"""
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database error
        mock_cursor.execute.side_effect = Exception("Database error")

        # ACT & ASSERT
        # TODO: (Task P5.9) Call get_facts_by_category and verify it raises an exception

if __name__ == '__main__':
    pytest.main([__file__])