qx.Class.define("test.draw.Test", {
    construct: function() {
        this.base(arguments);
        this.setWidget(this.create_MainWindow());
         /* The instance named 'statusbar' is of type 'QStatusBar' which is not supported (yet?) */

    }

    ,destruct: function() {

    }

    ,extend: qx.core.Object
    ,include: [qx.locale.MTranslation]
    ,members:  {
        FinestMenuItem_menu: null
        ,MainWindow: null
        ,__lv: null
        ,actionDeneme_toolbar: null
        ,actionFineMenuItem_menu: null
        ,actionMenuItem1_menu: null
        ,actionMenuItem1_toolbar: null
        ,actionSubMenuItem1_menu: null
        ,actionSubMenuItem2_menu: null
        ,actionSubMenuItem3_menu: null
        ,actionToolBarAction1_toolbar: null
        ,actionZopa_toolbar: null
        ,centralwidget: null
        ,checkBox: null
        ,checkBox_2: null
        ,checkBox_3: null
        ,checkBox_4: null
        ,comboBox: null
        ,create_FinestMenuItem_menu: function create_FinestMenuItem_menu() {
            this.FinestMenuItem_menu = new qx.ui.menu.Button();
            var retval  =  this.FinestMenuItem_menu;
            retval.setLabel(this.tr("FinestMenuItem"));
            retval.setMargin(1);
            return retval;

        }

        ,create_MainWindow: function create_MainWindow() {
             /* The 'windowTitle' property for widget named 'MainWindow'of type '<class 'jsqt.il.qt.container.QMainWindow'>' is not supported (yet?) */

            this.MainWindow = new qx.ui.container.Composite(this.create___lv());
            var retval  =  this.MainWindow;
            retval.setHeight(521);
            retval.setWidth(774);
            retval.setMargin(1);
            retval.add(this.create_menubar());
            retval.add(this.create_toolBar());
            retval.add(this.create_toolBar_2());
            retval.add(this.create_centralwidget(), {flex: 1});
            return retval;

        }

        ,create___lv: function create___lv() {
            this.__lv = new qx.ui.layout.VBox();
            var retval  =  this.__lv;
            return retval;

        }

        ,create_actionDeneme_toolbar: function create_actionDeneme_toolbar() {
            this.actionDeneme_toolbar = new qx.ui.toolbar.Button();
            var retval  =  this.actionDeneme_toolbar;
            retval.setLabel(this.tr("deneme"));
            return retval;

        }

        ,create_actionFineMenuItem_menu: function create_actionFineMenuItem_menu() {
            this.actionFineMenuItem_menu = new qx.ui.menu.Button();
            var retval  =  this.actionFineMenuItem_menu;
            retval.setLabel(this.tr("FineMenuItem"));
            retval.setMargin(1);
            return retval;

        }

        ,create_actionMenuItem1_menu: function create_actionMenuItem1_menu() {
            this.actionMenuItem1_menu = new qx.ui.menu.Button();
            var retval  =  this.actionMenuItem1_menu;
            retval.setLabel(this.tr("MenuItem1"));
            retval.setMargin(1);
            return retval;

        }

        ,create_actionMenuItem1_toolbar: function create_actionMenuItem1_toolbar() {
            this.actionMenuItem1_toolbar = new qx.ui.toolbar.Button();
            var retval  =  this.actionMenuItem1_toolbar;
            retval.setLabel(this.tr("MenuItem1"));
            return retval;

        }

        ,create_actionSubMenuItem1_menu: function create_actionSubMenuItem1_menu() {
            this.actionSubMenuItem1_menu = new qx.ui.menu.Button();
            var retval  =  this.actionSubMenuItem1_menu;
            retval.setLabel(this.tr("SubMenuItem1"));
            retval.setMargin(1);
            return retval;

        }

        ,create_actionSubMenuItem2_menu: function create_actionSubMenuItem2_menu() {
            this.actionSubMenuItem2_menu = new qx.ui.menu.Button();
            var retval  =  this.actionSubMenuItem2_menu;
            retval.setLabel(this.tr("SubMenuItem2"));
            retval.setMargin(1);
            return retval;

        }

        ,create_actionSubMenuItem3_menu: function create_actionSubMenuItem3_menu() {
            this.actionSubMenuItem3_menu = new qx.ui.menu.Button();
            var retval  =  this.actionSubMenuItem3_menu;
            retval.setLabel(this.tr("SubMenuItem3"));
            retval.setMargin(1);
            return retval;

        }

        ,create_actionToolBarAction1_toolbar: function create_actionToolBarAction1_toolbar() {
            this.actionToolBarAction1_toolbar = new qx.ui.toolbar.Button();
            var retval  =  this.actionToolBarAction1_toolbar;
            retval.setLabel(this.tr("ToolBarAction1"));
            return retval;

        }

        ,create_actionZopa_toolbar: function create_actionZopa_toolbar() {
            this.actionZopa_toolbar = new qx.ui.toolbar.Button();
            var retval  =  this.actionZopa_toolbar;
            retval.setLabel(this.tr("zopa"));
            return retval;

        }

        ,create_centralwidget: function create_centralwidget() {
            this.centralwidget = new qx.ui.container.Composite(this.create_verticalLayout());
            var retval  =  this.centralwidget;
            retval.setMargin(1);
            retval.add(this.create_splitter(), {flex: 1});
            return retval;

        }

        ,create_checkBox: function create_checkBox() {
            this.checkBox = new qx.ui.form.CheckBox();
            var retval  =  this.checkBox;
            retval.setLabel(this.tr("CheckBox"));
            retval.setMargin(1);
            return retval;

        }

        ,create_checkBox_2: function create_checkBox_2() {
            this.checkBox_2 = new qx.ui.form.CheckBox();
            var retval  =  this.checkBox_2;
            retval.setLabel(this.tr("CheckBox"));
            retval.setMargin(1);
            return retval;

        }

        ,create_checkBox_3: function create_checkBox_3() {
            this.checkBox_3 = new qx.ui.form.CheckBox();
            var retval  =  this.checkBox_3;
            retval.setLabel(this.tr("CheckBox"));
            retval.setMargin(1);
            return retval;

        }

        ,create_checkBox_4: function create_checkBox_4() {
            this.checkBox_4 = new qx.ui.form.CheckBox();
            var retval  =  this.checkBox_4;
            retval.setLabel(this.tr("CheckBox"));
            retval.setMargin(1);
            return retval;

        }

        ,create_comboBox: function create_comboBox() {
            this.comboBox = new qx.ui.form.SelectBox();
            var retval  =  this.comboBox;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            retval.add(new qx.ui.form.ListItem(this.tr("asd"),null,null));
            return retval;

        }

        ,create_dateEdit: function create_dateEdit() {
            this.dateEdit = new qx.ui.form.DateField();
            var retval  =  this.dateEdit;
            retval.setMargin(1);
            return retval;

        }

        ,create_gridLayout: function create_gridLayout() {
            this.gridLayout = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout;
            return retval;

        }

        ,create_gridLayout_2: function create_gridLayout_2() {
            this.gridLayout_2 = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout_2;
            return retval;

        }

        ,create_gridLayout_3: function create_gridLayout_3() {
            this.gridLayout_3 = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout_3;
            return retval;

        }

        ,create_gridLayout_4: function create_gridLayout_4() {
            this.gridLayout_4 = new qx.ui.layout.Grid();
            var retval  =  this.gridLayout_4;
            return retval;

        }

        ,create_groupBox: function create_groupBox() {
            this.groupBox = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox;
            retval.setMaxHeight(150);
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_7());
            retval.add(this.create_checkBox(), {flex: 1});
            retval.add(this.create_checkBox_2(), {flex: 1});
            retval.add(this.create_checkBox_3(), {flex: 1});
            retval.add(this.create_checkBox_4(), {flex: 1});
            return retval;

        }

        ,create_groupBox_10: function create_groupBox_10() {
            this.groupBox_10 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_10;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_10_il());
            return retval;

        }

        ,create_groupBox_10_il: function create_groupBox_10_il() {
            this.groupBox_10_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_10_il;
            return retval;

        }

        ,create_groupBox_11: function create_groupBox_11() {
            this.groupBox_11 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_11;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_11_il());
            return retval;

        }

        ,create_groupBox_11_il: function create_groupBox_11_il() {
            this.groupBox_11_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_11_il;
            return retval;

        }

        ,create_groupBox_15: function create_groupBox_15() {
            this.groupBox_15 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_15;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_15_il());
            return retval;

        }

        ,create_groupBox_15_il: function create_groupBox_15_il() {
            this.groupBox_15_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_15_il;
            return retval;

        }

        ,create_groupBox_16: function create_groupBox_16() {
            this.groupBox_16 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_16;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_16_il());
            return retval;

        }

        ,create_groupBox_16_il: function create_groupBox_16_il() {
            this.groupBox_16_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_16_il;
            return retval;

        }

        ,create_groupBox_2: function create_groupBox_2() {
             /* The 'spacing' property for widget named 'groupBox_2'of type '<class 'jsqt.il.qt.container.QGroupBox'>' is not supported (yet?) */

             /* The 'leftMargin' property for widget named 'groupBox_2'of type '<class 'jsqt.il.qt.container.QGroupBox'>' is not supported (yet?) */

             /* The 'topMargin' property for widget named 'groupBox_2'of type '<class 'jsqt.il.qt.container.QGroupBox'>' is not supported (yet?) */

             /* The 'rightMargin' property for widget named 'groupBox_2'of type '<class 'jsqt.il.qt.container.QGroupBox'>' is not supported (yet?) */

             /* The 'bottomMargin' property for widget named 'groupBox_2'of type '<class 'jsqt.il.qt.container.QGroupBox'>' is not supported (yet?) */

            this.groupBox_2 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_2;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_6());
            retval.add(this.create_radioButton(), {flex: 1});
            retval.add(this.create_radioButton_2(), {flex: 1});
            retval.add(this.create_radioButton_3(), {flex: 1});
            retval.add(this.create_radioButton_4(), {flex: 1});
            return retval;

        }

        ,create_groupBox_3: function create_groupBox_3() {
            this.groupBox_3 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_3;
            retval.setHeight(500);
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setMinHeight(500);
            retval.setLayout(this.create_verticalLayout_8());
            retval.add(this.create_label_3(), {flex: 1});
            retval.add(this.create_label_4(), {flex: 1});
            retval.add(this.create_verticalSpacer_2(), {flex: 1});
            return retval;

        }

        ,create_groupBox_4: function create_groupBox_4() {
            this.groupBox_4 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_4;
            retval.setMaxHeight(150);
            retval.setMaxWidth(300);
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_gridLayout_3());
            retval.add(this.create_dateEdit(), {column: 0,row: 0});
            retval.add(this.create_textEdit(), {column: 1,row: 0,rowSpan: 4});
            retval.add(this.create_lineEdit(), {column: 0,row: 2});
            retval.add(this.create_spinBox(), {column: 0,row: 1});
            var layout  =  retval.getLayout();
            layout.setRowFlex(0,1);
            layout.setRowFlex(1,1);
            layout.setRowFlex(2,1);
            layout.setColumnFlex(0,1);
            layout.setColumnFlex(1,1);
            return retval;

        }

        ,create_groupBox_6: function create_groupBox_6() {
            this.groupBox_6 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_6;
            retval.setHeight(500);
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setMinHeight(500);
            retval.setLayout(this.create_groupBox_6_il());
            return retval;

        }

        ,create_groupBox_6_il: function create_groupBox_6_il() {
            this.groupBox_6_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_6_il;
            return retval;

        }

        ,create_groupBox_7: function create_groupBox_7() {
            this.groupBox_7 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_7;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_7_il());
            return retval;

        }

        ,create_groupBox_7_il: function create_groupBox_7_il() {
            this.groupBox_7_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_7_il;
            return retval;

        }

        ,create_groupBox_8: function create_groupBox_8() {
            this.groupBox_8 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_8;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_8_il());
            return retval;

        }

        ,create_groupBox_8_il: function create_groupBox_8_il() {
            this.groupBox_8_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_8_il;
            return retval;

        }

        ,create_groupBox_bl: function create_groupBox_bl() {
            this.groupBox_bl = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_bl;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_bl_il());
            return retval;

        }

        ,create_groupBox_bl_2: function create_groupBox_bl_2() {
            this.groupBox_bl_2 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_bl_2;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_bl_2_il());
            return retval;

        }

        ,create_groupBox_bl_2_il: function create_groupBox_bl_2_il() {
            this.groupBox_bl_2_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_bl_2_il;
            return retval;

        }

        ,create_groupBox_bl_il: function create_groupBox_bl_il() {
            this.groupBox_bl_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_bl_il;
            return retval;

        }

        ,create_groupBox_br: function create_groupBox_br() {
            this.groupBox_br = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_br;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_br_il());
            return retval;

        }

        ,create_groupBox_br_2: function create_groupBox_br_2() {
            this.groupBox_br_2 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_br_2;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_br_2_il());
            return retval;

        }

        ,create_groupBox_br_2_il: function create_groupBox_br_2_il() {
            this.groupBox_br_2_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_br_2_il;
            return retval;

        }

        ,create_groupBox_br_il: function create_groupBox_br_il() {
            this.groupBox_br_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_br_il;
            return retval;

        }

        ,create_groupBox_centered: function create_groupBox_centered() {
            this.groupBox_centered = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_centered;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout_3());
            retval.add(this.create_comboBox(), {flex: 1});
            return retval;

        }

        ,create_groupBox_tl: function create_groupBox_tl() {
            this.groupBox_tl = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_tl;
            retval.setHeight(100);
            retval.setWidth(100);
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setMinWidth(100);
            retval.setMinHeight(100);
            retval.setAllowGrowX(false);
            retval.setAllowGrowY(false);
            retval.setLayout(this.create_verticalLayout_5());
            return retval;

        }

        ,create_groupBox_tl_2: function create_groupBox_tl_2() {
            this.groupBox_tl_2 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_tl_2;
            retval.setHeight(100);
            retval.setWidth(100);
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setMinWidth(100);
            retval.setMinHeight(100);
            retval.setAllowGrowX(false);
            retval.setAllowGrowY(false);
            retval.setLayout(this.create_verticalLayout_9());
            retval.add(this.create_textEdit_3(), {flex: 1});
            return retval;

        }

        ,create_groupBox_tr: function create_groupBox_tr() {
            this.groupBox_tr = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_tr;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_tr_il());
            return retval;

        }

        ,create_groupBox_tr_2: function create_groupBox_tr_2() {
            this.groupBox_tr_2 = new qx.ui.groupbox.GroupBox();
            var retval  =  this.groupBox_tr_2;
            retval.setLegend(this.tr("GroupBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_groupBox_tr_2_il());
            return retval;

        }

        ,create_groupBox_tr_2_il: function create_groupBox_tr_2_il() {
            this.groupBox_tr_2_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_tr_2_il;
            return retval;

        }

        ,create_groupBox_tr_il: function create_groupBox_tr_il() {
            this.groupBox_tr_il = new qx.ui.layout.Canvas();
            var retval  =  this.groupBox_tr_il;
            return retval;

        }

        ,create_horizontalLayout: function create_horizontalLayout() {
            this.horizontalLayout = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout;
            return retval;

        }

        ,create_horizontalLayout_2: function create_horizontalLayout_2() {
            this.horizontalLayout_2 = new qx.ui.layout.HBox();
            var retval  =  this.horizontalLayout_2;
            return retval;

        }

        ,create_horizontalLayout_2_implicit_container: function create_horizontalLayout_2_implicit_container() {
            this.horizontalLayout_2_implicit_container = new qx.ui.container.Composite(this.create_horizontalLayout_2());
            var retval  =  this.horizontalLayout_2_implicit_container;
            retval.setMargin(1);
            retval.add(this.create_groupBox_centered(), {flex: 1});
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
            this.horizontalLayout_4_implicit_container = new qx.ui.container.Composite(this.create_horizontalLayout_4());
            var retval  =  this.horizontalLayout_4_implicit_container;
            retval.setMargin(1);
            retval.add(this.create_horizontalSpacer(), {flex: 1});
            retval.add(this.create_groupBox_4(), {flex: 1});
            retval.add(this.create_horizontalSpacer_2(), {flex: 1});
            return retval;

        }

        ,create_horizontalSpacer: function create_horizontalSpacer() {
             /* The 'orientation' property for widget named 'horizontalSpacer'of type '<class 'jsqt.il.qt.gui.QSpacer'>' is not supported (yet?) */

            this.horizontalSpacer = new qx.ui.core.Spacer();
            var retval  =  this.horizontalSpacer;
            retval.setHeight(20);
            retval.setWidth(40);
            retval.setMargin(1);
            return retval;

        }

        ,create_horizontalSpacer_2: function create_horizontalSpacer_2() {
             /* The 'orientation' property for widget named 'horizontalSpacer_2'of type '<class 'jsqt.il.qt.gui.QSpacer'>' is not supported (yet?) */

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
            retval.setHeight(21);
            retval.setWidth(161);
            retval.setValue(this.tr("Signals do not work yet."));
            retval.setMargin(1);
            return retval;

        }

        ,create_label_2: function create_label_2() {
            this.label_2 = new qx.ui.basic.Label();
            var retval  =  this.label_2;
            retval.setHeight(31);
            retval.setWidth(131);
            retval.setValue(this.tr("hello"));
            retval.setMargin(1);
            return retval;

        }

        ,create_label_3: function create_label_3() {
            this.label_3 = new qx.ui.basic.Label();
            var retval  =  this.label_3;
            retval.setValue(this.tr("TextLabel"));
            retval.setMargin(1);
            return retval;

        }

        ,create_label_4: function create_label_4() {
            this.label_4 = new qx.ui.basic.Label();
            var retval  =  this.label_4;
            retval.setValue(this.tr("TextLabel"));
            retval.setMargin(1);
            return retval;

        }

        ,create_lineEdit: function create_lineEdit() {
            this.lineEdit = new qx.ui.form.TextField();
            var retval  =  this.lineEdit;
            retval.setMargin(1);
            return retval;

        }

        ,create_listWidget: function create_listWidget() {
            this.listWidget = new qx.ui.form.List();
            var retval  =  this.listWidget;
            retval.setHeight(192);
            retval.setWidth(256);
            retval.setMargin(1);
            return retval;

        }

        ,create_menuMenu1: function create_menuMenu1() {
            this.menuMenu1 = new qx.ui.menubar.Button();
            var retval  =  this.menuMenu1;
            retval.setLabel(this.tr("Menu1"));
            retval.setMargin(1);
            retval.setMenu(this.create_menuMenu1_implicit_menu());
            return retval;

        }

        ,create_menuMenu1_implicit_menu: function create_menuMenu1_implicit_menu() {
            this.menuMenu1_implicit_menu = new qx.ui.menu.Menu();
            var retval  =  this.menuMenu1_implicit_menu;
            retval.setMargin(1);
            retval.add(this.create_actionMenuItem1_menu());
            retval.addSeparator();
            retval.add(this.create_menuMenuItem2());
            return retval;

        }

        ,create_menuMenu2: function create_menuMenu2() {
            this.menuMenu2 = new qx.ui.menubar.Button();
            var retval  =  this.menuMenu2;
            retval.setLabel(this.tr("Menu2"));
            retval.setMargin(1);
            retval.setMenu(this.create_menuMenu2_implicit_menu());
            return retval;

        }

        ,create_menuMenu2_implicit_menu: function create_menuMenu2_implicit_menu() {
            this.menuMenu2_implicit_menu = new qx.ui.menu.Menu();
            var retval  =  this.menuMenu2_implicit_menu;
            retval.setMargin(1);
            retval.add(this.create_actionFineMenuItem_menu());
            retval.addSeparator();
            retval.add(this.create_FinestMenuItem_menu());
            return retval;

        }

        ,create_menuMenuItem2: function create_menuMenuItem2() {
            this.menuMenuItem2 = new qx.ui.menu.Button();
            var retval  =  this.menuMenuItem2;
            retval.setLabel(this.tr("MenuItem2"));
            retval.setMargin(1);
            retval.setMenu(this.create_menuMenuItem2_implicit_menu());
            return retval;

        }

        ,create_menuMenuItem2_implicit_menu: function create_menuMenuItem2_implicit_menu() {
            this.menuMenuItem2_implicit_menu = new qx.ui.menu.Menu();
            var retval  =  this.menuMenuItem2_implicit_menu;
            retval.setMargin(1);
            retval.add(this.create_actionSubMenuItem1_menu());
            retval.add(this.create_actionSubMenuItem2_menu());
            retval.addSeparator();
            retval.add(this.create_actionSubMenuItem3_menu());
            return retval;

        }

        ,create_menubar: function create_menubar() {
             /* The 'addaction' tag for widget named 'menubar'of type '<class 'jsqt.il.qt.bar.QMenuBar'>' is not supported (yet?) */

             /* The 'addaction' tag for widget named 'menubar'of type '<class 'jsqt.il.qt.bar.QMenuBar'>' is not supported (yet?) */

            this.menubar = new qx.ui.menubar.MenuBar();
            var retval  =  this.menubar;
            retval.setHeight(28);
            retval.setWidth(774);
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            retval.add(this.create_menuMenu1());
            retval.add(this.create_menuMenu2());
            return retval;

        }

        ,create_pushButton: function create_pushButton() {
            this.pushButton = new qx.ui.form.Button();
            var retval  =  this.pushButton;
            retval.setHeight(28);
            retval.setWidth(81);
            retval.setLabel(this.tr("Clear"));
            retval.setMargin(1);
            return retval;

        }

        ,create_pushButton_2: function create_pushButton_2() {
            this.pushButton_2 = new qx.ui.form.Button();
            var retval  =  this.pushButton_2;
            retval.setHeight(28);
            retval.setWidth(81);
            retval.setLabel(this.tr("nothing"));
            retval.setMargin(1);
            return retval;

        }

        ,create_radioButton: function create_radioButton() {
            this.radioButton = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton;
            retval.setLabel(this.tr("RadioButton"));
            retval.setMargin(1);
            return retval;

        }

        ,create_radioButton_2: function create_radioButton_2() {
            this.radioButton_2 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_2;
            retval.setLabel(this.tr("RadioButton"));
            retval.setMargin(1);
            return retval;

        }

        ,create_radioButton_3: function create_radioButton_3() {
            this.radioButton_3 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_3;
            retval.setLabel(this.tr("RadioButton"));
            retval.setMargin(1);
            return retval;

        }

        ,create_radioButton_4: function create_radioButton_4() {
            this.radioButton_4 = new qx.ui.form.RadioButton();
            var retval  =  this.radioButton_4;
            retval.setLabel(this.tr("RadioButton"));
            retval.setMargin(1);
            return retval;

        }

        ,create_scrollArea: function create_scrollArea() {
             /* The 'widgetResizable' property for widget named 'scrollArea'of type '<class 'jsqt.il.qt.container.QScrollArea'>' is not supported (yet?) */

            this.scrollArea = new qx.ui.container.Scroll();
            var retval  =  this.scrollArea;
            retval.setMaxHeight(200);
            retval.setMargin(1);
            retval.add(this.create_scrollAreaWidgetContents(), {left: 0,top: 0});
            return retval;

        }

        ,create_scrollAreaWidgetContents: function create_scrollAreaWidgetContents() {
            this.scrollAreaWidgetContents = new qx.ui.container.Composite(this.create_verticalLayout_2());
            var retval  =  this.scrollAreaWidgetContents;
            retval.setHeight(518);
            retval.setWidth(765);
            retval.setMargin(1);
            retval.add(this.create_groupBox_3(), {flex: 1});
            return retval;

        }

        ,create_scrollAreaWidgetContents_2: function create_scrollAreaWidgetContents_2() {
            this.scrollAreaWidgetContents_2 = new qx.ui.container.Composite(this.create_verticalLayout_3());
            var retval  =  this.scrollAreaWidgetContents_2;
            retval.setHeight(518);
            retval.setWidth(458);
            retval.setMargin(1);
            retval.add(this.create_groupBox_6(), {flex: 1});
            return retval;

        }

        ,create_scrollArea_2: function create_scrollArea_2() {
             /* The 'widgetResizable' property for widget named 'scrollArea_2'of type '<class 'jsqt.il.qt.container.QScrollArea'>' is not supported (yet?) */

            this.scrollArea_2 = new qx.ui.container.Scroll();
            var retval  =  this.scrollArea_2;
            retval.setMaxHeight(200);
            retval.setMaxWidth(500);
            retval.setMargin(1);
            retval.add(this.create_scrollAreaWidgetContents_2(), {left: 0,top: 0});
            return retval;

        }

        ,create_spinBox: function create_spinBox() {
            this.spinBox = new qx.ui.form.Spinner();
            var retval  =  this.spinBox;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            return retval;

        }

        ,create_splitter: function create_splitter() {
             /* The 'orientation' property for widget named 'splitter'of type '<class 'jsqt.il.qt.container.QSplitter'>' is not supported (yet?) */

            this.splitter = new qx.ui.splitpane.Pane("horizontal");
            var retval  =  this.splitter;
            retval.setMargin(1);
            retval.add(this.create_treeWidget(),1);
            retval.add(this.create_tabWidget(),1);
            return retval;

        }

        ,create_tab: function create_tab() {
            this.tab = new qx.ui.tabview.Page();
            var retval  =  this.tab;
            retval.setLabel(this.tr("Canvas"));
            retval.setMargin(1);
            retval.setLayout(this.create_tab_il());
            retval.add(this.create_pushButton_2(), {left: 60,top: 110});
            retval.add(this.create_label_2(), {left: 230,top: 80});
            retval.add(this.create_tableWidget(), {left: 20,top: 210});
            retval.add(this.create_listWidget(), {left: 310,top: 220});
            return retval;

        }

        ,create_tabWidget: function create_tabWidget() {
             /* The 'toolTip' property for widget named 'tabWidget'of type '<class 'jsqt.il.qt.container.QTabWidget'>' is not supported (yet?) */

             /* The 'currentIndex' property for widget named 'tabWidget'of type '<class 'jsqt.il.qt.container.QTabWidget'>' is not supported (yet?) */

            this.tabWidget = new qx.ui.tabview.TabView();
            var retval  =  this.tabWidget;
            retval.setMargin(1);
            retval.add(this.create_tab());
            retval.add(this.create_tab_2());
            retval.add(this.create_tab_3());
            retval.add(this.create_tab_4());
            retval.add(this.create_tab_grid_fixed());
            retval.add(this.create_tab_grid_fixed_filled());
            retval.add(this.create_tab_6());
            return retval;

        }

        ,create_tab_2: function create_tab_2() {
            this.tab_2 = new qx.ui.tabview.Page();
            var retval  =  this.tab_2;
            retval.setLabel(this.tr("HBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_horizontalLayout());
            retval.add(this.create_groupBox_2(), {flex: 1});
            retval.add(this.create_groupBox(), {flex: 1});
            retval.add(this.create_scrollArea(), {flex: 2});
            return retval;

        }

        ,create_tab_3: function create_tab_3() {
            this.tab_3 = new qx.ui.tabview.Page();
            var retval  =  this.tab_3;
            retval.setLabel(this.tr("VBox"));
            retval.setMargin(1);
            retval.setLayout(this.create_verticalLayout_4());
            retval.add(this.create_horizontalLayout_2_implicit_container(), {flex: 1});
            retval.add(this.create_scrollArea_2(), {flex: 3});
            retval.add(this.create_horizontalLayout_4_implicit_container(), {flex: 1});
            return retval;

        }

        ,create_tab_4: function create_tab_4() {
            this.tab_4 = new qx.ui.tabview.Page();
            var retval  =  this.tab_4;
            retval.setLabel(this.tr("Grid Span"));
            retval.setMargin(1);
            retval.setLayout(this.create_gridLayout());
            retval.add(this.create_groupBox_7(), {column: 0,row: 1,rowSpan: 2});
            retval.add(this.create_groupBox_8(), {column: 1,row: 1});
            retval.add(this.create_groupBox_10(), {column: 1,row: 2});
            retval.add(this.create_groupBox_11(), {colSpan: 2,column: 0,row: 3});
            retval.add(this.create_groupBox_15(), {colSpan: 2,column: 0,row: 0});
            retval.add(this.create_groupBox_16(), {column: 2,row: 0,rowSpan: 4});
            var layout  =  retval.getLayout();
            layout.setRowFlex(0,1);
            layout.setRowFlex(1,1);
            layout.setRowFlex(2,1);
            layout.setRowFlex(3,1);
            layout.setColumnFlex(0,1);
            layout.setColumnFlex(1,1);
            layout.setColumnFlex(2,1);
            return retval;

        }

        ,create_tab_6: function create_tab_6() {
            this.tab_6 = new qx.ui.tabview.Page();
            var retval  =  this.tab_6;
            retval.setLabel(this.tr("Signals"));
            retval.setMargin(1);
            retval.setLayout(this.create_tab_6_il());
            retval.add(this.create_pushButton(), {left: 30,top: 30});
            retval.add(this.create_label(), {left: 170,top: 40});
            return retval;

        }

        ,create_tab_6_il: function create_tab_6_il() {
            this.tab_6_il = new qx.ui.layout.Canvas();
            var retval  =  this.tab_6_il;
            return retval;

        }

        ,create_tab_grid_fixed: function create_tab_grid_fixed() {
            this.tab_grid_fixed = new qx.ui.tabview.Page();
            var retval  =  this.tab_grid_fixed;
            retval.setLabel(this.tr("Grid Fixed Empty"));
            retval.setMargin(1);
            retval.setLayout(this.create_gridLayout_2());
            retval.add(this.create_groupBox_tl(), {column: 0,row: 0});
            retval.add(this.create_groupBox_tr(), {column: 1,row: 0});
            retval.add(this.create_groupBox_br(), {column: 1,row: 1});
            retval.add(this.create_groupBox_bl(), {column: 0,row: 1});
            var layout  =  retval.getLayout();
            layout.setRowFlex(0,0);
            layout.setRowFlex(1,1);
            layout.setColumnFlex(0,0);
            layout.setColumnFlex(1,1);
            return retval;

        }

        ,create_tab_grid_fixed_filled: function create_tab_grid_fixed_filled() {
            this.tab_grid_fixed_filled = new qx.ui.tabview.Page();
            var retval  =  this.tab_grid_fixed_filled;
            retval.setLabel(this.tr("Grid Fixed Filled"));
            retval.setMargin(1);
            retval.setLayout(this.create_gridLayout_4());
            retval.add(this.create_groupBox_tl_2(), {column: 0,row: 0});
            retval.add(this.create_groupBox_tr_2(), {column: 1,row: 0});
            retval.add(this.create_groupBox_bl_2(), {column: 0,row: 1});
            retval.add(this.create_groupBox_br_2(), {column: 1,row: 1});
            var layout  =  retval.getLayout();
            layout.setRowFlex(0,0);
            layout.setRowFlex(1,1);
            layout.setColumnFlex(0,0);
            layout.setColumnFlex(1,1);
            return retval;

        }

        ,create_tab_il: function create_tab_il() {
            this.tab_il = new qx.ui.layout.Canvas();
            var retval  =  this.tab_il;
            return retval;

        }

        ,create_tableWidget: function create_tableWidget() {
            this.tableWidget = new qx.ui.table.Table();
            var retval  =  this.tableWidget;
            retval.setHeight(192);
            retval.setWidth(256);
            retval.setMargin(1);
            return retval;

        }

        ,create_textEdit: function create_textEdit() {
            this.textEdit = new qx.ui.form.TextArea();
            var retval  =  this.textEdit;
            retval.setMargin(1);
            return retval;

        }

        ,create_textEdit_3: function create_textEdit_3() {
            this.textEdit_3 = new qx.ui.form.TextArea();
            var retval  =  this.textEdit_3;
            retval.setMargin(1);
            return retval;

        }

        ,create_toolBar: function create_toolBar() {
             /* The 'windowTitle' property for widget named 'toolBar'of type '<class 'jsqt.il.qt.bar.QToolBar'>' is not supported (yet?) */

             /* The 'toolBarBreak' property for widget named 'toolBar'of type '<class 'jsqt.il.qt.bar.QToolBar'>' is not supported (yet?) */

            this.toolBar = new qx.ui.toolbar.ToolBar();
            var retval  =  this.toolBar;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            retval.add(this.create_actionMenuItem1_toolbar());
            retval.add(new qx.ui.toolbar.Separator());
            retval.add(this.create_actionToolBarAction1_toolbar());
            return retval;

        }

        ,create_toolBar_2: function create_toolBar_2() {
             /* The 'windowTitle' property for widget named 'toolBar_2'of type '<class 'jsqt.il.qt.bar.QToolBar'>' is not supported (yet?) */

             /* The 'toolBarBreak' property for widget named 'toolBar_2'of type '<class 'jsqt.il.qt.bar.QToolBar'>' is not supported (yet?) */

            this.toolBar_2 = new qx.ui.toolbar.ToolBar();
            var retval  =  this.toolBar_2;
            retval.setMargin(1);
            retval.setAllowGrowY(false);
            retval.add(this.create_actionDeneme_toolbar());
            retval.add(this.create_actionZopa_toolbar());
            return retval;

        }

        ,create_treeWidget: function create_treeWidget() {
             /* The 'headerVisible' property for widget named 'treeWidget'of type '<class 'jsqt.il.qt.itemview.QTreeWidget'>' is not supported (yet?) */

             /* The 'column' tag for widget named 'treeWidget'of type '<class 'jsqt.il.qt.itemview.QTreeWidget'>' is not supported (yet?) */

             /* The 'item' tag for widget named 'treeWidget'of type '<class 'jsqt.il.qt.itemview.QTreeWidget'>' is not supported (yet?) */

             /* The 'item' tag for widget named 'treeWidget'of type '<class 'jsqt.il.qt.itemview.QTreeWidget'>' is not supported (yet?) */

             /* The 'item' tag for widget named 'treeWidget'of type '<class 'jsqt.il.qt.itemview.QTreeWidget'>' is not supported (yet?) */

             /* The 'item' tag for widget named 'treeWidget'of type '<class 'jsqt.il.qt.itemview.QTreeWidget'>' is not supported (yet?) */

            this.treeWidget = new qx.ui.tree.Tree();
            var retval  =  this.treeWidget;
            retval.setMaxWidth(250);
            retval.setMargin(1);
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

        ,create_verticalLayout_7: function create_verticalLayout_7() {
            this.verticalLayout_7 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_7;
            return retval;

        }

        ,create_verticalLayout_8: function create_verticalLayout_8() {
            this.verticalLayout_8 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_8;
            return retval;

        }

        ,create_verticalLayout_9: function create_verticalLayout_9() {
            this.verticalLayout_9 = new qx.ui.layout.VBox();
            var retval  =  this.verticalLayout_9;
            return retval;

        }

        ,create_verticalSpacer_2: function create_verticalSpacer_2() {
             /* The 'orientation' property for widget named 'verticalSpacer_2'of type '<class 'jsqt.il.qt.gui.QSpacer'>' is not supported (yet?) */

            this.verticalSpacer_2 = new qx.ui.core.Spacer();
            var retval  =  this.verticalSpacer_2;
            retval.setHeight(411);
            retval.setWidth(20);
            retval.setMargin(1);
            return retval;

        }

        ,dateEdit: null
        ,gridLayout: null
        ,gridLayout_2: null
        ,gridLayout_3: null
        ,gridLayout_4: null
        ,groupBox: null
        ,groupBox_10: null
        ,groupBox_10_il: null
        ,groupBox_11: null
        ,groupBox_11_il: null
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
        ,groupBox_bl: null
        ,groupBox_bl_2: null
        ,groupBox_bl_2_il: null
        ,groupBox_bl_il: null
        ,groupBox_br: null
        ,groupBox_br_2: null
        ,groupBox_br_2_il: null
        ,groupBox_br_il: null
        ,groupBox_centered: null
        ,groupBox_tl: null
        ,groupBox_tl_2: null
        ,groupBox_tr: null
        ,groupBox_tr_2: null
        ,groupBox_tr_2_il: null
        ,groupBox_tr_il: null
        ,horizontalLayout: null
        ,horizontalLayout_2: null
        ,horizontalLayout_2_implicit_container: null
        ,horizontalLayout_3: null
        ,horizontalLayout_4: null
        ,horizontalLayout_4_implicit_container: null
        ,horizontalSpacer: null
        ,horizontalSpacer_2: null
        ,label: null
        ,label_2: null
        ,label_3: null
        ,label_4: null
        ,lineEdit: null
        ,listWidget: null
        ,menuMenu1: null
        ,menuMenu1_implicit_menu: null
        ,menuMenu2: null
        ,menuMenu2_implicit_menu: null
        ,menuMenuItem2: null
        ,menuMenuItem2_implicit_menu: null
        ,menubar: null
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
        ,tab_6: null
        ,tab_6_il: null
        ,tab_grid_fixed: null
        ,tab_grid_fixed_filled: null
        ,tab_il: null
        ,tableWidget: null
        ,textEdit: null
        ,textEdit_3: null
        ,toolBar: null
        ,toolBar_2: null
        ,treeWidget: null
        ,verticalLayout: null
        ,verticalLayout_2: null
        ,verticalLayout_3: null
        ,verticalLayout_4: null
        ,verticalLayout_5: null
        ,verticalLayout_6: null
        ,verticalLayout_7: null
        ,verticalLayout_8: null
        ,verticalLayout_9: null
        ,verticalSpacer_2: null
    }

    ,properties:  {
        widget:  {
            check: "qx.ui.container.Composite"
        }

    }

}
);
