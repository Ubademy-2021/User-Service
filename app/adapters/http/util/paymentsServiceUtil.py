import requests
from app.core.config import HEROKU_PAYMENTS_SERVICE_BASE_URL
from app.core.logger import logger
from fastapi.exceptions import HTTPException


class PaymentsServiceUtil:

    def makeUserWallet(id: int):

        logger.info("Creating wallet in payments service")

        url = HEROKU_PAYMENTS_SERVICE_BASE_URL + "/wallet"
        data = {'userId': id}
        r = requests.post(url=url, json=data)

        if r.status_code != 200:
            logger.warning("Wallet could not be created")
            raise HTTPException(status_code=400, detail="Wallet could not be created")
