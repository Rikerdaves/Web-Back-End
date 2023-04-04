from persistence.model import Document
from persistence.crud import create_document, read_document, update_document, delete_document

__all__ = [Document, 
           create_document, 
           read_document, 
           update_document, 
           delete_document]