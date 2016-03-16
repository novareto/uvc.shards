# -*- coding: utf-8 -*-

import ast
from chameleon.codegen import template
from chameleon.astutil import Symbol
from .interface import IShardedView


def render_shard(shard):
    shard.update()
    return shard.render()


try:
    # We might has zope.security
    from zope.security._proxy import _Proxy as Proxy

    def resolve_shard(shard):
        """If shard is a Proxy, we need to check the security.
        If not, we render it.
        """
        if type(shard) is Proxy:
            if (zope.security.canAccess(shard, 'update') and
                zope.security.canAccess(shard, 'render')):
                return render_shard(shard)
            else:
                return u''
        else:
            return render_shard(shard)

except ImportError:
    resolve_shard = render_shard


def query_shard(econtext, name):
    """Compute the result of a shard expression
    """
    context = econtext.get('context')
    request = econtext.get('request')
    view = econtext.get('view')
    if IShardedView.providedBy(view):
        shard = view.shards.get(name)
        if shard is not None:
            return resolve_shard(shard)
    return u""


class ShardExpr(object):
    """
    This is the interpreter of a shard: expression
    """
    def __init__(self, expression):
        self.expression = expression

    def __call__(self, target, engine):
        shard_name = self.expression.strip()
        value = template(
            "query_shard(econtext, name)",
            query_shard=Symbol(query_shard),  # ast of query_shard
            name=ast.Str(s=shard_name),  # our name parameter to query_shard
            mode="eval")
        return [ast.Assign(targets=[target], value=value)]
