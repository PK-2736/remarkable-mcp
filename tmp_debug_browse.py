import asyncio
from unittest.mock import Mock, patch
from remarkable_mcp.server import mcp

async def main():
    mock_client = Mock()
    mock_doc = Mock()
    mock_doc.VissibleName = 'Study Notes'
    mock_doc.ID = 'doc-123'
    mock_doc.Parent = ''
    mock_doc.is_folder = False
    mock_doc.ModifiedClient = '2024-01-15'
    mock_doc.tags = []
    mock_client.get_meta_items.return_value = [mock_doc]
    mock_client.download.return_value = b'zip-bytes'
    with patch('remarkable_mcp.tools.get_rmapi', return_value=mock_client):
        with patch('remarkable_mcp.tools.get_document_page_count', return_value=7):
            with patch('remarkable_mcp.tools._is_cloud_archived', return_value=False):
                result = await mcp.call_tool('remarkable_browse', {'path': '/'})
                print(result[0][0].text)

asyncio.run(main())
