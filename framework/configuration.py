from random import randint


class User:
    LOGIN: str = 'qwerty43567'
    PASSWORD: str = 'movietest'
    API_KEY: str = '446acb6bd624b536c2cfd6b8daf57f92'
    ACCESS_TOKEN:str = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NDZhY2I2YmQ2MjRiNTM2YzJjZmQ2YjhkYWY1N2Y5MiIsInN1YiI6IjY0MGEzYWVlNzc3NmYwMDA3YjU2YWExOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.arXr33Zgra-JbnreZNYLk50a0I78-po57JV1qGsmVoQ'


class RegForm:
    FIRST_NAME: str = 'FIRST_NAME'
    LAST_NAME: str = 'LAST_NAME'
    EMAIL: str = 'test@mail.com'
    RANDOM_EMAIL = f'test{randint(0, 99999)}test@mail.com'
    PHONE: str = '+91112345678'
    LOGIN: str = 'test'
    PASSWORD: str = 'test'


class UserList:
    NAME: str = 'test'
    DESCRIPTION: str = 'description'
    NAME_FILM: str = 'Avatar: The Way of Water'
