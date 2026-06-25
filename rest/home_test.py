# THIS FILE IS NOT A TASK, YOU CAN IGNORE IT. IT IS A TEST FILE FOR THE REST HOME ROUTE.
import pytest
from unittest.mock import patch
from rest.home import home_route


class TestHomeRoute:
    """Test the home_route function"""

    def test_home_route_success(self, app):
        """Test successful home route call"""
        with app.test_request_context('/'):
            with patch('rest.home.render_template') as mock_render:
                mock_render.return_value = "home template content"

                # ACT
                result = home_route()

                # ASSERT
                assert result == "home template content"
                mock_render.assert_called_once_with("home.html")

    def test_home_route_template_error(self, app):
        """Test handling of template rendering errors"""
        with app.test_request_context('/'):
            with patch('rest.home.render_template') as mock_render:
                mock_render.side_effect = Exception("Template not found")

                # ACT & ASSERT
                with pytest.raises(Exception) as exc_info:
                    home_route()

                assert "Template not found" in str(exc_info.value)
                mock_render.assert_called_once_with("home.html")

if __name__ == '__main__':
    pytest.main([__file__])