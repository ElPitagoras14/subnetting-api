from libraries.subnetting import create_tree, tree_to_str
from .responses import Network, SubnetInfo, VLSMInfo, FLSMInfo


def cast_subnet(subnet: dict, subnet_type_info: FLSMInfo | VLSMInfo):
    networks = subnet["networks"]

    tree = create_tree(subnet)
    tree_str = tree_to_str(tree, None, False)
    casted_networks = [Network(**network) for network in networks]
    tmp_dict = {
        "networks": casted_networks,
        "tree_str": tree_str,
        "subnet_info": subnet_type_info,
    }
    return SubnetInfo(**tmp_dict)


def cast_flsm_info(subnet: dict):
    subnet_info = FLSMInfo(**subnet["subnet_info"])
    return cast_subnet(subnet, subnet_info)


def cast_vlsm_info(subnet: dict):
    subnet_info = VLSMInfo(**subnet["subnet_info"])
    return cast_subnet(subnet, subnet_info)
