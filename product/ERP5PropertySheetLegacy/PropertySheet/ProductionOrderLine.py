##############################################################################
#
# Copyright (c) 2008 Nexedi SA and Contributors. All Rights Reserved.
#          Lukasz Nowak <lukasz.nowak@ventis.com.pl>
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


class ProductionOrderLine:
  """
  Constraints that can be enforced on Production Order Lines
  """

  _properties = (
  )

  _categories = (
  )

  _constraints = (
    { 'id'            : 'resource_category_existence',
      'description'   : 'Resource must be defined',
      'type'          : 'CategoryExistence',
      'portal_type'   : ('Component', 'Product'),
      'resource': 1,
      'message_category_not_set': 'Product must be defined',
    },
    { 'id'            : 'specialise_category_existence',
      'description'   : 'Specialise must be defined',
      'type'          : 'CategoryExistence',
      'portal_type'   : ('Transformation',),
      'specialise': 1,
      'message_category_not_set': 'Transformation must be defined',
    },
    { 'id'            : 'total_quantity',
      'description'   : 'Total Quantity must not be 0',
      'type'          : 'TALESConstraint',
      'expression'    : 'python: object.getTotalQuantity() > 0',
      'message_expression_false': 'Total Quantity must not be 0',
    },
    { 'id'            : 'date_coherency',
      'description'   : 'Stop Date must be after Start Date',
      'type'          : 'TALESConstraint',
      'expression'    : 'python: object.getStopDate() >= object.getStartDate()',
      'message_expression_false': 'Delivery Date must be after Shipping Date',
    },
    { 'id'            : 'transformation_for_resource',
      'description'   : 'Transformation must match chosen resource',
      'type'          : 'TALESConstraint',
      'expression'    : 'python: object.getResourceValue() is not None and object.getSpecialise() in \
          object.getResourceValue().getResourceRelatedList(portal_type=object.getPortalTransformationTypeList())',
      'message_expression_false': 'Transformation must match chosen resource',
    },
  )