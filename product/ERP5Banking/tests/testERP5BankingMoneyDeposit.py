##############################################################################
#
# Copyright (c) 2005-2010 Nexedi SA and Contributors. All Rights Reserved.
#                   Aurelien Calonne <aurel@nexedi.com>
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
##############################################################################


# import requested python module
import os
from Products.ERP5Type.tests.Sequence import SequenceList
from Products.ERP5Banking.tests.TestERP5BankingMixin import TestERP5BankingMixin

# Needed in order to have a log file inside the current folder
os.environ['EVENT_LOG_FILE']     = os.path.join(os.getcwd(), 'zLOG.log')
# Define the level of log we want, here is all
os.environ['EVENT_LOG_SEVERITY'] = '-300'


class TestERP5BankingMoneyDepositMixin(TestERP5BankingMixin):
  


  # pseudo constants
  RUN_ALL_TEST = 1 # we want to run all test
  QUIET = 0 # we don't want the test to be quiet

  #var_quantity_10000 = {'variation/1992':0,'variation/2003':1}
  #var_quantity_5000 = {'variation/1992':0,'variation/2003':2}


  def getTitle(self):
    """
      Return the title of the test
    """
    return "ERP5BankingMoneyDeposit"

  def afterSetUp(self):
    """
      Method called before the launch of the test to initialize some data
    """
    self.initDefaultVariable()
    # Set some variables : 
    self.money_deposit_module = self.getMoneyDepositModule()

    # Create a user and login as manager to populate the erp5 portal with objects for tests.
    self.createManagerAndLogin()

    self.createFunctionGroupSiteCategory(site_list=['paris'])

    """
    Windows to create the BANKNOTES of 10 000 and 5000, coins 200.
    It s same to click to the fast input button.  
    """

    # Before the test, we need to input the inventory
    inventory_dict_line_1 = {'id' : 'inventory_line_1',
                             'resource': self.billet_10000,
                             'variation_id': ('emission_letter', 'cash_status', 'variation'),
                             'variation_value': ('emission_letter/p', 'cash_status/valid') + self.variation_list,
                             'quantity': self.quantity_10000}

    inventory_dict_line_2 = {'id' : 'inventory_line_2',
                             'resource': self.billet_200,
                             'variation_id': ('emission_letter', 'cash_status', 'variation'),
                             'variation_value': ('emission_letter/p', 'cash_status/valid') + self.variation_list,
                             'quantity': self.quantity_200}

    inventory_dict_line_3 = {'id' : 'inventory_line_3',
                             'resource': self.billet_5000,
                             'variation_id': ('emission_letter', 'cash_status', 'variation'),
                             'variation_value': ('emission_letter/p', 'cash_status/valid') + self.variation_list,
                             'quantity': self.quantity_5000}


    
    
    line_list = [inventory_dict_line_1, inventory_dict_line_2, inventory_dict_line_3]
    
    self.money_deposit_counter = self.paris.surface.banque_interne
    self.money_deposit_counter_vault = self.paris.surface.banque_interne.guichet_1.encaisse_des_billets_et_monnaies.entrante
    
    self.createCashInventory(source=None, destination=self.money_deposit_counter_vault, currency=self.currency_1,
                             line_list=line_list)


    self.person_1 = self.createPerson(id='person_1',
                                      first_name='toto',
                                      last_name='titi')
    self.bank_account_1 = self.createBankAccount(person=self.person_1,
                                                 account_id='bank_account_1',
                                                 currency=self.currency_1,
                                                 amount=100000)



    # now we need to create a user as Manager to do the test
    # in order to have an assigment defined which is used to do transition
    # Create an Organisation that will be used for users assignment
    self.checkUserFolderType()
    self.organisation = self.organisation_module.newContent(id='paris', portal_type='Organisation',
                          function='banking', group='baobab',  site='testsite/paris')
    # define the user
    user_dict = {
        'super_user' : [['Manager'], self.organisation, 'banking/comptable', 'baobab', 'testsite/paris/surface/banque_interne/guichet_1']
      }
    # call method to create this user
    self.createERP5Users(user_dict)
    self.logout()
    self.login('super_user')
    # open counter date and counter
    self.openCounterDate(site=self.paris)
    self.openCounter(site=self.money_deposit_counter_vault)




  def stepCheckObjects(self, sequence=None, sequence_list=None, **kwd):
    """
    Check that all the objects we created in afterSetUp or
    that were added by the business template and that we rely
    on are really here.
    """
    self.checkResourceCreated()
    # check that MoneyDeposit Module was created
    self.assertEqual(self.money_deposit_module.getPortalType(), 'Money Deposit Module')
    # check cash sorting module is empty
    self.assertEqual(len(self.money_deposit_module.objectValues()), 0)


  def stepCheckInitialInventory(self, sequence=None, sequence_list=None, **kwd):
    """
    Check the initial inventory before any operations
    """
    self.simulation_tool = self.getSimulationTool()
    # check we have 5 banknotes of 10000 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(
                     node=self.money_deposit_counter_vault.getRelativeUrl(), 
                     resource = self.billet_10000.getRelativeUrl()), 5.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_10000.getRelativeUrl()), 5.0)
    # check we have 12 coin of 200 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_200.getRelativeUrl()), 12.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_200.getRelativeUrl()), 12.0)
    # check we have 24 banknotes of 200 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_5000.getRelativeUrl()), 24.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_5000.getRelativeUrl()), 24.0)
    # check the inventory of the bank account
    self.assertEqual(self.simulation_tool.getCurrentInventory(payment=self.bank_account_1.getRelativeUrl()), 100000)
    self.assertEqual(self.simulation_tool.getFutureInventory(payment=self.bank_account_1.getRelativeUrl()), 100000)



  def stepCreateMoneyDeposit(self, sequence=None, sequence_list=None, **kwd):
    """
    Create a cash sorting document and check it
    """
    # Cash sorting has encaisse_paris for source, guichet_1 for destination, and a price cooreponding to the sum of banknote of 10000 and banknotes of 200 ( (2+3) * 10000 + (2+3) * 200 )
    self.money_deposit = self.money_deposit_module.newContent(
                            id='money_deposit', 
                            portal_type='Money Deposit',
                            destination_payment_value = self.bank_account_1,
                            resource_value = self.currency_1,
                            description='test',
                            source_total_asset_price=20000.0)
    # execute tic
    self.stepTic()
    # set source reference
    self.setDocumentSourceReference(self.money_deposit)
    # check source reference
    self.assertNotEqual(self.money_deposit.getSourceReference(), '')
    self.assertNotEqual(self.money_deposit.getSourceReference(), None)
    
    self.money_deposit._setDestination(self.money_deposit_counter.getRelativeUrl())
    self.assertNotEqual(self.money_deposit, None)
    
    # check we have only one cash sorting
    self.assertEqual(len(self.money_deposit_module.objectValues()), 1)
    # get the cash sorting document
    self.money_deposit = getattr(self.money_deposit_module, 'money_deposit')
    # check its portal type
    self.assertEqual(self.money_deposit.getPortalType(), 'Money Deposit')
    self.assertEqual(self.money_deposit.getDestinationPayment(), self.bank_account_1.getRelativeUrl())
    # check that its destination is guichet_1
    self.assertEqual(self.money_deposit.getSourceTotalAssetPrice(), 20000.0)
    self.assertEqual(self.money_deposit.getDestination(), self.money_deposit_counter.getRelativeUrl())

    # the initial state must be draft
    self.assertEqual(self.money_deposit.getSimulationState(), 'draft')

    # source reference must be automatically generated
    self.money_deposit.setSourceReference(self.money_deposit.Baobab_getUniqueReference())
    self.assertNotEqual(self.money_deposit.getSourceReference(), None)
    self.assertNotEqual(self.money_deposit.getSourceReference(), '')

  def stepMoneyDepositSendToCounter(self, sequence=None, sequence_list=None, **kwd):
    """
    Send the check payment to the counter

    FIXME: check if the transition fails when a category or property is invalid.
    """
    self.workflow_tool.doActionFor(self.money_deposit, 'confirm_action', wf_id='money_deposit_workflow')
    self.assertEqual(self.money_deposit.getSimulationState(), 'confirmed')
    self.assertEqual(self.money_deposit.getSourceTotalAssetPrice(), 20000.0)

  def stepMoneyDepositSendToValidation(self, sequence=None, sequence_list=None, **kwd):
    """
    """
    self.workflow_tool.doActionFor(self.money_deposit, 'order_action', wf_id='money_deposit_workflow')
    self.assertEqual(self.money_deposit.getSimulationState(), 'ordered')
    self.assertEqual(self.money_deposit.getSourceTotalAssetPrice(), 20000.0)

  def stepMoneyDepositInputCashDetails(self, sequence=None, sequence_list=None, **kwd):
    """
    Input cash details
    """
    self.addCashLineToDelivery(self.money_deposit, 'line_1', 'Cash Delivery Line', self.billet_10000,
            ('emission_letter', 'cash_status', 'variation'),
            ('emission_letter/p', 'cash_status/valid') + self.variation_list[1:],
            {self.variation_list[1] : 1})
    self.assertEqual(self.money_deposit.line_1.getPrice(), 10000)

    self.addCashLineToDelivery(self.money_deposit, 'line_2', 'Cash Delivery Line', self.billet_5000,
            ('emission_letter', 'cash_status', 'variation'),
            ('emission_letter/p', 'cash_status/valid') + self.variation_list[1:],
            {self.variation_list[1] : 2})
    self.assertEqual(self.money_deposit.line_2.getPrice(), 5000)

  def stepCheckConfirmedInventory(self, sequence=None, sequence_list=None, **kwd):
    """
    Check the inventoryinb state confirmed
    """
    self.simulation_tool = self.getSimulationTool()
    # check we have 5 banknotes of 10000 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_10000.getRelativeUrl()), 5.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_10000.getRelativeUrl()), 5.0)
    # check we have 12 coin of 200 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_200.getRelativeUrl()), 12.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_200.getRelativeUrl()), 12.0)
    # check we have 24 banknotes of 200 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_5000.getRelativeUrl()), 24.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_5000.getRelativeUrl()), 24.0)
    # check the inventory of the bank account, must be planned to be decrease by 20000
    self.assertEqual(self.simulation_tool.getCurrentInventory(payment=self.bank_account_1.getRelativeUrl()), 100000)
    self.assertEqual(self.simulation_tool.getFutureInventory(payment=self.bank_account_1.getRelativeUrl()), 120000)

  def stepDeliverMoneyDeposit(self, sequence=None, sequence_list=None, **kwd):
    self.assertEqual(self.money_deposit.getSourceTotalAssetPrice(),
                     self.money_deposit.getTotalPrice(fast=0, portal_type = ['Cash Delivery Line', 'Cash Delivery Cell']))
    self.workflow_tool.doActionFor(self.money_deposit, 'deliver_action', wf_id='money_deposit_workflow')
    self.assertEqual(self.money_deposit.getSimulationState(), 'delivered')
    
    self.assertEqual(self.money_deposit.getSourceTotalAssetPrice(), 20000.0)
    self.assertEqual(20000.0, self.money_deposit.getTotalPrice(fast=0, portal_type = ['Cash Delivery Line', 'Cash Delivery Cell']))

  def stepCheckFinalInventory(self, sequence=None, sequence_list=None, **kwd):
    """
    Check the initial inventory before any operations
    """
    self.simulation_tool = self.getSimulationTool()
    # check we have 5 banknotes of 10000 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_10000.getRelativeUrl()), 6.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_10000.getRelativeUrl()), 6.0)
    # check we have 12 coin of 200 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_200.getRelativeUrl()), 12.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_200.getRelativeUrl()), 12.0)
    # check we have 24 banknotes of 200 in encaisse_billets_et_monnaies
    self.assertEqual(self.simulation_tool.getCurrentInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_5000.getRelativeUrl()), 26.0)
    self.assertEqual(self.simulation_tool.getFutureInventory(node=self.money_deposit_counter_vault.getRelativeUrl(), resource = self.billet_5000.getRelativeUrl()), 26.0)
    # check the final inventory of the bank account
    #self.assertEqual(self.simulation_tool.getCurrentInventory(payment=self.bank_account_1.getRelativeUrl()), 120000)
    self.assertEqual(self.simulation_tool.getCurrentInventory(payment=self.bank_account_1.getRelativeUrl(), resource=self.currency_1.getRelativeUrl()), 120000)
    self.assertEqual(self.simulation_tool.getFutureInventory(payment=self.bank_account_1.getRelativeUrl(), resource=self.currency_1.getRelativeUrl()), 120000)

  def stepDelMoneyDeposit(self, sequence=None, sequence_list=None, **kwd):
    """
    Delete the invalid vault_transfer line previously create
    """
    self.money_deposit_module.deleteContent('money_deposit_1')

  ##################################
  ##  Tests
  ##################################

class TestERP5BankingMoneyDeposit(TestERP5BankingMoneyDepositMixin):

  # pseudo constants
  RUN_ALL_TEST = 1 # we want to run all test
  QUIET = 0 # we don't want the test to be quiet

  def test_01_ERP5BankingMoneyDeposit(self, quiet=QUIET, run=RUN_ALL_TEST):
    """
    Define the sequence of step that will be play
    """
    if not run:
      return
    sequence_list = SequenceList()
    # define the sequence
    sequence_string = 'Tic CheckObjects Tic CheckInitialInventory ' \
                    + 'CreateMoneyDeposit Tic ' \
                    + 'MoneyDepositSendToValidation Tic ' \
                    + 'MoneyDepositSendToCounter Tic ' \
                    + 'MoneyDepositInputCashDetails ' \
                    + 'CheckConfirmedInventory Tic ' \
                    + 'DeliverMoneyDeposit Tic ' \
                    + 'CheckFinalInventory'
    sequence_list.addSequenceString(sequence_string)
    # play the sequence
    sequence_list.play(self)

