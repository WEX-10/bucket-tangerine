# Task P0.4, P1.4, P3.5
# To Run: pytest rest/router_test.py

import pytest
from unittest.mock import Mock, patch

from rest.router import create_app


class TestCreateApp:
    """Test the create_app function"""

    # Patch the Flask class to mock Flask app creation
    @patch('rest.router.Flask')
    def test_create_app_flask_initialization(self, mock_flask):
        """Test that Flask app is initialized with correct parameters"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        # Fix: Make url_map.iter_rules() return an empty list
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):  # Suppress print output
            result = create_app()

        # ASSERT
        mock_flask.assert_called_once_with(
            'rest.router',  # This should be the module name, not __name__
            template_folder='../templates',
            static_folder='../static'
        )
        assert result == mock_app_instance

    # Task P0.4
    @patch('rest.router.Flask')
    @patch('rest.router.get_route')
    def test_create_app_generate_route_registration(self, mock_get_route, mock_flask):
        """Test that the /generate route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/generate", view_func=mock_get_route, methods=["GET"]
        )

    # Task P1.4
    @patch('rest.router.Flask')
    @patch('rest.router.create_route')
    def test_create_app_create_route_registration(self, mock_create_route, mock_flask):
        """Test that the /create route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/create", view_func=mock_create_route, methods=["GET", "POST"]
        )

    # Task P3.5
    @patch('rest.router.Flask')
    @patch('rest.router.vote_route')
    def test_create_app_vote_route_registration(self, mock_vote_route, mock_flask):
        """Test that the /api/vote route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/api/vote", view_func=mock_vote_route, methods=["POST"]
        )

if __name__ == '__main__':
    pytest.main([__file__])