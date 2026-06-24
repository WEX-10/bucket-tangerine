# Task P5.9

import pytest
from unittest.mock import patch

from rest.get_facts_by_category import get_facts_by_category_route


class TestGetFactsByCategoryRoute:
	"""Test the get_facts_by_category_route function"""

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
			pass  # TODO: (Task P5.9) Call the get_facts_by_category_route function

		# TODO: (Task P5.9) Verify a 200 response with an empty categories list

	@patch('rest.get_facts_by_category.get_facts_by_category')
	def test_get_facts_by_category_route_database_error(self, mock_get_facts_by_category, app):
		"""Test propagation of database errors"""
		mock_get_facts_by_category.side_effect = Exception("Database connection failed")

		with app.test_request_context('/api/categories'):
			pass  # TODO: (Task P5.9) Call get_facts_by_category_route and verify it raises an exception


if __name__ == '__main__':
	pytest.main([__file__])