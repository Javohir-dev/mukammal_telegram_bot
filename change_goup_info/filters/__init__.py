from loader import dp
from .filter_admin import AdminFilter
from .filter_group import IsGroup
from .filter_private_chat import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
