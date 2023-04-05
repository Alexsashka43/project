class TheMovieDB:

    @staticmethod
    def create_request_token(api_key):
        dict_json = {
            "api_key": api_key
        }
        return dict_json

    @staticmethod
    def create_session_id(request_token):
        dict_json = {
            "request_token": request_token
        }
        return dict_json

    @staticmethod
    def create_list():
        dict_json = {
            "name": "Test list.",
            "description": "Test description.",
            "language": "en"
        }
        return dict_json

    @staticmethod
    def add_or_remove_movie(movie_id):
        dict_json = {
            "media_id": f"{movie_id}"
        }
        return dict_json
