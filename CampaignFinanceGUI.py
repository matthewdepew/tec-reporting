# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class frmCampaignFinanceMain
###########################################################################

class frmCampaignFinanceMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 651,704 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bMain = wx.BoxSizer( wx.VERTICAL )
		
		self.ntbMain = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pnlSummary = wx.Panel( self.ntbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnlSummary.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText351 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"Total Donations:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )
		gbSizer5.Add( self.m_staticText351, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblDonationTotal = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDonationTotal.Wrap( -1 )
		gbSizer5.Add( self.lblDonationTotal, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText371 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"Total Expenses:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		gbSizer5.Add( self.m_staticText371, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblExpenseTotal = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblExpenseTotal.Wrap( -1 )
		gbSizer5.Add( self.lblExpenseTotal, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"Balance:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		gbSizer5.Add( self.m_staticText42, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblBalance = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblBalance.Wrap( -1 )
		gbSizer5.Add( self.lblBalance, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.label1 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"In Kind:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		gbSizer5.Add( self.label1, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblInKind = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInKind.Wrap( -1 )
		gbSizer5.Add( self.lblInKind, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"Reports:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		gbSizer5.Add( self.m_staticText39, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		gbSizer5.Add( self.m_staticText40, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.dpkReportFrom = wx.adv.DatePickerCtrl( self.pnlSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer5.Add( self.dpkReportFrom, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.pnlSummary, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		gbSizer5.Add( self.m_staticText41, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.dpkReportTo = wx.adv.DatePickerCtrl( self.pnlSummary, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer5.Add( self.dpkReportTo, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnExpenseReport = wx.Button( self.pnlSummary, wx.ID_ANY, u"Expense Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnExpenseReport, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnDonationReport = wx.Button( self.pnlSummary, wx.ID_ANY, u"Donation Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnDonationReport, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.pnlSummary.SetSizer( gbSizer5 )
		self.pnlSummary.Layout()
		gbSizer5.Fit( self.pnlSummary )
		self.ntbMain.AddPage( self.pnlSummary, u"Summary", False )
		self.pnlUnitemizedDonations = wx.Panel( self.ntbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnlUnitemizedDonationFilter = wx.Panel( self.pnlUnitemizedDonations, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText58 = wx.StaticText( self.pnlUnitemizedDonationFilter, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		bSizer13.Add( self.m_staticText58, 0, wx.ALL, 5 )
		
		self.dpkFilterUnitemizedDonationFrom = wx.adv.DatePickerCtrl( self.pnlUnitemizedDonationFilter, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer13.Add( self.dpkFilterUnitemizedDonationFrom, 0, wx.ALL, 5 )
		
		self.m_staticText59 = wx.StaticText( self.pnlUnitemizedDonationFilter, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		bSizer13.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		self.dpkFilterUnitemizedDonationTo = wx.adv.DatePickerCtrl( self.pnlUnitemizedDonationFilter, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer13.Add( self.dpkFilterUnitemizedDonationTo, 0, wx.ALL, 5 )
		
		self.btnFilterUnitemizedDonations = wx.ToggleButton( self.pnlUnitemizedDonationFilter, wx.ID_ANY, u"Filter Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.btnFilterUnitemizedDonations, 0, wx.ALL, 5 )
		
		
		self.pnlUnitemizedDonationFilter.SetSizer( bSizer13 )
		self.pnlUnitemizedDonationFilter.Layout()
		bSizer13.Fit( self.pnlUnitemizedDonationFilter )
		bSizer12.Add( self.pnlUnitemizedDonationFilter, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.grdUnitemizedDonations = wx.grid.Grid( self.pnlUnitemizedDonations, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdUnitemizedDonations.CreateGrid( 5, 3 )
		self.grdUnitemizedDonations.EnableEditing( False )
		self.grdUnitemizedDonations.EnableGridLines( True )
		self.grdUnitemizedDonations.EnableDragGridSize( False )
		self.grdUnitemizedDonations.SetMargins( 0, 0 )
		
		# Columns
		self.grdUnitemizedDonations.EnableDragColMove( False )
		self.grdUnitemizedDonations.EnableDragColSize( True )
		self.grdUnitemizedDonations.SetColLabelSize( 30 )
		self.grdUnitemizedDonations.SetColLabelValue( 0, u"Date" )
		self.grdUnitemizedDonations.SetColLabelValue( 1, u"Amount" )
		self.grdUnitemizedDonations.SetColLabelValue( 2, u"Description" )
		self.grdUnitemizedDonations.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdUnitemizedDonations.EnableDragRowSize( True )
		self.grdUnitemizedDonations.SetRowLabelSize( 0 )
		self.grdUnitemizedDonations.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdUnitemizedDonations.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer12.Add( self.grdUnitemizedDonations, 1, wx.ALL, 5 )
		
		self.m_panel19 = wx.Panel( self.pnlUnitemizedDonations, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText60 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		gbSizer8.Add( self.m_staticText60, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.dpkUnitemizedDonationDate = wx.adv.DatePickerCtrl( self.m_panel19, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer8.Add( self.dpkUnitemizedDonationDate, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Amount:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gbSizer8.Add( self.m_staticText61, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtUnitemizedDonationAmount = wx.TextCtrl( self.m_panel19, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.txtUnitemizedDonationAmount, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		gbSizer8.Add( self.m_staticText62, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtUnitemizedDonationDescription = wx.TextCtrl( self.m_panel19, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.txtUnitemizedDonationDescription, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.btnAddUnitemizedDonation = wx.Button( self.m_panel19, wx.ID_ANY, u"Add Donation", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.btnAddUnitemizedDonation, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnUpdateUnitemizedDonation = wx.Button( self.m_panel19, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnUpdateUnitemizedDonation.Hide()
		
		gbSizer8.Add( self.btnUpdateUnitemizedDonation, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnCancelUnitemizedDonation = wx.Button( self.m_panel19, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCancelUnitemizedDonation.Hide()
		
		gbSizer8.Add( self.btnCancelUnitemizedDonation, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel19.SetSizer( gbSizer8 )
		self.m_panel19.Layout()
		gbSizer8.Fit( self.m_panel19 )
		bSizer12.Add( self.m_panel19, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pnlUnitemizedDonations.SetSizer( bSizer12 )
		self.pnlUnitemizedDonations.Layout()
		bSizer12.Fit( self.pnlUnitemizedDonations )
		self.ntbMain.AddPage( self.pnlUnitemizedDonations, u"Unitemized Donations", False )
		self.pnlDonations = wx.Panel( self.ntbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnlDonations.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bDonations = wx.BoxSizer( wx.VERTICAL )
		
		self.pnlDonationFilter = wx.Panel( self.pnlDonations, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.pnlDonationFilter, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.dpkDonationFrom = wx.adv.DatePickerCtrl( self.pnlDonationFilter, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer3.Add( self.dpkDonationFrom, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.pnlDonationFilter, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.dpkDonationTo = wx.adv.DatePickerCtrl( self.pnlDonationFilter, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer3.Add( self.dpkDonationTo, 0, wx.ALL, 5 )
		
		self.btnFilterDonations = wx.ToggleButton( self.pnlDonationFilter, wx.ID_ANY, u"Filter Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnFilterDonations, 0, wx.ALL, 5 )
		
		
		self.pnlDonationFilter.SetSizer( bSizer3 )
		self.pnlDonationFilter.Layout()
		bSizer3.Fit( self.pnlDonationFilter )
		bDonations.Add( self.pnlDonationFilter, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.grdDonations = wx.grid.Grid( self.pnlDonations, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDonations.CreateGrid( 5, 5 )
		self.grdDonations.EnableEditing( False )
		self.grdDonations.EnableGridLines( True )
		self.grdDonations.EnableDragGridSize( False )
		self.grdDonations.SetMargins( 0, 0 )
		
		# Columns
		self.grdDonations.AutoSizeColumns()
		self.grdDonations.EnableDragColMove( False )
		self.grdDonations.EnableDragColSize( True )
		self.grdDonations.SetColLabelSize( 30 )
		self.grdDonations.SetColLabelValue( 0, u"Date" )
		self.grdDonations.SetColLabelValue( 1, u"Donor" )
		self.grdDonations.SetColLabelValue( 2, u"Type" )
		self.grdDonations.SetColLabelValue( 3, u"Amount" )
		self.grdDonations.SetColLabelValue( 4, u"Description" )
		self.grdDonations.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdDonations.EnableDragRowSize( True )
		self.grdDonations.SetRowLabelSize( 0 )
		self.grdDonations.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdDonations.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bDonations.Add( self.grdDonations, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.pnlDonation = wx.Panel( self.pnlDonations, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbsDonation = wx.GridBagSizer( 0, 0 )
		gbsDonation.SetFlexibleDirection( wx.BOTH )
		gbsDonation.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self.pnlDonation, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbsDonation.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.dpkDonationDate = wx.adv.DatePickerCtrl( self.pnlDonation, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbsDonation.Add( self.dpkDonationDate, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.pnlDonation, wx.ID_ANY, u"Donor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gbsDonation.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbDonorChoices = []
		self.cmbDonor = wx.Choice( self.pnlDonation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbDonorChoices, 0 )
		self.cmbDonor.SetSelection( 0 )
		gbsDonation.Add( self.cmbDonor, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.pnlDonation, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gbsDonation.Add( self.m_staticText5, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbDonationTypeChoices = []
		self.cmbDonationType = wx.Choice( self.pnlDonation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbDonationTypeChoices, 0 )
		self.cmbDonationType.SetSelection( 0 )
		gbsDonation.Add( self.cmbDonationType, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.pnlDonation, wx.ID_ANY, u"Amount:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gbsDonation.Add( self.m_staticText6, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonationAmount = wx.TextCtrl( self.pnlDonation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbsDonation.Add( self.txtDonationAmount, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self.pnlDonation, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gbsDonation.Add( self.m_staticText7, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonationDescription = wx.TextCtrl( self.pnlDonation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbsDonation.Add( self.txtDonationDescription, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.pnlDonationButtons = wx.Panel( self.pnlDonation, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bDonationButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAddDonation = wx.Button( self.pnlDonationButtons, wx.ID_ANY, u"Add Donation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bDonationButtons.Add( self.btnAddDonation, 0, wx.ALL, 5 )
		
		self.btnUpdateDonation = wx.Button( self.pnlDonationButtons, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bDonationButtons.Add( self.btnUpdateDonation, 0, wx.ALL, 5 )
		
		self.btnCancelDonation = wx.Button( self.pnlDonationButtons, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bDonationButtons.Add( self.btnCancelDonation, 0, wx.ALL, 5 )
		
		
		self.pnlDonationButtons.SetSizer( bDonationButtons )
		self.pnlDonationButtons.Layout()
		bDonationButtons.Fit( self.pnlDonationButtons )
		gbsDonation.Add( self.pnlDonationButtons, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.pnlDonation.SetSizer( gbsDonation )
		self.pnlDonation.Layout()
		gbsDonation.Fit( self.pnlDonation )
		bDonations.Add( self.pnlDonation, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pnlDonations.SetSizer( bDonations )
		self.pnlDonations.Layout()
		bDonations.Fit( self.pnlDonations )
		self.ntbMain.AddPage( self.pnlDonations, u"Donations", False )
		self.pnlDonors = wx.Panel( self.ntbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnlDonors.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.grdDonors = wx.grid.Grid( self.pnlDonors, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDonors.CreateGrid( 5, 5 )
		self.grdDonors.EnableEditing( False )
		self.grdDonors.EnableGridLines( True )
		self.grdDonors.EnableDragGridSize( False )
		self.grdDonors.SetMargins( 0, 0 )
		
		# Columns
		self.grdDonors.AutoSizeColumns()
		self.grdDonors.EnableDragColMove( False )
		self.grdDonors.EnableDragColSize( True )
		self.grdDonors.SetColLabelSize( 30 )
		self.grdDonors.SetColLabelValue( 0, u"Type" )
		self.grdDonors.SetColLabelValue( 1, u"Name" )
		self.grdDonors.SetColLabelValue( 2, u"Address" )
		self.grdDonors.SetColLabelValue( 3, u"Employer" )
		self.grdDonors.SetColLabelValue( 4, u"Occupation" )
		self.grdDonors.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdDonors.EnableDragRowSize( True )
		self.grdDonors.SetRowLabelSize( 0 )
		self.grdDonors.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdDonors.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.grdDonors, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel9 = wx.Panel( self.pnlDonors, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gbSizer2.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbDonorTypeChoices = [ u"Individual", u"Entity" ]
		self.cmbDonorType = wx.Choice( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbDonorTypeChoices, 0 )
		self.cmbDonorType.SetSelection( 0 )
		gbSizer2.Add( self.cmbDonorType, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblLastName = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Last Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLastName.Wrap( -1 )
		gbSizer2.Add( self.lblLastName, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"First Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gbSizer2.Add( self.m_staticText13, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gbSizer2.Add( self.m_staticText14, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Suffix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gbSizer2.Add( self.m_staticText15, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorLastName = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorLastName, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorFirstName = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorFirstName, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorTitle = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorTitle, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorSuffix = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorSuffix, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gbSizer2.Add( self.m_staticText17, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorAddress = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorAddress, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gbSizer2.Add( self.m_staticText18, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"State:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gbSizer2.Add( self.m_staticText19, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Zip Code:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gbSizer2.Add( self.m_staticText20, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorCity = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorCity, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbDonorStateChoices = []
		self.cmbDonorState = wx.Choice( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbDonorStateChoices, 0 )
		self.cmbDonorState.SetSelection( 0 )
		gbSizer2.Add( self.cmbDonorState, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorZipCode = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorZipCode, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Employer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gbSizer2.Add( self.m_staticText21, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Occupation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gbSizer2.Add( self.m_staticText22, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorEmployer = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorEmployer, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtDonorOccupation = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtDonorOccupation, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.chkExcludeFromReporting = wx.CheckBox( self.m_panel9, wx.ID_ANY, u"Exclude From Reporting", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.chkExcludeFromReporting, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel10 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAddDonor = wx.Button( self.m_panel10, wx.ID_ANY, u"Add Donor", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnAddDonor, 0, wx.ALL, 5 )
		
		self.btnUpdateDonor = wx.Button( self.m_panel10, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnUpdateDonor, 0, wx.ALL, 5 )
		
		self.btnCancelDonor = wx.Button( self.m_panel10, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnCancelDonor, 0, wx.ALL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer6 )
		self.m_panel10.Layout()
		bSizer6.Fit( self.m_panel10 )
		gbSizer2.Add( self.m_panel10, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel9.SetSizer( gbSizer2 )
		self.m_panel9.Layout()
		gbSizer2.Fit( self.m_panel9 )
		bSizer5.Add( self.m_panel9, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pnlDonors.SetSizer( bSizer5 )
		self.pnlDonors.Layout()
		bSizer5.Fit( self.pnlDonors )
		self.ntbMain.AddPage( self.pnlDonors, u"Donors", True )
		self.pnlExpenses = wx.Panel( self.ntbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnlExpenses.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel11 = wx.Panel( self.pnlExpenses, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText23 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer8.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.dpkExpenseFrom = wx.adv.DatePickerCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer8.Add( self.dpkExpenseFrom, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer8.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.dpkExpenseTo = wx.adv.DatePickerCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer8.Add( self.dpkExpenseTo, 0, wx.ALL, 5 )
		
		self.btnFilterExpenses = wx.ToggleButton( self.m_panel11, wx.ID_ANY, u"Filter Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnFilterExpenses, 0, wx.ALL, 5 )
		
		
		self.m_panel11.SetSizer( bSizer8 )
		self.m_panel11.Layout()
		bSizer8.Fit( self.m_panel11 )
		bSizer7.Add( self.m_panel11, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.grdExpenses = wx.grid.Grid( self.pnlExpenses, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdExpenses.CreateGrid( 5, 5 )
		self.grdExpenses.EnableEditing( False )
		self.grdExpenses.EnableGridLines( True )
		self.grdExpenses.EnableDragGridSize( False )
		self.grdExpenses.SetMargins( 0, 0 )
		
		# Columns
		self.grdExpenses.AutoSizeColumns()
		self.grdExpenses.EnableDragColMove( False )
		self.grdExpenses.EnableDragColSize( True )
		self.grdExpenses.SetColLabelSize( 30 )
		self.grdExpenses.SetColLabelValue( 0, u"Date" )
		self.grdExpenses.SetColLabelValue( 1, u"Payee" )
		self.grdExpenses.SetColLabelValue( 2, u"Type" )
		self.grdExpenses.SetColLabelValue( 3, u"Amount" )
		self.grdExpenses.SetColLabelValue( 4, u"Description" )
		self.grdExpenses.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdExpenses.EnableDragRowSize( True )
		self.grdExpenses.SetRowLabelSize( 0 )
		self.grdExpenses.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdExpenses.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.grdExpenses, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel12 = wx.Panel( self.pnlExpenses, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText25 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gbSizer3.Add( self.m_staticText25, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.dpkExpenseDate = wx.adv.DatePickerCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer3.Add( self.dpkExpenseDate, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Amount:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gbSizer3.Add( self.m_staticText26, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtExpenseAmount = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.txtExpenseAmount, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Payee:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gbSizer3.Add( self.m_staticText27, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbPayeeChoices = []
		self.cmbPayee = wx.Choice( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbPayeeChoices, 0 )
		self.cmbPayee.SetSelection( 0 )
		gbSizer3.Add( self.cmbPayee, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gbSizer3.Add( self.m_staticText28, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbExpenseTypeChoices = []
		self.cmbExpenseType = wx.Choice( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbExpenseTypeChoices, 0 )
		self.cmbExpenseType.SetSelection( 0 )
		gbSizer3.Add( self.cmbExpenseType, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		gbSizer3.Add( self.m_staticText29, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtExpenseDescription = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.txtExpenseDescription, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAddExpense = wx.Button( self.m_panel13, wx.ID_ANY, u"Add Expense", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btnAddExpense, 0, wx.ALL, 5 )
		
		self.btnUpdateExpense = wx.Button( self.m_panel13, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btnUpdateExpense, 0, wx.ALL, 5 )
		
		self.btnCancelExpense = wx.Button( self.m_panel13, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btnCancelExpense, 0, wx.ALL, 5 )
		
		
		self.m_panel13.SetSizer( bSizer9 )
		self.m_panel13.Layout()
		bSizer9.Fit( self.m_panel13 )
		gbSizer3.Add( self.m_panel13, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( gbSizer3 )
		self.m_panel12.Layout()
		gbSizer3.Fit( self.m_panel12 )
		bSizer7.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pnlExpenses.SetSizer( bSizer7 )
		self.pnlExpenses.Layout()
		bSizer7.Fit( self.pnlExpenses )
		self.ntbMain.AddPage( self.pnlExpenses, u"Expenses", False )
		self.pnlPayees = wx.Panel( self.ntbMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnlPayees.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.grdPayees = wx.grid.Grid( self.pnlPayees, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdPayees.CreateGrid( 5, 3 )
		self.grdPayees.EnableEditing( False )
		self.grdPayees.EnableGridLines( True )
		self.grdPayees.EnableDragGridSize( False )
		self.grdPayees.SetMargins( 0, 0 )
		
		# Columns
		self.grdPayees.AutoSizeColumns()
		self.grdPayees.EnableDragColMove( False )
		self.grdPayees.EnableDragColSize( True )
		self.grdPayees.SetColLabelSize( 30 )
		self.grdPayees.SetColLabelValue( 0, u"Type" )
		self.grdPayees.SetColLabelValue( 1, u"Name" )
		self.grdPayees.SetColLabelValue( 2, u"Address" )
		self.grdPayees.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdPayees.EnableDragRowSize( True )
		self.grdPayees.SetRowLabelSize( 0 )
		self.grdPayees.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdPayees.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer10.Add( self.grdPayees, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel14 = wx.Panel( self.pnlPayees, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText38 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		gbSizer4.Add( self.m_staticText38, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbPayeeTypeChoices = [ u"Individual", u"Entity" ]
		self.cmbPayeeType = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbPayeeTypeChoices, 0 )
		self.cmbPayeeType.SetSelection( 0 )
		gbSizer4.Add( self.cmbPayeeType, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblPayeeLastName = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Last Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPayeeLastName.Wrap( -1 )
		gbSizer4.Add( self.lblPayeeLastName, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"First Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gbSizer4.Add( self.m_staticText31, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gbSizer4.Add( self.m_staticText32, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Suffix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gbSizer4.Add( self.m_staticText33, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeLastName = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeLastName, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeFirstName = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeFirstName, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeTitle = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeTitle, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeSuffix = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeSuffix, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gbSizer4.Add( self.m_staticText34, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeAddress = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeAddress, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gbSizer4.Add( self.m_staticText35, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"State:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gbSizer4.Add( self.m_staticText36, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Zip:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		gbSizer4.Add( self.m_staticText37, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeCity = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeCity, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		cmbPayeeStateChoices = []
		self.cmbPayeeState = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmbPayeeStateChoices, 0 )
		self.cmbPayeeState.SetSelection( 0 )
		gbSizer4.Add( self.cmbPayeeState, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPayeeZipCode = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.txtPayeeZipCode, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel15 = wx.Panel( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAddPayee = wx.Button( self.m_panel15, wx.ID_ANY, u"Add Payee", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnAddPayee, 0, wx.ALL, 5 )
		
		self.btnUpdatePayee = wx.Button( self.m_panel15, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnUpdatePayee, 0, wx.ALL, 5 )
		
		self.btnCancelPayee = wx.Button( self.m_panel15, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnCancelPayee, 0, wx.ALL, 5 )
		
		
		self.m_panel15.SetSizer( bSizer11 )
		self.m_panel15.Layout()
		bSizer11.Fit( self.m_panel15 )
		gbSizer4.Add( self.m_panel15, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel14.SetSizer( gbSizer4 )
		self.m_panel14.Layout()
		gbSizer4.Fit( self.m_panel14 )
		bSizer10.Add( self.m_panel14, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pnlPayees.SetSizer( bSizer10 )
		self.pnlPayees.Layout()
		bSizer10.Fit( self.pnlPayees )
		self.ntbMain.AddPage( self.pnlPayees, u"Payees", False )
		
		bMain.Add( self.ntbMain, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bMain )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.mFile = wx.Menu()
		self.mNew = wx.MenuItem( self.mFile, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFile.Append( self.mNew )
		
		self.mOpen = wx.MenuItem( self.mFile, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFile.Append( self.mOpen )
		
		self.m_menubar1.Append( self.mFile, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnExpenseReport.Bind( wx.EVT_BUTTON, self.btnExpenseReport_click )
		self.btnDonationReport.Bind( wx.EVT_BUTTON, self.btnDonationReport_click )
		self.grdUnitemizedDonations.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grdUnitemizedDonationsCell_click )
		self.btnAddUnitemizedDonation.Bind( wx.EVT_BUTTON, self.btnAddUnitemizedDonation_click )
		self.btnUpdateUnitemizedDonation.Bind( wx.EVT_BUTTON, self.btnUpdateUnitemizedDonation_click )
		self.btnCancelUnitemizedDonation.Bind( wx.EVT_BUTTON, self.btnCancelUnitemizedDonation_click )
		self.btnFilterDonations.Bind( wx.EVT_TOGGLEBUTTON, self.btnFilterDonations_click )
		self.grdDonations.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grdDonationsCell_click )
		self.grdDonations.Bind( wx.EVT_KEY_DOWN, self.grdDonations_key )
		self.btnAddDonation.Bind( wx.EVT_BUTTON, self.btnAddDonation_click )
		self.btnUpdateDonation.Bind( wx.EVT_BUTTON, self.btnUpdateDonation_click )
		self.btnCancelDonation.Bind( wx.EVT_BUTTON, self.btnCancelDonation_click )
		self.grdDonors.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grdDonorsCell_click )
		self.grdDonors.Bind( wx.EVT_KEY_DOWN, self.grdDonors_key )
		self.btnAddDonor.Bind( wx.EVT_BUTTON, self.btnAddDonor_click )
		self.btnUpdateDonor.Bind( wx.EVT_BUTTON, self.btnUpdateDonor_click )
		self.btnCancelDonor.Bind( wx.EVT_BUTTON, self.btnCancelDonor_click )
		self.btnFilterExpenses.Bind( wx.EVT_TOGGLEBUTTON, self.btnFIlterExpenses_click )
		self.grdExpenses.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grdExpensesCell_click )
		self.grdExpenses.Bind( wx.EVT_KEY_DOWN, self.grdExpenses_key )
		self.btnAddExpense.Bind( wx.EVT_BUTTON, self.btnAddExpense_click )
		self.btnUpdateExpense.Bind( wx.EVT_BUTTON, self.btnUpdateExpense_click )
		self.btnCancelExpense.Bind( wx.EVT_BUTTON, self.btnCancelExpense_click )
		self.grdPayees.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grdPayeesCell_click )
		self.grdPayees.Bind( wx.EVT_KEY_DOWN, self.grdPayees_key )
		self.btnAddPayee.Bind( wx.EVT_BUTTON, self.btnAddPayee_click )
		self.btnUpdatePayee.Bind( wx.EVT_BUTTON, self.btnUpdatePayee_click )
		self.btnCancelPayee.Bind( wx.EVT_BUTTON, self.btnCancelPayee_click )
		self.Bind( wx.EVT_MENU, self.mNew_click, id = self.mNew.GetId() )
		self.Bind( wx.EVT_MENU, self.mOpen_click, id = self.mOpen.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnExpenseReport_click( self, event ):
		event.Skip()
	
	def btnDonationReport_click( self, event ):
		event.Skip()
	
	def grdUnitemizedDonationsCell_click( self, event ):
		event.Skip()
	
	def btnAddUnitemizedDonation_click( self, event ):
		event.Skip()
	
	def btnUpdateUnitemizedDonation_click( self, event ):
		event.Skip()
	
	def btnCancelUnitemizedDonation_click( self, event ):
		event.Skip()
	
	def btnFilterDonations_click( self, event ):
		event.Skip()
	
	def grdDonationsCell_click( self, event ):
		event.Skip()
	
	def grdDonations_key( self, event ):
		event.Skip()
	
	def btnAddDonation_click( self, event ):
		event.Skip()
	
	def btnUpdateDonation_click( self, event ):
		event.Skip()
	
	def btnCancelDonation_click( self, event ):
		event.Skip()
	
	def grdDonorsCell_click( self, event ):
		event.Skip()
	
	def grdDonors_key( self, event ):
		event.Skip()
	
	def btnAddDonor_click( self, event ):
		event.Skip()
	
	def btnUpdateDonor_click( self, event ):
		event.Skip()
	
	def btnCancelDonor_click( self, event ):
		event.Skip()
	
	def btnFIlterExpenses_click( self, event ):
		event.Skip()
	
	def grdExpensesCell_click( self, event ):
		event.Skip()
	
	def grdExpenses_key( self, event ):
		event.Skip()
	
	def btnAddExpense_click( self, event ):
		event.Skip()
	
	def btnUpdateExpense_click( self, event ):
		event.Skip()
	
	def btnCancelExpense_click( self, event ):
		event.Skip()
	
	def grdPayeesCell_click( self, event ):
		event.Skip()
	
	def grdPayees_key( self, event ):
		event.Skip()
	
	def btnAddPayee_click( self, event ):
		event.Skip()
	
	def btnUpdatePayee_click( self, event ):
		event.Skip()
	
	def btnCancelPayee_click( self, event ):
		event.Skip()
	
	def mNew_click( self, event ):
		event.Skip()
	
	def mOpen_click( self, event ):
		event.Skip()
	

