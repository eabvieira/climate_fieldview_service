import os

'''
Ambiente
'''
STAGE = os.getenv('STAGE')
CLUSTER_URL = os.getenv('CLUSTER_URL')

'''
Versão do Microserviço

    MAJOR = nova versão da API
    MINOR = alteração/inclusão de endpoint
'''
build_id = os.getenv('BUILD_ID') or '0'
MAJOR_VERSION = '1'
MINOR_VERSION = '1'
BUILD_VERSION = build_id+'-'+STAGE
VERSION_STR = MAJOR_VERSION+'.'+MINOR_VERSION+'.'+BUILD_VERSION


'''
Database NOSQL
'''
MONGODB_URL = os.getenv('MONGODB_URL')

'''
Service Slug
'''
SERVICE_SLUG = 'climate_fieldview_service'
os.environ["SERVICE_SLUG"] = SERVICE_SLUG

'''
Service Auth Url - Para autenticar na documentação /docs 
'''
if os.getenv('DEV'):
    DEV = 1
    AUTH_URL = 'http://localhost'+'/'+STAGE+'/auth_service/auth/login'
    os.environ["AUTH_URL"] = AUTH_URL
else:
    DEV = 0
    AUTH_URL = CLUSTER_URL+'/'+STAGE+'/auth_service/auth/login'
    os.environ["AUTH_URL"] = AUTH_URL

'''
AWS Credentials
'''
AWS_ACCESS_KEY_ID = os.getenv('CUSTOM_AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('CUSTOM_AWS_SECRET_ACCESS_KEY', '')
AWS_DEFAULT_REGION = os.getenv('CUSTOM_AWS_DEFAULT_REGION', '')
os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

'''
CLIMATE_FIELDVIEW API
'''
CLIMATE_FIELDVIEW_TOKEN = os.getenv('CLIMATE_FIELDVIEW_TOKEN')
CLIMATE_FIELDVIEW_API_URL = os.getenv('CLIMATE_FIELDVIEW_API_URL')
CLIMATE_FIELDVIEW_TIMEOUT = int(os.getenv('CLIMATE_FIELDVIEW_TIMEOUT', 10))
CLIMATE_FIELDVIEW_AUTH_URL = os.getenv('CLIMATE_FIELDVIEW_AUTH_URL')

'''
SQS
'''
QUEUE_URL_PROPOSTAS_PUB_SERVICE = os.getenv('QUEUE_URL_PROPOSTAS_PUB_SERVICE')
