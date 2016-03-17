# -*- coding: utf-8 -*-

from uvc.shards.shard import ShardExpr
from uvc.shards.interface import IShard
from uvc.shards.components import BaseShard

# monkeypatching
from grokcore.chameleon import components
components.PageTemplate.expression_types['shard'] = ShardExpr
