from libraries.subnetting import SubnettingTree, tree_to_str

from .responses import VLSMInfo, FLSMInfo, SubnetInfo, Network


def get_network_tree(init_ip: int, init_mask: str, networks: list):
    sbnt_obj = SubnettingTree(init_mask, init_ip, networks)
    tree, _ = sbnt_obj.create_tree()
    tree_str = tree_to_str(tree, None, False)
    return tree, tree_str


def cast_flsm_info(flsm_info: dict, networks: list):
    casted_networks = [Network(**network) for network in networks]
    pass


def cast_vlsm_info(vlsm_info: dict):
    vlsm_info["init_ip"] = int(vlsm_info["init_ip"])
    vlsm_info["init_mask"] = int(vlsm_info["init_mask"])
    vlsm_info["host_list"] = [int(host) for host in vlsm_info["host_list"]]
    return vlsm_info
