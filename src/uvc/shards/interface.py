from zope.interface import Interface


class IShardedView(Interface):

    shards = Dict(
        title=u'Shards used to render content',
        required=True)
