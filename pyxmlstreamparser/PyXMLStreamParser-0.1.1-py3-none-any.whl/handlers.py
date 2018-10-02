from logging import getLogger
from xml.sax import handler

import re

logger = getLogger(__name__)


class HandlerCollection(handler.ContentHandler):
    def __init__(self, children=None, storage=None, max_parent_depth=None, min_parent_depth=None):
        super(HandlerCollection, self).__init__()
        self.depth = 0
        self.children = children or []
        self.storage = storage
        self.max_parent_depth = max_parent_depth
        self.min_parent_depth = min_parent_depth

    def startElement(self, name, attrs):
        self.depth += 1
        [c.startElement(name, attrs, self.storage)

         for c in self.children if c.active or (c.key == name and
                                                (c.min_parent_depth is None or c.min_parent_depth <= self.depth) and
                                                (c.max_parent_depth is None or c.max_parent_depth >= self.depth))]

    def endElement(self, name):
        [c.endElement(name)
         for c in self.children if c.active]
        self.depth -= 1

    def characters(self, content):
        [c.characters(content)
         for c in self.children if c.active]


class KeyHandler(HandlerCollection):
    def __init__(self, key, children=None, multi=False, store_chars=False,
                 stores=None, storage=None,
                 max_parent_depth=None, min_parent_depth=None):
        super(KeyHandler, self).__init__(children=children, storage=storage,
                                         max_parent_depth=max_parent_depth,
                                         min_parent_depth=min_parent_depth)
        self.active = False
        self.multi = multi
        self.key = key
        self.store_chars = store_chars
        self.chars_stored = ''
        self.stores = stores or []

    def startElement(self, name, attrs, storage=None):
        if name == self.key and not self.active:
            self.active = True
            self.storage = storage
            self.chars_stored = ''
            self.start_content(attrs)
            [s.start_store(attrs, self, storage) for s in self.stores]
        elif self.active:
            super(KeyHandler, self).startElement(name, attrs)

    def endElement(self, name):
        if self.active:
            if name == self.key and self.depth <= 1:
                [s.finish_store(self) for s in self.stores]
                self.finish_content()
                self.active = False
                self.depth = 0
            else:
                super(KeyHandler, self).endElement(name)

    def characters(self, content):
        if not self.active:
            return

        if self.store_chars and self.depth == 0:
            self.chars_stored += content
        else:
            super(KeyHandler, self).characters(content)

    def start_content(self, attrs):
        pass

    def finish_content(self):
        pass


class BaseStore:

    def start_store(self, attrs, handler, parent_storage):
        pass

    def finish_store(self, handler):
        pass


class StoreAttr(BaseStore):
    def __init__(self, attr_name, field_name=None):
        self.attr_name = attr_name
        self.field_name = field_name or attr_name

    def start_store(self, attrs, handler, parent_storage):
        try:
            try:
                handler.storage[self.field_name] = attrs.getValue(self.attr_name)
            except TypeError:
                setattr(handler.storage, self.field_name, attrs.getValue(self.attr_name))
        except KeyError as ex:
            logger.exception(ex)
            logger.warning(ex)


class ApplyAttr(BaseStore):
    def __init__(self, attr_name, func_name, extra_args=None, extra_kwargs=None):
        self.attr_name = attr_name
        self.func_name = func_name
        self.extra_args = extra_args or tuple()
        self.extra_kwargs = extra_kwargs or {}

    def start_store(self, attrs, handler, parent_storage):
        try:
            getattr(handler.storage, self.func_name)(attrs.getValue(self.attr_name),
                                                     *self.extra_args,
                                                     **self.extra_kwargs)
        except AttributeError as ex:
            logger.exception(ex)
            logger.warning(ex)


class StoreConstant(BaseStore):
    def __init__(self, constant, field_name):
        self.constant = constant
        self.field_name = field_name

    def start_store(self, attrs, handler, parent_storage):
        try:
            try:
                handler.storage[self.field_name] = self.constant
            except TypeError:
                setattr(handler.storage, self.field_name, self.constant)
        except KeyError as ex:
            logger.exception(ex)
            logger.warning(ex)


class StoreContent(BaseStore):
    def __init__(self, field_name=None):
        self.field_name = field_name

    def finish_store(self, handler):
        content = re.sub(r'(\n\s*|\s+)', ' ', handler.chars_stored, flags=re.MULTILINE).strip()
        try:
            handler.storage[self.field_name] = content
        except TypeError:
            setattr(handler.storage, self.field_name, content)


class SetAttrStorage(BaseStore):
    def __init__(self, key):
        self.key = key
        super(SetAttrStorage, self).__init__()

    def start_store(self, attrs, handler, parent_storage):
        handler.storage = getattr(parent_storage, self.key)


class StoreContentUsingAttribute(StoreContent):
    def __init__(self, attr_name):
        super(StoreContentUsingAttribute, self).__init__()
        self.attr_name = attr_name

    def start_store(self, attrs, handler, parent_storage):
        self.field_name = attrs.getValue(self.attr_name)


class BaseCreateStorage(BaseStore):
    def __init__(self, factory, factory_args=None, factory_kwargs=None):
        self.factory = factory
        self.factory_args = factory_args or []
        self.factory_kwargs = factory_kwargs or {}

    def start_store(self, attrs, handler, parent_storage):
        handler.storage = self.factory(*self.factory_args, **self.factory_kwargs)
        self.prepare_storage(handler, parent_storage)

    def prepare_storage(self, handler, parent_storage):
        pass


class ProxyStorage(BaseCreateStorage):
    def start_store(self, attrs, handler, parent_storage):
        handler.storage = self.factory(parent_storage, *self.factory_args, **self.factory_kwargs)
        self.prepare_storage(handler, parent_storage)


class BaseCreateStorageInKey(BaseCreateStorage):
    def __init__(self, key, factory, factory_args=None, factory_kwargs=None):
        self.key = key
        super(BaseCreateStorageInKey, self).__init__(factory, factory_args, factory_kwargs)


class SetStorageInKey(BaseCreateStorageInKey):
    def prepare_storage(self, handler, parent_storage):
        try:
            parent_storage[self.key] = handler.storage
        except TypeError:
            setattr(parent_storage, self.key, handler.storage)


class AppendStorageInKey(BaseCreateStorageInKey):
    def prepare_storage(self, handler, parent_storage):
        parent_storage[self.key].append(handler.storage)


class UseStorageInFunction(BaseCreateStorageInKey):
    def prepare_storage(self, handler, parent_storage):
        self.store_func = getattr(parent_storage, self.key)

    def finish_store(self, handler):
        self.store_func(handler.storage)
