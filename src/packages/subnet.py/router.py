from fastapi import APIRouter, Response
from utils.responses import InternalServerErrorResponse

from .service import (
    network_flsm_subnet,
    host_flsm_subnet,
    host_vlsm_subnet,
    ordered_host_vlsm_subnet,
)
from .schemas import FLSMInfo, VLSMInfo


subnet_router = APIRouter()


@subnet_router.post("/flsm/networks")
async def networks_FLSM(flsm_info: FLSMInfo, response: Response):
    try:
        subnets = network_flsm_subnet(flsm_info)
        return subnets
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))


@subnet_router.post("/flsm/hosts")
async def host_FLSM(flsm_info: FLSMInfo, response: Response):
    try:
        subnets = host_flsm_subnet(flsm_info)
        return subnets
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))


@subnet_router.post("/vlsm/hosts")
async def host_VLSM(vlsm_info: VLSMInfo, response: Response):
    try:
        subnets = host_vlsm_subnet(vlsm_info)
        return subnets
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))


@subnet_router.post("/vlsm/hosts-ordered")
async def ordered_host_VLSM(vlsm_info: VLSMInfo, response: Response):
    try:
        subnets = ordered_host_vlsm_subnet(vlsm_info)
        return subnets
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))
