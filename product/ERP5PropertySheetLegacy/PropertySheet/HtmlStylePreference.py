##############################################################################
#
# Copyright (c) 2005 Nexedi SARL and Contributors. All Rights Reserved.
#                    Vincent Pelletier <vincent@nexedi.com>
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

class HtmlStylePreference:
  """
    User Preferences for HtmlStyle
  """
  
  _properties = (
    { 'id'          : 'preferred_html_style_developper_mode',
      'description' : 'When true, useful links for developers are shown in '\
                      'the interface.',
      'type'        : 'boolean',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_html_style_translator_mode',
      'description' : 'When true, links to translation system will be '\
                      'displayed.',
      'type'        : 'boolean',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_html_style_contextual_help',
      'description' : 'When true, links to contextual help will be displayed.',
      'type'        : 'boolean',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_html_style_access_tab',
      'description' : 'When true, access tab will be used in front page.',
      'type'        : 'boolean',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_html_style_acknowledgeable_message',
      'description' : 'When true, some messages will be displayed on any page',
      'type'        : 'boolean',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_html_style_documentation_base_url',
      'description' : 'Defines the base URL where portal type action '\
                      'documentation will be searched for.',
      'type'        : 'string',
      'preference'  : 1,
      'default'     : 'http://www.erp5.com/erp5_help/',
      'mode'        : 'w' },
    { 'id'          : 'preferred_html_style_unsaved_form_warning',
      'description' : 'When true, display a javascript confirmation box if '\
                      'the user tries to navigate away from a form that was '\
                      'partially changed but is unsaved.',
      'type'        : 'boolean',
      'preference'  : 1,
      'default'     : True,
      'mode'        : 'w' },
    { 'id'          : 'preferred_string_field_width',
      'description' : 'The default width of string fields',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_textarea_width',
      'description' : 'The default width of text area fields',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_textarea_height',
      'description' : 'The default height of text area fields',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_money_quantity_field_width',
      'description' : 'The default width of fields displaying amounts of money',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_quantity_field_width',
      'description' : 'The default width of quantity fields',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_listbox_view_mode_line_count',
      'description' : 'Number of lines in a listbox in view mode',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_listbox_list_mode_line_count',
      'description' : 'Number of lines in a listbox in list mode',
      'type'        : 'int',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_category_child_item_list_method_id',
      'description' : 'The method used to list categories in ListFields',
      'type'        : 'string',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_nano_image_height',
      'description' : 'The height for nano image. The unit is the pixel',
      'type'        : 'int',
      'default'     : 25,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_nano_image_width',
      'description' : 'The width for nano image. The unit is the pixel',
      'type'        : 'int',
      'default'     : 25,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_micro_image_height',
      'description' : 'The height for micro image. The unit is the pixel',
      'type'        : 'int',
      'default'     : 64,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_micro_image_width',
      'description' : 'The width for micro image. The unit is the pixel',
      'type'        : 'int',
      'default'     : 64,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_thumbnail_image_height',
      'description' : 'The height for thumbnail image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 128,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_thumbnail_image_width',
      'description' : 'The width for thumbnail image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 128,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_xsmall_image_height',
      'description' : 'The height for thumbnail image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 200,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_xsmall_image_width',
      'description' : 'The width for xsmall image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 200,
      'preference'  : 1,
      'mode'        : 'w' },

    { 'id'          : 'preferred_small_image_height',
      'description' : 'The height for small image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 320,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_small_image_width',
      'description' : 'The width for small image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 320,
      'preference'  : 1,
      'mode'        : 'w' },

    { 'id'          : 'preferred_medium_image_height',
      'description' : 'The height for medium image.The unit is the pixel',
      'type'        : 'int',
      'default'     : '480',
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_medium_image_width',
      'description' : 'The width for medium image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 480,
      'preference'  : 1,
      'mode'        : 'w' },

    { 'id'          : 'preferred_large_image_height',
      'description' : 'The height for large image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 768,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_large_image_width',
      'description' : 'The width for large image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 768,
      'preference'  : 1,
      'mode'        : 'w' },

    { 'id'          : 'preferred_xlarge_image_height',
      'description' : 'The height for xlarge image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 1024,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_xlarge_image_width',
      'description' : 'The width for xlarge image.The unit is the pixel',
      'type'        : 'int',
      'default'     : 1024,
      'preference'  : 1,
      'mode'        : 'w' },
    { 'id'          : 'preferred_image_format',
      'description' : 'Preferred image format.',
      'type'        : 'string',
      'preference'  : 1,
      'default'     : 'png',
      'mode'        : 'w' },
    { 'id'          : 'preferred_image_size',
      'description' : 'Preferred image size.',
      'type'        : 'string',
      'preference'  : 1,
      'default'     : 'large',
      'mode'        : 'w' },
    { 'id'          : 'preferred_image_quality',
      'description' : 'Preferred image quality.',
      'type'        : 'float',
      'preference'  : 1,
      'default'     : 75.0,
      'mode'        : 'w' },
)