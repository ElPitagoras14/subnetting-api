from pydantic import BaseModel


class CommonData(BaseModel):
    init_ip: str
    init_mask: int


class FLSMInfo(CommonData):
    min_value: int


class VLSMInfo(CommonData):
    host_list: list[int]
