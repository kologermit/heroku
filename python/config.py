# TOKEN = "1280854719:AAF2TPbUupfyTxPDZIThKpy-6JInwkViHZ0"
# TOKEN = "1375982367:AAFWkCEWt4A67Bs2REOwM-e2AdQEpYfd7Fw" # Основной
import os
API_KEY = os.environ.get('WEATHER_API_KEY')
TOKEN = os.environ.get('TELEGRAM_TOKEN')
mysql_config = {
	"user": os.environ.get('DB_LOGIN'),
	"password": os.environ.get('DB_PASSWORD'),
	"host": os.environ.get('DB_HOST'),
	"database": os.environ.get('DB_DATABASE')
}
# mysql_config = {
# 	"user": 'u8igkxzwd81yntdn',
# 	"password": 'Jgq5nufz54qFkDYVQg8e',
# 	"host": 'beyeskww9gu4pwr7pwoc-mysql.services.clever-cloud.com',
# 	"database": 'beyeskww9gu4pwr7pwoc'
# }