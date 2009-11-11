qx.Class.define("test.draw.Add", {
    construct: function() {
        this.base(arguments);
        this.setWidget(this.create_Add());
         /* The instance named 'buttonBox' is of type 'QDialogButtonBox' which is not supported (yet?) */
        
         /* The instance named 'horizontalSlider' is of type 'QSlider' which is not supported (yet?) */
        
         /* The instance named 'verticalSlider' is of type 'QSlider' which is not supported (yet?) */
        
         /* The instance named 'verticalScrollBar' is of type 'QScrollBar' which is not supported (yet?) */
        
         /* The instance named 'horizontalScrollBar' is of type 'QScrollBar' which is not supported (yet?) */
        
        
    }
    
    ,destruct: function() {
        
    }
    
    ,extend: qx.core.Object
    ,include: [qx.locale.MTranslation]
    ,members:  {
        Add: null
        ,HLTest: null
        ,HLTest_2: null
        ,HLTest_2_implicit_container: null
        ,HLTest_implicit_container: null
        ,HLTrackingMethod: null
        ,HLTrackingMethod_2: null
        ,HLTrackingMethod_2_implicit_container: null
        ,HLTrackingMethod_implicit_container: null
        ,VLEmail: null
        ,VLEmail_2: null
        ,VLEmail_2_implicit_container: null
        ,VLEmail_implicit_container: null
        ,__lv: null
        ,centralwidget: null
        ,checkBox: null
        ,chkEmail: null
        ,chkEmail_2: null
        ,chkLRITTest: null
        ,chkLRITTest_2: null
        ,comboInterval: null
        ,comboInterval_2: null
        ,comboSubAddress: null
        ,comboSubAddress_2: null
        ,comboTrackingMethod: null
        ,comboTrackingMethod_2: null
        ,create_Add: function create_Add() {
            this.Add = new qx.ui.container.Composite();
            this.Add.setWidth(629);
            this.Add.setHeight(484);
            this.Add.setMarginBottom(1);
            this.Add.setMarginTop(1);
            this.Add.setMarginLeft(1);
            this.Add.setMarginRight(1);
            this.Add.setLayout(this.create___lv());
            this.Add.add(this.create_centralwidget(), {flex: 1});
            return this.Add;
            
        }
        
        ,create_HLTest: function create_HLTest() {
            this.HLTest = new qx.ui.layout.HBox();
            return this.HLTest;
            
        }
        
        ,create_HLTest_2: function create_HLTest_2() {
            this.HLTest_2 = new qx.ui.layout.HBox();
            return this.HLTest_2;
            
        }
        
        ,create_HLTest_2_implicit_container: function create_HLTest_2_implicit_container() {
            this.HLTest_2_implicit_container = new qx.ui.container.Composite();
            this.HLTest_2_implicit_container.setMarginBottom(1);
            this.HLTest_2_implicit_container.setMarginTop(1);
            this.HLTest_2_implicit_container.setMarginLeft(1);
            this.HLTest_2_implicit_container.setMarginRight(1);
            this.HLTest_2_implicit_container.setLayout(this.create_HLTest_2());
            this.HLTest_2_implicit_container.add(this.create_chkLRITTest_2(), {flex: 1});
            this.HLTest_2_implicit_container.add(this.create_radioButton_6(), {flex: 1});
            this.HLTest_2_implicit_container.add(this.create_radioButton_7(), {flex: 1});
            return this.HLTest_2_implicit_container;
            
        }
        
        ,create_HLTest_implicit_container: function create_HLTest_implicit_container() {
            this.HLTest_implicit_container = new qx.ui.container.Composite();
            this.HLTest_implicit_container.setMarginBottom(1);
            this.HLTest_implicit_container.setMarginTop(1);
            this.HLTest_implicit_container.setMarginLeft(1);
            this.HLTest_implicit_container.setMarginRight(1);
            this.HLTest_implicit_container.setLayout(this.create_HLTest());
            this.HLTest_implicit_container.add(this.create_chkLRITTest(), {flex: 1});
            this.HLTest_implicit_container.add(this.create_radioButton_2(), {flex: 1});
            this.HLTest_implicit_container.add(this.create_radioButton(), {flex: 1});
            return this.HLTest_implicit_container;
            
        }
        
        ,create_HLTrackingMethod: function create_HLTrackingMethod() {
            this.HLTrackingMethod = new qx.ui.layout.HBox();
            return this.HLTrackingMethod;
            
        }
        
        ,create_HLTrackingMethod_2: function create_HLTrackingMethod_2() {
            this.HLTrackingMethod_2 = new qx.ui.layout.HBox();
            return this.HLTrackingMethod_2;
            
        }
        
        ,create_HLTrackingMethod_2_implicit_container: function create_HLTrackingMethod_2_implicit_container() {
            this.HLTrackingMethod_2_implicit_container = new qx.ui.container.Composite();
            this.HLTrackingMethod_2_implicit_container.setMarginBottom(1);
            this.HLTrackingMethod_2_implicit_container.setMarginTop(1);
            this.HLTrackingMethod_2_implicit_container.setMarginLeft(1);
            this.HLTrackingMethod_2_implicit_container.setMarginRight(1);
            this.HLTrackingMethod_2_implicit_container.setLayout(this.create_HLTrackingMethod_2());
            this.HLTrackingMethod_2_implicit_container.add(this.create_comboTrackingMethod_2(), {flex: 1});
            this.HLTrackingMethod_2_implicit_container.add(this.create_horizontalSpacer(), {flex: 1});
            this.HLTrackingMethod_2_implicit_container.add(this.create_lblInterval_2(), {flex: 1});
            this.HLTrackingMethod_2_implicit_container.add(this.create_comboInterval_2(), {flex: 1});
            this.HLTrackingMethod_2_implicit_container.add(this.create_horizontalSpacer_2(), {flex: 1});
            return this.HLTrackingMethod_2_implicit_container;
            
        }
        
        ,create_HLTrackingMethod_implicit_container: function create_HLTrackingMethod_implicit_container() {
            this.HLTrackingMethod_implicit_container = new qx.ui.container.Composite();
            this.HLTrackingMethod_implicit_container.setMarginBottom(1);
            this.HLTrackingMethod_implicit_container.setMarginTop(1);
            this.HLTrackingMethod_implicit_container.setMarginLeft(1);
            this.HLTrackingMethod_implicit_container.setMarginRight(1);
            this.HLTrackingMethod_implicit_container.setLayout(this.create_HLTrackingMethod());
            this.HLTrackingMethod_implicit_container.add(this.create_comboTrackingMethod(), {flex: 1});
            this.HLTrackingMethod_implicit_container.add(this.create_horizontalSpacer(), {flex: 1});
            this.HLTrackingMethod_implicit_container.add(this.create_lblInterval(), {flex: 1});
            this.HLTrackingMethod_implicit_container.add(this.create_comboInterval(), {flex: 1});
            this.HLTrackingMethod_implicit_container.add(this.create_horizontalSpacer_2(), {flex: 1});
            return this.HLTrackingMethod_implicit_container;
            
        }
        
        ,create_VLEmail: function create_VLEmail() {
            this.VLEmail = new qx.ui.layout.VBox();
            return this.VLEmail;
            
        }
        
        ,create_VLEmail_2: function create_VLEmail_2() {
            this.VLEmail_2 = new qx.ui.layout.VBox();
            return this.VLEmail_2;
            
        }
        
        ,create_VLEmail_2_implicit_container: function create_VLEmail_2_implicit_container() {
            this.VLEmail_2_implicit_container = new qx.ui.container.Composite();
            this.VLEmail_2_implicit_container.setMarginBottom(1);
            this.VLEmail_2_implicit_container.setMarginTop(1);
            this.VLEmail_2_implicit_container.setMarginLeft(1);
            this.VLEmail_2_implicit_container.setMarginRight(1);
            this.VLEmail_2_implicit_container.setLayout(this.create_VLEmail_2());
            this.VLEmail_2_implicit_container.add(this.create_edtEmail_2(), {flex: 1});
            this.VLEmail_2_implicit_container.add(this.create_horizontalLayout_10_implicit_container(), {flex: 1});
            return this.VLEmail_2_implicit_container;
            
        }
        
        ,create_VLEmail_implicit_container: function create_VLEmail_implicit_container() {
            this.VLEmail_implicit_container = new qx.ui.container.Composite();
            this.VLEmail_implicit_container.setMarginBottom(1);
            this.VLEmail_implicit_container.setMarginTop(1);
            this.VLEmail_implicit_container.setMarginLeft(1);
            this.VLEmail_implicit_container.setMarginRight(1);
            this.VLEmail_implicit_container.setLayout(this.create_VLEmail());
            this.VLEmail_implicit_container.add(this.create_edtEmail(), {flex: 1});
            this.VLEmail_implicit_container.add(this.create_horizontalLayout_5_implicit_container(), {flex: 1});
            return this.VLEmail_implicit_container;
            
        }
        
        ,create___lv: function create___lv() {
            this.__lv = new qx.ui.layout.VBox();
            return this.__lv;
            
        }
        
        ,create_centralwidget: function create_centralwidget() {
            this.centralwidget = new qx.ui.container.Composite();
            this.centralwidget.setMarginBottom(1);
            this.centralwidget.setMarginTop(1);
            this.centralwidget.setMarginLeft(1);
            this.centralwidget.setMarginRight(1);
            this.centralwidget.setLayout(this.create_horizontalLayout_3());
            this.centralwidget.add(this.create_tabWidget(), {flex: 1});
            return this.centralwidget;
            
        }
        
        ,create_checkBox: function create_checkBox() {
            this.checkBox = new qx.ui.form.CheckBox();
            this.checkBox.setWidth(81);
            this.checkBox.setHeight(21);
            this.checkBox.setMarginBottom(1);
            this.checkBox.setMarginTop(1);
            this.checkBox.setMarginLeft(1);
            this.checkBox.setMarginRight(1);
            this.checkBox.setLabel(this.tr("CheckBox"));
            return this.checkBox;
            
        }
        
        ,create_chkEmail: function create_chkEmail() {
            this.chkEmail = new qx.ui.form.CheckBox();
            this.chkEmail.setMarginBottom(1);
            this.chkEmail.setMarginTop(1);
            this.chkEmail.setMarginLeft(1);
            this.chkEmail.setMarginRight(1);
            this.chkEmail.setLabel(this.tr("No Email"));
            return this.chkEmail;
            
        }
        
        ,create_chkEmail_2: function create_chkEmail_2() {
            this.chkEmail_2 = new qx.ui.form.CheckBox();
            this.chkEmail_2.setMarginBottom(1);
            this.chkEmail_2.setMarginTop(1);
            this.chkEmail_2.setMarginLeft(1);
            this.chkEmail_2.setMarginRight(1);
            this.chkEmail_2.setLabel(this.tr("No Email"));
            return this.chkEmail_2;
            
        }
        
        ,create_chkLRITTest: function create_chkLRITTest() {
            this.chkLRITTest = new qx.ui.form.CheckBox();
            this.chkLRITTest.setMarginBottom(1);
            this.chkLRITTest.setMarginTop(1);
            this.chkLRITTest.setMarginLeft(1);
            this.chkLRITTest.setMarginRight(1);
            this.chkLRITTest.setLabel(this.tr("Start"));
            return this.chkLRITTest;
            
        }
        
        ,create_chkLRITTest_2: function create_chkLRITTest_2() {
            this.chkLRITTest_2 = new qx.ui.form.CheckBox();
            this.chkLRITTest_2.setMarginBottom(1);
            this.chkLRITTest_2.setMarginTop(1);
            this.chkLRITTest_2.setMarginLeft(1);
            this.chkLRITTest_2.setMarginRight(1);
            this.chkLRITTest_2.setLabel(this.tr("Start"));
            return this.chkLRITTest_2;
            
        }
        
        ,create_comboInterval: function create_comboInterval() {
            this.comboInterval = new qx.ui.form.SelectBox();
            this.comboInterval.setMarginBottom(1);
            this.comboInterval.setMarginTop(1);
            this.comboInterval.setMarginLeft(1);
            this.comboInterval.setMarginRight(1);
            return this.comboInterval;
            
        }
        
        ,create_comboInterval_2: function create_comboInterval_2() {
            this.comboInterval_2 = new qx.ui.form.SelectBox();
            this.comboInterval_2.setMarginBottom(1);
            this.comboInterval_2.setMarginTop(1);
            this.comboInterval_2.setMarginLeft(1);
            this.comboInterval_2.setMarginRight(1);
            return this.comboInterval_2;
            
        }
        
        ,create_comboSubAddress: function create_comboSubAddress() {
            this.comboSubAddress = new qx.ui.form.SelectBox();
            this.comboSubAddress.setMinWidth(80);
            this.comboSubAddress.setMarginBottom(1);
            this.comboSubAddress.setMarginTop(1);
            this.comboSubAddress.setMarginLeft(1);
            this.comboSubAddress.setMarginRight(1);
            this.comboSubAddress.add(new qx.ui.form.ListItem("1",null,null));
            this.comboSubAddress.add(new qx.ui.form.ListItem("2",null,null));
            this.comboSubAddress.add(new qx.ui.form.ListItem("3",null,null));
            this.comboSubAddress.add(new qx.ui.form.ListItem("4",null,null));
            this.comboSubAddress.add(new qx.ui.form.ListItem("5",null,null));
            this.comboSubAddress.add(new qx.ui.form.ListItem("6",null,null));
            this.comboSubAddress.add(new qx.ui.form.ListItem("7",null,null));
            return this.comboSubAddress;
            
        }
        
        ,create_comboSubAddress_2: function create_comboSubAddress_2() {
            this.comboSubAddress_2 = new qx.ui.form.SelectBox();
            this.comboSubAddress_2.setMinWidth(80);
            this.comboSubAddress_2.setMarginBottom(1);
            this.comboSubAddress_2.setMarginTop(1);
            this.comboSubAddress_2.setMarginLeft(1);
            this.comboSubAddress_2.setMarginRight(1);
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("1",null,null));
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("2",null,null));
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("3",null,null));
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("4",null,null));
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("5",null,null));
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("6",null,null));
            this.comboSubAddress_2.add(new qx.ui.form.ListItem("7",null,null));
            return this.comboSubAddress_2;
            
        }
        
        ,create_comboTrackingMethod: function create_comboTrackingMethod() {
            this.comboTrackingMethod = new qx.ui.form.SelectBox();
            this.comboTrackingMethod.setMarginBottom(1);
            this.comboTrackingMethod.setMarginTop(1);
            this.comboTrackingMethod.setMarginLeft(1);
            this.comboTrackingMethod.setMarginRight(1);
            return this.comboTrackingMethod;
            
        }
        
        ,create_comboTrackingMethod_2: function create_comboTrackingMethod_2() {
            this.comboTrackingMethod_2 = new qx.ui.form.SelectBox();
            this.comboTrackingMethod_2.setMarginBottom(1);
            this.comboTrackingMethod_2.setMarginTop(1);
            this.comboTrackingMethod_2.setMarginLeft(1);
            this.comboTrackingMethod_2.setMarginRight(1);
            return this.comboTrackingMethod_2;
            
        }
        
        ,create_dateEdit: function create_dateEdit() {
            this.dateEdit = new qx.ui.form.DateField();
            this.dateEdit.setMarginBottom(1);
            this.dateEdit.setMarginTop(1);
            this.dateEdit.setMarginLeft(1);
            this.dateEdit.setMarginRight(1);
            return this.dateEdit;
            
        }
        
        ,create_dateEdit_2: function create_dateEdit_2() {
            this.dateEdit_2 = new qx.ui.form.DateField();
            this.dateEdit_2.setMarginBottom(1);
            this.dateEdit_2.setMarginTop(1);
            this.dateEdit_2.setMarginLeft(1);
            this.dateEdit_2.setMarginRight(1);
            return this.dateEdit_2;
            
        }
        
        ,create_edtAnswerBack: function create_edtAnswerBack() {
            this.edtAnswerBack = new qx.ui.form.TextField();
            this.edtAnswerBack.setMarginBottom(1);
            this.edtAnswerBack.setMarginTop(1);
            this.edtAnswerBack.setMarginLeft(1);
            this.edtAnswerBack.setMarginRight(1);
            return this.edtAnswerBack;
            
        }
        
        ,create_edtAnswerBack_2: function create_edtAnswerBack_2() {
            this.edtAnswerBack_2 = new qx.ui.form.TextField();
            this.edtAnswerBack_2.setMarginBottom(1);
            this.edtAnswerBack_2.setMarginTop(1);
            this.edtAnswerBack_2.setMarginLeft(1);
            this.edtAnswerBack_2.setMarginRight(1);
            return this.edtAnswerBack_2;
            
        }
        
        ,create_edtCompany: function create_edtCompany() {
            this.edtCompany = new qx.ui.form.TextField();
            this.edtCompany.setMinWidth(300);
            this.edtCompany.setMaxWidth(5);
            this.edtCompany.setMarginBottom(1);
            this.edtCompany.setMarginTop(1);
            this.edtCompany.setMarginLeft(1);
            this.edtCompany.setMarginRight(1);
            return this.edtCompany;
            
        }
        
        ,create_edtCompany_2: function create_edtCompany_2() {
            this.edtCompany_2 = new qx.ui.form.TextField();
            this.edtCompany_2.setMarginBottom(1);
            this.edtCompany_2.setMarginTop(1);
            this.edtCompany_2.setMarginLeft(1);
            this.edtCompany_2.setMarginRight(1);
            return this.edtCompany_2;
            
        }
        
        ,create_edtDNID: function create_edtDNID() {
            this.edtDNID = new qx.ui.form.TextField();
            this.edtDNID.setMinWidth(50);
            this.edtDNID.setMarginBottom(1);
            this.edtDNID.setMarginTop(1);
            this.edtDNID.setMarginLeft(1);
            this.edtDNID.setMarginRight(1);
            return this.edtDNID;
            
        }
        
        ,create_edtDNID_2: function create_edtDNID_2() {
            this.edtDNID_2 = new qx.ui.form.TextField();
            this.edtDNID_2.setMinWidth(50);
            this.edtDNID_2.setMarginBottom(1);
            this.edtDNID_2.setMarginTop(1);
            this.edtDNID_2.setMarginLeft(1);
            this.edtDNID_2.setMarginRight(1);
            return this.edtDNID_2;
            
        }
        
        ,create_edtEmail: function create_edtEmail() {
            this.edtEmail = new qx.ui.form.TextField();
            this.edtEmail.setMarginBottom(1);
            this.edtEmail.setMarginTop(1);
            this.edtEmail.setMarginLeft(1);
            this.edtEmail.setMarginRight(1);
            return this.edtEmail;
            
        }
        
        ,create_edtEmail_2: function create_edtEmail_2() {
            this.edtEmail_2 = new qx.ui.form.TextField();
            this.edtEmail_2.setMarginBottom(1);
            this.edtEmail_2.setMarginTop(1);
            this.edtEmail_2.setMarginLeft(1);
            this.edtEmail_2.setMarginRight(1);
            return this.edtEmail_2;
            
        }
        
        ,create_edtIOWN: function create_edtIOWN() {
            this.edtIOWN = new qx.ui.form.TextField();
            this.edtIOWN.setMarginBottom(1);
            this.edtIOWN.setMarginTop(1);
            this.edtIOWN.setMarginLeft(1);
            this.edtIOWN.setMarginRight(1);
            return this.edtIOWN;
            
        }
        
        ,create_edtIOWN_2: function create_edtIOWN_2() {
            this.edtIOWN_2 = new qx.ui.form.TextField();
            this.edtIOWN_2.setMarginBottom(1);
            this.edtIOWN_2.setMarginTop(1);
            this.edtIOWN_2.setMarginLeft(1);
            this.edtIOWN_2.setMarginRight(1);
            return this.edtIOWN_2;
            
        }
        
        ,create_edtMN: function create_edtMN() {
            this.edtMN = new qx.ui.form.TextField();
            this.edtMN.setMinWidth(30);
            this.edtMN.setMarginBottom(1);
            this.edtMN.setMarginTop(1);
            this.edtMN.setMarginLeft(1);
            this.edtMN.setMarginRight(1);
            return this.edtMN;
            
        }
        
        ,create_edtMN_2: function create_edtMN_2() {
            this.edtMN_2 = new qx.ui.form.TextField();
            this.edtMN_2.setMinWidth(30);
            this.edtMN_2.setMarginBottom(1);
            this.edtMN_2.setMarginTop(1);
            this.edtMN_2.setMarginLeft(1);
            this.edtMN_2.setMarginRight(1);
            return this.edtMN_2;
            
        }
        
        ,create_edtName: function create_edtName() {
            this.edtName = new qx.ui.form.TextField();
            this.edtName.setMarginBottom(1);
            this.edtName.setMarginTop(1);
            this.edtName.setMarginLeft(1);
            this.edtName.setMarginRight(1);
            return this.edtName;
            
        }
        
        ,create_edtName_2: function create_edtName_2() {
            this.edtName_2 = new qx.ui.form.TextField();
            this.edtName_2.setMinWidth(300);
            this.edtName_2.setMaxWidth(400);
            this.edtName_2.setMarginBottom(1);
            this.edtName_2.setMarginTop(1);
            this.edtName_2.setMarginLeft(1);
            this.edtName_2.setMarginRight(1);
            return this.edtName_2;
            
        }
        
        ,create_edtTerminalSN: function create_edtTerminalSN() {
            this.edtTerminalSN = new qx.ui.form.TextField();
            this.edtTerminalSN.setMarginBottom(1);
            this.edtTerminalSN.setMarginTop(1);
            this.edtTerminalSN.setMarginLeft(1);
            this.edtTerminalSN.setMarginRight(1);
            return this.edtTerminalSN;
            
        }
        
        ,create_edtTerminalSN_2: function create_edtTerminalSN_2() {
            this.edtTerminalSN_2 = new qx.ui.form.TextField();
            this.edtTerminalSN_2.setMarginBottom(1);
            this.edtTerminalSN_2.setMarginTop(1);
            this.edtTerminalSN_2.setMarginLeft(1);
            this.edtTerminalSN_2.setMarginRight(1);
            return this.edtTerminalSN_2;
            
        }
        
        ,create_formLayout: function create_formLayout() {
            this.formLayout = new qx.ui.layout.Grid();
            this.formLayout.setRowFlex(0,1);
            this.formLayout.setRowFlex(1,1);
            this.formLayout.setRowFlex(2,1);
            this.formLayout.setColumnFlex(0,1);
            this.formLayout.setColumnFlex(1,1);
            return this.formLayout;
            
        }
        
        ,create_formLayout_implicit_container: function create_formLayout_implicit_container() {
            this.formLayout_implicit_container = new qx.ui.container.Composite();
            this.formLayout_implicit_container.setMarginBottom(1);
            this.formLayout_implicit_container.setMarginTop(1);
            this.formLayout_implicit_container.setMarginLeft(1);
            this.formLayout_implicit_container.setMarginRight(1);
            this.formLayout_implicit_container.setLayout(this.create_formLayout());
            this.formLayout_implicit_container.add(this.create_pushButton_3(), {column: 0,row: 0});
            this.formLayout_implicit_container.add(this.create_label_2(), {column: 1,row: 0});
            return this.formLayout_implicit_container;
            
        }
        
        ,create_gridLayout: function create_gridLayout() {
            this.gridLayout = new qx.ui.layout.Grid();
            this.gridLayout.setRowFlex(0,1);
            this.gridLayout.setRowFlex(1,1);
            this.gridLayout.setRowFlex(2,1);
            this.gridLayout.setRowFlex(3,1);
            this.gridLayout.setRowFlex(4,1);
            this.gridLayout.setRowFlex(5,1);
            this.gridLayout.setRowFlex(6,1);
            this.gridLayout.setRowFlex(7,1);
            this.gridLayout.setRowFlex(8,1);
            this.gridLayout.setColumnFlex(0,1);
            this.gridLayout.setColumnFlex(2,1);
            return this.gridLayout;
            
        }
        
        ,create_gridLayout_2: function create_gridLayout_2() {
            this.gridLayout_2 = new qx.ui.layout.Grid();
            this.gridLayout_2.setRowFlex(0,1);
            this.gridLayout_2.setColumnFlex(0,1);
            this.gridLayout_2.setColumnFlex(1,1);
            return this.gridLayout_2;
            
        }
        
        ,create_gridLayout_2_implicit_container: function create_gridLayout_2_implicit_container() {
            this.gridLayout_2_implicit_container = new qx.ui.container.Composite();
            this.gridLayout_2_implicit_container.setMarginBottom(1);
            this.gridLayout_2_implicit_container.setMarginTop(1);
            this.gridLayout_2_implicit_container.setMarginLeft(1);
            this.gridLayout_2_implicit_container.setMarginRight(1);
            this.gridLayout_2_implicit_container.setLayout(this.create_gridLayout_2());
            this.gridLayout_2_implicit_container.add(this.create_pushButton_2(), {column: 0,row: 0});
            this.gridLayout_2_implicit_container.add(this.create_tabWidget_2(), {column: 1,row: 0});
            return this.gridLayout_2_implicit_container;
            
        }
        
        ,create_gridLayout_3: function create_gridLayout_3() {
            this.gridLayout_3 = new qx.ui.layout.Grid();
            this.gridLayout_3.setRowFlex(1,1);
            this.gridLayout_3.setRowFlex(2,1);
            this.gridLayout_3.setRowFlex(3,1);
            this.gridLayout_3.setRowFlex(4,1);
            this.gridLayout_3.setRowFlex(5,1);
            this.gridLayout_3.setRowFlex(6,1);
            this.gridLayout_3.setRowFlex(7,1);
            this.gridLayout_3.setRowFlex(8,1);
            this.gridLayout_3.setColumnFlex(0,1);
            return this.gridLayout_3;
            
        }
        
        ,create_groupBox: function create_groupBox() {
            this.groupBox = new qx.ui.groupbox.GroupBox();
            this.groupBox.setMinWidth(400);
            this.groupBox.setMaxWidth(600);
            this.groupBox.setMarginBottom(1);
            this.groupBox.setMarginTop(1);
            this.groupBox.setMarginLeft(1);
            this.groupBox.setMarginRight(1);
            this.groupBox.setLayout(this.create_gridLayout());
            this.groupBox.add(this.create_lblCompany(), {column: 0,row: 0});
            this.groupBox.add(this.create_edtCompany(), {column: 2,row: 0});
            this.groupBox.add(this.create_lblName(), {column: 0,row: 1});
            this.groupBox.add(this.create_edtName(), {column: 2,row: 1});
            this.groupBox.add(this.create_lblIdentifers(), {column: 0,row: 2});
            this.groupBox.add(this.create_horizontalLayout_implicit_container(), {column: 2,row: 2});
            this.groupBox.add(this.create_lblDetails(), {column: 0,row: 3});
            this.groupBox.add(this.create_horizontalLayout_2_implicit_container(), {column: 2,row: 3});
            this.groupBox.add(this.create_lblEmail(), {column: 0,row: 4});
            this.groupBox.add(this.create_lblTrackingMethod(), {column: 0,row: 5});
            this.groupBox.add(this.create_HLTrackingMethod_implicit_container(), {column: 2,row: 5});
            this.groupBox.add(this.create_lblTest(), {column: 0,row: 6});
            this.groupBox.add(this.create_HLTest_implicit_container(), {column: 2,row: 6});
            this.groupBox.add(this.create_lblAnswerBack(), {column: 0,row: 7});
            this.groupBox.add(this.create_edtAnswerBack(), {column: 2,row: 7});
            this.groupBox.add(this.create_label(), {column: 0,row: 8});
            this.groupBox.add(this.create_horizontalLayout_4_implicit_container(), {column: 2,row: 8});
            this.groupBox.add(this.create_VLEmail_implicit_container(), {column: 2,row: 4});
            this.groupBox.setLegend(this.tr("Add"));
            return this.groupBox;
            
        }
        
        ,create_groupBox_2: function create_groupBox_2() {
            this.groupBox_2 = new qx.ui.groupbox.GroupBox();
            this.groupBox_2.setMarginBottom(1);
            this.groupBox_2.setMarginTop(1);
            this.groupBox_2.setMarginLeft(1);
            this.groupBox_2.setMarginRight(1);
            this.groupBox_2.setLayout(this.create_verticalLayout_3());
            this.groupBox_2.add(this.create_gridLayout_2_implicit_container(), {flex: 1});
            this.groupBox_2.setLegend(this.tr("GroupBox"));
            return this.groupBox_2;
            
        }
        
        ,create_groupBox_3: function create_groupBox_3() {
            this.groupBox_3 = new qx.ui.groupbox.GroupBox();
            this.groupBox_3.setMarginBottom(1);
            this.groupBox_3.setMarginTop(1);
            this.groupBox_3.setMarginLeft(1);
            this.groupBox_3.setMarginRight(1);
            this.groupBox_3.setLayout(this.create_gridLayout_3());
            this.groupBox_3.add(this.create_lblCompany_2(), {column: 0,row: 0});
            this.groupBox_3.add(this.create_edtCompany_2(), {column: 2,row: 0});
            this.groupBox_3.add(this.create_lblName_2(), {column: 0,row: 1});
            this.groupBox_3.add(this.create_edtName_2(), {column: 2,row: 1});
            this.groupBox_3.add(this.create_lblIdentifers_2(), {column: 0,row: 2});
            this.groupBox_3.add(this.create_horizontalLayout_7_implicit_container(), {column: 2,row: 2});
            this.groupBox_3.add(this.create_lblDetails_2(), {column: 0,row: 3});
            this.groupBox_3.add(this.create_horizontalLayout_8_implicit_container(), {column: 2,row: 3});
            this.groupBox_3.add(this.create_lblEmail_2(), {column: 0,row: 4});
            this.groupBox_3.add(this.create_lblTrackingMethod_2(), {column: 0,row: 5});
            this.groupBox_3.add(this.create_HLTrackingMethod_2_implicit_container(), {column: 2,row: 5});
            this.groupBox_3.add(this.create_lblTest_2(), {column: 0,row: 6});
            this.groupBox_3.add(this.create_HLTest_2_implicit_container(), {column: 2,row: 6});
            this.groupBox_3.add(this.create_lblAnswerBack_2(), {column: 0,row: 7});
            this.groupBox_3.add(this.create_edtAnswerBack_2(), {column: 2,row: 7});
            this.groupBox_3.add(this.create_label_3(), {column: 0,row: 8});
            this.groupBox_3.add(this.create_horizontalLayout_9_implicit_container(), {column: 2,row: 8});
            this.groupBox_3.add(this.create_VLEmail_2_implicit_container(), {column: 2,row: 4});
            this.groupBox_3.setLegend(this.tr("Add"));
            return this.groupBox_3;
            
        }
        
        ,create_horizontalLayout: function create_horizontalLayout() {
            this.horizontalLayout = new qx.ui.layout.HBox();
            return this.horizontalLayout;
            
        }
        
        ,create_horizontalLayout_10: function create_horizontalLayout_10() {
            this.horizontalLayout_10 = new qx.ui.layout.HBox();
            return this.horizontalLayout_10;
            
        }
        
        ,create_horizontalLayout_10_implicit_container: function create_horizontalLayout_10_implicit_container() {
            this.horizontalLayout_10_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_10_implicit_container.setMarginBottom(1);
            this.horizontalLayout_10_implicit_container.setMarginTop(1);
            this.horizontalLayout_10_implicit_container.setMarginLeft(1);
            this.horizontalLayout_10_implicit_container.setMarginRight(1);
            this.horizontalLayout_10_implicit_container.setLayout(this.create_horizontalLayout_10());
            this.horizontalLayout_10_implicit_container.add(this.create_radioButton_8(), {flex: 1});
            this.horizontalLayout_10_implicit_container.add(this.create_chkEmail_2(), {flex: 1});
            this.horizontalLayout_10_implicit_container.add(this.create_radioButton_9(), {flex: 1});
            return this.horizontalLayout_10_implicit_container;
            
        }
        
        ,create_horizontalLayout_2: function create_horizontalLayout_2() {
            this.horizontalLayout_2 = new qx.ui.layout.HBox();
            return this.horizontalLayout_2;
            
        }
        
        ,create_horizontalLayout_2_implicit_container: function create_horizontalLayout_2_implicit_container() {
            this.horizontalLayout_2_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_2_implicit_container.setMarginBottom(1);
            this.horizontalLayout_2_implicit_container.setMarginTop(1);
            this.horizontalLayout_2_implicit_container.setMarginLeft(1);
            this.horizontalLayout_2_implicit_container.setMarginRight(1);
            this.horizontalLayout_2_implicit_container.setLayout(this.create_horizontalLayout_2());
            this.horizontalLayout_2_implicit_container.add(this.create_lblDNID(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_edtDNID(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_lblMN(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_edtMN(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_lblSubAddress(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_comboSubAddress(), {flex: 1});
            return this.horizontalLayout_2_implicit_container;
            
        }
        
        ,create_horizontalLayout_3: function create_horizontalLayout_3() {
            this.horizontalLayout_3 = new qx.ui.layout.HBox();
            return this.horizontalLayout_3;
            
        }
        
        ,create_horizontalLayout_4: function create_horizontalLayout_4() {
            this.horizontalLayout_4 = new qx.ui.layout.HBox();
            return this.horizontalLayout_4;
            
        }
        
        ,create_horizontalLayout_4_implicit_container: function create_horizontalLayout_4_implicit_container() {
            this.horizontalLayout_4_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_4_implicit_container.setMarginBottom(1);
            this.horizontalLayout_4_implicit_container.setMarginTop(1);
            this.horizontalLayout_4_implicit_container.setMarginLeft(1);
            this.horizontalLayout_4_implicit_container.setMarginRight(1);
            this.horizontalLayout_4_implicit_container.setLayout(this.create_horizontalLayout_4());
            this.horizontalLayout_4_implicit_container.add(this.create_dateEdit(), {flex: 1});
            this.horizontalLayout_4_implicit_container.add(this.create_spinBox(), {flex: 1});
            return this.horizontalLayout_4_implicit_container;
            
        }
        
        ,create_horizontalLayout_5: function create_horizontalLayout_5() {
            this.horizontalLayout_5 = new qx.ui.layout.HBox();
            return this.horizontalLayout_5;
            
        }
        
        ,create_horizontalLayout_5_implicit_container: function create_horizontalLayout_5_implicit_container() {
            this.horizontalLayout_5_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_5_implicit_container.setMarginBottom(1);
            this.horizontalLayout_5_implicit_container.setMarginTop(1);
            this.horizontalLayout_5_implicit_container.setMarginLeft(1);
            this.horizontalLayout_5_implicit_container.setMarginRight(1);
            this.horizontalLayout_5_implicit_container.setLayout(this.create_horizontalLayout_5());
            this.horizontalLayout_5_implicit_container.add(this.create_radioButton_4(), {flex: 1});
            this.horizontalLayout_5_implicit_container.add(this.create_chkEmail(), {flex: 1});
            this.horizontalLayout_5_implicit_container.add(this.create_radioButton_3(), {flex: 1});
            return this.horizontalLayout_5_implicit_container;
            
        }
        
        ,create_horizontalLayout_6: function create_horizontalLayout_6() {
            this.horizontalLayout_6 = new qx.ui.layout.HBox();
            return this.horizontalLayout_6;
            
        }
        
        ,create_horizontalLayout_7: function create_horizontalLayout_7() {
            this.horizontalLayout_7 = new qx.ui.layout.HBox();
            return this.horizontalLayout_7;
            
        }
        
        ,create_horizontalLayout_7_implicit_container: function create_horizontalLayout_7_implicit_container() {
            this.horizontalLayout_7_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_7_implicit_container.setMarginBottom(1);
            this.horizontalLayout_7_implicit_container.setMarginTop(1);
            this.horizontalLayout_7_implicit_container.setMarginLeft(1);
            this.horizontalLayout_7_implicit_container.setMarginRight(1);
            this.horizontalLayout_7_implicit_container.setLayout(this.create_horizontalLayout_7());
            this.horizontalLayout_7_implicit_container.add(this.create_lblIOWN_2(), {flex: 1});
            this.horizontalLayout_7_implicit_container.add(this.create_edtIOWN_2(), {flex: 1});
            this.horizontalLayout_7_implicit_container.add(this.create_lblTerminalSN_2(), {flex: 1});
            this.horizontalLayout_7_implicit_container.add(this.create_edtTerminalSN_2(), {flex: 1});
            return this.horizontalLayout_7_implicit_container;
            
        }
        
        ,create_horizontalLayout_8: function create_horizontalLayout_8() {
            this.horizontalLayout_8 = new qx.ui.layout.HBox();
            return this.horizontalLayout_8;
            
        }
        
        ,create_horizontalLayout_8_implicit_container: function create_horizontalLayout_8_implicit_container() {
            this.horizontalLayout_8_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_8_implicit_container.setMarginBottom(1);
            this.horizontalLayout_8_implicit_container.setMarginTop(1);
            this.horizontalLayout_8_implicit_container.setMarginLeft(1);
            this.horizontalLayout_8_implicit_container.setMarginRight(1);
            this.horizontalLayout_8_implicit_container.setLayout(this.create_horizontalLayout_8());
            this.horizontalLayout_8_implicit_container.add(this.create_lblDNID_2(), {flex: 1});
            this.horizontalLayout_8_implicit_container.add(this.create_edtDNID_2(), {flex: 1});
            this.horizontalLayout_8_implicit_container.add(this.create_lblMN_2(), {flex: 1});
            this.horizontalLayout_8_implicit_container.add(this.create_edtMN_2(), {flex: 1});
            this.horizontalLayout_8_implicit_container.add(this.create_lblSubAddress_2(), {flex: 1});
            this.horizontalLayout_8_implicit_container.add(this.create_comboSubAddress_2(), {flex: 1});
            return this.horizontalLayout_8_implicit_container;
            
        }
        
        ,create_horizontalLayout_9: function create_horizontalLayout_9() {
            this.horizontalLayout_9 = new qx.ui.layout.HBox();
            return this.horizontalLayout_9;
            
        }
        
        ,create_horizontalLayout_9_implicit_container: function create_horizontalLayout_9_implicit_container() {
            this.horizontalLayout_9_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_9_implicit_container.setMarginBottom(1);
            this.horizontalLayout_9_implicit_container.setMarginTop(1);
            this.horizontalLayout_9_implicit_container.setMarginLeft(1);
            this.horizontalLayout_9_implicit_container.setMarginRight(1);
            this.horizontalLayout_9_implicit_container.setLayout(this.create_horizontalLayout_9());
            this.horizontalLayout_9_implicit_container.add(this.create_spinBox_2(), {flex: 1});
            this.horizontalLayout_9_implicit_container.add(this.create_dateEdit_2(), {flex: 1});
            return this.horizontalLayout_9_implicit_container;
            
        }
        
        ,create_horizontalLayout_implicit_container: function create_horizontalLayout_implicit_container() {
            this.horizontalLayout_implicit_container = new qx.ui.container.Composite();
            this.horizontalLayout_implicit_container.setMarginBottom(1);
            this.horizontalLayout_implicit_container.setMarginTop(1);
            this.horizontalLayout_implicit_container.setMarginLeft(1);
            this.horizontalLayout_implicit_container.setMarginRight(1);
            this.horizontalLayout_implicit_container.setLayout(this.create_horizontalLayout());
            this.horizontalLayout_implicit_container.add(this.create_lblIOWN(), {flex: 1});
            this.horizontalLayout_implicit_container.add(this.create_edtIOWN(), {flex: 1});
            this.horizontalLayout_implicit_container.add(this.create_lblTerminalSN(), {flex: 1});
            this.horizontalLayout_implicit_container.add(this.create_edtTerminalSN(), {flex: 1});
            return this.horizontalLayout_implicit_container;
            
        }
        
        ,create_horizontalSpacer: function create_horizontalSpacer() {
            this.horizontalSpacer = new qx.ui.core.Spacer();
            this.horizontalSpacer.setMarginBottom(1);
            this.horizontalSpacer.setMarginTop(1);
            this.horizontalSpacer.setMarginLeft(1);
            this.horizontalSpacer.setMarginRight(1);
            return this.horizontalSpacer;
            
        }
        
        ,create_horizontalSpacer_2: function create_horizontalSpacer_2() {
            this.horizontalSpacer_2 = new qx.ui.core.Spacer();
            this.horizontalSpacer_2.setMarginBottom(1);
            this.horizontalSpacer_2.setMarginTop(1);
            this.horizontalSpacer_2.setMarginLeft(1);
            this.horizontalSpacer_2.setMarginRight(1);
            return this.horizontalSpacer_2;
            
        }
        
        ,create_label: function create_label() {
            this.label = new qx.ui.basic.Label();
            this.label.setMarginBottom(1);
            this.label.setMarginTop(1);
            this.label.setMarginLeft(1);
            this.label.setMarginRight(1);
            this.label.setValue(this.tr("Date & Count: "));
            return this.label;
            
        }
        
        ,create_label_2: function create_label_2() {
            this.label_2 = new qx.ui.basic.Label();
            this.label_2.setMarginBottom(1);
            this.label_2.setMarginTop(1);
            this.label_2.setMarginLeft(1);
            this.label_2.setMarginRight(1);
            this.label_2.setValue(this.tr("TextLabel"));
            return this.label_2;
            
        }
        
        ,create_label_3: function create_label_3() {
            this.label_3 = new qx.ui.basic.Label();
            this.label_3.setMarginBottom(1);
            this.label_3.setMarginTop(1);
            this.label_3.setMarginLeft(1);
            this.label_3.setMarginRight(1);
            this.label_3.setValue(this.tr("Time & Count: "));
            return this.label_3;
            
        }
        
        ,create_lblAnswerBack: function create_lblAnswerBack() {
            this.lblAnswerBack = new qx.ui.basic.Label();
            this.lblAnswerBack.setMarginBottom(1);
            this.lblAnswerBack.setMarginTop(1);
            this.lblAnswerBack.setMarginLeft(1);
            this.lblAnswerBack.setMarginRight(1);
            this.lblAnswerBack.setValue(this.tr("Answer Back : "));
            return this.lblAnswerBack;
            
        }
        
        ,create_lblAnswerBack_2: function create_lblAnswerBack_2() {
            this.lblAnswerBack_2 = new qx.ui.basic.Label();
            this.lblAnswerBack_2.setMarginBottom(1);
            this.lblAnswerBack_2.setMarginTop(1);
            this.lblAnswerBack_2.setMarginLeft(1);
            this.lblAnswerBack_2.setMarginRight(1);
            this.lblAnswerBack_2.setValue(this.tr("Answer Back : "));
            return this.lblAnswerBack_2;
            
        }
        
        ,create_lblCompany: function create_lblCompany() {
            this.lblCompany = new qx.ui.basic.Label();
            this.lblCompany.setMarginBottom(1);
            this.lblCompany.setMarginTop(1);
            this.lblCompany.setMarginLeft(1);
            this.lblCompany.setMarginRight(1);
            this.lblCompany.setValue(this.tr("Company : "));
            return this.lblCompany;
            
        }
        
        ,create_lblCompany_2: function create_lblCompany_2() {
            this.lblCompany_2 = new qx.ui.basic.Label();
            this.lblCompany_2.setMarginBottom(1);
            this.lblCompany_2.setMarginTop(1);
            this.lblCompany_2.setMarginLeft(1);
            this.lblCompany_2.setMarginRight(1);
            this.lblCompany_2.setValue(this.tr("Company : "));
            return this.lblCompany_2;
            
        }
        
        ,create_lblDNID: function create_lblDNID() {
            this.lblDNID = new qx.ui.basic.Label();
            this.lblDNID.setMarginBottom(1);
            this.lblDNID.setMarginTop(1);
            this.lblDNID.setMarginLeft(1);
            this.lblDNID.setMarginRight(1);
            this.lblDNID.setValue(this.tr("ABC: "));
            return this.lblDNID;
            
        }
        
        ,create_lblDNID_2: function create_lblDNID_2() {
            this.lblDNID_2 = new qx.ui.basic.Label();
            this.lblDNID_2.setMarginBottom(1);
            this.lblDNID_2.setMarginTop(1);
            this.lblDNID_2.setMarginLeft(1);
            this.lblDNID_2.setMarginRight(1);
            this.lblDNID_2.setValue(this.tr("ABC: "));
            return this.lblDNID_2;
            
        }
        
        ,create_lblDetails: function create_lblDetails() {
            this.lblDetails = new qx.ui.basic.Label();
            this.lblDetails.setMarginBottom(1);
            this.lblDetails.setMarginTop(1);
            this.lblDetails.setMarginLeft(1);
            this.lblDetails.setMarginRight(1);
            this.lblDetails.setValue(this.tr("Details: "));
            return this.lblDetails;
            
        }
        
        ,create_lblDetails_2: function create_lblDetails_2() {
            this.lblDetails_2 = new qx.ui.basic.Label();
            this.lblDetails_2.setMarginBottom(1);
            this.lblDetails_2.setMarginTop(1);
            this.lblDetails_2.setMarginLeft(1);
            this.lblDetails_2.setMarginRight(1);
            this.lblDetails_2.setValue(this.tr("Details: "));
            return this.lblDetails_2;
            
        }
        
        ,create_lblEmail: function create_lblEmail() {
            this.lblEmail = new qx.ui.basic.Label();
            this.lblEmail.setMarginBottom(1);
            this.lblEmail.setMarginTop(1);
            this.lblEmail.setMarginLeft(1);
            this.lblEmail.setMarginRight(1);
            this.lblEmail.setValue(this.tr("Email: "));
            return this.lblEmail;
            
        }
        
        ,create_lblEmail_2: function create_lblEmail_2() {
            this.lblEmail_2 = new qx.ui.basic.Label();
            this.lblEmail_2.setMarginBottom(1);
            this.lblEmail_2.setMarginTop(1);
            this.lblEmail_2.setMarginLeft(1);
            this.lblEmail_2.setMarginRight(1);
            this.lblEmail_2.setValue(this.tr("Email: "));
            return this.lblEmail_2;
            
        }
        
        ,create_lblIOWN: function create_lblIOWN() {
            this.lblIOWN = new qx.ui.basic.Label();
            this.lblIOWN.setMarginBottom(1);
            this.lblIOWN.setMarginTop(1);
            this.lblIOWN.setMarginLeft(1);
            this.lblIOWN.setMarginRight(1);
            this.lblIOWN.setValue(this.tr("OWN: : "));
            return this.lblIOWN;
            
        }
        
        ,create_lblIOWN_2: function create_lblIOWN_2() {
            this.lblIOWN_2 = new qx.ui.basic.Label();
            this.lblIOWN_2.setMarginBottom(1);
            this.lblIOWN_2.setMarginTop(1);
            this.lblIOWN_2.setMarginLeft(1);
            this.lblIOWN_2.setMarginRight(1);
            this.lblIOWN_2.setValue(this.tr("OWN: : "));
            return this.lblIOWN_2;
            
        }
        
        ,create_lblIdentifers: function create_lblIdentifers() {
            this.lblIdentifers = new qx.ui.basic.Label();
            this.lblIdentifers.setMarginBottom(1);
            this.lblIdentifers.setMarginTop(1);
            this.lblIdentifers.setMarginLeft(1);
            this.lblIdentifers.setMarginRight(1);
            this.lblIdentifers.setValue(this.tr("Identifiers: "));
            return this.lblIdentifers;
            
        }
        
        ,create_lblIdentifers_2: function create_lblIdentifers_2() {
            this.lblIdentifers_2 = new qx.ui.basic.Label();
            this.lblIdentifers_2.setMarginBottom(1);
            this.lblIdentifers_2.setMarginTop(1);
            this.lblIdentifers_2.setMarginLeft(1);
            this.lblIdentifers_2.setMarginRight(1);
            this.lblIdentifers_2.setValue(this.tr("Identifiers: "));
            return this.lblIdentifers_2;
            
        }
        
        ,create_lblInterval: function create_lblInterval() {
            this.lblInterval = new qx.ui.basic.Label();
            this.lblInterval.setMarginBottom(1);
            this.lblInterval.setMarginTop(1);
            this.lblInterval.setMarginLeft(1);
            this.lblInterval.setMarginRight(1);
            this.lblInterval.setValue(this.tr("Interval"));
            return this.lblInterval;
            
        }
        
        ,create_lblInterval_2: function create_lblInterval_2() {
            this.lblInterval_2 = new qx.ui.basic.Label();
            this.lblInterval_2.setMarginBottom(1);
            this.lblInterval_2.setMarginTop(1);
            this.lblInterval_2.setMarginLeft(1);
            this.lblInterval_2.setMarginRight(1);
            this.lblInterval_2.setValue(this.tr("Interval"));
            return this.lblInterval_2;
            
        }
        
        ,create_lblMN: function create_lblMN() {
            this.lblMN = new qx.ui.basic.Label();
            this.lblMN.setMarginBottom(1);
            this.lblMN.setMarginTop(1);
            this.lblMN.setMarginLeft(1);
            this.lblMN.setMarginRight(1);
            this.lblMN.setValue(this.tr("MN: "));
            return this.lblMN;
            
        }
        
        ,create_lblMN_2: function create_lblMN_2() {
            this.lblMN_2 = new qx.ui.basic.Label();
            this.lblMN_2.setMarginBottom(1);
            this.lblMN_2.setMarginTop(1);
            this.lblMN_2.setMarginLeft(1);
            this.lblMN_2.setMarginRight(1);
            this.lblMN_2.setValue(this.tr("MN: "));
            return this.lblMN_2;
            
        }
        
        ,create_lblName: function create_lblName() {
            this.lblName = new qx.ui.basic.Label();
            this.lblName.setMarginBottom(1);
            this.lblName.setMarginTop(1);
            this.lblName.setMarginLeft(1);
            this.lblName.setMarginRight(1);
            this.lblName.setValue(this.tr("Name : "));
            return this.lblName;
            
        }
        
        ,create_lblName_2: function create_lblName_2() {
            this.lblName_2 = new qx.ui.basic.Label();
            this.lblName_2.setMarginBottom(1);
            this.lblName_2.setMarginTop(1);
            this.lblName_2.setMarginLeft(1);
            this.lblName_2.setMarginRight(1);
            this.lblName_2.setValue(this.tr("Name : "));
            return this.lblName_2;
            
        }
        
        ,create_lblSubAddress: function create_lblSubAddress() {
            this.lblSubAddress = new qx.ui.basic.Label();
            this.lblSubAddress.setMarginBottom(1);
            this.lblSubAddress.setMarginTop(1);
            this.lblSubAddress.setMarginLeft(1);
            this.lblSubAddress.setMarginRight(1);
            this.lblSubAddress.setValue(this.tr("SA"));
            return this.lblSubAddress;
            
        }
        
        ,create_lblSubAddress_2: function create_lblSubAddress_2() {
            this.lblSubAddress_2 = new qx.ui.basic.Label();
            this.lblSubAddress_2.setMarginBottom(1);
            this.lblSubAddress_2.setMarginTop(1);
            this.lblSubAddress_2.setMarginLeft(1);
            this.lblSubAddress_2.setMarginRight(1);
            this.lblSubAddress_2.setValue(this.tr("SA"));
            return this.lblSubAddress_2;
            
        }
        
        ,create_lblTerminalSN: function create_lblTerminalSN() {
            this.lblTerminalSN = new qx.ui.basic.Label();
            this.lblTerminalSN.setMarginBottom(1);
            this.lblTerminalSN.setMarginTop(1);
            this.lblTerminalSN.setMarginLeft(1);
            this.lblTerminalSN.setMarginRight(1);
            this.lblTerminalSN.setValue(this.tr("S/N: "));
            return this.lblTerminalSN;
            
        }
        
        ,create_lblTerminalSN_2: function create_lblTerminalSN_2() {
            this.lblTerminalSN_2 = new qx.ui.basic.Label();
            this.lblTerminalSN_2.setMarginBottom(1);
            this.lblTerminalSN_2.setMarginTop(1);
            this.lblTerminalSN_2.setMarginLeft(1);
            this.lblTerminalSN_2.setMarginRight(1);
            this.lblTerminalSN_2.setValue(this.tr("S/N: "));
            return this.lblTerminalSN_2;
            
        }
        
        ,create_lblTest: function create_lblTest() {
            this.lblTest = new qx.ui.basic.Label();
            this.lblTest.setMarginBottom(1);
            this.lblTest.setMarginTop(1);
            this.lblTest.setMarginLeft(1);
            this.lblTest.setMarginRight(1);
            this.lblTest.setValue(this.tr("BJ Test: "));
            return this.lblTest;
            
        }
        
        ,create_lblTest_2: function create_lblTest_2() {
            this.lblTest_2 = new qx.ui.basic.Label();
            this.lblTest_2.setMarginBottom(1);
            this.lblTest_2.setMarginTop(1);
            this.lblTest_2.setMarginLeft(1);
            this.lblTest_2.setMarginRight(1);
            this.lblTest_2.setValue(this.tr("BJ Test: "));
            return this.lblTest_2;
            
        }
        
        ,create_lblTrackingMethod: function create_lblTrackingMethod() {
            this.lblTrackingMethod = new qx.ui.basic.Label();
            this.lblTrackingMethod.setMarginBottom(1);
            this.lblTrackingMethod.setMarginTop(1);
            this.lblTrackingMethod.setMarginLeft(1);
            this.lblTrackingMethod.setMarginRight(1);
            this.lblTrackingMethod.setValue(this.tr("Method : "));
            return this.lblTrackingMethod;
            
        }
        
        ,create_lblTrackingMethod_2: function create_lblTrackingMethod_2() {
            this.lblTrackingMethod_2 = new qx.ui.basic.Label();
            this.lblTrackingMethod_2.setMarginBottom(1);
            this.lblTrackingMethod_2.setMarginTop(1);
            this.lblTrackingMethod_2.setMarginLeft(1);
            this.lblTrackingMethod_2.setMarginRight(1);
            this.lblTrackingMethod_2.setValue(this.tr("Method : "));
            return this.lblTrackingMethod_2;
            
        }
        
        ,create_pushButton: function create_pushButton() {
            this.pushButton = new qx.ui.form.Button();
            this.pushButton.setWidth(75);
            this.pushButton.setHeight(26);
            this.pushButton.setMarginBottom(1);
            this.pushButton.setMarginTop(1);
            this.pushButton.setMarginLeft(1);
            this.pushButton.setMarginRight(1);
            this.pushButton.setLabel(this.tr("PushButton"));
            return this.pushButton;
            
        }
        
        ,create_pushButton_2: function create_pushButton_2() {
            this.pushButton_2 = new qx.ui.form.Button();
            this.pushButton_2.setMarginBottom(1);
            this.pushButton_2.setMarginTop(1);
            this.pushButton_2.setMarginLeft(1);
            this.pushButton_2.setMarginRight(1);
            this.pushButton_2.setLabel(this.tr("PushButton"));
            return this.pushButton_2;
            
        }
        
        ,create_pushButton_3: function create_pushButton_3() {
            this.pushButton_3 = new qx.ui.form.Button();
            this.pushButton_3.setMarginBottom(1);
            this.pushButton_3.setMarginTop(1);
            this.pushButton_3.setMarginLeft(1);
            this.pushButton_3.setMarginRight(1);
            this.pushButton_3.setLabel(this.tr("PushButton"));
            return this.pushButton_3;
            
        }
        
        ,create_radioButton: function create_radioButton() {
            this.radioButton = new qx.ui.form.RadioButton();
            this.radioButton.setMarginBottom(1);
            this.radioButton.setMarginTop(1);
            this.radioButton.setMarginLeft(1);
            this.radioButton.setMarginRight(1);
            this.radioButton.setLabel(this.tr("Later"));
            return this.radioButton;
            
        }
        
        ,create_radioButton_2: function create_radioButton_2() {
            this.radioButton_2 = new qx.ui.form.RadioButton();
            this.radioButton_2.setMarginBottom(1);
            this.radioButton_2.setMarginTop(1);
            this.radioButton_2.setMarginLeft(1);
            this.radioButton_2.setMarginRight(1);
            this.radioButton_2.setLabel(this.tr("Now"));
            return this.radioButton_2;
            
        }
        
        ,create_radioButton_3: function create_radioButton_3() {
            this.radioButton_3 = new qx.ui.form.RadioButton();
            this.radioButton_3.setMarginBottom(1);
            this.radioButton_3.setMarginTop(1);
            this.radioButton_3.setMarginLeft(1);
            this.radioButton_3.setMarginRight(1);
            this.radioButton_3.setLabel(this.tr("do"));
            return this.radioButton_3;
            
        }
        
        ,create_radioButton_4: function create_radioButton_4() {
            this.radioButton_4 = new qx.ui.form.RadioButton();
            this.radioButton_4.setMarginBottom(1);
            this.radioButton_4.setMarginTop(1);
            this.radioButton_4.setMarginLeft(1);
            this.radioButton_4.setMarginRight(1);
            this.radioButton_4.setLabel(this.tr("don't"));
            return this.radioButton_4;
            
        }
        
        ,create_radioButton_5: function create_radioButton_5() {
            this.radioButton_5 = new qx.ui.form.RadioButton();
            this.radioButton_5.setWidth(91);
            this.radioButton_5.setHeight(22);
            this.radioButton_5.setMarginBottom(1);
            this.radioButton_5.setMarginTop(1);
            this.radioButton_5.setMarginLeft(1);
            this.radioButton_5.setMarginRight(1);
            this.radioButton_5.setLabel(this.tr("RadioButton"));
            return this.radioButton_5;
            
        }
        
        ,create_radioButton_6: function create_radioButton_6() {
            this.radioButton_6 = new qx.ui.form.RadioButton();
            this.radioButton_6.setMarginBottom(1);
            this.radioButton_6.setMarginTop(1);
            this.radioButton_6.setMarginLeft(1);
            this.radioButton_6.setMarginRight(1);
            this.radioButton_6.setLabel(this.tr("Now"));
            return this.radioButton_6;
            
        }
        
        ,create_radioButton_7: function create_radioButton_7() {
            this.radioButton_7 = new qx.ui.form.RadioButton();
            this.radioButton_7.setMarginBottom(1);
            this.radioButton_7.setMarginTop(1);
            this.radioButton_7.setMarginLeft(1);
            this.radioButton_7.setMarginRight(1);
            this.radioButton_7.setLabel(this.tr("Later"));
            return this.radioButton_7;
            
        }
        
        ,create_radioButton_8: function create_radioButton_8() {
            this.radioButton_8 = new qx.ui.form.RadioButton();
            this.radioButton_8.setMarginBottom(1);
            this.radioButton_8.setMarginTop(1);
            this.radioButton_8.setMarginLeft(1);
            this.radioButton_8.setMarginRight(1);
            this.radioButton_8.setLabel(this.tr("don't"));
            return this.radioButton_8;
            
        }
        
        ,create_radioButton_9: function create_radioButton_9() {
            this.radioButton_9 = new qx.ui.form.RadioButton();
            this.radioButton_9.setMarginBottom(1);
            this.radioButton_9.setMarginTop(1);
            this.radioButton_9.setMarginLeft(1);
            this.radioButton_9.setMarginRight(1);
            this.radioButton_9.setLabel(this.tr("do"));
            return this.radioButton_9;
            
        }
        
        ,create_scrollArea: function create_scrollArea() {
            this.scrollArea = new qx.ui.container.Scroll();
            this.scrollArea.setMarginBottom(1);
            this.scrollArea.setMarginTop(1);
            this.scrollArea.setMarginLeft(1);
            this.scrollArea.setMarginRight(1);
            this.scrollArea.add(this.create_scrollAreaWidgetContents(), {left: 0,top: 0});
            return this.scrollArea;
            
        }
        
        ,create_scrollAreaWidgetContents: function create_scrollAreaWidgetContents() {
            this.scrollAreaWidgetContents = new qx.ui.container.Composite();
            this.scrollAreaWidgetContents.setWidth(569);
            this.scrollAreaWidgetContents.setHeight(463);
            this.scrollAreaWidgetContents.setMarginBottom(1);
            this.scrollAreaWidgetContents.setMarginTop(1);
            this.scrollAreaWidgetContents.setMarginLeft(1);
            this.scrollAreaWidgetContents.setMarginRight(1);
            this.scrollAreaWidgetContents.setLayout(this.create_verticalLayout_2());
            this.scrollAreaWidgetContents.add(this.create_groupBox_2(), {flex: 1});
            return this.scrollAreaWidgetContents;
            
        }
        
        ,create_scrollAreaWidgetContents_2: function create_scrollAreaWidgetContents_2() {
            this.scrollAreaWidgetContents_2 = new qx.ui.container.Composite();
            this.scrollAreaWidgetContents_2.setWidth(431);
            this.scrollAreaWidgetContents_2.setHeight(355);
            this.scrollAreaWidgetContents_2.setMarginBottom(1);
            this.scrollAreaWidgetContents_2.setMarginTop(1);
            this.scrollAreaWidgetContents_2.setMarginLeft(1);
            this.scrollAreaWidgetContents_2.setMarginRight(1);
            this.scrollAreaWidgetContents_2.setLayout(this.create_verticalLayout_5());
            this.scrollAreaWidgetContents_2.add(this.create_groupBox_3(), {flex: 1});
            return this.scrollAreaWidgetContents_2;
            
        }
        
        ,create_scrollArea_2: function create_scrollArea_2() {
            this.scrollArea_2 = new qx.ui.container.Scroll();
            this.scrollArea_2.setMarginBottom(1);
            this.scrollArea_2.setMarginTop(1);
            this.scrollArea_2.setMarginLeft(1);
            this.scrollArea_2.setMarginRight(1);
            this.scrollArea_2.add(this.create_scrollAreaWidgetContents_2(), {left: 0,top: 0});
            return this.scrollArea_2;
            
        }
        
        ,create_spinBox: function create_spinBox() {
            this.spinBox = new qx.ui.form.Spinner();
            this.spinBox.setMarginBottom(1);
            this.spinBox.setMarginTop(1);
            this.spinBox.setMarginLeft(1);
            this.spinBox.setMarginRight(1);
            this.spinBox.setValue(55);
            this.spinBox.setMax(88);
            this.spinBox.setMargin(1);
            return this.spinBox;
            
        }
        
        ,create_spinBox_2: function create_spinBox_2() {
            this.spinBox_2 = new qx.ui.form.Spinner();
            this.spinBox_2.setMarginBottom(1);
            this.spinBox_2.setMarginTop(1);
            this.spinBox_2.setMarginLeft(1);
            this.spinBox_2.setMarginRight(1);
            this.spinBox_2.setValue(55);
            this.spinBox_2.setMax(88);
            this.spinBox_2.setMargin(1);
            return this.spinBox_2;
            
        }
        
        ,create_tab: function create_tab() {
            this.tab = new qx.ui.tabview.Page();
            this.tab.setMarginBottom(1);
            this.tab.setMarginTop(1);
            this.tab.setMarginLeft(1);
            this.tab.setMarginRight(1);
            this.tab.setLayout(this.create_horizontalLayout_6());
            this.tab.add(this.create_groupBox(), {flex: 1});
            this.tab.setLabel(this.tr("Tab 1"));
            return this.tab;
            
        }
        
        ,create_tabWidget: function create_tabWidget() {
            this.tabWidget = new qx.ui.tabview.TabView();
            this.tabWidget.setMaxWidth(1200);
            this.tabWidget.setMarginBottom(1);
            this.tabWidget.setMarginTop(1);
            this.tabWidget.setMarginLeft(1);
            this.tabWidget.setMarginRight(1);
            this.tabWidget.add(this.create_tab(), {left: 0,top: 0});
            this.tabWidget.add(this.create_tab_2(), {left: 0,top: 0});
            this.tabWidget.add(this.create_tab_3(), {left: 0,top: 0});
            return this.tabWidget;
            
        }
        
        ,create_tabWidget_2: function create_tabWidget_2() {
            this.tabWidget_2 = new qx.ui.tabview.TabView();
            this.tabWidget_2.setMarginBottom(1);
            this.tabWidget_2.setMarginTop(1);
            this.tabWidget_2.setMarginLeft(1);
            this.tabWidget_2.setMarginRight(1);
            this.tabWidget_2.add(this.create_tab_4(), {left: 0,top: 0});
            this.tabWidget_2.add(this.create_tab_5(), {left: 0,top: 0});
            return this.tabWidget_2;
            
        }
        
        ,create_tab_2: function create_tab_2() {
            this.tab_2 = new qx.ui.tabview.Page();
            this.tab_2.setMarginBottom(1);
            this.tab_2.setMarginTop(1);
            this.tab_2.setMarginLeft(1);
            this.tab_2.setMarginRight(1);
            this.tab_2.setLayout(this.create_tab_2_il());
            this.tab_2.add(this.create_checkBox(), {left: 180,top: 180});
            this.tab_2.add(this.create_radioButton_5(), {left: 130,top: 290});
            this.tab_2.add(this.create_pushButton(), {left: 180,top: 120});
            this.tab_2.setLabel(this.tr("Tab 2"));
            return this.tab_2;
            
        }
        
        ,create_tab_2_il: function create_tab_2_il() {
            this.tab_2_il = new qx.ui.layout.Canvas();
            return this.tab_2_il;
            
        }
        
        ,create_tab_3: function create_tab_3() {
            this.tab_3 = new qx.ui.tabview.Page();
            this.tab_3.setMarginBottom(1);
            this.tab_3.setMarginTop(1);
            this.tab_3.setMarginLeft(1);
            this.tab_3.setMarginRight(1);
            this.tab_3.setLayout(this.create_verticalLayout());
            this.tab_3.add(this.create_scrollArea(), {flex: 1});
            this.tab_3.setLabel(this.tr("Page"));
            return this.tab_3;
            
        }
        
        ,create_tab_4: function create_tab_4() {
            this.tab_4 = new qx.ui.tabview.Page();
            this.tab_4.setMarginBottom(1);
            this.tab_4.setMarginTop(1);
            this.tab_4.setMarginLeft(1);
            this.tab_4.setMarginRight(1);
            this.tab_4.setLayout(this.create_verticalLayout_4());
            this.tab_4.add(this.create_formLayout_implicit_container(), {flex: 1});
            this.tab_4.setLabel(this.tr("Tab 1"));
            return this.tab_4;
            
        }
        
        ,create_tab_5: function create_tab_5() {
            this.tab_5 = new qx.ui.tabview.Page();
            this.tab_5.setMarginBottom(1);
            this.tab_5.setMarginTop(1);
            this.tab_5.setMarginLeft(1);
            this.tab_5.setMarginRight(1);
            this.tab_5.setLayout(this.create_verticalLayout_6());
            this.tab_5.add(this.create_scrollArea_2(), {flex: 0});
            this.tab_5.setLabel(this.tr("Tab 2"));
            return this.tab_5;
            
        }
        
        ,create_verticalLayout: function create_verticalLayout() {
            this.verticalLayout = new qx.ui.layout.VBox();
            return this.verticalLayout;
            
        }
        
        ,create_verticalLayout_2: function create_verticalLayout_2() {
            this.verticalLayout_2 = new qx.ui.layout.VBox();
            return this.verticalLayout_2;
            
        }
        
        ,create_verticalLayout_3: function create_verticalLayout_3() {
            this.verticalLayout_3 = new qx.ui.layout.VBox();
            return this.verticalLayout_3;
            
        }
        
        ,create_verticalLayout_4: function create_verticalLayout_4() {
            this.verticalLayout_4 = new qx.ui.layout.VBox();
            return this.verticalLayout_4;
            
        }
        
        ,create_verticalLayout_5: function create_verticalLayout_5() {
            this.verticalLayout_5 = new qx.ui.layout.VBox();
            return this.verticalLayout_5;
            
        }
        
        ,create_verticalLayout_6: function create_verticalLayout_6() {
            this.verticalLayout_6 = new qx.ui.layout.VBox();
            return this.verticalLayout_6;
            
        }
        
        ,dateEdit: null
        ,dateEdit_2: null
        ,edtAnswerBack: null
        ,edtAnswerBack_2: null
        ,edtCompany: null
        ,edtCompany_2: null
        ,edtDNID: null
        ,edtDNID_2: null
        ,edtEmail: null
        ,edtEmail_2: null
        ,edtIOWN: null
        ,edtIOWN_2: null
        ,edtMN: null
        ,edtMN_2: null
        ,edtName: null
        ,edtName_2: null
        ,edtTerminalSN: null
        ,edtTerminalSN_2: null
        ,formLayout: null
        ,formLayout_implicit_container: null
        ,gridLayout: null
        ,gridLayout_2: null
        ,gridLayout_2_implicit_container: null
        ,gridLayout_3: null
        ,groupBox: null
        ,groupBox_2: null
        ,groupBox_3: null
        ,horizontalLayout: null
        ,horizontalLayout_10: null
        ,horizontalLayout_10_implicit_container: null
        ,horizontalLayout_2: null
        ,horizontalLayout_2_implicit_container: null
        ,horizontalLayout_3: null
        ,horizontalLayout_4: null
        ,horizontalLayout_4_implicit_container: null
        ,horizontalLayout_5: null
        ,horizontalLayout_5_implicit_container: null
        ,horizontalLayout_6: null
        ,horizontalLayout_7: null
        ,horizontalLayout_7_implicit_container: null
        ,horizontalLayout_8: null
        ,horizontalLayout_8_implicit_container: null
        ,horizontalLayout_9: null
        ,horizontalLayout_9_implicit_container: null
        ,horizontalLayout_implicit_container: null
        ,horizontalSpacer: null
        ,horizontalSpacer_2: null
        ,label: null
        ,label_2: null
        ,label_3: null
        ,lblAnswerBack: null
        ,lblAnswerBack_2: null
        ,lblCompany: null
        ,lblCompany_2: null
        ,lblDNID: null
        ,lblDNID_2: null
        ,lblDetails: null
        ,lblDetails_2: null
        ,lblEmail: null
        ,lblEmail_2: null
        ,lblIOWN: null
        ,lblIOWN_2: null
        ,lblIdentifers: null
        ,lblIdentifers_2: null
        ,lblInterval: null
        ,lblInterval_2: null
        ,lblMN: null
        ,lblMN_2: null
        ,lblName: null
        ,lblName_2: null
        ,lblSubAddress: null
        ,lblSubAddress_2: null
        ,lblTerminalSN: null
        ,lblTerminalSN_2: null
        ,lblTest: null
        ,lblTest_2: null
        ,lblTrackingMethod: null
        ,lblTrackingMethod_2: null
        ,pushButton: null
        ,pushButton_2: null
        ,pushButton_3: null
        ,radioButton: null
        ,radioButton_2: null
        ,radioButton_3: null
        ,radioButton_4: null
        ,radioButton_5: null
        ,radioButton_6: null
        ,radioButton_7: null
        ,radioButton_8: null
        ,radioButton_9: null
        ,scrollArea: null
        ,scrollAreaWidgetContents: null
        ,scrollAreaWidgetContents_2: null
        ,scrollArea_2: null
        ,spinBox: null
        ,spinBox_2: null
        ,tab: null
        ,tabWidget: null
        ,tabWidget_2: null
        ,tab_2: null
        ,tab_2_il: null
        ,tab_3: null
        ,tab_4: null
        ,tab_5: null
        ,verticalLayout: null
        ,verticalLayout_2: null
        ,verticalLayout_3: null
        ,verticalLayout_4: null
        ,verticalLayout_5: null
        ,verticalLayout_6: null
    }
    
    ,properties:  {
        widget:  {
            check: "qx.ui.container.Composite"
        }
        
    }
    
}
);
