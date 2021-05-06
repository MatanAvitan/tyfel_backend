from mongoengine import Document


def select_documents(collection: Document):
    returned_documents_list = []
    recieved_documents_list = list(collection.objects.filter())
    for item in recieved_documents_list:
        item_as_dict = item._data
        del item_as_dict['id']
        returned_documents_list.append(item_as_dict)
    return returned_documents_list


def select_document_by_id(collection: Document, _id: str):
    return collection.objects.get(id=_id)
