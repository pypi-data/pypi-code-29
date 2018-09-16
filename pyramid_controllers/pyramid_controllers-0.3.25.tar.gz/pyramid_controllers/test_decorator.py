# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2017/02/25
# copy: (C) Copyright 2017-EOT Cadit Inc., All Rights Reserved.
#------------------------------------------------------------------------------

import unittest

from pyramid_controllers import \
  Controller, RestController, expose, lookup, expose_defaults
from .test_helpers import TestHelper

#------------------------------------------------------------------------------
class TestDecorator(TestHelper):

  #----------------------------------------------------------------------------
  def test_multiPathController(self):

    # TODO: NOCI implement...
    raise unittest.SkipTest('TODO! FIXME!')

    ## TODO: this `expose_defaults` causes problems when there are multiple
    ##       pathways to a controller... or, something is.
    @expose_defaults(renderer='json')
    class BaseRestController(RestController):
      pass
    class Item(BaseRestController):
      @expose
      def get(self, request): return 'item:' + request._item
    class Items(BaseRestController):
      ITEM_ID = Item(expose=False)
      @expose
      def archive(self, erquest): return 'archive!'
      @lookup
      def lookup(self, request, item_id, *rem):
        request._item = item_id
        return (self.ITEM_ID, rem)
    class Container(BaseRestController):
      items = Items()
      @expose
      def get(self, request): return 'container!'
    class Containers(BaseRestController):
      CONTAINER_ID = Container(expose=False)
      @lookup
      def lookup(self, request, container_id, *rem):
        request._container = container_id
        return (self.CONTAINER_ID, rem)
    class Root(Controller):
      containers = Containers()
      items = Items()
    root = Root()
    self.assertResponse(self.send(root, '/items/10'),                    200, 'item:10')
    self.assertResponse(self.send(root, '/containers/15/items/archive'), 200, 'archive!')


#------------------------------------------------------------------------------
# end of $Id$
# $ChangeLog$
#------------------------------------------------------------------------------
