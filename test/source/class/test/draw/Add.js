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
            var retval  =  this.Add;
            retval.setHeight(484);
            retval.setWidth(629);
            retval.setMargin(1);
            retval.setLayout(this.create___lv());
            retval.add(this.create_centralwidget(), {flex: 1});
            return retval;
            
        }
        
        ,create_HLTest: function create_HLTest() {
            this.HLTest = new qx.ui.layout.HBox();
            var retval  =  this.HLTest;
            return retval;
            
        }
        
        ,create_HLTest_2: function create_HLTest_2() {
            this.HLTest_2 = new qx.ui.layout.HBox();
            var retval  =  this.HLTest_2;
            return retval;
            
        }
        
        ,create_HLTest_2_implicit_container: function create_HLTest_2_implicit_container() {
            this.HLTest_2_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.HLTest_2_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_HLTest_2());
            retval.add(this.create_chkLRITTest_2(), {flex: 1});
            retval.add(this.create_radioButton_6(), {flex: 1});
            retval.add(this.create_radioButton_7(), {flex: 1});
            return retval;
            
        }
        
        ,create_HLTest_implicit_container: function create_HLTest_implicit_container() {
            this.HLTest_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.HLTest_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_HLTest());
            retval.add(this.create_chkLRITTest(), {flex: 1});
            retval.add(this.create_radioButton_2(), {flex: 1});
            retval.add(this.create_radioButton(), {flex: 1});
            return retval;
            
        }
        
        ,create_HLTrackingMethod: function create_HLTrackingMethod() {
            this.HLTrackingMethod = new qx.ui.layout.HBox();
            var retval  =  this.HLTrackingMethod;
            return retval;
            
        }
        
        ,create_HLTrackingMethod_2: function create_HLTrackingMethod_2() {
            this.HLTrackingMethod_2 = new qx.ui.layout.HBox();
            var retval  =  this.HLTrackingMethod_2;
            return retval;
            
        }
        
        ,create_HLTrackingMethod_2_implicit_container: function create_HLTrackingMethod_2_implicit_container() {
            this.HLTrackingMethod_2_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.HLTrackingMethod_2_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_HLTrackingMethod_2());
            retval.add(this.create_comboTrackingMethod_2(), {flex: 1});
            retval.add(this.create_horizontalSpacer(), {flex: 1});
            retval.add(this.create_lblInterval_2(), {flex: 1});
            retval.add(this.create_comboInterval_2(), {flex: 1});
            retval.add(this.create_horizontalSpacer_2(), {flex: 1});
            return retval;
            
        }
        
        ,create_HLTrackingMethod_implicit_container: function create_HLTrackingMethod_implicit_container() {
            this.HLTrackingMethod_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.HLTrackingMethod_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_HLTrackingMethod());
            retval.add(this.create_comboTrackingMethod(), {flex: 1});
            retval.add(this.create_horizontalSpacer(), {flex: 1});
            retval.add(this.create_lblInterval(), {flex: 1});
            retval.add(this.create_comboInterval(), {flex: 1});
            retval.add(this.create_horizontalSpacer_2(), {flex: 1});
            return retval;
            
        }
        
        ,create_VLEmail: function create_VLEmail() {
            this.VLEmail = new qx.ui.layout.VBox();
            var retval  =  this.VLEmail;
            return retval;
            
        }
        
        ,create_VLEmail_2: function create_VLEmail_2() {
            this.VLEmail_2 = new qx.ui.layout.VBox();
            var retval  =  this.VLEmail_2;
            return retval;
            
        }
        
        ,create_VLEmail_2_implicit_container: function create_VLEmail_2_implicit_container() {
            this.VLEmail_2_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.VLEmail_2_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_VLEmail_2());
            retval.add(this.create_edtEmail_2(), {flex: 1});
            retval.add(this.create_horizontalLayout_10_implicit_container(), {flex: 1});
            return retval;
            
        }
        
        ,create_VLEmail_implicit_container: function create_VLEmail_implicit_container() {
            this.VLEmail_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.VLEmail_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_VLEmail());
            retval.add(this.create_edtEmail(), {flex: 1});
            retval.add(this.create_horizontalLayout_5_implicit_container(), {flex: 1});
            return retval;
            
        }
        
        ,create___lv: function create___lv() {
            this.__lv = new qx.ui.layout.VBox();
            var retval  =  this.__lv;
            return retval;
            
        }
        
        ,create_centralwidget: function create_centralwidget() {
            this.centralwidget = new qx.ui.container.Composite();
            var retval  =  this.centralwidget;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_3());
            retval.add(this.create_tabWidget(), {flex: 1});
            return retval;
            
        }
        
        ,create_checkBox: function create_checkBox() {
            this.checkBox = new qx.ui.form.CheckBox();
            var retval  =  this.checkBox;
            retval.setHeight(21);
            retval.setWidth(81);
            retval.setLabel(this.tr("CheckBox"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_chkEmail: function create_chkEmail() {
            this.chkEmail = new qx.ui.form.CheckBox();
            var retval  =  this.chkEmail;
            retval.setValue(true);
            retval.setLabel(this.tr("No Email"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_chkEmail_2: function create_chkEmail_2() {
            this.chkEmail_2 = new qx.ui.form.CheckBox();
            var retval  =  this.chkEmail_2;
            retval.setValue(true);
            retval.setLabel(this.tr("No Email"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_chkLRITTest: function create_chkLRITTest() {
            this.chkLRITTest = new qx.ui.form.CheckBox();
            var retval  =  this.chkLRITTest;
            retval.setLabel(this.tr("Start"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_chkLRITTest_2: function create_chkLRITTest_2() {
            this.chkLRITTest_2 = new qx.ui.form.CheckBox();
            var retval  =  this.chkLRITTest_2;
            retval.setLabel(this.tr("Start"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_comboInterval: function create_comboInterval() {
            this.comboInterval = new qx.ui.form.SelectBox();
            var retval  =  this.comboInterval;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_comboInterval_2: function create_comboInterval_2() {
            this.comboInterval_2 = new qx.ui.form.SelectBox();
            var retval  =  this.comboInterval_2;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_comboSubAddress: function create_comboSubAddress() {
            this.comboSubAddress = new qx.ui.form.SelectBox();
            var retval  =  this.comboSubAddress;
            retval.setWidth(80);
            retval.setMargin(1);
            retval.setMinWidth(80);
            retval.setAllowGrowY(false);
            retval.add(new qx.ui.form.ListItem("1",null,null));
            retval.add(new qx.ui.form.ListItem("2",null,null));
            retval.add(new qx.ui.form.ListItem("3",null,null));
            retval.add(new qx.ui.form.ListItem("4",null,null));
            retval.add(new qx.ui.form.ListItem("5",null,null));
            retval.add(new qx.ui.form.ListItem("6",null,null));
            retval.add(new qx.ui.form.ListItem("7",null,null));
            return retval;
            
        }
        
        ,create_comboSubAddress_2: function create_comboSubAddress_2() {
            this.comboSubAddress_2 = new qx.ui.form.SelectBox();
            var retval  =  this.comboSubAddress_2;
            retval.setWidth(80);
            retval.setMargin(1);
            retval.setMinWidth(80);
            retval.setAllowGrowY(false);
            retval.add(new qx.ui.form.ListItem("1",null,null));
            retval.add(new qx.ui.form.ListItem("2",null,null));
            retval.add(new qx.ui.form.ListItem("3",null,null));
            retval.add(new qx.ui.form.ListItem("4",null,null));
            retval.add(new qx.ui.form.ListItem("5",null,null));
            retval.add(new qx.ui.form.ListItem("6",null,null));
            retval.add(new qx.ui.form.ListItem("7",null,null));
            return retval;
            
        }
        
        ,create_comboTrackingMethod: function create_comboTrackingMethod() {
            this.comboTrackingMethod = new qx.ui.form.SelectBox();
            var retval  =  this.comboTrackingMethod;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_comboTrackingMethod_2: function create_comboTrackingMethod_2() {
            this.comboTrackingMethod_2 = new qx.ui.form.SelectBox();
            var retval  =  this.comboTrackingMethod_2;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_dateEdit: function create_dateEdit() {
            this.dateEdit = new qx.ui.form.DateField();
            var retval  =  this.dateEdit;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_dateEdit_2: function create_dateEdit_2() {
            this.dateEdit_2 = new qx.ui.form.DateField();
            var retval  =  this.dateEdit_2;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtAnswerBack: function create_edtAnswerBack() {
            this.edtAnswerBack = new qx.ui.form.TextField();
            var retval  =  this.edtAnswerBack;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtAnswerBack_2: function create_edtAnswerBack_2() {
            this.edtAnswerBack_2 = new qx.ui.form.TextField();
            var retval  =  this.edtAnswerBack_2;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtCompany: function create_edtCompany() {
            this.edtCompany = new qx.ui.form.TextField();
            var retval  =  this.edtCompany;
            retval.setWidth(300);
            retval.setMaxWidth(5);
            retval.setMargin(1);
            retval.setMinWidth(300);
            return retval;
            
        }
        
        ,create_edtCompany_2: function create_edtCompany_2() {
            this.edtCompany_2 = new qx.ui.form.TextField();
            var retval  =  this.edtCompany_2;
            retval.setMargin(1);
            retval.setAllowGrowX(false);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_edtDNID: function create_edtDNID() {
            this.edtDNID = new qx.ui.form.TextField();
            var retval  =  this.edtDNID;
            retval.setWidth(50);
            retval.setMargin(1);
            retval.setMinWidth(50);
            return retval;
            
        }
        
        ,create_edtDNID_2: function create_edtDNID_2() {
            this.edtDNID_2 = new qx.ui.form.TextField();
            var retval  =  this.edtDNID_2;
            retval.setWidth(50);
            retval.setMargin(1);
            retval.setMinWidth(50);
            return retval;
            
        }
        
        ,create_edtEmail: function create_edtEmail() {
            this.edtEmail = new qx.ui.form.TextField();
            var retval  =  this.edtEmail;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtEmail_2: function create_edtEmail_2() {
            this.edtEmail_2 = new qx.ui.form.TextField();
            var retval  =  this.edtEmail_2;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtIOWN: function create_edtIOWN() {
            this.edtIOWN = new qx.ui.form.TextField();
            var retval  =  this.edtIOWN;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtIOWN_2: function create_edtIOWN_2() {
            this.edtIOWN_2 = new qx.ui.form.TextField();
            var retval  =  this.edtIOWN_2;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtMN: function create_edtMN() {
            this.edtMN = new qx.ui.form.TextField();
            var retval  =  this.edtMN;
            retval.setWidth(30);
            retval.setMargin(1);
            retval.setMinWidth(30);
            return retval;
            
        }
        
        ,create_edtMN_2: function create_edtMN_2() {
            this.edtMN_2 = new qx.ui.form.TextField();
            var retval  =  this.edtMN_2;
            retval.setWidth(30);
            retval.setMargin(1);
            retval.setMinWidth(30);
            return retval;
            
        }
        
        ,create_edtName: function create_edtName() {
            this.edtName = new qx.ui.form.TextField();
            var retval  =  this.edtName;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtName_2: function create_edtName_2() {
            this.edtName_2 = new qx.ui.form.TextField();
            var retval  =  this.edtName_2;
            retval.setWidth(300);
            retval.setMaxWidth(400);
            retval.setMargin(1);
            retval.setMinWidth(300);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_edtTerminalSN: function create_edtTerminalSN() {
            this.edtTerminalSN = new qx.ui.form.TextField();
            var retval  =  this.edtTerminalSN;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_edtTerminalSN_2: function create_edtTerminalSN_2() {
            this.edtTerminalSN_2 = new qx.ui.form.TextField();
            var retval  =  this.edtTerminalSN_2;
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_formLayout: function create_formLayout() {
            this.formLayout = new qx.ui.layout.Grid();
            var retval  =  this.formLayout;
            retval.setRowFlex(0,1);
            retval.setRowFlex(1,1);
            retval.setRowFlex(2,1);
            retval.setColumnFlex(0,1);
            retval.setColumnFlex(1,1);
            return retval;
            
        }
        
        ,create_formLayout_implicit_container: function create_formLayout_implicit_container() {
            this.formLayout_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.formLayout_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_formLayout());
            retval.add(this.create_pushButton_3(), {column: 0,row: 0});
            retval.add(this.create_label_2(), {column: 1,row: 0});
            return retval;
            
        }
        
        ,create_gridLayout: function create_gridLayout() {
            this.gridLayout = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout;
            retval.setRowFlex(0,1);
            retval.setRowFlex(1,1);
            retval.setRowFlex(2,1);
            retval.setRowFlex(3,1);
            retval.setRowFlex(4,1);
            retval.setRowFlex(5,1);
            retval.setRowFlex(6,1);
            retval.setRowFlex(7,1);
            retval.setRowFlex(8,1);
            retval.setColumnFlex(0,1);
            retval.setColumnFlex(2,1);
            return retval;
            
        }
        
        ,create_gridLayout_2: function create_gridLayout_2() {
            this.gridLayout_2 = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout_2;
            retval.setRowFlex(0,1);
            retval.setColumnFlex(0,1);
            retval.setColumnFlex(1,1);
            return retval;
            
        }
        
        ,create_gridLayout_2_implicit_container: function create_gridLayout_2_implicit_container() {
            this.gridLayout_2_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.gridLayout_2_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_gridLayout_2());
            retval.add(this.create_pushButton_2(), {column: 0,row: 0});
            retval.add(this.create_tabWidget_2(), {column: 1,row: 0});
            return retval;
            
        }
        
        ,create_gridLayout_3: function create_gridLayout_3() {
            this.gridLayout_3 = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout_3;
            retval.setRowFlex(1,1);
            retval.setRowFlex(2,1);
            retval.setRowFlex(3,1);
            retval.setRowFlex(4,1);
            retval.setRowFlex(5,1);
            retval.setRowFlex(6,1);
            retval.setRowFlex(7,1);
            retval.setRowFlex(8,1);
            retval.setColumnFlex(0,1);
            return retval;
            
        }
        
        ,create_groupBox: function create_groupBox() {
            this.groupBox = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox;
            retval.setWidth(400);
            retval.setMaxWidth(600);
            retval.setLegend(this.tr("Add"));
            retval.setMargin(1);
            retval.setMinWidth(400);
            retval.setLayout(this.create_gridLayout());
            retval.add(this.create_lblCompany(), {column: 0,row: 0});
            retval.add(this.create_edtCompany(), {column: 2,row: 0});
            retval.add(this.create_lblName(), {column: 0,row: 1});
            retval.add(this.create_edtName(), {column: 2,row: 1});
            retval.add(this.create_lblIdentifers(), {column: 0,row: 2});
            retval.add(this.create_horizontalLayout_implicit_container(), {column: 2,row: 2});
            retval.add(this.create_lblDetails(), {column: 0,row: 3});
            retval.add(this.create_horizontalLayout_2_implicit_container(), {column: 2,row: 3});
            retval.add(this.create_lblEmail(), {column: 0,row: 4});
            retval.add(this.create_lblTrackingMethod(), {column: 0,row: 5});
            retval.add(this.create_HLTrackingMethod_implicit_container(), {column: 2,row: 5});
            retval.add(this.create_lblTest(), {column: 0,row: 6});
            retval.add(this.create_HLTest_implicit_container(), {column: 2,row: 6});
            retval.add(this.create_lblAnswerBack(), {column: 0,row: 7});
            retval.add(this.create_edtAnswerBack(), {column: 2,row: 7});
            retval.add(this.create_label(), {column: 0,row: 8});
            retval.add(this.create_horizontalLayout_4_implicit_container(), {column: 2,row: 8});
            retval.add(this.create_VLEmail_implicit_container(), {column: 2,row: 4});
            return retval;
            
        }
        
        ,create_groupBox_2: function create_groupBox_2() {
            this.groupBox_2 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_2;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_3());
            retval.add(this.create_gridLayout_2_implicit_container(), {flex: 1});
            return retval;
            
        }
        
        ,create_groupBox_3: function create_groupBox_3() {
            this.groupBox_3 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_3;
            retval.setLegend(this.tr("Add"));
            retval.setMargin(1);
            retval.setLayout(this.create_gridLayout_3());
            retval.add(this.create_lblCompany_2(), {column: 0,row: 0});
            retval.add(this.create_edtCompany_2(), {column: 2,row: 0});
            retval.add(this.create_lblName_2(), {column: 0,row: 1});
            retval.add(this.create_edtName_2(), {column: 2,row: 1});
            retval.add(this.create_lblIdentifers_2(), {column: 0,row: 2});
            retval.add(this.create_horizontalLayout_7_implicit_container(), {column: 2,row: 2});
            retval.add(this.create_lblDetails_2(), {column: 0,row: 3});
            retval.add(this.create_horizontalLayout_8_implicit_container(), {column: 2,row: 3});
            retval.add(this.create_lblEmail_2(), {column: 0,row: 4});
            retval.add(this.create_lblTrackingMethod_2(), {column: 0,row: 5});
            retval.add(this.create_HLTrackingMethod_2_implicit_container(), {column: 2,row: 5});
            retval.add(this.create_lblTest_2(), {column: 0,row: 6});
            retval.add(this.create_HLTest_2_implicit_container(), {column: 2,row: 6});
            retval.add(this.create_lblAnswerBack_2(), {column: 0,row: 7});
            retval.add(this.create_edtAnswerBack_2(), {column: 2,row: 7});
            retval.add(this.create_label_3(), {column: 0,row: 8});
            retval.add(this.create_horizontalLayout_9_implicit_container(), {column: 2,row: 8});
            retval.add(this.create_VLEmail_2_implicit_container(), {column: 2,row: 4});
            return retval;
            
        }
        
        ,create_horizontalLayout: function create_horizontalLayout() {
            this.horizontalLayout = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout;
            return retval;
            
        }
        
        ,create_horizontalLayout_10: function create_horizontalLayout_10() {
            this.horizontalLayout_10 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_10;
            return retval;
            
        }
        
        ,create_horizontalLayout_10_implicit_container: function create_horizontalLayout_10_implicit_container() {
            this.horizontalLayout_10_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_10_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_10());
            retval.add(this.create_radioButton_8(), {flex: 1});
            retval.add(this.create_chkEmail_2(), {flex: 1});
            retval.add(this.create_radioButton_9(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_2: function create_horizontalLayout_2() {
            this.horizontalLayout_2 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_2;
            return retval;
            
        }
        
        ,create_horizontalLayout_2_implicit_container: function create_horizontalLayout_2_implicit_container() {
            this.horizontalLayout_2_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_2_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_2());
            retval.add(this.create_lblDNID(), {flex: 1});
            retval.add(this.create_edtDNID(), {flex: 1});
            retval.add(this.create_lblMN(), {flex: 1});
            retval.add(this.create_edtMN(), {flex: 1});
            retval.add(this.create_lblSubAddress(), {flex: 1});
            retval.add(this.create_comboSubAddress(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_3: function create_horizontalLayout_3() {
            this.horizontalLayout_3 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_3;
            return retval;
            
        }
        
        ,create_horizontalLayout_4: function create_horizontalLayout_4() {
            this.horizontalLayout_4 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_4;
            return retval;
            
        }
        
        ,create_horizontalLayout_4_implicit_container: function create_horizontalLayout_4_implicit_container() {
            this.horizontalLayout_4_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_4_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_4());
            retval.add(this.create_dateEdit(), {flex: 1});
            retval.add(this.create_spinBox(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_5: function create_horizontalLayout_5() {
            this.horizontalLayout_5 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_5;
            return retval;
            
        }
        
        ,create_horizontalLayout_5_implicit_container: function create_horizontalLayout_5_implicit_container() {
            this.horizontalLayout_5_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_5_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_5());
            retval.add(this.create_radioButton_4(), {flex: 1});
            retval.add(this.create_chkEmail(), {flex: 1});
            retval.add(this.create_radioButton_3(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_6: function create_horizontalLayout_6() {
            this.horizontalLayout_6 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_6;
            return retval;
            
        }
        
        ,create_horizontalLayout_7: function create_horizontalLayout_7() {
            this.horizontalLayout_7 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_7;
            return retval;
            
        }
        
        ,create_horizontalLayout_7_implicit_container: function create_horizontalLayout_7_implicit_container() {
            this.horizontalLayout_7_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_7_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_7());
            retval.add(this.create_lblIOWN_2(), {flex: 1});
            retval.add(this.create_edtIOWN_2(), {flex: 1});
            retval.add(this.create_lblTerminalSN_2(), {flex: 1});
            retval.add(this.create_edtTerminalSN_2(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_8: function create_horizontalLayout_8() {
            this.horizontalLayout_8 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_8;
            return retval;
            
        }
        
        ,create_horizontalLayout_8_implicit_container: function create_horizontalLayout_8_implicit_container() {
            this.horizontalLayout_8_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_8_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_8());
            retval.add(this.create_lblDNID_2(), {flex: 1});
            retval.add(this.create_edtDNID_2(), {flex: 1});
            retval.add(this.create_lblMN_2(), {flex: 1});
            retval.add(this.create_edtMN_2(), {flex: 1});
            retval.add(this.create_lblSubAddress_2(), {flex: 1});
            retval.add(this.create_comboSubAddress_2(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_9: function create_horizontalLayout_9() {
            this.horizontalLayout_9 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_9;
            return retval;
            
        }
        
        ,create_horizontalLayout_9_implicit_container: function create_horizontalLayout_9_implicit_container() {
            this.horizontalLayout_9_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_9_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_9());
            retval.add(this.create_spinBox_2(), {flex: 1});
            retval.add(this.create_dateEdit_2(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalLayout_implicit_container: function create_horizontalLayout_implicit_container() {
            this.horizontalLayout_implicit_container = new qx.ui.container.Composite();
            var retval  =  this.horizontalLayout_implicit_container;
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout());
            retval.add(this.create_lblIOWN(), {flex: 1});
            retval.add(this.create_edtIOWN(), {flex: 1});
            retval.add(this.create_lblTerminalSN(), {flex: 1});
            retval.add(this.create_edtTerminalSN(), {flex: 1});
            return retval;
            
        }
        
        ,create_horizontalSpacer: function create_horizontalSpacer() {
            this.horizontalSpacer = new qx.ui.core.Spacer();
            var retval  =  this.horizontalSpacer;
            retval.setHeight(20);
            retval.setWidth(40);
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_horizontalSpacer_2: function create_horizontalSpacer_2() {
            this.horizontalSpacer_2 = new qx.ui.core.Spacer();
            var retval  =  this.horizontalSpacer_2;
            retval.setHeight(20);
            retval.setWidth(40);
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_label: function create_label() {
            this.label = new qx.ui.basic.Label();
            var retval  =  this.label;
            retval.setValue(this.tr("Date & Count: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_label_2: function create_label_2() {
            this.label_2 = new qx.ui.basic.Label();
            var retval  =  this.label_2;
            retval.setValue(this.tr("TextLabel"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_label_3: function create_label_3() {
            this.label_3 = new qx.ui.basic.Label();
            var retval  =  this.label_3;
            retval.setValue(this.tr("Time & Count: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblAnswerBack: function create_lblAnswerBack() {
            this.lblAnswerBack = new qx.ui.basic.Label();
            var retval  =  this.lblAnswerBack;
            retval.setValue(this.tr("Answer Back : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblAnswerBack_2: function create_lblAnswerBack_2() {
            this.lblAnswerBack_2 = new qx.ui.basic.Label();
            var retval  =  this.lblAnswerBack_2;
            retval.setValue(this.tr("Answer Back : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblCompany: function create_lblCompany() {
            this.lblCompany = new qx.ui.basic.Label();
            var retval  =  this.lblCompany;
            retval.setValue(this.tr("Company : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblCompany_2: function create_lblCompany_2() {
            this.lblCompany_2 = new qx.ui.basic.Label();
            var retval  =  this.lblCompany_2;
            retval.setValue(this.tr("Company : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblDNID: function create_lblDNID() {
            this.lblDNID = new qx.ui.basic.Label();
            var retval  =  this.lblDNID;
            retval.setValue(this.tr("ABC: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblDNID_2: function create_lblDNID_2() {
            this.lblDNID_2 = new qx.ui.basic.Label();
            var retval  =  this.lblDNID_2;
            retval.setValue(this.tr("ABC: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblDetails: function create_lblDetails() {
            this.lblDetails = new qx.ui.basic.Label();
            var retval  =  this.lblDetails;
            retval.setValue(this.tr("Details: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblDetails_2: function create_lblDetails_2() {
            this.lblDetails_2 = new qx.ui.basic.Label();
            var retval  =  this.lblDetails_2;
            retval.setValue(this.tr("Details: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblEmail: function create_lblEmail() {
            this.lblEmail = new qx.ui.basic.Label();
            var retval  =  this.lblEmail;
            retval.setValue(this.tr("Email: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblEmail_2: function create_lblEmail_2() {
            this.lblEmail_2 = new qx.ui.basic.Label();
            var retval  =  this.lblEmail_2;
            retval.setValue(this.tr("Email: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblIOWN: function create_lblIOWN() {
            this.lblIOWN = new qx.ui.basic.Label();
            var retval  =  this.lblIOWN;
            retval.setValue(this.tr("OWN: : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblIOWN_2: function create_lblIOWN_2() {
            this.lblIOWN_2 = new qx.ui.basic.Label();
            var retval  =  this.lblIOWN_2;
            retval.setValue(this.tr("OWN: : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblIdentifers: function create_lblIdentifers() {
            this.lblIdentifers = new qx.ui.basic.Label();
            var retval  =  this.lblIdentifers;
            retval.setValue(this.tr("Identifiers: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblIdentifers_2: function create_lblIdentifers_2() {
            this.lblIdentifers_2 = new qx.ui.basic.Label();
            var retval  =  this.lblIdentifers_2;
            retval.setValue(this.tr("Identifiers: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblInterval: function create_lblInterval() {
            this.lblInterval = new qx.ui.basic.Label();
            var retval  =  this.lblInterval;
            retval.setValue(this.tr("Interval"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblInterval_2: function create_lblInterval_2() {
            this.lblInterval_2 = new qx.ui.basic.Label();
            var retval  =  this.lblInterval_2;
            retval.setValue(this.tr("Interval"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblMN: function create_lblMN() {
            this.lblMN = new qx.ui.basic.Label();
            var retval  =  this.lblMN;
            retval.setValue(this.tr("MN: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblMN_2: function create_lblMN_2() {
            this.lblMN_2 = new qx.ui.basic.Label();
            var retval  =  this.lblMN_2;
            retval.setValue(this.tr("MN: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblName: function create_lblName() {
            this.lblName = new qx.ui.basic.Label();
            var retval  =  this.lblName;
            retval.setValue(this.tr("Name : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblName_2: function create_lblName_2() {
            this.lblName_2 = new qx.ui.basic.Label();
            var retval  =  this.lblName_2;
            retval.setValue(this.tr("Name : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblSubAddress: function create_lblSubAddress() {
            this.lblSubAddress = new qx.ui.basic.Label();
            var retval  =  this.lblSubAddress;
            retval.setValue(this.tr("SA"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblSubAddress_2: function create_lblSubAddress_2() {
            this.lblSubAddress_2 = new qx.ui.basic.Label();
            var retval  =  this.lblSubAddress_2;
            retval.setValue(this.tr("SA"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblTerminalSN: function create_lblTerminalSN() {
            this.lblTerminalSN = new qx.ui.basic.Label();
            var retval  =  this.lblTerminalSN;
            retval.setValue(this.tr("S/N: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblTerminalSN_2: function create_lblTerminalSN_2() {
            this.lblTerminalSN_2 = new qx.ui.basic.Label();
            var retval  =  this.lblTerminalSN_2;
            retval.setValue(this.tr("S/N: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblTest: function create_lblTest() {
            this.lblTest = new qx.ui.basic.Label();
            var retval  =  this.lblTest;
            retval.setValue(this.tr("BJ Test: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblTest_2: function create_lblTest_2() {
            this.lblTest_2 = new qx.ui.basic.Label();
            var retval  =  this.lblTest_2;
            retval.setValue(this.tr("BJ Test: "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblTrackingMethod: function create_lblTrackingMethod() {
            this.lblTrackingMethod = new qx.ui.basic.Label();
            var retval  =  this.lblTrackingMethod;
            retval.setValue(this.tr("Method : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_lblTrackingMethod_2: function create_lblTrackingMethod_2() {
            this.lblTrackingMethod_2 = new qx.ui.basic.Label();
            var retval  =  this.lblTrackingMethod_2;
            retval.setValue(this.tr("Method : "));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_pushButton: function create_pushButton() {
            this.pushButton = new qx.ui.form.Button();
            var retval  =  this.pushButton;
            retval.setHeight(26);
            retval.setWidth(75);
            retval.setLabel(this.tr("PushButton"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_pushButton_2: function create_pushButton_2() {
            this.pushButton_2 = new qx.ui.form.Button();
            var retval  =  this.pushButton_2;
            retval.setLabel(this.tr("PushButton"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_pushButton_3: function create_pushButton_3() {
            this.pushButton_3 = new qx.ui.form.Button();
            var retval  =  this.pushButton_3;
            retval.setLabel(this.tr("PushButton"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton: function create_radioButton() {
            this.radioButton = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton;
            retval.setLabel(this.tr("Later"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_2: function create_radioButton_2() {
            this.radioButton_2 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_2;
            retval.setLabel(this.tr("Now"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_3: function create_radioButton_3() {
            this.radioButton_3 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_3;
            retval.setLabel(this.tr("do"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_4: function create_radioButton_4() {
            this.radioButton_4 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_4;
            retval.setLabel(this.tr("don't"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_5: function create_radioButton_5() {
            this.radioButton_5 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_5;
            retval.setHeight(22);
            retval.setWidth(91);
            retval.setLabel(this.tr("RadioButton"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_6: function create_radioButton_6() {
            this.radioButton_6 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_6;
            retval.setLabel(this.tr("Now"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_7: function create_radioButton_7() {
            this.radioButton_7 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_7;
            retval.setLabel(this.tr("Later"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_8: function create_radioButton_8() {
            this.radioButton_8 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_8;
            retval.setLabel(this.tr("don't"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_radioButton_9: function create_radioButton_9() {
            this.radioButton_9 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_9;
            retval.setLabel(this.tr("do"));
            retval.setMargin(1);
            return retval;
            
        }
        
        ,create_scrollArea: function create_scrollArea() {
            this.scrollArea = new qx.ui.container.Scroll();
            var retval  =  this.scrollArea;
            retval.setMargin(1);
            retval.add(this.create_scrollAreaWidgetContents(), {left: 0,top: 0});
            return retval;
            
        }
        
        ,create_scrollAreaWidgetContents: function create_scrollAreaWidgetContents() {
            this.scrollAreaWidgetContents = new qx.ui.container.Composite();
            var retval  =  this.scrollAreaWidgetContents;
            retval.setHeight(478);
            retval.setWidth(569);
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_2());
            retval.add(this.create_groupBox_2(), {flex: 1});
            return retval;
            
        }
        
        ,create_scrollAreaWidgetContents_2: function create_scrollAreaWidgetContents_2() {
            this.scrollAreaWidgetContents_2 = new qx.ui.container.Composite();
            var retval  =  this.scrollAreaWidgetContents_2;
            retval.setHeight(366);
            retval.setWidth(438);
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_5());
            retval.add(this.create_groupBox_3(), {flex: 1});
            return retval;
            
        }
        
        ,create_scrollArea_2: function create_scrollArea_2() {
            this.scrollArea_2 = new qx.ui.container.Scroll();
            var retval  =  this.scrollArea_2;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            retval.add(this.create_scrollAreaWidgetContents_2(), {left: 0,top: -16});
            return retval;
            
        }
        
        ,create_spinBox: function create_spinBox() {
            this.spinBox = new qx.ui.form.Spinner();
            var retval  =  this.spinBox;
            retval.setMaximum(88);
            retval.setMinimum(44);
            retval.setSingleStep(4);
            retval.setValue(55);
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_spinBox_2: function create_spinBox_2() {
            this.spinBox_2 = new qx.ui.form.Spinner();
            var retval  =  this.spinBox_2;
            retval.setMaximum(88);
            retval.setMinimum(44);
            retval.setSingleStep(4);
            retval.setValue(55);
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;
            
        }
        
        ,create_tab: function create_tab() {
            this.tab = new qx.ui.tabview.Page();
            var retval  =  this.tab;
            retval.setLabel(this.tr("Tab 1"));
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_6());
            retval.add(this.create_groupBox(), {flex: 1});
            return retval;
            
        }
        
        ,create_tabWidget: function create_tabWidget() {
            this.tabWidget = new qx.ui.tabview.TabView();
            var retval  =  this.tabWidget;
            retval.setMaxWidth(1200);
            retval.setMargin(1);
            retval.add(this.create_tab());
            retval.add(this.create_tab_2());
            retval.add(this.create_tab_3());
            return retval;
            
        }
        
        ,create_tabWidget_2: function create_tabWidget_2() {
            this.tabWidget_2 = new qx.ui.tabview.TabView();
            var retval  =  this.tabWidget_2;
            retval.setMargin(1);
            retval.add(this.create_tab_4());
            retval.add(this.create_tab_5());
            return retval;
            
        }
        
        ,create_tab_2: function create_tab_2() {
            this.tab_2 = new qx.ui.tabview.Page();
            var retval  =  this.tab_2;
            retval.setLabel(this.tr("Tab 2"));
            retval.setMargin(1);
            retval.setLayout(this.create_tab_2_il());
            retval.add(this.create_checkBox(), {left: 180,top: 180});
            retval.add(this.create_radioButton_5(), {left: 130,top: 290});
            retval.add(this.create_pushButton(), {left: 180,top: 120});
            return retval;
            
        }
        
        ,create_tab_2_il: function create_tab_2_il() {
            this.tab_2_il = new qx.ui.layout.Canvas();
            var retval  =  this.tab_2_il;
            return retval;
            
        }
        
        ,create_tab_3: function create_tab_3() {
            this.tab_3 = new qx.ui.tabview.Page();
            var retval  =  this.tab_3;
            retval.setLabel(this.tr("Page"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout());
            retval.add(this.create_scrollArea(), {flex: 1});
            return retval;
            
        }
        
        ,create_tab_4: function create_tab_4() {
            this.tab_4 = new qx.ui.tabview.Page();
            var retval  =  this.tab_4;
            retval.setLabel(this.tr("Tab 1"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_4());
            retval.add(this.create_formLayout_implicit_container(), {flex: 1});
            return retval;
            
        }
        
        ,create_tab_5: function create_tab_5() {
            this.tab_5 = new qx.ui.tabview.Page();
            var retval  =  this.tab_5;
            retval.setLabel(this.tr("Tab 2"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_6());
            retval.add(this.create_scrollArea_2());
            return retval;
            
        }
        
        ,create_verticalLayout: function create_verticalLayout() {
            this.verticalLayout = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout;
            return retval;
            
        }
        
        ,create_verticalLayout_2: function create_verticalLayout_2() {
            this.verticalLayout_2 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_2;
            return retval;
            
        }
        
        ,create_verticalLayout_3: function create_verticalLayout_3() {
            this.verticalLayout_3 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_3;
            return retval;
            
        }
        
        ,create_verticalLayout_4: function create_verticalLayout_4() {
            this.verticalLayout_4 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_4;
            return retval;
            
        }
        
        ,create_verticalLayout_5: function create_verticalLayout_5() {
            this.verticalLayout_5 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_5;
            return retval;
            
        }
        
        ,create_verticalLayout_6: function create_verticalLayout_6() {
            this.verticalLayout_6 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_6;
            return retval;
            
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
