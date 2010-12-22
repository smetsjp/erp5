##############################################################################
#
# Copyright (c) 2009 Nexedi SA and Contributors. All Rights Reserved.
#                    Fabien Morin <fabien@nexedi.com>
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

class TradeModelLineConstraint:
  """
   Trade Model Line Constraints
  """
  _constraints = (
    { 'id'            : 'reference_existence',
      'description'   : 'Property reference must be defined',
      'type'          : 'PropertyExistence',
      'reference'    : None,
      "message_property_not_set" : 'Reference must be defined in lines',
      "message_no_such_property" : 'Reference must be defined in lines'
    },
    { 'id'            : 'resource',
      'description'   : 'Resource must be defined',
      'type'          : 'CategoryMembershipArity',
      'min_arity'     : '1',
      'max_arity'     : '1',
      'portal_type'   : ( ),
      'base_category' : ('resource',),
      'message_arity_not_in_range' : 'Service must be defined in lines',
    },
    { 'id'            : 'trade_phase',
      'description'   : 'Trade Phase must be defined',
      'type'          : 'CategoryMembershipArity',
      'min_arity'     : '1',
      'max_arity'     : '1',
      'portal_type'   : ( ),
      'base_category' : ('trade_phase',),
      'message_arity_not_in_range' : 'Trade Phase must be defined in lines',
    },
    { 'id': 'cell_existence',
      'description': 'If variation categories are define on Trade Model Line \
                      cell corresponding to this categories should exist too',
      'base_id': 'movement',
      'type': 'TradeModelLineCellConsistency',
    },
  )