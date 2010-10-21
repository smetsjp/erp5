##############################################################################
#
# Copyright (c) 2002-2010 Nexedi SARL and Contributors. All Rights Reserved.
#                         Sebastien Robin <seb@nexedi.com>
#                         Romain Courteaud <romain@nexedi.com>
#                         Arnaud Fontaine <arnaud.fontaine@nexedi.com>
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

from Products.ERP5Type.mixin.constraint import ConstraintMixin
from AccessControl import ClassSecurityInfo
from Products.ERP5Type import Permissions, PropertySheet

class CategoryExistenceConstraint(ConstraintMixin):
  """
  This constraint checks whether a category has been defined on this
  object (without acquisition). This is only relevant for ZODB
  Property Sheets (filesystem Property Sheets rely on
  Products.ERP5Type.Constraint.CategoryExistence instead).
  """
  meta_type = 'ERP5 Category Existence Constraint'
  portal_type = 'Category Existence Constraint'

  # Declarative security
  security = ClassSecurityInfo()
  security.declareObjectProtected(Permissions.AccessContentsInformation)

  property_sheets = (PropertySheet.SimpleItem,
                     PropertySheet.Predicate,
                     PropertySheet.Reference,
                     PropertySheet.CategoryExistenceConstraint)

  _message_id_list = [ 'message_category_not_set',
                       'message_category_not_associated_with_portal_type' ]
  message_category_not_set = "Category existence error for base"\
      " category ${base_category}, this category is not defined"
  message_category_not_associated_with_portal_type = "Category existence"\
      " error for base category ${base_category}, this"\
      " document has no such category"

  def _calculateArity(self, obj, base_category, portal_type):
    return len(obj.getCategoryMembershipList(base_category,
                                             portal_type=portal_type))

  security.declareProtected(Permissions.AccessContentsInformation,
                            'checkConsistency')
  def checkConsistency(self, obj, fixit=0):
    """
    Check the object's consistency.
    """
    error_list = []
    if not self.test(obj):
      return []

    portal_type = self.getConstraintPortalTypeList() or ()
    # For each attribute name, we check if defined
    for base_category in self.getConstraintBaseCategoryList() or ():
      mapping = dict(base_category=base_category)
      # Check existence of base category
      if base_category not in obj.getBaseCategoryList():
        error_message = 'message_category_not_associated_with_portal_type'
      elif self._calculateArity(obj, base_category, portal_type) == 0:
        error_message = 'message_category_not_set'
      else:
        error_message = None

      # Raise error
      if error_message:
        error_list.append(
          self._generateError(obj,
                              self._getMessage(error_message), mapping))
    return error_list

class CategoryAcquiredExistenceConstraint(CategoryExistenceConstraint):
  """
  This constraint checks whether a category has been defined on this
  object (with acquisition). This is only relevant for ZODB Property
  Sheets (filesystem Property Sheets rely on
  Products.ERP5Type.Constraint.CategoryExistence instead).
  """
  def _calculateArity(self, obj, base_category, portal_type):
    return len(obj.getAcquiredCategoryMembershipList(base_category,
                                             portal_type=portal_type))