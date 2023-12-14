from fastapi import APIRouter
from packages.subnet.router import subnet_router


router = APIRouter()

router.include_router(subnet_router, prefix="/subnet", tags=["Subnet"])
