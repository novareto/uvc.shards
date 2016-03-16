# -*- coding: utf-8 -*-

from uvc.shards.shard import ShardExpr
from grokcore.chameleon import components

# monkeypatching
components.PageTemplate.expression_types['shard'] = ShardExpr
