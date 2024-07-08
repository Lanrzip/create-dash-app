from abc import ABC, abstractmethod
from fastapi import Depends, Request, Form
from sqlalchemy.orm import Session


from {{cookiecutter.app_name}}.schemas.test import TestDataModelIn, TestDataModelOut
from utils.log_utils import logger
from utils.response_utils import *
from models.system import Test


class ITestService(ABC):
        
    @abstractmethod
    async def test(self, request: Request, test_data_in: TestDataModelIn, query_db: Session):
        pass


class TestService(ITestService):
     
    async def test(self, request: Request, test_data_in: TestDataModelIn, query_db: Session):
        """
        测试服务接口
        :param request: Request对象
        :param test_data_in: 入参对象
        :param query_db: orm对象
        """
        try:
            user = await self.do_something(test_data_in.name, query_db)
            if user:
                logger.info("测试服务接口调用成功")
                return response_200(data=TestDataModelOut.model_validate(user), message="测试服务接口调用成功")
            else:
                logger.warning("测试服务接口调用失败")
                return response_400(data="", message="测试服务接口调用失败")
        except Exception as e:
            logger.exception(e)
            return response_500(data="", message=str(e))
    
    def __init__(self, request: Request):
        pass

    async def do_something(self, name, db: Session):
        logger.info(f"当前请求的name为{name}")
        user = db.query(Test)\
            .filter(Test.name == name) \
            .distinct() \
            .first()
        if user:
            return user
        else:
            return None
        
    @classmethod
    async def instance(cls, request: Request):

        return cls(request)