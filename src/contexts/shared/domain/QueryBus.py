from abc import abstractmethod
from typing import Any

from src.contexts.shared.domain.Interface import Interface
from src.contexts.shared.domain.Query import Query


class QueryBus(Interface):

    @abstractmethod
    async def ask(self, query: Query) -> Any:
        raise NotImplementedError()
