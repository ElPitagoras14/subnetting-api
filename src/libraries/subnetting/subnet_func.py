from .utils import (
    get_previous_ip,
    get_next_ip,
    get_potential_bit_number,
    add_host,
)


def networks_FLSM(ip: str, mask: int, min_networks: int):
    network_list = []
    n = get_potential_bit_number(min_networks)
    new_mask = mask + n
    m = 32 - new_mask

    for i in range(pow(2, n)):
        red = "Net " + str(i + 1)
        net_tmp = {
            "name": red,
            "subnet": ip,
            "mask": new_mask,
            "firstIp": get_next_ip(ip),
        }
        ip = add_host(ip, pow(2, m))
        net_tmp["lastIp"] = get_previous_ip(get_previous_ip(ip))
        net_tmp["broadcast"] = get_previous_ip(ip)
        network_list.append(net_tmp)

    subnet = {
        "subnet_info": {
            "initial_ip": ip,
            "initial_mask": mask,
            "n": n,
            "m": m,
            "number_of_networks": pow(2, n),
            "number_of_hosts": pow(2, m),
        },
        "networks": network_list,
    }
    return subnet


def host_FLSM(ip: str, mask: int, min_host: int):
    m = get_potential_bit_number(min_host + 2)
    n = 32 - mask - m
    return networks_FLSM(ip, mask, pow(2, n))


def host_VLSM(ip: str, mask: int, host_list: list[int]):
    network_list = []
    final_host_list = []
    cnt = 0

    for host in host_list:
        m = get_potential_bit_number(host + 2)
        n = 32 - mask - m
        new_mask = mask + n
        red = "Net " + str(cnt + 1)
        net_tmp = {
            "name": red,
            "subnet": ip,
            "mask": new_mask,
            "firstIp": get_next_ip(ip),
        }
        ip = add_host(ip, pow(2, m))
        net_tmp["lastIp"] = get_previous_ip(get_previous_ip(ip))
        net_tmp["broadcast"] = get_previous_ip(ip)
        network_list.append(net_tmp)
        final_host_list.append(pow(2, m))
        cnt += 1

    subnet = {
        "subnet_info": {
            "initial_ip": ip,
            "initial_mask": mask,
            "initial_host_per_network": host_list,
            "host_per_network": final_host_list,
        },
        "networks": network_list,
    }
    return subnet


def ordered_host_VLSM(ip: str, mask: int, host_list: list[int]):
    ordered_list = sorted(host_list, reverse=True)
    return host_VLSM(ip, mask, ordered_list)
