import json
import os
path_name_json = 'framework/resources/json/'


class Data:

    # записать файл
    @staticmethod
    def file_write(data_json, filename):
        if not os.path.exists(path_name_json):
            os.makedirs(path_name_json)

        with open(f"{path_name_json}{filename}", "w", encoding='utf-8') as write_file:
            json.dump(data_json, write_file, indent=2, ensure_ascii=False)

    # прочитать файл
    @staticmethod
    def file_open(filename):
        with open(f"{path_name_json}{filename}", "r", encoding='utf-8') as read_file:
            return json.load(read_file)

    @staticmethod
    def get_json_object(dict_json):
        return json.dumps(dict_json)
