import os
from agristamp_common.utils.services import service_get, service_post


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
LISTA_UFS = [
    "ac",
    "al",
    "ap",
    "am",
    "ba",
    "ce",
    "es",
    "go",
    "ma",
    "mt",
    "ms",
    "mg",
    "pa",
    "pb",
    "pr",
    "pe",
    "pi",
    "rj",
    "rn",
    "rs",
    "ro",
    "rr",
    "sc",
    "sp",
    "se",
    "to",
    "df"
]


def get_culturas_climate_fieldview():
    print('Obtendo culturas na API da Climate_Fieldview')

    culturas_response = service_get(
        'climate_fieldview_service', 'v1/culturas', headers=HEADERS)

    if culturas_response.status_code == 200:
        return culturas_response.json()
    else:
        return None
