##############################################################################
#
# Copyright (c) 2006 Nexedi SARL and Contributors. All Rights Reserved.
#                    Ivan Tyagov <ivan@nexedi.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from AccessControl import ClassSecurityInfo
from Products.ERP5Type import Permissions, PropertySheet
from Products.ERP5Type.XMLObject import XMLObject
from Products.CMFCore.utils import getToolByName
from Products.ERP5Configurator.mixin.configurator_item import ConfiguratorItemMixin

class CustomerBT5ConfiguratorItem(ConfiguratorItemMixin, XMLObject):
  """ Create a new bt5 for customer configuration.

      This business template is not installed locally, only build.
  """

  meta_type = 'ERP5 Customer BT5 Configurator Item'
  portal_type = 'Customer BT5 Configurator Item'
  add_permission = Permissions.AddPortalContent
  isPortalContent = 1
  isRADContent = 1

  # Declarative security
  security = ClassSecurityInfo()
  security.declareObjectProtected(Permissions.AccessContentsInformation)

  # Declarative properties
  property_sheets = ( PropertySheet.Base
                    , PropertySheet.XMLObject
                    , PropertySheet.CategoryCore
                    , PropertySheet.DublinCore )

  def build(self, business_configuration):
    template_tool = getToolByName(self.getPortalObject(),
                                  'portal_templates')
    bt5 = template_tool.newContent(portal_type="Business Template", \
                                   title=self.bt5_id)

    ## ..and set it as current
    business_configuration.setSpecialise(bt5.getRelativeUrl())