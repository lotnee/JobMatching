from dataclasses import dataclass

@dataclass
class InvalidObjectType(Exception):
    message: str
