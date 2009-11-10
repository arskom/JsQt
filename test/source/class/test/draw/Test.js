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
            this.MainWindow.setWidth(637);
            this.MainWindow.setHeight(419);
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
        
        ,create_comboBox: function create_comboBox() {
            this.comboBox = new qx.ui.form.SelectBox();
            this.comboBox.setMarginBottom(1);
            this.comboBox.setMarginTop(1);
            this.comboBox.setMarginLeft(1);
            this.comboBox.setMarginRight(1);
            this.comboBox.add(new qx.ui.form.ListItem("asd",null,"zorta"));
            return this.comboBox;
            
        }
        
        ,create_frame: function create_frame() {
            this.frame = new qx.ui.container.Composite();
            this.frame.setWidth(120);
            this.frame.setHeight(80);
            this.frame.setMarginBottom(1);
            this.frame.setMarginTop(1);
            this.frame.setMarginLeft(1);
            this.frame.setMarginRight(1);
            this.frame.setLayout(this.create_frame_il());
            return this.frame;
            
        }
        
        ,create_frame_2: function create_frame_2() {
            this.frame_2 = new qx.ui.container.Composite();
            this.frame_2.setWidth(120);
            this.frame_2.setHeight(80);
            this.frame_2.setMarginBottom(1);
            this.frame_2.setMarginTop(1);
            this.frame_2.setMarginLeft(1);
            this.frame_2.setMarginRight(1);
            this.frame_2.setLayout(this.create_frame_2_il());
            return this.frame_2;
            
        }
        
        ,create_frame_2_il: function create_frame_2_il() {
            this.frame_2_il = new qx.ui.layout.Canvas();
            return this.frame_2_il;
            
        }
        
        ,create_frame_il: function create_frame_il() {
            this.frame_il = new qx.ui.layout.Canvas();
            return this.frame_il;
            
        }
        
        ,create_gridLayout: function create_gridLayout() {
            this.gridLayout = new qx.ui.layout.Grid();
            this.gridLayout.setRowFlex(0,1);
            this.gridLayout.setRowFlex(1,1);
            this.gridLayout.setRowFlex(2,1);
            this.gridLayout.setColumnFlex(0,1);
            this.gridLayout.setColumnFlex(1,1);
            return this.gridLayout;
            
        }
        
        ,create_gridLayout_2: function create_gridLayout_2() {
            this.gridLayout_2 = new qx.ui.layout.Grid();
            this.gridLayout_2.setRowFlex(1,1);
            this.gridLayout_2.setColumnFlex(1,1);
            return this.gridLayout_2;
            
        }
        
        ,create_groupBox: function create_groupBox() {
            this.groupBox = new qx.ui.groupbox.GroupBox();
            this.groupBox.setMaxHeight(150);
            this.groupBox.setMarginBottom(1);
            this.groupBox.setMarginTop(1);
            this.groupBox.setMarginLeft(1);
            this.groupBox.setMarginRight(1);
            this.groupBox.setLayout(this.create_groupBox_il());
            this.groupBox.setLegend(this.tr("GroupBox"));
            return this.groupBox;
            
        }
        
        ,create_groupBox_10: function create_groupBox_10() {
            this.groupBox_10 = new qx.ui.groupbox.GroupBox();
            this.groupBox_10.setMarginBottom(1);
            this.groupBox_10.setMarginTop(1);
            this.groupBox_10.setMarginLeft(1);
            this.groupBox_10.setMarginRight(1);
            this.groupBox_10.setLayout(this.create_groupBox_10_il());
            this.groupBox_10.setLegend(this.tr("GroupBox"));
            return this.groupBox_10;
            
        }
        
        ,create_groupBox_10_il: function create_groupBox_10_il() {
            this.groupBox_10_il = new qx.ui.layout.Canvas();
            return this.groupBox_10_il;
            
        }
        
        ,create_groupBox_11: function create_groupBox_11() {
            this.groupBox_11 = new qx.ui.groupbox.GroupBox();
            this.groupBox_11.setMarginBottom(1);
            this.groupBox_11.setMarginTop(1);
            this.groupBox_11.setMarginLeft(1);
            this.groupBox_11.setMarginRight(1);
            this.groupBox_11.setLayout(this.create_groupBox_11_il());
            this.groupBox_11.setLegend(this.tr("GroupBox"));
            return this.groupBox_11;
            
        }
        
        ,create_groupBox_11_il: function create_groupBox_11_il() {
            this.groupBox_11_il = new qx.ui.layout.Canvas();
            return this.groupBox_11_il;
            
        }
        
        ,create_groupBox_12: function create_groupBox_12() {
            this.groupBox_12 = new qx.ui.groupbox.GroupBox();
            this.groupBox_12.setMarginBottom(1);
            this.groupBox_12.setMarginTop(1);
            this.groupBox_12.setMarginLeft(1);
            this.groupBox_12.setMarginRight(1);
            this.groupBox_12.setLayout(this.create_groupBox_12_il());
            this.groupBox_12.setLegend(this.tr("GroupBox"));
            return this.groupBox_12;
            
        }
        
        ,create_groupBox_12_il: function create_groupBox_12_il() {
            this.groupBox_12_il = new qx.ui.layout.Canvas();
            return this.groupBox_12_il;
            
        }
        
        ,create_groupBox_13: function create_groupBox_13() {
            this.groupBox_13 = new qx.ui.groupbox.GroupBox();
            this.groupBox_13.setMarginBottom(1);
            this.groupBox_13.setMarginTop(1);
            this.groupBox_13.setMarginLeft(1);
            this.groupBox_13.setMarginRight(1);
            this.groupBox_13.setLayout(this.create_groupBox_13_il());
            this.groupBox_13.setLegend(this.tr("GroupBox"));
            return this.groupBox_13;
            
        }
        
        ,create_groupBox_13_il: function create_groupBox_13_il() {
            this.groupBox_13_il = new qx.ui.layout.Canvas();
            return this.groupBox_13_il;
            
        }
        
        ,create_groupBox_14: function create_groupBox_14() {
            this.groupBox_14 = new qx.ui.groupbox.GroupBox();
            this.groupBox_14.setMarginBottom(1);
            this.groupBox_14.setMarginTop(1);
            this.groupBox_14.setMarginLeft(1);
            this.groupBox_14.setMarginRight(1);
            this.groupBox_14.setLayout(this.create_groupBox_14_il());
            this.groupBox_14.setLegend(this.tr("GroupBox"));
            return this.groupBox_14;
            
        }
        
        ,create_groupBox_14_il: function create_groupBox_14_il() {
            this.groupBox_14_il = new qx.ui.layout.Canvas();
            return this.groupBox_14_il;
            
        }
        
        ,create_groupBox_2: function create_groupBox_2() {
            this.groupBox_2 = new qx.ui.groupbox.GroupBox();
            this.groupBox_2.setMarginBottom(1);
            this.groupBox_2.setMarginTop(1);
            this.groupBox_2.setMarginLeft(1);
            this.groupBox_2.setMarginRight(1);
            this.groupBox_2.setLayout(this.create_groupBox_2_il());
            this.groupBox_2.setLegend(this.tr("GroupBox"));
            return this.groupBox_2;
            
        }
        
        ,create_groupBox_2_il: function create_groupBox_2_il() {
            this.groupBox_2_il = new qx.ui.layout.Canvas();
            return this.groupBox_2_il;
            
        }
        
        ,create_groupBox_3: function create_groupBox_3() {
            this.groupBox_3 = new qx.ui.groupbox.GroupBox();
            this.groupBox_3.setMinHeight(500);
            this.groupBox_3.setMarginBottom(1);
            this.groupBox_3.setMarginTop(1);
            this.groupBox_3.setMarginLeft(1);
            this.groupBox_3.setMarginRight(1);
            this.groupBox_3.setLayout(this.create_groupBox_3_il());
            this.groupBox_3.setLegend(this.tr("GroupBox"));
            return this.groupBox_3;
            
        }
        
        ,create_groupBox_3_il: function create_groupBox_3_il() {
            this.groupBox_3_il = new qx.ui.layout.Canvas();
            return this.groupBox_3_il;
            
        }
        
        ,create_groupBox_4: function create_groupBox_4() {
            this.groupBox_4 = new qx.ui.groupbox.GroupBox();
            this.groupBox_4.setMaxWidth(300);
            this.groupBox_4.setMaxHeight(150);
            this.groupBox_4.setMarginBottom(1);
            this.groupBox_4.setMarginTop(1);
            this.groupBox_4.setMarginLeft(1);
            this.groupBox_4.setMarginRight(1);
            this.groupBox_4.setLayout(this.create_groupBox_4_il());
            this.groupBox_4.setLegend(this.tr("GroupBox"));
            return this.groupBox_4;
            
        }
        
        ,create_groupBox_4_il: function create_groupBox_4_il() {
            this.groupBox_4_il = new qx.ui.layout.Canvas();
            return this.groupBox_4_il;
            
        }
        
        ,create_groupBox_5: function create_groupBox_5() {
            this.groupBox_5 = new qx.ui.groupbox.GroupBox();
            this.groupBox_5.setMaxWidth(150);
            this.groupBox_5.setMarginBottom(1);
            this.groupBox_5.setMarginTop(1);
            this.groupBox_5.setMarginLeft(1);
            this.groupBox_5.setMarginRight(1);
            this.groupBox_5.setLayout(this.create_verticalLayout_5());
            this.groupBox_5.add(this.create_comboBox(), {flex: 1});
            this.groupBox_5.add(this.create_verticalSpacer(), {flex: 1});
            this.groupBox_5.setLegend(this.tr("GroupBox"));
            return this.groupBox_5;
            
        }
        
        ,create_groupBox_6: function create_groupBox_6() {
            this.groupBox_6 = new qx.ui.groupbox.GroupBox();
            this.groupBox_6.setMinHeight(500);
            this.groupBox_6.setMarginBottom(1);
            this.groupBox_6.setMarginTop(1);
            this.groupBox_6.setMarginLeft(1);
            this.groupBox_6.setMarginRight(1);
            this.groupBox_6.setLayout(this.create_groupBox_6_il());
            this.groupBox_6.setLegend(this.tr("GroupBox"));
            return this.groupBox_6;
            
        }
        
        ,create_groupBox_6_il: function create_groupBox_6_il() {
            this.groupBox_6_il = new qx.ui.layout.Canvas();
            return this.groupBox_6_il;
            
        }
        
        ,create_groupBox_7: function create_groupBox_7() {
            this.groupBox_7 = new qx.ui.groupbox.GroupBox();
            this.groupBox_7.setMarginBottom(1);
            this.groupBox_7.setMarginTop(1);
            this.groupBox_7.setMarginLeft(1);
            this.groupBox_7.setMarginRight(1);
            this.groupBox_7.setLayout(this.create_groupBox_7_il());
            this.groupBox_7.setLegend(this.tr("GroupBox"));
            return this.groupBox_7;
            
        }
        
        ,create_groupBox_7_il: function create_groupBox_7_il() {
            this.groupBox_7_il = new qx.ui.layout.Canvas();
            return this.groupBox_7_il;
            
        }
        
        ,create_groupBox_8: function create_groupBox_8() {
            this.groupBox_8 = new qx.ui.groupbox.GroupBox();
            this.groupBox_8.setMarginBottom(1);
            this.groupBox_8.setMarginTop(1);
            this.groupBox_8.setMarginLeft(1);
            this.groupBox_8.setMarginRight(1);
            this.groupBox_8.setLayout(this.create_groupBox_8_il());
            this.groupBox_8.setLegend(this.tr("GroupBox"));
            return this.groupBox_8;
            
        }
        
        ,create_groupBox_8_il: function create_groupBox_8_il() {
            this.groupBox_8_il = new qx.ui.layout.Canvas();
            return this.groupBox_8_il;
            
        }
        
        ,create_groupBox_9: function create_groupBox_9() {
            this.groupBox_9 = new qx.ui.groupbox.GroupBox();
            this.groupBox_9.setMinWidth(100);
            this.groupBox_9.setMinHeight(100);
            this.groupBox_9.setMarginBottom(1);
            this.groupBox_9.setMarginTop(1);
            this.groupBox_9.setMarginLeft(1);
            this.groupBox_9.setMarginRight(1);
            this.groupBox_9.setLayout(this.create_groupBox_9_il());
            this.groupBox_9.setLegend(this.tr("GroupBox"));
            return this.groupBox_9;
            
        }
        
        ,create_groupBox_9_il: function create_groupBox_9_il() {
            this.groupBox_9_il = new qx.ui.layout.Canvas();
            return this.groupBox_9_il;
            
        }
        
        ,create_groupBox_il: function create_groupBox_il() {
            this.groupBox_il = new qx.ui.layout.Canvas();
            return this.groupBox_il;
            
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
            this.horizontalLayout_2_implicit_container.add(this.create_groupBox_5(), {flex: 1});
            this.horizontalLayout_2_implicit_container.add(this.create_horizontalSpacer_2(), {flex: 1});
            return this.horizontalLayout_2_implicit_container;
            
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
            this.label.setWidth(161);
            this.label.setHeight(18);
            this.label.setMarginBottom(1);
            this.label.setMarginTop(1);
            this.label.setMarginLeft(1);
            this.label.setMarginRight(1);
            this.label.setValue(this.tr("This wil be cleared"));
            return this.label;
            
        }
        
        ,create_pushButton: function create_pushButton() {
            this.pushButton = new qx.ui.form.Button();
            this.pushButton.setWidth(83);
            this.pushButton.setHeight(28);
            this.pushButton.setMarginBottom(1);
            this.pushButton.setMarginTop(1);
            this.pushButton.setMarginLeft(1);
            this.pushButton.setMarginRight(1);
            this.pushButton.setLabel(this.tr("Clear"));
            return this.pushButton;
            
        }
        
        ,create_scrollArea: function create_scrollArea() {
            this.scrollArea = new qx.ui.container.Scroll();
            this.scrollArea.setMaxHeight(200);
            this.scrollArea.setMarginBottom(1);
            this.scrollArea.setMarginTop(1);
            this.scrollArea.setMarginLeft(1);
            this.scrollArea.setMarginRight(1);
            this.scrollArea.add(this.create_scrollAreaWidgetContents(), {edge: 0});
            return this.scrollArea;
            
        }
        
        ,create_scrollAreaWidgetContents: function create_scrollAreaWidgetContents() {
            this.scrollAreaWidgetContents = new qx.ui.container.Composite();
            this.scrollAreaWidgetContents.setWidth(143);
            this.scrollAreaWidgetContents.setHeight(518);
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
            this.scrollAreaWidgetContents_2.setWidth(321);
            this.scrollAreaWidgetContents_2.setHeight(518);
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
            this.scrollArea_2.setMaxWidth(500);
            this.scrollArea_2.setMaxHeight(200);
            this.scrollArea_2.setMarginBottom(1);
            this.scrollArea_2.setMarginTop(1);
            this.scrollArea_2.setMarginLeft(1);
            this.scrollArea_2.setMarginRight(1);
            this.scrollArea_2.add(this.create_scrollAreaWidgetContents_2(), {edge: 0});
            return this.scrollArea_2;
            
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
            this.tab.setMarginBottom(1);
            this.tab.setMarginTop(1);
            this.tab.setMarginLeft(1);
            this.tab.setMarginRight(1);
            this.tab.setLayout(this.create_tab_il());
            this.tab.add(this.create_frame(), {edge: 0});
            this.tab.add(this.create_frame_2(), {edge: 0});
            this.tab.setLabel(this.tr("Canvas"));
            return this.tab;
            
        }
        
        ,create_tabWidget: function create_tabWidget() {
            this.tabWidget = new qx.ui.tabview.TabView();
            this.tabWidget.setMarginBottom(1);
            this.tabWidget.setMarginTop(1);
            this.tabWidget.setMarginLeft(1);
            this.tabWidget.setMarginRight(1);
            this.tabWidget.add(this.create_tab(), {edge: 0});
            this.tabWidget.add(this.create_tab_2(), {edge: 0});
            this.tabWidget.add(this.create_tab_3(), {edge: 0});
            this.tabWidget.add(this.create_tab_4(), {edge: 0});
            this.tabWidget.add(this.create_tab_5(), {edge: 0});
            this.tabWidget.add(this.create_tab_6(), {edge: 0});
            return this.tabWidget;
            
        }
        
        ,create_tab_2: function create_tab_2() {
            this.tab_2 = new qx.ui.tabview.Page();
            this.tab_2.setMarginBottom(1);
            this.tab_2.setMarginTop(1);
            this.tab_2.setMarginLeft(1);
            this.tab_2.setMarginRight(1);
            this.tab_2.setLayout(this.create_horizontalLayout());
            this.tab_2.add(this.create_groupBox_2(), {flex: 1});
            this.tab_2.add(this.create_groupBox(), {flex: 1});
            this.tab_2.add(this.create_scrollArea(), {flex: 1});
            this.tab_2.setLabel(this.tr("HBox"));
            return this.tab_2;
            
        }
        
        ,create_tab_3: function create_tab_3() {
            this.tab_3 = new qx.ui.tabview.Page();
            this.tab_3.setMarginBottom(1);
            this.tab_3.setMarginTop(1);
            this.tab_3.setMarginLeft(1);
            this.tab_3.setMarginRight(1);
            this.tab_3.setLayout(this.create_verticalLayout_4());
            this.tab_3.add(this.create_horizontalLayout_2_implicit_container(), {flex: 1});
            this.tab_3.add(this.create_scrollArea_2(), {flex: 1});
            this.tab_3.add(this.create_groupBox_4(), {flex: 1});
            this.tab_3.setLabel(this.tr("VBox"));
            return this.tab_3;
            
        }
        
        ,create_tab_4: function create_tab_4() {
            this.tab_4 = new qx.ui.tabview.Page();
            this.tab_4.setMarginBottom(1);
            this.tab_4.setMarginTop(1);
            this.tab_4.setMarginLeft(1);
            this.tab_4.setMarginRight(1);
            this.tab_4.setLayout(this.create_gridLayout());
            this.tab_4.add(this.create_groupBox_7(), {column: 0,row: 0,rowSpan: 2});
            this.tab_4.add(this.create_groupBox_8(), {column: 1,row: 0});
            this.tab_4.add(this.create_groupBox_10(), {column: 1,row: 1});
            this.tab_4.add(this.create_groupBox_11(), {colSpan: 2,column: 0,row: 2});
            this.tab_4.setLabel(this.tr("Grid Span"));
            return this.tab_4;
            
        }
        
        ,create_tab_5: function create_tab_5() {
            this.tab_5 = new qx.ui.tabview.Page();
            this.tab_5.setMarginBottom(1);
            this.tab_5.setMarginTop(1);
            this.tab_5.setMarginLeft(1);
            this.tab_5.setMarginRight(1);
            this.tab_5.setLayout(this.create_gridLayout_2());
            this.tab_5.add(this.create_groupBox_9(), {column: 0,row: 0});
            this.tab_5.add(this.create_groupBox_12(), {column: 1,row: 0});
            this.tab_5.add(this.create_groupBox_13(), {column: 1,row: 1});
            this.tab_5.add(this.create_groupBox_14(), {column: 0,row: 1});
            this.tab_5.setLabel(this.tr("Grid Fixed"));
            return this.tab_5;
            
        }
        
        ,create_tab_6: function create_tab_6() {
            this.tab_6 = new qx.ui.tabview.Page();
            this.tab_6.setMarginBottom(1);
            this.tab_6.setMarginTop(1);
            this.tab_6.setMarginLeft(1);
            this.tab_6.setMarginRight(1);
            this.tab_6.setLayout(this.create_tab_6_il());
            this.tab_6.add(this.create_pushButton(), {edge: 0});
            this.tab_6.add(this.create_label(), {edge: 0});
            this.tab_6.setLabel(this.tr("Signals"));
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
        
        ,create_verticalSpacer: function create_verticalSpacer() {
            this.verticalSpacer = new qx.ui.core.Spacer();
            this.verticalSpacer.setMarginBottom(1);
            this.verticalSpacer.setMarginTop(1);
            this.verticalSpacer.setMarginLeft(1);
            this.verticalSpacer.setMarginRight(1);
            return this.verticalSpacer;
            
        }
        
        ,frame: null
        ,frame_2: null
        ,frame_2_il: null
        ,frame_il: null
        ,gridLayout: null
        ,gridLayout_2: null
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
        ,groupBox_2: null
        ,groupBox_2_il: null
        ,groupBox_3: null
        ,groupBox_3_il: null
        ,groupBox_4: null
        ,groupBox_4_il: null
        ,groupBox_5: null
        ,groupBox_6: null
        ,groupBox_6_il: null
        ,groupBox_7: null
        ,groupBox_7_il: null
        ,groupBox_8: null
        ,groupBox_8_il: null
        ,groupBox_9: null
        ,groupBox_9_il: null
        ,groupBox_il: null
        ,horizontalLayout: null
        ,horizontalLayout_2: null
        ,horizontalLayout_2_implicit_container: null
        ,horizontalSpacer: null
        ,horizontalSpacer_2: null
        ,label: null
        ,pushButton: null
        ,scrollArea: null
        ,scrollAreaWidgetContents: null
        ,scrollAreaWidgetContents_2: null
        ,scrollArea_2: null
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
        ,verticalLayout: null
        ,verticalLayout_2: null
        ,verticalLayout_3: null
        ,verticalLayout_4: null
        ,verticalLayout_5: null
        ,verticalSpacer: null
    }
    
    ,properties:  {
        widget:  {
            check: "qx.ui.container.Composite"
        }
        
    }
    
}
);
