import os
import json
from dotenv import load_dotenv

load_dotenv()

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

headers = {
    'Authorization': 'Bearer '+os.getenv('AGRISTAMP_KEY')
}


def test_get_documento():
        
    params = {
        "numero_cotacao_proposta": "3794353",
        "codigo_corretor": "0",
        "tipo": "cotacao"
    }

    response = client.get(f"/climate_fieldview_service/v1/documentos/", headers=headers, params=params)

    assert response.status_code in [200, 201]
    assert 'arquivo' in response.json()
