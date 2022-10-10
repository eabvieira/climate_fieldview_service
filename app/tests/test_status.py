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


def test_get_status():
        
    params = {
        "numero_cotacao_proposta": "3794353",
        "codigo_corretor": "0"
    }

    response = client.get(f"/climate_fieldview_service/v1/status_proposta/", headers=headers, params=params)

    assert response.status_code in [200, 201]
