from libraries.subnetting import (
    networks_FLSM,
    host_FLSM,
    host_VLSM,
    ordered_host_VLSM,
)

from .schemas import FLSMInfo
from .utils import cast_flsm_info


def network_flsm_subnet(flsm_info: FLSMInfo):
    init_ip = flsm_info.init_ip
    init_mask = flsm_info.init_mask
    min_value = flsm_info.min_value
    networks = networks_FLSM(init_ip, init_mask, min_value)
    return cast_flsm_info(flsm_info, networks)


def host_flsm_subnet(flsm_info: FLSMInfo):
    init_ip = flsm_info.init_ip
    init_mask = flsm_info.init_mask
    min_value = flsm_info.min_value

    return host_FLSM(init_ip, init_mask, min_value)


def host_vlsm_subnet(flsm_info: FLSMInfo):
    init_ip = flsm_info.init_ip
    init_mask = flsm_info.init_mask
    host_list = flsm_info.host_list

    return host_VLSM(init_ip, init_mask, host_list)


def ordered_host_vlsm_subnet(flsm_info: FLSMInfo):
    init_ip = flsm_info.init_ip
    init_mask = flsm_info.init_mask
    host_list = flsm_info.host_list

    return ordered_host_VLSM(init_ip, init_mask, host_list)
