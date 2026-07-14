import requests
from django.conf import settings




class BanxicoService:
    URL_BASE = "https://www.banxico.org.mx/SieAPIRest/service/v1"
    SERIE_FIX = "SF43718"

    @classmethod
    def get_tipo_cambio(cls):
        url = f"{cls.URL_BASE}/series/{cls.SERIE_FIX}/datos/oportuno"
        headers = {
            "Bmx-Token": settings.BANXICO_TOKEN,
            "Accept": "application/json"
        }    

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        return None