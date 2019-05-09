class SearchFilters():
    def __init__(self):
        self.phone_list = None
        self.search_query = None

    def set_phone_list(self,query_list):
        self.phone_list = query_list

    def get_phone_list(self):
        return self.phone_list

    def set_search_query(self,query):
        self.search_query = query

    def get_search_query(self):
        return self.search_query
