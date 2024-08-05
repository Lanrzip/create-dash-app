from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from {{cookiecutter.app_name}}.service.system.test_service import *
from {{cookiecutter.app_name}}.schemas.test import *
from utils.db_utils import get_db


systemRouter = APIRouter(prefix="/system", tags=["系统模块"])


@systemRouter.post("/api-test")
async def test(request: Request,
                test_data_in: TestDataModelIn,
                test_service: ITestService = Depends(TestService.instance),
                query_db: Session = Depends(get_db)):
    
    return await test_service.test(request, test_data_in, query_db)
