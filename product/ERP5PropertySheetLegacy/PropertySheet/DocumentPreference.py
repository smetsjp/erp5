# -*- coding: utf-8 -*-
#############################################################################
#
# Copyright (c) 2002 Nexedi SARL and Contributors. All Rights Reserved.
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

from Products.ERP5Type import Permissions

class DocumentPreference:
  """
    This property sheet defines the user configurable taxonomy.
  """

  _properties = (
    { 'id'          : 'preferred_ooodoc_server_address',
      'description' : 'Address of a server for converting docs (ip or domain)',
      'type'        : 'string',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    { 'id'          : 'preferred_ooodoc_server_port_number',
      'description' : 'Port number of a server for converting docs',
      'type'        : 'int',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    { 'id'          : 'preferred_ooodoc_server_timeout',
      'description' : 'Timeout when connecting to the document conversion'
                      ' server (in seconds)',
      'type'        : 'int',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    { 'id'          : 'preferred_document_reference_regular_expression',
      'description' : 'A regular expression to find and verify doc references',
      'type'        : 'string',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    { 'id'          : 'preferred_document_filename_regular_expression',
      'storage_id'  : 'preferred_document_file_name_regular_expression', # Compatibility
      'description' : 'A regular expression to parse file names',
      'type'        : 'string',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    { 'id'          : 'preferred_document_reference_method_id',
      'description' : 'Function for parsing, finding and verifying doc reference',
      'type'        : 'string',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    { 'id'              : 'preferred_document_ingestion_email_notification',
      'description'     : 'None - always, "always", "problem (only if problem), "never"', # XXX-JPS this is not a description
      'type'            : 'selection',
      'select_variable' : 'getPreferredDocumentIngestionEmailNotificationSelectionList',
      'write_permission': Permissions.ManageProperties,
      'preference'      : 1,
      'mode'            : '' },
    { 'id'          : 'preferred_document_email_ingestion_address',
      'description' : 'Email ingestion address',
      'type'        : 'string',
      'write_permission': Permissions.ManageProperties,
      'preference'  : 1,
      'mode'        : '' },
    { 'id'          : 'preferred_document_classification',
      'description' : 'Preffered classification policy for newly created documents',
      'type'        : 'string',
      'write_permission': Permissions.ManageProperties,
      'preference'  : 1,
      'mode'        : '' },
    # XXX-JPS. This is not a real property - it is somehow a hack.
    # BG: I was advised by somebody from Nexedi (I think it was Jerome)
    { 'id'              : 'preferred_document_ingestion_email_notification_selection',
      'description'     : 'List of possible values for preferred_document_ingestion_email_notification',
      'type'            : 'tokens',
      'default'         : ['always','problem','never'],
      'write_permission': Permissions.ManageProperties,
      'mode'            : 'w'},
    { 'id'          : 'preferred_conversion_cache_factory',
      'description' : 'Preferred Conversion Cache',
      'type'        : 'string',
      'write_permission': Permissions.ManageProperties,
      'preference'  : 1,
      'mode'        : '' },
    { 'id'          : 'preferred_synchronous_metadata_discovery',
      'description' : 'Is preferred synchronous metadata discovery',
      'type'        : 'boolean',
      'write_permission': Permissions.ManageProperties,
      'default'     : False,
      'preference'  : 1,
      'mode'        : '' },
    { 'id'          : 'preferred_redirect_to_document',
      'description' : 'Is preferred to redirect user to ingested document',
      'type'        : 'boolean',
      'write_permission': Permissions.ManageProperties,
      'default'     : False,
      'preference'  : 1,
      'mode'        : '' },
    { 'id'          : 'preferred_ingestion_namespace',
      'description' : 'Namespace to use for url registry',
      'type'        : 'string',
      'write_permission': Permissions.ManageProperties,
      'default'     : '',
      'preference'  : 1,
      'mode'        : 'w' },
    # Kept for compatibility - will be removed some day
    { 'id'          : 'preferred_document_file_name_regular_expression',
      'description' : 'An alias of preferred_document_filename_regular_expression',
      'type'        : 'string',
      'preference'  : 1,
      'write_permission': Permissions.ManageProperties,
      'mode'        : '' },
    )

# vim: shiftwidth=2
