'''
Created on Jul 28, 2017

@author: Matt
'''
import sqlite3
import wx
from CampaignFinanceGUI import frmCampaignFinanceMain
import datetime
import csv
import os

def pydate2wxdate(date):
        assert isinstance(date, (datetime.datetime, datetime.date))
        tt = date.timetuple()
        dmy = (tt[2], tt[1]-1, tt[0])
        return wx.DateTimeFromDMY(*dmy)

class CampaignFinanceForm(frmCampaignFinanceMain):
    def __init__(self,parent=None):
        super(CampaignFinanceForm,self).__init__(parent)
        
        self.setupGUI()
        self.con = None
        
        self.donation_edit_id = None
        self.donor_edit_id = None
        
        self.state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        
        self.expense_type_list = ['ADVERTISE','ACCOUNT','CONSULT','CREDITCARD','EVENT','FEES',
                                  'GIFTS''LEGAL','FOOD','POLLING','PRINTING','SALARIES','FUNDRAISE',
                                  'TRAVELIN','TRAVELOUT','OVERHEAD','LOAN','TRANSPORT','DONATIONS','OTHER']
        self.cmbExpenseType.SetItems(self.expense_type_list)
        
        self.cmbDonorState.SetItems(self.state_list)
        self.cmbPayeeState.SetItems(self.state_list)

        self.ntbMain.Disable()
        
        self.clearAll()
        
    
    def color_grid_row(self,grid,row_num,color):
        ncols = grid.GetNumberCols()
        for c in range(0,ncols):
            grid.SetCellBackgroundColour(row_num,c,color)
        grid.Refresh()
        
    def color_all_grid_cells(self,grid,color):
        ncols = grid.GetNumberCols()
        nrows = grid.GetNumberRows()
        for c in range(0,ncols):
            for r in range(0,nrows):
                grid.SetCellBackgroundColour(r,c,color)
        grid.Refresh()
    
    def mNew_click(self,event):
        saveFileDialog = wx.FileDialog(self,"Create New Database File",wildcard="db files (*.db)|*.db",style=wx.FD_SAVE)
        if saveFileDialog.ShowModal() != wx.ID_CANCEL:
            filename = saveFileDialog.GetPath()
            self.con = self.createDB(filename)
            self.ntbMain.Enable()
            self.refreshDBData()
            self.updateChoices()
            self.updateTableData()

            
    def mOpen_click(self,event):
        openFileDialog = wx.FileDialog(self,"Create New Database File",wildcard="db files (*.db)|*.db",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() != wx.ID_CANCEL:
            self.clearAll();
            filename = openFileDialog.GetPath()
            self.con = self.openDB(filename)
            #TODO: Verify Schema integrity
            self.ntbMain.Enable()
            self.refreshDBData()
            self.updateChoices()
            self.updateTableData()
            
    
    def refreshDBData(self):
        self.donation_list = self.getDonations()
        self.unitemized_donation_list = self.getUnitemizedDonations()
        self.donor_list = self.getDonors()
        self.donation_type_list = self.getDonationTypes()
        self.expense_list = self.getExpenses()
        self.payee_list = self.getPayees()
        
        self.total_expenses = self.getTotalExpenses()
        self.total_donations = self.getTotalDonations()
        self.total_in_kind = self.getTotalInKind()
        self.balance = self.total_donations-self.total_expenses
        
    def btnDonationReport_click(self,event):
        from_date = self.dpkReportFrom.Value.Format('%Y-%m-%d')
        to_date = self.dpkReportTo.Value.Format('%Y-%m-%d')
                
        if self.con:
            cur = self.con.cursor()
            cur.execute('''SELECT 
                                don.type, 
                                don.first_name, 
                                don.last_name, 
                                don.title, 
                                don.suffix, 
                                don.address, 
                                don.city, 
                                don.state, 
                                don.zip, 
                                don.employer, 
                                don.occupation,
                                donations.date, 
                                donations.amount, 
                                donations.description, 
                                don_typ.code,
                                don.exclude_from_reporting 
                            FROM donations
                            INNER JOIN donors don ON donations.donor_id = don.id 
                            INNER JOIN donation_types don_typ ON donations.type_id = don_typ.id 
                            WHERE donations.date BETWEEN ? AND ? 
                            AND exclude_from_reporting = 0 
                            ORDER BY donations.date, don.last_name''',(from_date,to_date))
            res = cur.fetchall()
            csv_rows = []
            for row in res:
                date_code = datetime.datetime.strptime(row[11],'%Y-%m-%d').strftime('%Y%m%d')
                csv_rows += [['RCPT',row[14],'',row[0],row[2],row[1],row[3],row[4],row[5],
                            '',row[6],row[7],row[8],'USA',
                            '','',date_code,row[12],row[13],row[9],row[10],'','','','']]
            saveFileDialog = wx.FileDialog(self,"Report File",defaultFile='report.csv',wildcard="csv files (*.csv)|*.csv",style=wx.FD_SAVE)
            if saveFileDialog.ShowModal() != wx.ID_CANCEL:
                filename = saveFileDialog.GetPath()
                if os.path.splitext(filename)[1].lower != '.csv':
                    filename += '.csv'
                with open(filename,'wb') as fout:
                    writer = csv.writer(fout)
                    writer.writerow(['#Rec_Type','Form_Type','Item_ID','Entity_Cd','Ctrib_NamL','Ctrib_NamF','Ctrib_NamT','Ctrib_NamS',
                                    'Ctrib_Adr1','Ctrib_Adr2','Ctrib_City','Ctrib_StCd','Ctrib_ZIP4','Ctrib_CtryCD',
                                    'OS_PAC_CB','OS_PAC_FEC','Ctrib_Date','Ctrib_Amt','Ctrib_Dscr','Employer','Occup','Job_Title','Spous_Law','Parent1','Parent2'])
                    writer.writerows(csv_rows)
            
    def btnExpenseReport_click(self,event):
        from_date = self.dpkReportFrom.Value.Format('%Y-%m-%d')
        to_date = self.dpkReportTo.Value.Format('%Y-%m-%d')
                
        if self.con:
            cur = self.con.cursor()
            cur.execute('''SELECT 
                                pay.type, 
                                pay.first_name, 
                                pay.last_name, 
                                pay.title, 
                                pay.suffix, 
                                pay.address, 
                                pay.city, 
                                pay.state, 
                                pay.zip, 
                                exp.date, 
                                exp.amount, 
                                exp.description, 
                                exp.type 
                            FROM expenses exp 
                            INNER JOIN payees pay ON exp.payee_id = pay.id 
                            WHERE exp.date BETWEEN ? AND ? 
                            ORDER BY exp.date, pay.last_name''',(from_date,to_date))
            res = cur.fetchall()
            csv_rows = []
            for row in res:
                date_code = datetime.datetime.strptime(row[9],'%Y-%m-%d').strftime('%Y%m%d')
                csv_rows += [['EXPN','F1','',row[0],row[2],row[1],row[3],row[4],row[5],
                            '',row[6],row[7],row[8],'USA',
                            date_code,row[10],row[11],'Y','',
                            '','','','',
                            '','','','','','','','',
                            '','','','','','','','','',
                            '','','','','','','',row[12],'',
                            ]]
            saveFileDialog = wx.FileDialog(self,"Report File",defaultFile='report.csv',wildcard="csv files (*.csv)|*.csv",style=wx.FD_SAVE)
            if saveFileDialog.ShowModal() != wx.ID_CANCEL:
                filename = saveFileDialog.GetPath()
                if os.path.splitext(filename)[1].lower != 'csv':
                    filename += '.csv'
                with open(filename,'wb') as fout:
                    writer = csv.writer(fout)
                    writer.writerow(['#Rec_Type','Form_Type','Item_ID','Entity_Cd','Payee_NamL','Payee_NamF','Payee_NamT','Payee_NamS',
                                    'Payee_Adr1','Payee_Adr2','Payee_City','Payee_StCd','Payee_ZIP4','Payee_CtryCD',
                                    'Expn_Date','Expn_Amt','Expn_Dscr','ExpCntr_YN', 'Reimbur_CB', 
                                    'Cand_NamL', 'Cand_NamF', 'Cand_NamT', 'Cand_NamS', 
                                    'OffHldCd', 'OffHldNam', 'OffHldDist','OffHldPlace', 'OffSeekCd', 'OffseekNam', 'OffseekDist','OffSeekPlace', 
                                    'BakRef_ID', 'ExpnCorp_YN', 'Trvl_CB', 'Trvl_NamL', 'Trvl_NamF', 'Trvl_NamT', 'Trvl_NamS', 'Tran_Type','Tran_Descr', 
                                    'Dpt_City', 'Dpt_Date', 'Arv_City', 'Arv_Date', 'Trvl_Purp', 'Trvl_BakRef', 'Expn_CatgOth', 'Expn_Catg', 'Aus_Living_Exp_CB'])
                    writer.writerows(csv_rows)        
                            
    
    def grdDonationsCell_click(self, event):
        edit_row = event.GetRow()
        self.editDonation(edit_row)
        
    def grdUnitemizedDonationsCell_click(self, event):
        edit_row = event.GetRow()
        self.editUnitemizedDonation(edit_row)
        
    def grdDonorsCell_click(self, event):
        edit_row = event.GetRow()
        self.editDonor(edit_row)
        
    def grdExpensesCell_click(self, event):
        edit_row = event.GetRow()
        self.editExpense(edit_row)
        
    def grdPayeesCell_click(self, event):
        edit_row = event.GetRow()
        self.editPayee(edit_row)
        
    def chkCandidate_click(self, event):
        if self.chkCandidate.IsChecked():
            self.pnlCandidate.Show()
            self.pnlPayees.Layout()
            self.pnlPayees.Refresh()
        else:
            self.pnlCandidate.Hide()
            self.pnlPayees.Layout()
            self.pnlPayees.Refresh()
        
    def grdDonors_key(self,event):
        key = event.GetKeyCode()
        if key == wx.WXK_DELETE:
            delete_row = self.grdDonors.GetGridCursorRow()
            self.deleteDonor(delete_row)
    
    def grdDonations_key(self,event):
        key = event.GetKeyCode()
        if key == wx.WXK_DELETE:
            delete_row = self.grdDonations.GetGridCursorRow()
            self.deleteDonation(delete_row)
            
    def grdPayees_key(self,event):
        key = event.GetKeyCode()
        if key == wx.WXK_DELETE:
            delete_row = self.grdPayees.GetGridCursorRow()
            self.deletePayee(delete_row)
            
    def grdExpenses_key(self,event):
        key = event.GetKeyCode()
        if key == wx.WXK_DELETE:
            delete_row = self.grdExpenses.GetGridCursorRow()
            self.deleteExpense(delete_row)

    
    def editUnitemizedDonation(self,row_num):
        self.clearUnitemizedDonationForm()
        donation_to_edit = self.unitemized_donation_list[row_num]
        self.unitemized_donation_edit_id = donation_to_edit['id']
        
        self.txtUnitemizedDonationAmount.Value = '%1.2f' % donation_to_edit['amount']
        self.txtUnitemizedDonationDescription.Value = donation_to_edit['description']
        dt = wx.DateTime()
        dt.ParseFormat(donation_to_edit['date'],'%Y-%m-%d')
        self.dpkUnitemizedDonationDate.Value = dt
        self.color_grid_row(self.grdUnitemizedDonations,row_num,'yellow')
        self.grdUnitemizedDonations.Refresh()
        self.btnUpdateUnitemizedDonation.Show()
        self.btnCancelUnitemizedDonation.Show()
        self.btnAddUnitemizedDonation.Hide()
        
    def editDonation(self,row_num):
        self.clearDonationForm()
        donation_to_edit = self.donation_list[row_num]
        self.donation_edit_id = donation_to_edit['id']
        
        self.txtDonationAmount.Value = '%1.2f' % donation_to_edit['amount']
        self.txtDonationDescription.Value = donation_to_edit['description']
        dt = wx.DateTime()
        dt.ParseFormat(donation_to_edit['date'],'%Y-%m-%d')
        self.dpkDonationDate.Value = dt
        self.cmbDonor.SetSelection(( i for i,d in enumerate(self.donor_list) if d['id']==donation_to_edit['donor_id']).next())
        self.cmbDonationType.SetSelection(( i for i,d in enumerate(self.donation_type_list) if d['id']==donation_to_edit['type_id']).next())
        self.color_grid_row(self.grdDonations,row_num,'yellow')
        self.grdDonations.Refresh()
        self.btnUpdateDonation.Show()
        self.btnCancelDonation.Show()
        self.btnAddDonation.Hide()
        
    def editDonor(self,row_num):
        self.clearDonorForm()
        donor_to_edit = self.donor_list[row_num]
        self.donor_edit_id = donor_to_edit['id']
        
        self.txtDonorFirstName.Value = donor_to_edit['first_name']
        self.txtDonorLastName.Value = donor_to_edit['last_name']
        self.txtDonorTitle.Value = donor_to_edit['title']
        self.txtDonorSuffix.Value = donor_to_edit['suffix']
        self.txtDonorAddress.Value = donor_to_edit['address']
        self.txtDonorCity.Value = donor_to_edit['city']
        self.txtDonorZipCode.Value = donor_to_edit['zip']
        self.txtDonorEmployer.Value = donor_to_edit['employer']
        self.txtDonorOccupation.Value = donor_to_edit['occupation']
        self.cmbDonorState.Selection = self.state_list.index(donor_to_edit['state'])
        self.chkExcludeFromReporting.Value = donor_to_edit['exclude_from_reporting']
        if donor_to_edit['type'] == 'I':
            self.cmbDonorType.Selection = 0
        else:
            self.cmbDonorType.Selection = 1
        self.color_grid_row(self.grdDonors,row_num,'yellow')
        self.grdDonors.Refresh()
        self.btnAddDonor.Hide()
        self.btnUpdateDonor.Show()
        self.btnCancelDonor.Show()
        
    def editPayee(self,row_num):
        self.clearPayeeForm()
        payee_to_edit = self.payee_list[row_num]
        self.payee_edit_id = payee_to_edit['id']
        
        self.txtPayeeFirstName.Value = payee_to_edit['first_name']
        self.txtPayeeLastName.Value = payee_to_edit['last_name']
        self.txtPayeeTitle.Value = payee_to_edit['title']
        self.txtPayeeSuffix.Value = payee_to_edit['suffix']
        self.txtPayeeAddress.Value = payee_to_edit['address']
        self.txtPayeeCity.Value = payee_to_edit['city']
        self.txtPayeeZipCode.Value = payee_to_edit['zip']
        self.cmbPayeeState.Selection = self.state_list.index(payee_to_edit['state'])
        if payee_to_edit['type'] == 'I':
            self.cmbPayeeType.Selection = 0
        else:
            self.cmbPayeeType.Selection = 1
            
        self.color_grid_row(self.grdPayees,row_num,'yellow')
        self.grdPayees.Refresh()
        self.btnUpdatePayee.Show()
        self.btnCancelPayee.Show()
        self.btnAddPayee.Hide()
        
    def editExpense(self,row_num):
        self.clearExpenseForm()
        expense_to_edit = self.expense_list[row_num]
        self.expense_edit_id = expense_to_edit['id']
        
        self.txtExpenseAmount.Value = '%1.2f' % expense_to_edit['amount']
        self.txtExpenseDescription.Value = expense_to_edit['description']
        dt = wx.DateTime()
        dt.ParseFormat(expense_to_edit['date'],'%Y-%m-%d')
        self.dpkExpenseDate.Value = dt
        self.cmbPayee.SetSelection(( i for i,d in enumerate(self.payee_list) if d['id']==expense_to_edit['payee_id']).next())
        self.cmbExpenseType.SetSelection(( i for i,d in enumerate(self.expense_type_list) if d==expense_to_edit['type']).next())
        self.color_grid_row(self.grdExpenses,row_num,'yellow')
        self.grdExpenses.Refresh()
        self.btnUpdateExpense.Show()
        self.btnCancelExpense.Show()
        self.btnAddExpense.Hide()
        
    def deleteDonor(self,row_num):
        donor_to_delete = self.donor_list[row_num]
        dlg = wx.MessageDialog(self, "Are you sure you want to delete the Donor:%s"%donor_to_delete['full_name'], "Confirm Delete", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            if self.con:
                cur = self.con.cursor()
                cur.execute('DELETE FROM donors WHERE id=?',(donor_to_delete['id'],))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
                self.updateChoices()
                
    def deletePayee(self,row_num):
        payee_to_delete = self.payee_list[row_num]
        dlg = wx.MessageDialog(self, "Are you sure you want to delete the payee:%s"%payee_to_delete['full_name'], "Confirm Delete", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            if self.con:
                cur = self.con.cursor()
                cur.execute('DELETE FROM payees WHERE id=?',(payee_to_delete['id'],))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
                self.updateChoices()
                
    def deleteExpense(self,row_num):
        expense_to_delete = self.expense_list[row_num]
        dlg = wx.MessageDialog(self, "Are you sure you want to delete the Expense:%s (%1.2f)"%(expense_to_delete['payee_name'],expense_to_delete['amount']), "Confirm Delete", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            if self.con:
                cur = self.con.cursor()
                cur.execute('DELETE FROM expenses WHERE id=?',(expense_to_delete['id'],))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
                
    def deleteDonation(self,row_num):
        donation_to_delete = self.donation_list[row_num]
        dlg = wx.MessageDialog(self, "Are you sure you want to delete the Donation:%s (%1.2f)"%(donation_to_delete['donor_name'],donation_to_delete['amount']), "Confirm Delete", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            if self.con:
                cur = self.con.cursor()
                cur.execute('DELETE FROM donations WHERE id=?',(donation_to_delete['id'],))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
        
    def clearUnitemizedDonationForm(self):
        self.txtUnitemizedDonationAmount.Value = ''
        self.txtUnitemizedDonationDescription.Value = ''
        dt = wx.DateTime()
        self.dpkUnitemizedDonationDate.Value = dt.Now()
        self.color_all_grid_cells(self.grdUnitemizedDonations,'white')
    
    def clearDonationForm(self):
        self.cmbDonor.Selection = wx.NOT_FOUND
        self.cmbDonationType.Selection = wx.NOT_FOUND
        self.txtDonationAmount.Value = ''
        self.txtDonationDescription.Value = ''
        dt = wx.DateTime()
        self.dpkDonationDate.Value = dt.Now()
        self.color_all_grid_cells(self.grdDonations,'white')
        
    def clearDonorForm(self):
        self.txtDonorFirstName.Value = ''
        self.txtDonorLastName.Value = ''
        self.txtDonorTitle.Value = ''
        self.txtDonorSuffix.Value = ''
        self.txtDonorAddress.Value = ''
        self.txtDonorCity.Value = ''
        self.cmbDonorState.Selection = wx.NOT_FOUND
        self.txtDonorZipCode.Value = ''
        self.txtDonorEmployer.Value = ''
        self.txtDonorOccupation.Value = ''
        self.cmbDonorType.Selection = 0
        self.chkExcludeFromReporting.Value = False
        self.color_all_grid_cells(self.grdDonors,'white')
        
    def clearPayeeForm(self):
        self.txtPayeeFirstName.Value = ''
        self.txtPayeeLastName.Value = ''
        self.txtPayeeTitle.Value = ''
        self.txtPayeeSuffix.Value = ''
        self.txtPayeeAddress.Value = ''
        self.txtPayeeCity.Value = ''
        self.cmbPayeeState.Selection = wx.NOT_FOUND
        self.txtPayeeZipCode.Value = ''
        self.cmbPayeeType.Selection = 0
        self.color_all_grid_cells(self.grdPayees,'white')
    
    def clearAll(self):
        self.clearDonorForm()
        self.clearPayeeForm()
        self.clearDonationForm()
        self.clearExpenseForm()
        
        self.btnUpdateDonation.Hide()
        self.btnCancelDonation.Hide()
        self.btnAddDonation.Show()
        
        self.btnAddDonor.Show()
        self.btnUpdateDonor.Hide()
        self.btnCancelDonor.Hide()

        self.btnAddPayee.Show()        
        self.btnUpdatePayee.Hide()
        self.btnCancelPayee.Hide()

        self.btnAddExpense.Show()        
        self.btnUpdateExpense.Hide()
        self.btnCancelExpense.Hide()   
    
    def btnUpdateUnitemizedDonation_click(self, event):
        if self.unitemized_donation_edit_id:
            amount = self.txtUnitemizedDonationAmount.Value
            date = self.dpkUnitemizedDonationDate.Value.Format('%Y-%m-%d')
            description = self.txtUnitemizedDonationDescription.Value
            if self.con:
                cur = self.con.cursor()
                cur.execute('UPDATE unitemized_donations SET amount=?,date=?,description=? WHERE id=?',(amount,date,description,self.unitemized_donation_edit_id))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
        self.clearUnitemizedDonationForm()
        self.btnUpdateUnitemizedDonation.Hide()
        self.btnCancelUnitemizedDonation.Hide()
        self.btnAddUnitemizedDonation.Show()
        self.unitemized_donation_edit_id = None
    
    def btnUpdateDonation_click(self, event):
        if self.donation_edit_id:
            amount = self.txtDonationAmount.Value
            date = self.dpkDonationDate.Value.Format('%Y-%m-%d')
            description = self.txtDonationDescription.Value
            donor_id = self.donor_list[self.cmbDonor.GetSelection()]['id']
            type_id = self.donation_type_list[self.cmbDonationType.GetSelection()]['id']
            if self.con:
                cur = self.con.cursor()
                cur.execute('UPDATE donations SET amount=?,date=?,description=?,donor_id=?,type_id=? WHERE id=?',(amount,date,description,donor_id,type_id,self.donation_edit_id))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
        self.clearDonationForm()
        self.btnUpdateDonation.Hide()
        self.btnCancelDonation.Hide()
        self.btnAddDonation.Show()
        self.donation_edit_id = None
    
    def btnCancelDonation_click(self, event):
        self.clearDonationForm()
        self.btnUpdateDonation.Hide()
        self.btnCancelDonation.Hide()
        self.btnAddDonation.Show()
        self.donation_edit_id = None
        
    def btnCancelUnitemizedDonation_click(self, event):
        self.clearUnitemizedDonationForm()
        self.btnUpdateUnitemizedDonation.Hide()
        self.btnCancelUnitemizedDonation.Hide()
        self.btnAddUnitemizedDonation.Show()
        self.unitemized_donation_edit_id = None
        
    
    def btnAddUnitemizedDonation_click(self, event):
        amount = self.txtUnitemizedDonationAmount.Value
        date = self.dpkUnitemizedDonationDate.Value.Format('%Y-%m-%d')
        description = self.txtUnitemizedDonationDescription.Value
        if self.con:
            cur = self.con.cursor()
            cur.execute('INSERT INTO unitemized_donations (amount,date,description) VALUES (?,?,?)',(amount,date,description))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
            self.updateChoices()
        self.clearUnitemizedDonationForm()
    
    def btnAddDonation_click(self, event):
        amount = self.txtDonationAmount.Value
        date = self.dpkDonationDate.Value.Format('%Y-%m-%d')
        description = self.txtDonationDescription.Value
        donor_id = self.donor_list[self.cmbDonor.GetSelection()]['id']
        type_id = self.donation_type_list[self.cmbDonationType.GetSelection()]['id']
        if self.con:
            cur = self.con.cursor()
            cur.execute('INSERT INTO donations (amount,date,description,donor_id,type_id) VALUES (?,?,?,?,?)',(amount,date,description,donor_id,type_id))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
            self.updateChoices()
        self.clearDonationForm()
    
    
    
    def btnAddDonor_click(self, event):
        first_name = self.txtDonorFirstName.Value
        last_name = self.txtDonorLastName.Value
        title = self.txtDonorTitle.Value
        suffix = self.txtDonorSuffix.Value
        address = self.txtDonorAddress.Value
        city = self.txtDonorCity.Value
        state = self.state_list[self.cmbDonorState.Selection]
        zipcode = self.txtDonorZipCode.Value
        employer = self.txtDonorEmployer.Value
        occupation = self.txtDonorOccupation.Value
        exclude_from_reporting = self.chkExcludeFromReporting.Value
        if self.cmbDonorType.Selection == 0:
            donor_type = 'I'
        else:
            donor_type = 'E'
        if self.con:
            cur = self.con.cursor()
            cur.execute('INSERT INTO donors ('
                        'first_name,'
                        'last_name,'
                        'title,'
                        'suffix,'
                        'address,'
                        'city,'
                        'state,'
                        'zip,'
                        'employer,'
                        'occupation,'
                        'type,'
                        'exclude_from_reporting) '
                        'VALUES ('
                        '?,?,?,?,?,?,?,?,?,?,?,?)',(first_name,
                                                    last_name,
                                                    title,
                                                    suffix,
                                                    address,
                                                    city,
                                                    state,
                                                    zipcode,
                                                    employer,
                                                    occupation,
                                                    donor_type,
                                                    exclude_from_reporting))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
            self.updateChoices()
        
        self.clearDonorForm()
        
    def btnAddPayee_click(self, event):
        first_name = self.txtPayeeFirstName.Value
        last_name = self.txtPayeeLastName.Value
        title = self.txtPayeeTitle.Value
        suffix = self.txtPayeeSuffix.Value
        address = self.txtPayeeAddress.Value
        city = self.txtPayeeCity.Value
        state = self.state_list[self.cmbPayeeState.Selection]
        zipcode = self.txtPayeeZipCode.Value
        if self.cmbPayeeType.Selection == 0:
            payee_type = 'I'
        else:
            payee_type = 'E'
        if self.con:
            cur = self.con.cursor()
            cur.execute('INSERT INTO payees (first_name,last_name,title,suffix,address,city,state,zip,type) VALUES (?,?,?,?,?,?,?,?,?)',(first_name,last_name,title,suffix,address,city,state,zipcode,payee_type))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
            self.updateChoices()
        
        self.clearPayeeForm()

    def btnUpdateDonor_click(self, event):
        first_name = self.txtDonorFirstName.Value
        last_name = self.txtDonorLastName.Value
        title = self.txtDonorTitle.Value
        suffix = self.txtDonorSuffix.Value
        address = self.txtDonorAddress.Value
        city = self.txtDonorCity.Value
        state = self.state_list[self.cmbDonorState.Selection]
        zipcode = self.txtDonorZipCode.Value
        employer = self.txtDonorEmployer.Value
        occupation = self.txtDonorOccupation.Value
        exclude_from_reporting = self.chkExcludeFromReporting.Value
        if self.cmbDonorType.Selection == 0:
            donor_type = 'I'
        else:
            donor_type = 'E'
        if self.con:
            cur = self.con.cursor()
            cur.execute('UPDATE donors '
                        'SET first_name=?,'
                        'last_name=?,'
                        'title=?,'
                        'suffix=?,'
                        'address=?,'
                        'city=?,'
                        'state=?,'
                        'zip=?,'
                        'employer=?,'
                        'occupation=?,'
                        'type=?,'
                        'exclude_from_reporting=? '
                        'WHERE id=?',(first_name,
                                      last_name,
                                      title,suffix,
                                      address,
                                      city,
                                      state,
                                      zipcode,
                                      employer,
                                      occupation,
                                      donor_type,
                                      exclude_from_reporting,
                                      self.donor_edit_id))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
            self.updateChoices()
        
        self.clearDonorForm()
        self.btnUpdateDonor.Hide()
        self.btnCancelDonor.Hide()
        self.btnAddDonor.Show()
        self.donor_edit_id = None

        
    def btnCancelDonor_click(self, event):
        self.clearDonorForm()
        self.btnUpdateDonor.Hide()
        self.btnCancelDonor.Hide()
        self.btnAddDonor.Show()
        self.donor_edit_id = None

        
    def btnUpdatePayee_click(self, event):
        first_name = self.txtPayeeFirstName.Value
        last_name = self.txtPayeeLastName.Value
        title = self.txtPayeeTitle.Value
        suffix = self.txtPayeeSuffix.Value
        address = self.txtPayeeAddress.Value
        city = self.txtPayeeCity.Value
        state = self.state_list[self.cmbPayeeState.Selection]
        zipcode = self.txtPayeeZipCode.Value
        if self.cmbPayeeType.Selection == 0:
            payee_type = 'I'
        else:
            payee_type = 'E'
        if self.con:
            cur = self.con.cursor()
            cur.execute('UPDATE payees SET first_name=?,last_name=?,title=?,suffix=?,address=?,city=?,state=?,zip=?,type=? WHERE id=?',(first_name,last_name,title,suffix,address,city,state,zipcode,payee_type,self.payee_edit_id))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
            self.updateChoices()
        
        self.clearPayeeForm()
        self.btnUpdatePayee.Hide()
        self.btnCancelPayee.Hide()
        self.btnAddPayee.Show()
        self.payee_edit_id = None
        
    def btnCancelPayee_click(self, event):
        self.clearPayeeForm()
        self.btnUpdatePayee.Hide()
        self.btnCancelPayee.Hide()
        self.btnAddPayee.Show()
        self.payee_edit_id = None
        
    def btnAddExpense_click(self, event):
        amount = self.txtExpenseAmount.Value
        date = self.dpkExpenseDate.Value.Format('%Y-%m-%d')
        description = self.txtExpenseDescription.Value
        donor_id = self.payee_list[self.cmbPayee.GetSelection()]['id']
        expense_type = self.expense_type_list[self.cmbExpenseType.GetSelection()]
        if self.con:
            cur = self.con.cursor()
            cur.execute('INSERT INTO expenses (amount,date,description,payee_id,type) VALUES (?,?,?,?,?)',(amount,date,description,donor_id,expense_type))
            self.con.commit()
            self.refreshDBData()
            self.updateTableData()
        self.clearExpenseForm()
        
    def clearExpenseForm(self):
        self.cmbPayee.Selection = wx.NOT_FOUND
        self.cmbExpenseType.Selection = wx.NOT_FOUND
        self.txtExpenseAmount.Value = ''
        self.txtExpenseDescription.Value = ''
        dt = wx.DateTime()
        self.dpkExpenseDate.Value = dt.Now()
        self.color_all_grid_cells(self.grdExpenses,'white')        
        
    
        
        
    def btnUpdateExpense_click(self, event):
        if self.expense_edit_id:
            amount = self.txtExpenseAmount.Value
            date = self.dpkExpenseDate.Value.Format('%Y-%m-%d')
            description = self.txtExpenseDescription.Value
            payee_id = self.payee_list[self.cmbPayee.GetSelection()]['id']
            expense_type = self.expense_type_list[self.cmbExpenseType.GetSelection()]
            if self.con:
                cur = self.con.cursor()
                cur.execute('UPDATE expenses SET amount=?,date=?,description=?,payee_id=?,type=? WHERE id=?',(amount,date,description,payee_id,expense_type,self.expense_edit_id))
                self.con.commit()
                self.refreshDBData()
                self.updateTableData()
        self.clearExpenseForm()
        self.btnUpdateExpense.Hide()
        self.btnCancelExpense.Hide()
        self.btnAddExpense.Show()
        self.expense_edit_id = None
        
    def btnCancelExpense_click(self, event):
        self.clearExpenseForm()
        self.btnUpdateExpense.Hide()
        self.btnCancelExpense.Hide()
        self.btnAddExpense.Show()
        self.expense_edit_id = None
        
    def getDonationTypes(self):
        if self.con:
            types = []
            cur = self.con.cursor()
            cur.execute('''SELECT id, 
                                  name, 
                                  code
                                  FROM donation_types''')
            for row in cur.fetchall():
                types += [{'id':row[0],'name':row[1],'code':row[2]}]
            return types
        
    
    def getDonors(self):
        if self.con:
            donors = []
            cur = self.con.cursor()
            cur.execute('''SELECT id, 
                                  title,
                                  first_name,
                                  last_name,
                                  suffix,
                                  address,
                                  city,
                                  state,
                                  zip,
                                  employer, 
                                  occupation, 
                                  type,
                                  exclude_from_reporting 
                                  FROM donors''')
            for row in cur.fetchall():
                donors += [{'id':row[0],
                            'title':row[1],
                            'first_name':row[2],
                            'last_name':row[3],
                            'suffix':row[4],
                            'full_name':(row[1]+' '+row[2]+' '+row[3]+' '+row[4]).strip(),
                            'address':row[5],
                            'city':row[6],
                            'state':row[7],
                            'zip':row[8],
                            'full_address':row[5]+','+row[6]+','+row[7]+' '+row[8],
                            'employer':row[9],
                            'occupation':row[10],
                            'type':row[11],
                            'exclude_from_reporting':row[12]}]
            return donors
        
    def getPayees(self):
        if self.con:
            payees = []
            cur = self.con.cursor()
            cur.execute('''SELECT id, 
                                  title,
                                  first_name,
                                  last_name,
                                  suffix,
                                  address,
                                  city,
                                  state,
                                  zip,
                                  type FROM payees''')
            for row in cur.fetchall():
                payees += [{'id':row[0],'title':row[1],'first_name':row[2],'last_name':row[3],'suffix':row[4],'full_name':(row[1]+' '+row[2]+' '+row[3]+' '+row[4]).strip(),'address':row[5],'city':row[6],'state':row[7],'zip':row[8],'full_address':row[5]+','+row[6]+','+row[7]+' '+row[8],'type':row[9]}]
            return payees
        
    
    def getDonations(self,start_date=None,end_date=None):
        if self.con:
            donations = []
            cur = self.con.cursor()
            query = '''SELECT   don.id,
                                don.date,
                                don.amount,
                                don.description,
                                don_typ.name,
                                donors.first_name || " " || donors.last_name AS donor_name,  
                                donors.id,
                                don.type_id 
                            FROM donations don 
                            INNER JOIN donation_types don_typ ON don_typ.id = don.type_id 
                            INNER JOIN donors ON donors.id = don.donor_id'''
            if start_date and end_date:
                query += ' WHERE don.date BETWEEN ? AND ? ORDER BY don.date'
                cur.execute(query,(start_date,end_date))
            else:
                query += ' ORDER BY don.date'
                cur.execute(query)
            
            for row in cur.fetchall():
                donations += [{'id':row[0],'date':row[1],'amount':row[2],'description':row[3],'type':row[4],'donor_name':row[5],'donor_id':row[6],'type_id':row[7]}]
            
            return donations
        
    def getUnitemizedDonations(self,start_date=None,end_date=None):
        if self.con:
            donations = []
            cur = self.con.cursor()
            query = '''SELECT   don.id,
                                don.date,
                                don.amount,
                                don.description
                            FROM unitemized_donations don '''
            if start_date and end_date:
                query += ' WHERE don.date BETWEEN ? AND ? ORDER BY don.date'
                cur.execute(query,(start_date,end_date))
            else:
                query += ' ORDER BY don.date'
                cur.execute(query)
            
            for row in cur.fetchall():
                donations += [{'id':row[0],'date':row[1],'amount':row[2],'description':row[3]}]
            
            return donations
        
    def getExpenses(self,start_date=None,end_date=None):
        if self.con:
            expenses = []
            cur = self.con.cursor()
            query = '''SELECT   exp.id,
                                exp.date,
                                exp.amount,
                                exp.description,
                                exp.type,
                                payees.first_name || " " || payees.last_name AS payee_name,  
                                payees.id 
                            FROM expenses exp 
                            INNER JOIN payees ON payees.id = exp.payee_id'''
            if start_date and end_date:
                query += ' WHERE exp.date BETWEEN ? AND ? ORDER BY exp.date'
                cur.execute(query,(start_date,end_date))
            else:
                query += ' ORDER BY exp.date '
                cur.execute(query)
            
            for row in cur.fetchall():
                expenses += [{'id':row[0],'date':row[1],'amount':row[2],'description':row[3],'type':row[4],'payee_name':row[5],'payee_id':row[6]}]
            
            return expenses
    
    def getTotalExpenses(self):
        if self.con:
            cur = self.con.cursor()
            query = 'SELECT COALESCE(SUM(amount),0) FROM expenses'
            cur.execute(query)
            return cur.fetchone()[0]
        else:
            return 0
            
    def getTotalDonations(self):
        if self.con:
            cur = self.con.cursor()
            query = 'SELECT COALESCE(SUM(donations.amount),0) FROM donations LEFT JOIN donation_types don_typ ON donations.type_id=don_typ.id WHERE don_typ.code="A1"'
            cur.execute(query)
            donation_total = cur.fetchone()[0]
            query = 'SELECT COALESCE(SUM(amount),0) FROM unitemized_donations'
            cur.execute(query)
            unitemized_total = cur.fetchone()[0]
            return donation_total+unitemized_total
        else:
            return 0
        
    def getTotalInKind(self):
        if self.con:
            cur = self.con.cursor()
            query = 'SELECT COALESCE(SUM(donations.amount),0) FROM donations LEFT JOIN donation_types don_typ ON donations.type_id=don_typ.id WHERE don_typ.code="A2"'
            cur.execute(query)
            return cur.fetchone()[0]
        else:
            return 0
                
    def updateChoices(self):
        self.cmbDonor.SetItems([d['full_name'] for d in self.donor_list])
        self.cmbDonationType.SetItems([d['name'] for d in self.donation_type_list])
        self.cmbPayee.SetItems([p['full_name'] for p in self.payee_list])
    
    def updateTableData(self):
        if self.con:
            #Unitemized Donations
            if self.grdUnitemizedDonations.GetNumberRows() > 0:
                self.grdUnitemizedDonations.DeleteRows(0,self.grdDonations.GetNumberRows())
            self.grdUnitemizedDonations.AppendRows(len(self.unitemized_donation_list))
            row = 0
            for donation in self.unitemized_donation_list:
                self.grdUnitemizedDonations.SetCellValue(row,0,donation['date'])
                self.grdUnitemizedDonations.SetCellValue(row,1,'%1.2f'%donation['amount'])
                self.grdUnitemizedDonations.SetCellValue(row,2,donation['description'])
                row+=1
            self.grdUnitemizedDonations.AutoSizeColumns()
            
            #Donations
            if self.grdDonations.GetNumberRows() > 0:
                self.grdDonations.DeleteRows(0,self.grdDonations.GetNumberRows())
            self.grdDonations.AppendRows(len(self.donation_list))
            row = 0
            for donation in self.donation_list:
                self.grdDonations.SetCellValue(row,0,donation['date'])
                self.grdDonations.SetCellValue(row,1,donation['donor_name'])
                self.grdDonations.SetCellValue(row,2,donation['type'])
                self.grdDonations.SetCellValue(row,3,'%1.2f'%donation['amount'])
                self.grdDonations.SetCellValue(row,4,donation['description'])
                row+=1
            self.grdDonations.AutoSizeColumns()
            
            #Donors
            if self.grdDonors.GetNumberRows() > 0:
                self.grdDonors.DeleteRows(0,self.grdDonors.GetNumberRows())
            self.grdDonors.AppendRows(len(self.donor_list))
            row = 0
            for donor in self.donor_list:
                if donor['type'] == 'I':
                    type_str = 'Individual'
                elif donor['type'] == 'E':
                    type_str = 'Entity'
                else:
                    type_str = 'OTHER'
                self.grdDonors.SetCellValue(row,0,type_str)
                self.grdDonors.SetCellValue(row,1,donor['full_name'])
                self.grdDonors.SetCellValue(row,2,donor['full_address'])
                self.grdDonors.SetCellValue(row,3,donor['employer'])
                self.grdDonors.SetCellValue(row,4,donor['occupation'])
                row+=1
            self.grdDonors.AutoSizeColumns()
            
            #Expenses
            if self.grdExpenses.GetNumberRows() > 0:
                self.grdExpenses.DeleteRows(0,self.grdExpenses.GetNumberRows())
            self.grdExpenses.AppendRows(len(self.expense_list))
            row = 0
            for expense in self.expense_list:
                self.grdExpenses.SetCellValue(row,0,expense['date'])
                self.grdExpenses.SetCellValue(row,1,expense['payee_name'])
                self.grdExpenses.SetCellValue(row,2,expense['type'])
                self.grdExpenses.SetCellValue(row,3,'%1.2f'%expense['amount'])
                self.grdExpenses.SetCellValue(row,4,expense['description'])
                row+=1
            self.grdExpenses.AutoSizeColumns()
            
            #Payees
            if self.grdPayees.GetNumberRows() > 0:
                self.grdPayees.DeleteRows(0,self.grdPayees.GetNumberRows())
            self.grdPayees.AppendRows(len(self.payee_list))
            row = 0
            for payee in self.payee_list:
                if payee['type'] == 'I':
                    type_str = 'Individual'
                elif payee['type'] == 'E':
                    type_str = 'Entity'
                else:
                    payee = 'OTHER'
                self.grdPayees.SetCellValue(row,0,type_str)
                self.grdPayees.SetCellValue(row,1,payee['full_name'])
                self.grdPayees.SetCellValue(row,2,payee['full_address'])
                row+=1
            self.grdPayees.AutoSizeColumns()
            
            #Summary
            self.lblInKind.Label = '%1.2f' % self.total_in_kind
            self.lblDonationTotal.Label = '%1.2f' % self.total_donations
            self.lblExpenseTotal.Label = '%1.2f' % self.total_expenses
            self.lblBalance.Label = '%1.2f' % self.balance
            
            
    
    def setupGUI(self):
        pass
        
    def createDB(self,filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
                
        cur.execute('''CREATE TABLE IF NOT EXISTS donations
        (id INTEGER PRIMARY KEY,
        date DATE NOT NULL,
        amount REAL NOT NULL,
        description TEXT,
        type_id INTEGER NOT NULL,
        donor_id INTEGER NOT NULL,
        FOREIGN KEY(type_id) REFERENCES donation_types(id),
        FOREIGN KEY(donor_id) REFERENCES donors(id))''')
        
        cur.execute('''CREATE TABLE IF NOT EXISTS unitemized_donations
        (id INTEGER PRIMARY KEY,
        date DATE NOT NULL,
        amount REAL NOT NULL,
        description TEXT''')
        
        cur.execute('''CREATE TABLE IF NOT EXISTS donation_types
        (id INTEGER PRIMARY KEY,
        code TEXT UNIQUE,
        name TEXT)''')
        
        cur.execute('''CREATE TABLE IF NOT EXISTS donors
        (id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        title TEXT,
        suffix TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        zip TEXT,
        employer TEXT,
        occupation TEXT,
        type TEXT,
        exclude_from_reporting INTEGER)''')
        
        cur.execute('''CREATE TABLE IF NOT EXISTS expenses
        (id INTEGER PRIMARY KEY,
        date DATE,
        amount REAL,
        description TEXT,
        type TEXT NOT NULL,
        payee_id INTEGER NOT NULL,
        FOREIGN KEY (payee_id) REFERENCES payees(id))''')
        
        
        cur.execute('''CREATE TABLE IF NOT EXISTS payees
        (id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        title TEXT,
        suffix TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        zip TEXT,
        type TEXT)''')
        
        cur.execute('''PRAGMA foreign_keys = ON;''')
        
        cur.execute('''INSERT OR IGNORE INTO donation_types (code,name) VALUES (?,?)''',('A1','Cash'))
        cur.execute('''INSERT OR IGNORE INTO donation_types (code,name) VALUES (?,?)''',('A2','In-Kind'))
        
        con.commit()
        return con
        
        
    def openDB(self,filename):
        con = sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute('''PRAGMA foreign_keys = ON;''')
        con.commit()
        return con
        

class CampaignFinanceApp(wx.App):
    def OnInit(self):
        self.frame = CampaignFinanceForm()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = CampaignFinanceApp()
    app.MainLoop()
