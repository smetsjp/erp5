# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 Nexedi SA and Contributors. All Rights Reserved.
#                    Jean-Paul Smets-Solanes <jp@nexedi.com>
#                    Yusuke Muraoka <yusuke@nexedi.com>
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

from Products.ERP5Type import Permissions, PropertySheet, interfaces
from Products.ERP5Type.XMLObject import XMLObject

import zope.interface

class BusinessState(XMLObject):
  """
    The BusinessState class defines the various states in 
    a Business Process. It defines the synchronisation milestones
    between movements related to the trade phases of business.
  """
  meta_type = 'ERP5 Business State'
  portal_type = 'Business State'

  # Declarative security
  security = ClassSecurityInfo()
  security.declareObjectProtected(Permissions.AccessContentsInformation)

  # Declarative properties
  property_sheets = ( PropertySheet.Base
                    , PropertySheet.XMLObject
                    , PropertySheet.CategoryCore
                    , PropertySheet.DublinCore
                    , PropertySheet.Folder
                    , PropertySheet.Comment
                    , PropertySheet.SortIndex
                    )

  # Declarative interfaces
  zope.interface.implements(
                            )

  # IBusinessCompletable implementation
  def isCompleted(self, explanation):
    """
      If all path which reach this state are completed
      then this state is completed
    """
    for path in self.getSuccessorRelatedValueList():
      if not path.isCompleted(explanation):
        return False
    return True


  def isPartiallyCompleted(self, explanation):
    """
      If all path which reach this state are partially completed
      then this state is completed
    """
    for path in self.getSuccessorRelatedValueList():
      if not path.isPartiallyCompleted(explanation):
        return False
    return True

  # IBusinessCompletable - duration calculation
  def getExpectedCompletionDate(self, explanation, *args, **kwargs):
    """
      Returns the expected completion date for this
      state based on the explanation.

      explanation -- the document
    """
    # Should be re-calculated?
    if 'predecessor_date' in kwargs:
      del kwargs['predecessor_date']
    date_list = self._getExpectedDateList(explanation,
                                          self.getSuccessorRelatedValueList(),
                                          self._getExpectedCompletionDate,
                                          *args,
                                          **kwargs)
    if len(date_list) > 0:
      return min(date_list)

  def _getExpectedCompletionDate(self, path, *args, **kwargs):
    return path.getExpectedStopDate(*args, **kwargs)

  def getExpectedBeginningDate(self, explanation, *args, **kwargs):
    """
      Returns the expected beginning date for this
      state based on the explanation.

      explanation -- the document
    """
    # Should be re-calculated?
    if 'predecessor_date' in kwargs:
      del kwargs['predecessor_date']
    date_list = self._getExpectedDateList(explanation,
                                          self.getPredecessorRelatedValueList(),
                                          self._getExpectedBeginningDate,
                                          *args,
                                          **kwargs)
    if len(date_list) > 0:
      return min(date_list)

  def _getExpectedBeginningDate(self, path, *args, **kwargs):
    expected_date = path.getExpectedStartDate(*args, **kwargs)
    if expected_date is not None:
      return expected_date - path.getWaitTime()

  def _getExpectedDateList(self, explanation, path_list, path_method,
                           visited=None, *args, **kwargs):
    """
      getExpected(Beginning/Completion)Date are same structure
      expected date of each path should be returned.

      explanation -- the document
      path_list -- list of target business path
      path_method -- used to get expected date on each path
      visited -- only used to prevent infinite recursion internally
    """
    if visited is None:
      visited = []

    expected_date_list = []
    for path in path_list:
      # filter paths without path of root explanation
      if path not in visited or path.isDeliverable():
        expected_date = path_method(path, explanation, visited=visited, *args, **kwargs)
        if expected_date is not None:
          expected_date_list.append(expected_date)

    return expected_date_list

  def getExpectedCompletionDuration(self, explanation):
    """
      Returns the expected completion duration for this
      state.
    """

  def getRemainingTradePhaseList(self, explanation, trade_phase_list=None):
    """
      Returns the list of remaining trade phase for this
      state based on the explanation.

      trade_phase_list -- if provide, the result is filtered by it after collected
    """
    remaining_trade_phase_list = []
    for path in self.getPredecessorRelatedValueList():
      # XXX When no simulations related to path, what should path.isCompleted return?
      #     if True we don't have way to add remaining trade phases to new movement
      if not (path.getRelatedSimulationMovementValueList(explanation) and
              path.isCompleted(explanation)):
        remaining_trade_phase_list += path.getTradePhaseValueList()

      # collect to successor direction recursively
      state = path.getSuccessorValue()
      if state is not None:
        remaining_trade_phase_list.extend(
          state.getRemainingTradePhaseList(explanation, None))

    # filter just at once if given
    if trade_phase_list is not None:
      remaining_trade_phase_list = filter(
        lambda x : x.getLogicalPath() in trade_phase_list,
        remaining_trade_phase_list)

    return remaining_trade_phase_list
