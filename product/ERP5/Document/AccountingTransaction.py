##############################################################################
#
# Copyright (c) 2002 Nexedi SARL and Contributors. All Rights Reserved.
#                    Jean-Paul Smets-Solanes <jp@nexedi.com>
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

from Globals import InitializeClass, PersistentMapping
from AccessControl import ClassSecurityInfo
from Products.ERP5Type import Permissions, PropertySheet, Constraint, Interface
from Products.CMFCore.utils import getToolByName

from Products.ERP5.Document.Delivery import Delivery

class AccountingTransaction(Delivery):
    """
      A Transaction object allows to add
      elementary accounting transactions in the general ledger
    """

    # CMF Type Definition
    meta_type = 'ERP5 Accounting Transaction'
    portal_type = 'Accounting Transaction'
    add_permission = Permissions.AddPortalContent
    isPortalContent = 1
    isRADContent = 1
    isDelivery = 1

    # Declarative security
    security = ClassSecurityInfo()
    security.declareObjectProtected(Permissions.AccessContentsInformation)

    # Default Properties
    property_sheets = ( PropertySheet.Base
                      , PropertySheet.XMLObject
                      , PropertySheet.CategoryCore
                      , PropertySheet.DublinCore
                      , PropertySheet.Task
                      , PropertySheet.Arrow
                      , PropertySheet.Movement
                      , PropertySheet.Delivery
                      , PropertySheet.Amount
                      , PropertySheet.Reference
                      , PropertySheet.PaymentCondition
                      )

    def manage_beforeDelete(self, item, container):
      """
          Accounting transactions can only be deleted 
          in draft or cancelled state
      """
      if self.getSimulationState() not in ("draft", "cancelled") :
        from OFS.ObjectManager import BeforeDeleteException
        raise BeforeDeleteException, \
              "%s can only be deleted in draft or cancelled states." % self.getPortalType()
      Delivery.manage_beforeDelete(self, item, container) 

    def manage_afterClone(self, item):
      # Reset reference on paste
      # XXX This implementation is quite bad because it is not generic
      # it is related to the general problem of "what should I reset after paste"
      if self.getReference != None:
        self.setReference(None)
      AccountingTransaction.manage_afterClone(self, item)

# Compatibility
# It may be necessary to create an alias after removing the Transaction class
# Products.ERP5Type.Document.Transaction = AccountingTransaction