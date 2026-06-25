# Task P3.5
# To Run: pytest database/vote_fact_test.py

import pytest
from unittest.mock import Mock, patch
import sys

from database.vote_fact import vote_fact
from fact import Fact


class TestVoteFact:
    """Test the vote_fact function"""

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.vote_fact'], 'SQLiteConnectionProvider')
    def test_vote_fact_like_success(self, mock_provider_class, mock_db):
        """Test successful like vote on a fact"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return values after like
        mock_cursor.fetchone.return_value = (1, "Test fact", "science", 6, 2)

        # ACT
        result = vote_fact(1, "like")

        # ASSERT
        assert isinstance(result, Fact)
        assert result.id == 1
        assert result.fact == "Test fact"
        assert result.category == "science"
        assert result.likes == 6
        assert result.dislikes == 2

        # Verify SQL execution
        assert mock_cursor.execute.call_count == 2
        # Check like update query
        mock_cursor.execute.assert_any_call(
            "UPDATE facts SET likes = likes + 1 WHERE id = ?;",
            (1,)
        )
        # Check select query
        mock_cursor.execute.assert_any_call(
            "SELECT id, fact, category, likes, dislikes FROM facts WHERE id = ?;",
            (1,)
        )
        mock_provider.commit.assert_called_once()

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.vote_fact'], 'SQLiteConnectionProvider')
    def test_vote_fact_dislike_success(self, mock_provider_class, mock_db):
        """Test successful dislike vote on a fact"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock database return values after dislike
        mock_cursor.fetchone.return_value = (2, "Another fact", "history", 5, 8)

        # ACT
        # TODO: Call the vote_fact function with a dislike vote

        # ASSERT
        # TODO: Verify the returned Fact object has the expected values
        # TODO: Verify SQL execution (execute called twice, correct UPDATE and SELECT queries, commit called once)

    # Patch the SQLiteConnectionProvider to mock database interactions
    @pytest.mark.parametrize("invalid_vote", ["invalid", ""])
    @patch.object(sys.modules['database.vote_fact'], 'SQLiteConnectionProvider')
    def test_vote_fact_invalid_vote_type(self, mock_provider_class, mock_db, invalid_vote):
        """Test error handling for invalid or empty vote types"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # ACT
        with pytest.raises(ValueError) as exc_info:
            pass  # TODO: Call the vote_fact function with invalid_vote as the vote type

        # ASSERT
        assert "" in str(exc_info.value) # TODO: Check that the error message contains the expected text

        # Verify no SQL execution for update (only cursor setup)
        mock_cursor.execute.assert_not_called()
        mock_provider.commit.assert_not_called()

    # Patch the SQLiteConnectionProvider to mock database interactions
    @patch.object(sys.modules['database.vote_fact'], 'SQLiteConnectionProvider')
    def test_vote_fact_with_null_likes_dislikes(self, mock_provider_class, mock_db):
        """Test voting on fact with NULL likes/dislikes"""
        # ARRANGE
        mock_provider, mock_cursor = mock_db
        mock_provider_class.return_value = mock_provider

        # Mock result with NULL values
        mock_cursor.fetchone.return_value = (3, "Fact with nulls", "trivia", None, None)

        # ACT
        # TODO: Call the vote_fact function with a like or dislike vote

        # ASSERT
        # TODO: Verify that the returned Fact object handles NULL likes/dislikes appropriately

if __name__ == '__main__':
    pytest.main([__file__])