import pytest
from unittest.mock import patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
from rest.get_facts_by_category import get_facts_by_category_route


class TestGetFactsByCategoryRoute:
	"""Test the get_facts_by_category_route function"""

	@pytest.fixture
	def app(self):
		"""Create test Flask app"""
		app = Flask(__name__)
		app.config['TESTING'] = True
		return app

	@patch('rest.get_facts_by_category.get_facts_by_category')
	def test_get_facts_by_category_route_success(self, mock_get_facts_by_category, app):
		"""Test successful category retrieval"""
		mock_get_facts_by_category.return_value = ["animal", "food", "science"]

		with app.test_request_context('/api/categories'):
			response = get_facts_by_category_route()

		assert response.status_code == 200
		assert response.get_json() == {"categories": ["animal", "food", "science"]}
		mock_get_facts_by_category.assert_called_once_with()

	@patch('rest.get_facts_by_category.get_facts_by_category')
	def test_get_facts_by_category_route_empty_list(self, mock_get_facts_by_category, app):
		"""Test category retrieval when no categories exist"""
		mock_get_facts_by_category.return_value = []

		with app.test_request_context('/api/categories'):
			response = get_facts_by_category_route()

		assert response.status_code == 200
		assert response.get_json() == {"categories": []}
		mock_get_facts_by_category.assert_called_once_with()

	@patch('rest.get_facts_by_category.get_facts_by_category')
	def test_get_facts_by_category_route_database_error(self, mock_get_facts_by_category, app):
		"""Test propagation of database errors"""
		mock_get_facts_by_category.side_effect = Exception("Database connection failed")

		with app.test_request_context('/api/categories'):
			with pytest.raises(Exception) as exc_info:
				get_facts_by_category_route()

		assert "Database connection failed" in str(exc_info.value)
		mock_get_facts_by_category.assert_called_once_with()


if __name__ == '__main__':
	pytest.main([__file__])