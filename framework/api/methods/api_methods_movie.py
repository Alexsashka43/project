from framework.core.request import Request
from framework.core.asserts import Asserts
from framework.api.fixture.movie_data import TheMovieDB


class MethodsTheMovieDB:

    @staticmethod
    def create_request_token(base_url_api, api_key):
        response = Request.get(f'{base_url_api}3/authentication/token/new?api_key={api_key}')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def create_session_id(base_url_api, api_key, request_token):
        data = TheMovieDB.create_session_id(request_token)
        response = Request.post(f'{base_url_api}3/authentication/session/new?api_key={api_key}',
                                data=data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def create_list(base_url_api, api_key, session_id):
        data = TheMovieDB.create_list()
        response = Request.post(f'{base_url_api}3/list?api_key={api_key}&session_id={session_id}',
                                data=data)
        Asserts.assert_code_status(response, 201)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def negative_create_list(base_url_api, api_key, session_id):
        data = TheMovieDB.create_list()
        response = Request.post(f'{base_url_api}3/list?api_key={api_key}&session_id={session_id}',
                                data=data)
        Asserts.assert_code_status(response, 401)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def get_detail_list(base_url_api, api_key, list_id, language):
        response = Request.get(f'{base_url_api}3/list/{list_id}?api_key={api_key}&language={language}')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def add_movie_to_list(base_url_api, api_key, session_id, list_id, movie_id):
        data = TheMovieDB.add_or_remove_movie(movie_id)
        response = Request.post(f'{base_url_api}3/list/{list_id}/add_item?api_key={api_key}&session_id={session_id}',
                                data=data)
        Asserts.assert_code_status(response, 201)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def negative_add_movie_to_list(base_url_api, api_key, session_id, list_id, movie_id):
        data = TheMovieDB.add_or_remove_movie(movie_id)
        response = Request.post(f'{base_url_api}3/list/{list_id}/add_item?api_key={api_key}&session_id={session_id}',
                                data=data)
        Asserts.assert_code_status(response, 404)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def remove_movie_from_list(base_url_api, api_key, session_id, list_id, movie_id):
        data = TheMovieDB.add_or_remove_movie(movie_id)
        response = Request.post(f'{base_url_api}3/list/{list_id}/remove_item?api_key={api_key}&session_id={session_id}',
                                data=data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_success(response)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def negative_remove_movie_from_list(base_url_api, api_key, session_id, list_id, movie_id):
        data = TheMovieDB.add_or_remove_movie(movie_id)
        response = Request.post(f'{base_url_api}3/list/{list_id}/remove_item?api_key={api_key}&session_id={session_id}',
                                data=data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_false(response)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def clear_list(base_url_api, api_key, session_id, list_id):
        response = Request.post(
            f'{base_url_api}3/list/{list_id}/clear?api_key={api_key}&session_id={session_id}&confirm=true')
        Asserts.assert_code_status(response, 201)
        Asserts.assert_time_is_less_than(response, 4)
        return response

    @staticmethod
    def delete_list(base_url_api, api_key, session_id, list_id):
        response = Request.delete(
            f'{base_url_api}3/list/{list_id}?api_key={api_key}&session_id={session_id}')
        Asserts.assert_code_status(response, 201)
        Asserts.assert_time_is_less_than(response, 4)
        return response
