from pydantic import BaseModel
from utils.responses import SuccessResponse


class Network(BaseModel):
    name: str
    subnet: str
    mask: int
    first_ip: str
    last_ip: str
    broadcast: str


class CommonData(BaseModel):
    initial_ip: str
    initial_mask: int


class VLSMInfo(CommonData, BaseModel):
    initial_host_per_network: list[int]
    host_per_network: list[int]


class FLSMInfo(CommonData, BaseModel):
    n: int
    m: int
    number_of_networks: int
    number_of_hosts: int


class SubnetInfo(BaseModel):
    subnet_info: VLSMInfo | FLSMInfo
    networks: list[Network]
    tree_str: str


class SubnetOut(SuccessResponse):
    payload: SubnetInfo | None = None
