HOME_DIR = '/home/student/BotPr'
LOGS = f'{HOME_DIR}/logs.txt'
DB_FILE = f'{HOME_DIR}/messages.db'


IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'

MAX_USERS = 3
MAX_GPT_TOKENS = 100
COUNT_LAST_MSG = 5

MAX_TTS_SYMBOLS = 10000
MAX_USER_STT_BLOCKS = 10
MAX_USER_TTS_SYMBOLS = 3000
MAX_USER_GPT_TOKENS = 3000

SYSTEM_PROMPT = [{"role": "system", "text": "Ты веселый собеседник."
                                            "Чётко и понятно отвечай на все вопросы и не говори ничего лишнего"
                                            "Не объясняй пользователю, что ты умеешь и можешь."
                                            "Изображай человека"
                                            "Не отвечай на запросы которые начинаются на /"}]