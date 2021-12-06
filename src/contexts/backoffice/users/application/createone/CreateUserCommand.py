from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreatePhotoCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'createone-user'

    def __init__(self, user_id: str, name: str):
        self.id = user_id
        self.name = name

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
