#############################################################################
#
# Copyright (c) 2007 Nexedi SA and Contributors. All Rights Reserved.
#                    Daniel Feliubadalo <daniel@sip2000.com>
#                    Romain Courteaud  <romain@nexedi.com>
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


class ProductDataPreference:
  """
    This property sheet defines the user configurable taxonomy.
  """

  _properties = (
    { 'id'          : 'preferred_product_variation_base_category',
      'description' : 'Defines base categories axes in products variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
      'write_permission': 'Manage properties',
      'mode'        : '' },
    { 'id'          : 'preferred_product_optional_variation_base_category',
      'description' : 'Defines optional base categories axes in products variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
      'write_permission': 'Manage properties',
      'mode'        : '' },
    { 'id'          : 'preferred_product_individual_variation_base_category',
      'description' : 'Defines individual base categories axes in products variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
      'write_permission': 'Manage properties',
      'mode'        : '' },
      { 'id'          : 'preferred_component_variation_base_category',
      'description' : 'Defines base categories axes in components variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
        'write_permission': 'Manage properties',
      'mode'        : '' },
      { 'id'          : 'preferred_component_optional_variation_base_category',
      'description' : 'Defines optional base categories axes in components variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
        'write_permission': 'Manage properties',
      'mode'        : '' },
      { 'id'          : 'preferred_component_individual_variation_base_category',
      'description' : 'Defines individual base categories axes in components variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
        'write_permission': 'Manage properties',
      'mode'        : '' },
      { 'id'          : 'preferred_service_variation_base_category',
      'description' : 'Defines base categories axes in services variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
        'write_permission': 'Manage properties',
      'mode'        : '' },
      { 'id'          : 'preferred_service_optional_variation_base_category',
      'description' : 'Defines optional base categories axes in services variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
        'write_permission': 'Manage properties',
      'mode'        : '' },
      { 'id'          : 'preferred_service_individual_variation_base_category',
      'description' : 'Defines individual base categories axes in services variations',
      'type'        : 'lines',
      'preference'  : 1,
      'default'     : [],
        'write_permission': 'Manage properties',
      'mode'        : '' },
    )