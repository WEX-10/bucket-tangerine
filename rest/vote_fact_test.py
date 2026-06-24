# Task P3.5

import pytest
from unittest.mock import Mock, patch
import sys
import json

from flask import Flask
from rest.vote_fact import vote_route
from fact import Fact


class TestVoteFactRoute:
    """Test the vote_route function"""

    @patch('rest.vote_fact.vote_fact')
    def test_vote_route_like_success(self, mock_vote_fact, app):
        """Test successful like vote"""
        # ARRANGE
        mock_fact = Fact(id=1, fact="Test fact", category="science", likes=6, dislikes=2)
        mock_vote_fact.return_value = mock_fact

        json_data = {"fact_id": 1, "vote_type": "like"}

        with app.test_request_context('/', method='POST', json=json_data):
            with patch('rest.vote_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "json response"

                # ACT
                result = vote_route()

                # ASSERT
                mock_vote_fact.assert_called_once_with(1, "like")
                mock_jsonify.assert_called_once_with({
                    "fact_id": 1,
                    "new_count": 6,  # updated_fact.likes (like vote)
                    "likes": 6,
                    "dislikes": 2
                })
                assert result == ("json response", 200)

    @patch('rest.vote_fact.vote_fact')
    def test_vote_route_dislike_success(self, mock_vote_fact, app):
        """Test successful dislike vote"""
        # ARRANGE
        mock_fact = Fact(id=2, fact="Another fact", category="history", likes=5, dislikes=8)
        mock_vote_fact.return_value = mock_fact

        json_data = {"fact_id": 2, "vote_type": "dislike"}

        with app.test_request_context('/', method='POST', json=json_data):
            with patch('rest.vote_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "dislike response"

                # ACT
                # TODO: (Task P3.5) Call the vote_route function

                # ASSERT
                # TODO: (Task P3.5) Verify vote_fact was called with the correct arguments
                # TODO: (Task P3.5) Verify the JSON response contains the correct data and 200 status code

    @patch('rest.vote_fact.vote_fact')
    def test_vote_route_value_error_handling(self, mock_vote_fact, app):
        """Test handling of ValueError from vote_fact function"""
        # ARRANGE
        mock_vote_fact.side_effect = ValueError("Invalid vote type")
        json_data = {"fact_id": 1, "vote_type": "invalid"}

        with app.test_request_context('/', method='POST', json=json_data):
            with patch('rest.vote_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "error response"

                # ACT
                # TODO: (Task P3.5) Call the vote_route function

                # ASSERT
                # TODO: (Task P3.5) Verify vote_fact was called with the invalid vote type
                # TODO: (Task P3.5) Verify the error JSON response and 400 status code

if __name__ == '__main__':
    pytest.main([__file__])