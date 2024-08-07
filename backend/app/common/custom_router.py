import logging
from copy import deepcopy
from typing import Union

from fastapi import Depends, Header, Request, Response

from backend.app.common.exceptions import CustomException

logger = logging.getLogger(__name__)


class ProjectAuthDependencies:

    __DEFAULT_SETTINGS = {
        "company_info": False,
    }

    def __init__(self, settings: dict = None):
        self.settings = deepcopy(self.__DEFAULT_SETTINGS)
        self.settings.update(settings or {})
        self.injected_dependencies = [
            Depends(self.add_company_context),
        ]

    @staticmethod
    def add_company_context(
        request: Request,
        company_id: Union[str, None] = Header(convert_underscores=False),
    ):
        try:
            logger.info("Adding company context...")
            context = {
                "company_id": company_id,
            }
            request.state.context = context
            return request
        except Exception as e:
            logger.exception(f"Error in add_company_context: {e}")
            raise CustomException(
                status_code=400, message="Bad Client Request"
            )