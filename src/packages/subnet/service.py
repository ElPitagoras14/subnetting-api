from libraries.subnetting import (
    networks_FLSM,
    host_FLSM,
    host_VLSM,
    ordered_host_VLSM,
)

from .schemas import FLSMInfo, VLSMInfo
from .utils import cast_flsm_info, cast_vlsm_info


def network_flsm_subnet(flsm_info: FLSMInfo):
    init_ip = flsm_info.init_ip
    init_mask = flsm_info.init_mask
    min_value = flsm_info.min_value

    subnet = networks_FLSM(init_ip, init_mask, min_value)
    subnet = cast_flsm_info(subnet)
    return subnet


def host_flsm_subnet(flsm_info: FLSMInfo):
    init_ip = flsm_info.init_ip
    init_mask = flsm_info.init_mask
    min_value = flsm_info.min_value

    subnet = host_FLSM(init_ip, init_mask, min_value)
    subnet = cast_flsm_info(subnet)
    return subnet


def host_vlsm_subnet(vlsm_info: VLSMInfo):
    init_ip = vlsm_info.init_ip
    init_mask = vlsm_info.init_mask
    host_list = vlsm_info.host_list

    subnet = host_VLSM(init_ip, init_mask, host_list)
    subnet = cast_vlsm_info(subnet)
    return subnet


def ordered_host_vlsm_subnet(vlsm_info: VLSMInfo):
    init_ip = vlsm_info.init_ip
    init_mask = vlsm_info.init_mask
    host_list = vlsm_info.host_list

    subnet = ordered_host_VLSM(init_ip, init_mask, host_list)
    subnet = cast_vlsm_info(subnet)
    return subnet
