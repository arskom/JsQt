qx.Class.define("test.draw.Test", {
    construct: function() {
        this.base(arguments);
        this.setWidget(this.create_MainWindow());
         /* The instance named 'treeWidget' is of type 'QTreeWidget' which is not supported (yet?) */
        
         /* The instance named 'menubar' is of type 'QMenuBar' which is not supported (yet?) */
        
         /* The instance named 'statusbar' is of type 'QStatusBar' which is not supported (yet?) */
        
         /* The instance named 'toolBar' is of type 'QToolBar' which is not supported (yet?) */
        
        
    }
    
    ,destruct: function() {
        
    }
    
    ,extend: qx.core.Object
    ,include: [qx.locale.MTranslation]
    ,members:  {
        MainWindow: null
        ,__lv: null
        ,centralwidget: null
        ,checkBox: null
        ,checkBox_2: null
        ,checkBox_3: null
        ,checkBox_4: null
        ,comboBox: null
        ,create_MainWindow: function create_MainWindow() {
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
             /* The 'action' tag for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */
            
            this.MainWindow = new qx.ui.container.Composite();
            this.MainWindow.setHeight(593);
            this.MainWindow.setWidth(747);
            this.MainWindow.setMarginBottom(1);
            this.MainWindow.setMarginTop(1);
            this.MainWindow.setMarginLeft(1);
            this.MainWindow.setMarginRight(1);
            this.MainWindow.setLayout(this.create___lv());
            this.MainWindow.add(this.create_centralwidget(), {flex: 1});
            return this.MainWindow;
            
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
            this.centralwidget.setLayout(this.create_verticalLayout());
            this.centralwidget.add(this.create_splitter(), {flex: 1});
            return this.centralwidget;
            
        }
        
        ,create_checkBox: function create_checkBox() {
            this.checkBox = new qx.ui.form.CheckBox();
            this.checkBox.setLabel(this.tr("CheckBox"));
            this.checkBox.setMarginBottom(1);
            this.checkBox.setMarginTop(1);
            this.checkBox.setMarginLeft(1);
            this.checkBox.setMarginRight(1);
            return this.checkBox;
            
        }
        
        ,create_checkBox_2: function create_checkBox_2() {
            this.checkBox_2 = new qx.ui.form.CheckBox();
            this.checkBox_2.setLabel(this.tr("CheckBox"));
            this.checkBox_2.setMarginBottom(1);
            this.checkBox_2.setMarginTop(1);
            this.checkBox_2.setMarginLeft(1);
            this.checkBox_2.setMarginRight(1);
            return this.checkBox_2;
            
        }
        
        ,create_checkBox_3: function create_checkBox_3() {
            this.checkBox_3 = new qx.ui.form.CheckBox();
            this.checkBox_3.setLabel(this.tr("CheckBox"));
            this.checkBox_3.setMarginBottom(1);
            this.checkBox_3.setMarginTop(1);
            this.checkBox_3.setMarginLeft(1);
            this.checkBox_3.setMarginRight(1);
            return this.checkBox_3;
            
        }
        
        ,create_checkBox_4: function create_checkBox_4() {
            this.checkBox_4 = new qx.ui.form.CheckBox();
            this.checkBox_4.setLabel(this.tr("CheckBox"));
            this.checkBox_4.setMarginBottom(1);
            this.checkBox_4.setMarginTop(1);
            this.checkBox_4.setMarginLeft(1);
            this.checkBox_4.setMarginRight(1);
            return this.checkBox_4;
            
        }
        
        ,create_comboBox: function create_comboBox() {
            this.comboBox = new qx.ui.form.SelectBox();
            this.comboBox.setMarginBottom(1);
            this.comboBox.setMarginTop(1);
            this.comboBox.setMarginLeft(1);
            this.comboBox.setMarginRight(1);
            this.comboBox.add(new qx.ui.form.ListItem("asd",null,null));
            return this.comboBox;
            
        }
        
        ,create_dateEdit: function create_dateEdit() {
            this.dateEdit = new qx.ui.form.DateField();
            this.dateEdit.setMarginBottom(1);
            this.dateEdit.setMarginTop(1);
            this.dateEdit.setMarginLeft(1);
            this.dateEdit.setMarginRight(1);
            return this.dateEdit;
            
        }
        
        ,create_gridLayout: function create_gridLayout() {
            this.gridLayout = new qx.ui.layout.Grid();
            this.gridLayout.setRowFlex(0,1);
            this.gridLayout.setRowFlex(1,1);
            this.gridLayout.setRowFlex(2,1);
            this.gridLayout.setRowFlex(3,1);
            this.gridLayout.setColumnFlex(0,1);
            this.gridLayout.setColumnFlex(1,1);
            this.gridLayout.setColumnFlex(2,1);
            return this.gridLayout;
            
        }
        
        ,create_gridLayout_2: function create_gridLayout_2() {
            this.gridLayout_2 = new qx.ui.layout.Grid();
            this.gridLayout_2.setRowFlex(1,1);
            this.gridLayout_2.setColumnFlex(1,1);
            return this.gridLayout_2;
            
        }
        
        ,create_gridLayout_3: function create_gridLayout_3() {
            this.gridLayout_3 = new qx.ui.layout.Grid();
            this.gridLayout_3.setRowFlex(0,1);
            this.gridLayout_3.setRowFlex(1,1);
            this.gridLayout_3.setRowFlex(2,1);
            this.gridLayout_3.setColumnFlex(0,1);
            this.gridLayout_3.setColumnFlex(1,1);
            return this.gridLayout_3;
            
        }
        
        ,create_groupBox: function create_groupBox() {
            this.groupBox = new qx.ui.groupbox.GroupBox();
            this.groupBox.setMaxHeight(150);
            this.groupBox.setMaxWidth(16777215);
            this.groupBox.setLegend(this.tr("GroupBox"));
            this.groupBox.setMarginBottom(1);
            this.groupBox.setMarginTop(1);
            this.groupBox.setMarginLeft(1);
            this.groupBox.setMarginRight(1);
            this.groupBox.setLayout(this.create_verticalLayout_7());
            this.groupBox.add(this.create_checkBox(), {flex: 1});
            this.groupBox.add(this.create_checkBox_2(), {flex: 1});
            this.groupBox.add(this.create_checkBox_3(), {flex: 1});
            this.groupBox.add(this.create_checkBox_4(), {flex: 1});
            return this.groupBox;
            
        }
        
        ,create_groupBox_10: function create_groupBox_10() {
            this.groupBox_10 = new qx.ui.groupbox.GroupBox();
            this.groupBox_10.setLegend(this.tr("GroupBox"));
            this.groupBox_10.setMarginBottom(1);
            this.groupBox_10.setMarginTop(1);
            this.groupBox_10.setMarginLeft(1);
            this.groupBox_10.setMarginRight(1);
            this.groupBox_10.setLayout(this.create_groupBox_10_il());
            return this.groupBox_10;
            
        }
        
        ,create_groupBox_10_il: function create_groupBox_10_il() {
            this.groupBox_10_il = new qx.ui.layout.Canvas();
            return this.groupBox_10_il;
            
        }
        
        ,create_groupBox_11: function create_groupBox_11() {
            this.groupBox_11 = new qx.ui.groupbox.GroupBox();
            this.groupBox_11.setLegend(this.tr("GroupBox"));
            this.groupBox_11.setMarginBottom(1);
            this.groupBox_11.setMarginTop(1);
            this.groupBox_11.setMarginLeft(1);
            this.groupBox_11.setMarginRight(1);
            this.groupBox_11.setLayout(this.create_groupBox_11_il());
            return this.groupBox_11;
            
        }
        
        ,create_groupBox_11_il: function create_groupBox_11_il() {
            this.groupBox_11_il = new qx.ui.layout.Canvas();
            return this.groupBox_11_il;
            
        }
        
        ,create_groupBox_12: function create_groupBox_12() {
            this.groupBox_12 = new qx.ui.groupbox.GroupBox();
            this.groupBox_12.setLegend(this.tr("GroupBox"));
            this.groupBox_12.setMarginBottom(1);
            this.groupBox_12.setMarginTop(1);
            this.groupBox_12.setMarginLeft(1);
            this.groupBox_12.setMarginRight(1);
            this.groupBox_12.setLayout(this.create_groupBox_12_il());
            return this.groupBox_12;
            
        }
        
        ,create_groupBox_12_il: function create_groupBox_12_il() {
            this.groupBox_12_il = new qx.ui.layout.Canvas();
            return this.groupBox_12_il;
            
        }
        
        ,create_groupBox_13: function create_groupBox_13() {
            this.groupBox_13 = new qx.ui.groupbox.GroupBox();
            this.groupBox_13.setLegend(this.tr("GroupBox"));
            this.groupBox_13.setMarginBottom(1);
            this.groupBox_13.setMarginTop(1);
            this.groupBox_13.setMarginLeft(1);
            this.groupBox_13.setMarginRight(1);
            this.groupBox_13.setLayout(this.create_groupBox_13_il());
            return this.groupBox_13;
            
        }
        
        ,create_groupBox_13_il: function create_groupBox_13_il() {
            this.groupBox_13_il = new qx.ui.layout.Canvas();
            return this.groupBox_13_il;
            
        }
        
        ,create_groupBox_14: function create_groupBox_14() {
            this.groupBox_14 = new qx.ui.groupbox.GroupBox();
            this.groupBox_14.setLegend(this.tr("GroupBox"));
            this.groupBox_14.setMarginBottom(1);
            this.groupBox_14.setMarginTop(1);
            this.groupBox_14.setMarginLeft(1);
            this.groupBox_14.setMarginRight(1);
            this.groupBox_14.setLayout(this.create_groupBox_14_il());
            return this.groupBox_14;
            
        }
        
        ,create_groupBox_14_il: function create_groupBox_14_il() {
            this.groupBox_14_il = new qx.ui.layout.Canvas();
            return this.groupBox_14_il;
            
        }
        
        ,create_groupBox_15: function create_groupBox_15() {
            this.groupBox_15 = new qx.ui.groupbox.GroupBox();
            this.groupBox_15.setLegend(this.tr("GroupBox"));
            this.groupBox_15.setMarginBottom(1);
            this.groupBox_15.setMarginTop(1);
            this.groupBox_15.setMarginLeft(1);
            this.groupBox_15.setMarginRight(1);
            this.groupBox_15.setLayout(this.create_groupBox_15_il());
            return this.groupBox_15;
            
        }
        
        ,create_groupBox_15_il: function create_groupBox_15_il() {
            this.groupBox_15_il = new qx.ui.layout.Canvas();
            return this.groupBox_15_il;
            
        }
        
        ,create_groupBox_16: function create_groupBox_16() {
            this.groupBox_16 = new qx.ui.groupbox.GroupBox();
            this.groupBox_16.setLegend(this.tr("GroupBox"));
            this.groupBox_16.setMarginBottom(1);
            this.groupBox_16.setMarginTop(1);
            this.groupBox_16.setMarginLeft(1);
            this.groupBox_16.setMarginRight(1);
            this.groupBox_16.setLayout(this.create_groupBox_16_il());
            return this.groupBox_16;
            
        }
        
        ,create_groupBox_16_il: function create_groupBox_16_il() {
            this.groupBox_16_il = new qx.ui.layout.Canvas();
            return this.groupBox_16_il;
            
        }
        
        ,create_groupBox_2: function create_groupBox_2() {
            this.groupBox_2 = new qx.ui.groupbox.GroupBox();
            this.groupBox_2.setLegend(this.tr("GroupBox"));
            this.groupBox_2.setMarginBottom(1);
            this.groupBox_2.setMarginTop(1);
            this.groupBox_2.setMarginLeft(1);
            this.groupBox_2.setMarginRight(1);
            this.groupBox_2.setLayout(this.create_verticalLayout_6());
            this.groupBox_2.add(this.create_radioButton(), {flex: 1});
            this.groupBox_2.add(this.create_radioButton_2(), {flex: 1});
            this.groupBox_2.add(this.create_radioButton_3(), {flex: 1});
            this.groupBox_2.add(this.create_radioButton_4(), {flex: 1});
            return this.groupBox_2;
            
        }
        
        ,create_groupBox_3: function create_groupBox_3() {
            this.groupBox_3 = new qx.ui.groupbox.GroupBox();
            this.groupBox_3.setMinHeight(500);
            this.groupBox_3.setMinWidth(0);
            this.groupBox_3.setLegend(this.tr("GroupBox"));
            this.groupBox_3.setMarginBottom(1);
            this.groupBox_3.setMarginTop(1);
            this.groupBox_3.setMarginLeft(1);
            this.groupBox_3.setMarginRight(1);
            this.groupBox_3.setLayout(this.create_verticalLayout_8());
            this.groupBox_3.add(this.create_label_3(), {flex: 1});
            this.groupBox_3.add(this.create_label_4(), {flex: 1});
            this.groupBox_3.add(this.create_verticalSpacer_2(), {flex: 1});
            return this.groupBox_3;
            
        }
        
        ,create_groupBox_4: function create_groupBox_4() {
            this.groupBox_4 = new qx.ui.groupbox.GroupBox();
            this.groupBox_4.setMaxHeight(150);
            this.groupBox_4.setMaxWidth(300);
            this.groupBox_4.setLegend(this.tr("GroupBox"));
            this.groupBox_4.setMarginBottom(1);
            this.groupBox_4.setMarginTop(1);
            this.groupBox_4.setMarginLeft(1);
            this.groupBox_4.setMarginRight(1);
            this.groupBox_4.setLayout(this.create_gridLayout_3());
            this.groupBox_4.add(this.create_dateEdit(), {column: 0,row: 0});
            this.groupBox_4.add(this.create_textEdit(), {column: 1,row: 0,rowSpan: 4});
            this.groupBox_4.add(this.create_lineEdit(), {column: 0,row: 2});
            this.groupBox_4.add(this.create_spinBox(), {column: 0,row: 1});
            return this.groupBox_4;
            
        }
        
        ,create_groupBox_6: function create_groupBox_6() {
            this.groupBox_6 = new qx.ui.groupbox.GroupBox();
            this.groupBox_6.setMinHeight(500);
            this.groupBox_6.setMinWidth(0);
            this.groupBox_6.setLegend(this.tr("GroupBox"));
            this.groupBox_6.setMarginBottom(1);
            this.groupBox_6.setMarginTop(1);
            this.groupBox_6.setMarginLeft(1);
            this.groupBox_6.setMarginRight(1);
            this.groupBox_6.setLayout(this.create_groupBox_6_il());
            return this.groupBox_6;
            
        }
        
        ,create_groupBox_6_il: function create_groupBox_6_il() {
            this.groupBox_6_il = new qx.ui.layout.Canvas();
            return this.groupBox_6_il;
            
        }
        
        ,create_groupBox_7: function create_groupBox_7() {
            this.groupBox_7 = new qx.ui.groupbox.GroupBox();
            this.groupBox_7.setLegend(this.tr("GroupBox"));
            this.groupBox_7.setMarginBottom(1);
            this.groupBox_7.setMarginTop(1);
            this.groupBox_7.setMarginLeft(1);
            this.groupBox_7.setMarginRight(1);
            this.groupBox_7.setLayout(this.create_groupBox_7_il());
            return this.groupBox_7;
            
        }
        
        ,create_groupBox_7_il: function create_groupBox_7_il() {
            this.groupBox_7_il = new qx.ui.layout.Canvas();
            return this.groupBox_7_il;
            
        }
        
        ,create_groupBox_8: function create_groupBox_8() {
            this.groupBox_8 = new qx.ui.groupbox.GroupBox();
            this.groupBox_8.setLegend(this.tr("GroupBox"));
            this.groupBox_8.setMarginBottom(1);
            this.groupBox_8.setMarginTop(1);
            this.groupBox_8.setMarginLeft(1);
            this.groupBox_8.setMarginRight(1);
            this.groupBox_8.setLayout(this.create_groupBox_8_il());
            return this.groupBox_8;
            
        }
        
        ,create_groupBox_8_il: function create_groupBox_8_il() {
            this.groupBox_8_il = new qx.ui.layout.Canvas();
            return this.groupBox_8_il;
            
        }
        
        ,create_groupBox_9: function create_groupBox_9() {
            this.groupBox_9 = new qx.ui.groupbox.GroupBox();
            this.groupBox_9.setMinHeight(100);
            this.groupBox_9.setMinWidth(100);
            this.groupBox_9.setLegend(this.tr("GroupBox"));
            this.groupBox_9.setMarginBottom(1);
            this.groupBox_9.setMarginTop(1);
            this.groupBox_9.setMarginLeft(1);
            this.groupBox_9.setMarginRight(1);
            this.groupBox_9.setLayout(this.create_groupBox_9_il());
            return this.groupBox_9;
            
        }
        
        ,create_groupBox_9_il: function create_groupBox_9_il() {
            this.groupBox_9_il = new qx.ui.layout.Canvas();
            return this.groupBox_9_il;
            
        }
        
        ,create_groupBox_centered: function create_groupBox_centered() {
            this.groupBox_centered = new qx.ui.groupbox.GroupBox();
            this.groupBox_centered.setMaxHeight(16777215);
            this.groupBox_centered.setMaxWidth(150);
            this.groupBox_centered.setLegend(this.tr("GroupBox"));
            this.groupBox_centered.setMarginBottom(1);
            this.groupBox_centered.setMarginTop(1);
            this.groupBox_centered.setMarginLeft(1);
            this.groupBox_centered.setMarginRight(1);
            this.groupBox_centered.setLayout(this.create_verticalLayout_5());
            this.groupBox_centered.add(this.create_comboBox(), {flex: 1});
            return this.groupBox_centered;
            
        }
        
        ,create_horizontalLayout: function create_horizontalLayout() {
            this.horizontalLayout = new qx.ui.layout.HBox();
            return this.horizontalLayout;
            
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
            this.horizontalLayout_2_implicit_container.add(this.create_horizontalSpacer(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_groupBox_centered(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_horizontalSpacer_2(), {flex: 1});
            return this.horizontalLayout_2_implicit_container;
            
        }
        
        ,create_horizontalSpacer: function create_horizontalSpacer() {
            this.horizontalSpacer = new qx.ui.core.Spacer();
            this.horizontalSpacer.setHeight(20);
            this.horizontalSpacer.setWidth(40);
            this.horizontalSpacer.setMarginBottom(1);
            this.horizontalSpacer.setMarginTop(1);
            this.horizontalSpacer.setMarginLeft(1);
            this.horizontalSpacer.setMarginRight(1);
            return this.horizontalSpacer;
            
        }
        
        ,create_horizontalSpacer_2: function create_horizontalSpacer_2() {
            this.horizontalSpacer_2 = new qx.ui.core.Spacer();
            this.horizontalSpacer_2.setHeight(20);
            this.horizontalSpacer_2.setWidth(40);
            this.horizontalSpacer_2.setMarginBottom(1);
            this.horizontalSpacer_2.setMarginTop(1);
            this.horizontalSpacer_2.setMarginLeft(1);
            this.horizontalSpacer_2.setMarginRight(1);
            return this.horizontalSpacer_2;
            
        }
        
        ,create_label: function create_label() {
            this.label = new qx.ui.basic.Label();
            this.label.setHeight(31);
            this.label.setWidth(131);
            this.label.setLabel(this.tr("This wil be cleared"));
            this.label.setMarginBottom(1);
            this.label.setMarginTop(1);
            this.label.setMarginLeft(1);
            this.label.setMarginRight(1);
            return this.label;
            
        }
        
        ,create_label_2: function create_label_2() {
            this.label_2 = new qx.ui.basic.Label();
            this.label_2.setHeight(31);
            this.label_2.setWidth(131);
            this.label_2.setLabel(this.tr("hello"));
            this.label_2.setMarginBottom(1);
            this.label_2.setMarginTop(1);
            this.label_2.setMarginLeft(1);
            this.label_2.setMarginRight(1);
            return this.label_2;
            
        }
        
        ,create_label_3: function create_label_3() {
            this.label_3 = new qx.ui.basic.Label();
            this.label_3.setLabel(this.tr("TextLabel"));
            this.label_3.setMarginBottom(1);
            this.label_3.setMarginTop(1);
            this.label_3.setMarginLeft(1);
            this.label_3.setMarginRight(1);
            return this.label_3;
            
        }
        
        ,create_label_4: function create_label_4() {
            this.label_4 = new qx.ui.basic.Label();
            this.label_4.setLabel(this.tr("TextLabel"));
            this.label_4.setMarginBottom(1);
            this.label_4.setMarginTop(1);
            this.label_4.setMarginLeft(1);
            this.label_4.setMarginRight(1);
            return this.label_4;
            
        }
        
        ,create_lineEdit: function create_lineEdit() {
            this.lineEdit = new qx.ui.form.TextField();
            this.lineEdit.setMarginBottom(1);
            this.lineEdit.setMarginTop(1);
            this.lineEdit.setMarginLeft(1);
            this.lineEdit.setMarginRight(1);
            return this.lineEdit;
            
        }
        
        ,create_listWidget: function create_listWidget() {
            this.listWidget = new qx.ui.form.List();
            this.listWidget.setHeight(192);
            this.listWidget.setWidth(256);
            this.listWidget.setMarginBottom(1);
            this.listWidget.setMarginTop(1);
            this.listWidget.setMarginLeft(1);
            this.listWidget.setMarginRight(1);
            return this.listWidget;
            
        }
        
        ,create_pushButton: function create_pushButton() {
            this.pushButton = new qx.ui.form.Button();
            this.pushButton.setHeight(28);
            this.pushButton.setWidth(81);
            this.pushButton.setLabel(this.tr("Clear"));
            this.pushButton.setMarginBottom(1);
            this.pushButton.setMarginTop(1);
            this.pushButton.setMarginLeft(1);
            this.pushButton.setMarginRight(1);
            return this.pushButton;
            
        }
        
        ,create_pushButton_2: function create_pushButton_2() {
            this.pushButton_2 = new qx.ui.form.Button();
            this.pushButton_2.setHeight(28);
            this.pushButton_2.setWidth(81);
            this.pushButton_2.setLabel(this.tr("nothing"));
            this.pushButton_2.setMarginBottom(1);
            this.pushButton_2.setMarginTop(1);
            this.pushButton_2.setMarginLeft(1);
            this.pushButton_2.setMarginRight(1);
            return this.pushButton_2;
            
        }
        
        ,create_radioButton: function create_radioButton() {
            this.radioButton = new qx.ui.form.RadioButton();
            this.radioButton.setLabel(this.tr("RadioButton"));
            this.radioButton.setMarginBottom(1);
            this.radioButton.setMarginTop(1);
            this.radioButton.setMarginLeft(1);
            this.radioButton.setMarginRight(1);
            return this.radioButton;
            
        }
        
        ,create_radioButton_2: function create_radioButton_2() {
            this.radioButton_2 = new qx.ui.form.RadioButton();
            this.radioButton_2.setLabel(this.tr("RadioButton"));
            this.radioButton_2.setMarginBottom(1);
            this.radioButton_2.setMarginTop(1);
            this.radioButton_2.setMarginLeft(1);
            this.radioButton_2.setMarginRight(1);
            return this.radioButton_2;
            
        }
        
        ,create_radioButton_3: function create_radioButton_3() {
            this.radioButton_3 = new qx.ui.form.RadioButton();
            this.radioButton_3.setLabel(this.tr("RadioButton"));
            this.radioButton_3.setMarginBottom(1);
            this.radioButton_3.setMarginTop(1);
            this.radioButton_3.setMarginLeft(1);
            this.radioButton_3.setMarginRight(1);
            return this.radioButton_3;
            
        }
        
        ,create_radioButton_4: function create_radioButton_4() {
            this.radioButton_4 = new qx.ui.form.RadioButton();
            this.radioButton_4.setLabel(this.tr("RadioButton"));
            this.radioButton_4.setMarginBottom(1);
            this.radioButton_4.setMarginTop(1);
            this.radioButton_4.setMarginLeft(1);
            this.radioButton_4.setMarginRight(1);
            return this.radioButton_4;
            
        }
        
        ,create_scrollArea: function create_scrollArea() {
            this.scrollArea = new qx.ui.container.Scroll();
            this.scrollArea.setMaxHeight(200);
            this.scrollArea.setMaxWidth(16777215);
            this.scrollArea.setMarginBottom(1);
            this.scrollArea.setMarginTop(1);
            this.scrollArea.setMarginLeft(1);
            this.scrollArea.setMarginRight(1);
            this.scrollArea.add(this.create_scrollAreaWidgetContents(), {left: 0,top: 0});
            return this.scrollArea;
            
        }
        
        ,create_scrollAreaWidgetContents: function create_scrollAreaWidgetContents() {
            this.scrollAreaWidgetContents = new qx.ui.container.Composite();
            this.scrollAreaWidgetContents.setHeight(518);
            this.scrollAreaWidgetContents.setWidth(186);
            this.scrollAreaWidgetContents.setMarginBottom(1);
            this.scrollAreaWidgetContents.setMarginTop(1);
            this.scrollAreaWidgetContents.setMarginLeft(1);
            this.scrollAreaWidgetContents.setMarginRight(1);
            this.scrollAreaWidgetContents.setLayout(this.create_verticalLayout_2());
            this.scrollAreaWidgetContents.add(this.create_groupBox_3(), {flex: 1});
            return this.scrollAreaWidgetContents;
            
        }
        
        ,create_scrollAreaWidgetContents_2: function create_scrollAreaWidgetContents_2() {
            this.scrollAreaWidgetContents_2 = new qx.ui.container.Composite();
            this.scrollAreaWidgetContents_2.setHeight(518);
            this.scrollAreaWidgetContents_2.setWidth(431);
            this.scrollAreaWidgetContents_2.setMarginBottom(1);
            this.scrollAreaWidgetContents_2.setMarginTop(1);
            this.scrollAreaWidgetContents_2.setMarginLeft(1);
            this.scrollAreaWidgetContents_2.setMarginRight(1);
            this.scrollAreaWidgetContents_2.setLayout(this.create_verticalLayout_3());
            this.scrollAreaWidgetContents_2.add(this.create_groupBox_6(), {flex: 1});
            return this.scrollAreaWidgetContents_2;
            
        }
        
        ,create_scrollArea_2: function create_scrollArea_2() {
            this.scrollArea_2 = new qx.ui.container.Scroll();
            this.scrollArea_2.setMaxHeight(200);
            this.scrollArea_2.setMaxWidth(500);
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
            return this.spinBox;
            
        }
        
        ,create_splitter: function create_splitter() {
            this.splitter = new qx.ui.splitpane.Pane("horizontal");
            this.splitter.setMarginBottom(1);
            this.splitter.setMarginTop(1);
            this.splitter.setMarginLeft(1);
            this.splitter.setMarginRight(1);
            this.splitter.add(this.create_tabWidget(),1);
            return this.splitter;
            
        }
        
        ,create_tab: function create_tab() {
            this.tab = new qx.ui.tabview.Page();
            this.tab.setLabel(this.tr("Canvas"));
            this.tab.setMarginBottom(1);
            this.tab.setMarginTop(1);
            this.tab.setMarginLeft(1);
            this.tab.setMarginRight(1);
            this.tab.setLayout(this.create_tab_il());
            this.tab.add(this.create_pushButton_2(), {left: 60,top: 110});
            this.tab.add(this.create_label_2(), {left: 230,top: 80});
            this.tab.add(this.create_tableWidget(), {left: 20,top: 210});
            this.tab.add(this.create_listWidget(), {left: 310,top: 220});
            return this.tab;
            
        }
        
        ,create_tabWidget: function create_tabWidget() {
            this.tabWidget = new qx.ui.tabview.TabView();
            this.tabWidget.setMarginBottom(1);
            this.tabWidget.setMarginTop(1);
            this.tabWidget.setMarginLeft(1);
            this.tabWidget.setMarginRight(1);
            this.tabWidget.add(this.create_tab());
            this.tabWidget.add(this.create_tab_2());
            this.tabWidget.add(this.create_tab_3());
            this.tabWidget.add(this.create_tab_4());
            this.tabWidget.add(this.create_tab_5());
            this.tabWidget.add(this.create_tab_6());
            return this.tabWidget;
            
        }
        
        ,create_tab_2: function create_tab_2() {
            this.tab_2 = new qx.ui.tabview.Page();
            this.tab_2.setLabel(this.tr("HBox"));
            this.tab_2.setMarginBottom(1);
            this.tab_2.setMarginTop(1);
            this.tab_2.setMarginLeft(1);
            this.tab_2.setMarginRight(1);
            this.tab_2.setLayout(this.create_horizontalLayout());
            this.tab_2.add(this.create_groupBox_2(), {flex: 1});
            this.tab_2.add(this.create_groupBox(), {flex: 1});
            this.tab_2.add(this.create_scrollArea(), {flex: 2});
            return this.tab_2;
            
        }
        
        ,create_tab_3: function create_tab_3() {
            this.tab_3 = new qx.ui.tabview.Page();
            this.tab_3.setLabel(this.tr("VBox"));
            this.tab_3.setMarginBottom(1);
            this.tab_3.setMarginTop(1);
            this.tab_3.setMarginLeft(1);
            this.tab_3.setMarginRight(1);
            this.tab_3.setLayout(this.create_verticalLayout_4());
            this.tab_3.add(this.create_horizontalLayout_2_implicit_container(), {flex: 1});
            this.tab_3.add(this.create_scrollArea_2(), {flex: 3});
            this.tab_3.add(this.create_groupBox_4(), {flex: 1});
            return this.tab_3;
            
        }
        
        ,create_tab_4: function create_tab_4() {
            this.tab_4 = new qx.ui.tabview.Page();
            this.tab_4.setLabel(this.tr("Grid Span"));
            this.tab_4.setMarginBottom(1);
            this.tab_4.setMarginTop(1);
            this.tab_4.setMarginLeft(1);
            this.tab_4.setMarginRight(1);
            this.tab_4.setLayout(this.create_gridLayout());
            this.tab_4.add(this.create_groupBox_7(), {column: 0,row: 1,rowSpan: 2});
            this.tab_4.add(this.create_groupBox_8(), {column: 1,row: 1});
            this.tab_4.add(this.create_groupBox_10(), {column: 1,row: 2});
            this.tab_4.add(this.create_groupBox_11(), {colSpan: 2,column: 0,row: 3});
            this.tab_4.add(this.create_groupBox_15(), {colSpan: 2,column: 0,row: 0});
            this.tab_4.add(this.create_groupBox_16(), {column: 2,row: 0,rowSpan: 4});
            return this.tab_4;
            
        }
        
        ,create_tab_5: function create_tab_5() {
            this.tab_5 = new qx.ui.tabview.Page();
            this.tab_5.setLabel(this.tr("Grid Fixed"));
            this.tab_5.setMarginBottom(1);
            this.tab_5.setMarginTop(1);
            this.tab_5.setMarginLeft(1);
            this.tab_5.setMarginRight(1);
            this.tab_5.setLayout(this.create_gridLayout_2());
            this.tab_5.add(this.create_groupBox_9(), {column: 0,row: 0});
            this.tab_5.add(this.create_groupBox_12(), {column: 1,row: 0});
            this.tab_5.add(this.create_groupBox_13(), {column: 1,row: 1});
            this.tab_5.add(this.create_groupBox_14(), {column: 0,row: 1});
            return this.tab_5;
            
        }
        
        ,create_tab_6: function create_tab_6() {
            this.tab_6 = new qx.ui.tabview.Page();
            this.tab_6.setLabel(this.tr("Signals"));
            this.tab_6.setMarginBottom(1);
            this.tab_6.setMarginTop(1);
            this.tab_6.setMarginLeft(1);
            this.tab_6.setMarginRight(1);
            this.tab_6.setLayout(this.create_tab_6_il());
            this.tab_6.add(this.create_pushButton(), {left: 30,top: 30});
            this.tab_6.add(this.create_label(), {left: 230,top: 40});
            return this.tab_6;
            
        }
        
        ,create_tab_6_il: function create_tab_6_il() {
            this.tab_6_il = new qx.ui.layout.Canvas();
            return this.tab_6_il;
            
        }
        
        ,create_tab_il: function create_tab_il() {
            this.tab_il = new qx.ui.layout.Canvas();
            return this.tab_il;
            
        }
        
        ,create_tableWidget: function create_tableWidget() {
            this.tableWidget = new qx.ui.table.Table(null, {
                tableColumnModel: function(obj) {
                    return new qx.ui.table.columnmodel.Resize(obj);
                    
                }
                
            }
            );
            this.tableWidget.setHeight(192);
            this.tableWidget.setWidth(256);
            this.tableWidget.setMarginBottom(1);
            this.tableWidget.setMarginTop(1);
            this.tableWidget.setMarginLeft(1);
            this.tableWidget.setMarginRight(1);
            return this.tableWidget;
            
        }
        
        ,create_textEdit: function create_textEdit() {
            this.textEdit = new qx.ui.form.TextArea();
            this.textEdit.setMarginBottom(1);
            this.textEdit.setMarginTop(1);
            this.textEdit.setMarginLeft(1);
            this.textEdit.setMarginRight(1);
            return this.textEdit;
            
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
        
        ,create_verticalLayout_7: function create_verticalLayout_7() {
            this.verticalLayout_7 = new qx.ui.layout.VBox();
            return this.verticalLayout_7;
            
        }
        
        ,create_verticalLayout_8: function create_verticalLayout_8() {
            this.verticalLayout_8 = new qx.ui.layout.VBox();
            return this.verticalLayout_8;
            
        }
        
        ,create_verticalSpacer_2: function create_verticalSpacer_2() {
            this.verticalSpacer_2 = new qx.ui.core.Spacer();
            this.verticalSpacer_2.setHeight(411);
            this.verticalSpacer_2.setWidth(20);
            this.verticalSpacer_2.setMarginBottom(1);
            this.verticalSpacer_2.setMarginTop(1);
            this.verticalSpacer_2.setMarginLeft(1);
            this.verticalSpacer_2.setMarginRight(1);
            return this.verticalSpacer_2;
            
        }
        
        ,dateEdit: null
        ,gridLayout: null
        ,gridLayout_2: null
        ,gridLayout_3: null
        ,groupBox: null
        ,groupBox_10: null
        ,groupBox_10_il: null
        ,groupBox_11: null
        ,groupBox_11_il: null
        ,groupBox_12: null
        ,groupBox_12_il: null
        ,groupBox_13: null
        ,groupBox_13_il: null
        ,groupBox_14: null
        ,groupBox_14_il: null
        ,groupBox_15: null
        ,groupBox_15_il: null
        ,groupBox_16: null
        ,groupBox_16_il: null
        ,groupBox_2: null
        ,groupBox_3: null
        ,groupBox_4: null
        ,groupBox_6: null
        ,groupBox_6_il: null
        ,groupBox_7: null
        ,groupBox_7_il: null
        ,groupBox_8: null
        ,groupBox_8_il: null
        ,groupBox_9: null
        ,groupBox_9_il: null
        ,groupBox_centered: null
        ,horizontalLayout: null
        ,horizontalLayout_2: null
        ,horizontalLayout_2_implicit_container: null
        ,horizontalSpacer: null
        ,horizontalSpacer_2: null
        ,label: null
        ,label_2: null
        ,label_3: null
        ,label_4: null
        ,lineEdit: null
        ,listWidget: null
        ,pushButton: null
        ,pushButton_2: null
        ,radioButton: null
        ,radioButton_2: null
        ,radioButton_3: null
        ,radioButton_4: null
        ,scrollArea: null
        ,scrollAreaWidgetContents: null
        ,scrollAreaWidgetContents_2: null
        ,scrollArea_2: null
        ,spinBox: null
        ,splitter: null
        ,tab: null
        ,tabWidget: null
        ,tab_2: null
        ,tab_3: null
        ,tab_4: null
        ,tab_5: null
        ,tab_6: null
        ,tab_6_il: null
        ,tab_il: null
        ,tableWidget: null
        ,textEdit: null
        ,verticalLayout: null
        ,verticalLayout_2: null
        ,verticalLayout_3: null
        ,verticalLayout_4: null
        ,verticalLayout_5: null
        ,verticalLayout_6: null
        ,verticalLayout_7: null
        ,verticalLayout_8: null
        ,verticalSpacer_2: null
    }
    
    ,properties:  {
        widget:  {
            check: "qx.ui.container.Composite"
        }
        
    }
    
}
);
