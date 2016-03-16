from zope.interface import Interface
from zope.schema import Dict


class IShardedView(Interface):

    shards = Dict(
        title=u'Shards used to render content',
        required=True)
