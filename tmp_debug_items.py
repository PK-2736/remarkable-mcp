from unittest.mock import Mock
from remarkable_mcp.api import get_items_by_parent

mock_doc = Mock()
mock_doc.VissibleName = 'Study Notes'
mock_doc.ID = 'doc-123'
mock_doc.Parent = ''
mock_doc.is_folder = False
mock_doc.ModifiedClient = '2024-01-15'
mock_doc.tags = []
print(get_items_by_parent([mock_doc]))
