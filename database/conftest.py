import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_db():
    """Pre-wired SQLite mock provider and cursor.

    Returns a tuple of (mock_provider, mock_cursor) with the context manager
    protocol already configured. Use it in database tests like this:

        @patch.object(sys.modules['database.xxx'], 'SQLiteConnectionProvider')
        def test_something(self, mock_provider_class, mock_db):
            mock_provider, mock_cursor = mock_db
            mock_provider_class.return_value = mock_provider
            ...
    """
    mock_provider = Mock()
    mock_cursor = Mock()
    mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
    mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)
    return mock_provider, mock_cursor
