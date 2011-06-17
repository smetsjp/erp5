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

from AccessControl import ClassSecurityInfo

from Products.ERP5Type import Permissions, PropertySheet
from Products.ERP5Type.Base import Base
from Products.ERP5Type.Utils import deprecated

from Products.ERP5.Document.Coordinate import Coordinate

import string

class GeographicAddress(Coordinate, Base):
    """
        A geographic address holds a complete set of
        geographic coordinates including street, number,
        city, zip code, region.

        Geographic address is a terminating leaf
        in the OFS. It can not contain anything.

        Geographic address inherits from Base and
        from the mix-in Coordinate
    """
    meta_type = 'ERP5 Geographic Address'
    portal_type = 'Address'
    add_permission = Permissions.AddPortalContent

    # Declarative security
    security = ClassSecurityInfo()
    security.declareObjectProtected(Permissions.AccessContentsInformation)

    # Declarative properties
    property_sheets = ( PropertySheet.Base
                      , PropertySheet.SimpleItem
                      , PropertySheet.SortIndex
                      , PropertySheet.CategoryCore
                      , PropertySheet.Coordinate
                      , PropertySheet.GeographicAddress
                      )


    security.declareProtected(Permissions.AccessContentsInformation, 'asText')
    def asText(self):
        """
          Returns the address as a complete formatted string
          with street address, zip, city and region
        """
        result = Coordinate.asText(self)
        if result is None:
          result = ('%s\n%s %s') % (self.getStreetAddress() or '',
                      self.getCity() or '', self.getZipCode() or '')
        if not result.strip():
          return ''
        return result

    security.declareProtected(Permissions.ModifyPortalContent, 'fromText')
    @deprecated
    def fromText(self, coordinate_text):
        """
          Tries to recognize the coordinate_text to update
          this address
          XXX fromText will be removed.
          Instead, store text value as user filled in text attribute,
          then display text value through a configurable output filter, suitable
          for all addresses patterns.
        """
        lines = string.split(coordinate_text, '\n')
        self.setStreetAddress('')
        self.setZipCode('')
        self.setCity('')
        zip_city = None
        if len(lines ) > 1:
          self.setStreetAddress(lines[0:-1])
          zip_city = string.split(lines[-1])
        elif len(lines ) > 0:
          self.setStreetAddress('')
          zip_city = string.split(lines[-1])
        if zip_city:
          self.setZipCode(zip_city[0])
          if len(zip_city) > 1:
            self.setCity(string.join(zip_city[1:]))

    security.declareProtected(Permissions.AccessContentsInformation,
                              'standardTextFormat')
    def standardTextFormat(self):
        """
          Returns the standard text format for geographic addresses
        """
        return ("""\
c/o Jean-Paul Sartre
43, avenue Kleber
75118 Paris Cedex 5
""",
)

