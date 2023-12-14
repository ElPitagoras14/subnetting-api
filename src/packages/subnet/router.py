from fastapi import APIRouter, Response
from utils.responses import InternalServerErrorResponse
from typing import Union

from .service import (
    network_flsm_subnet,
    host_flsm_subnet,
    host_vlsm_subnet,
    ordered_host_vlsm_subnet,
)
from .schemas import FLSMInfo, VLSMInfo
from .responses import SubnetInfo


subnet_router = APIRouter()


@subnet_router.post(
    "/flsm/networks",
    response_model=Union[SubnetInfo, InternalServerErrorResponse],
)
async def networks_FLSM(flsm_info: FLSMInfo, response: Response):
    try:
        subnet = network_flsm_subnet(flsm_info)
        return subnet
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))


@subnet_router.post(
    "/flsm/hosts",
    response_model=Union[SubnetInfo, InternalServerErrorResponse],
)
async def host_FLSM(flsm_info: FLSMInfo, response: Response):
    try:
        subnet = host_flsm_subnet(flsm_info)
        return subnet
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))


@subnet_router.post(
    "/vlsm/hosts",
    response_model=Union[SubnetInfo, InternalServerErrorResponse],
)
async def host_VLSM(vlsm_info: VLSMInfo, response: Response):
    try:
        subnet = host_vlsm_subnet(vlsm_info)
        return subnet
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))


@subnet_router.post(
    "/vlsm/hosts-ordered",
    response_model=Union[SubnetInfo, InternalServerErrorResponse],
)
async def ordered_host_VLSM(vlsm_info: VLSMInfo, response: Response):
    try:
        subnet = ordered_host_vlsm_subnet(vlsm_info)
        return subnet
    except Exception as e:
        response.status_code = 500
        return InternalServerErrorResponse(message=str(e))
