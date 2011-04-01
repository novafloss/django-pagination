def get_page(self):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """
    try:
        return int(self.REQUEST['page'])
    except (KeyError, ValueError, TypeError):
        return 1
        
def get_pagination(self):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current pagination.
    """
    try:
        return int(self.REQUEST['pagination'])
    except (KeyError, ValueError, TypeError):
        return None

class PaginationMiddleware(object):
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def process_request(self, request):
        request.__class__.page = property(get_page)
        request.__class__.pagination = property(get_pagination)