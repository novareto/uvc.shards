# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


from .interface import IShard
from grokcore.view import View
from zope.interface import Interface
from grokcore.component import provides, context, baseclass


class BaseShard(View):
    provides(IShard)
    context(Interface)
    baseclass()
    _namespace = None

    def update(self, namespace=None):
        if namespace:
            self._namespace = namespace

    def namespace(self):
        ns = dict(shard=self)
        if self._namespace:
            ns.update(self._namespace)
        return ns

    def render(self):
        template = getattr(self, 'template', None)
        if template is not None:
            return self._render_template()
    render.base_method = True


class ShardsAsViews(object):
    """A shard factories component that acts as a querier
    """

    def get(self, name):
        def shard_querier(namespace):
            from zope.component import queryMultiAdapter
            context = namespace['context']
            request = namespace['request']
            shard = queryMultiAdapter((context, request), IShard, name=name)
            shard.update(namespace)
            return shard
        return shard_querier
