#summary Known Widgets and their status
#labels Featured

Here are the known widgets, and their level of support. Widgets that are not mentioned here are not yet even been considered for code generation.

===Layouts===
<table border="1" cellpadding="7">
  <tr>
     <td></td>
     <td>*What works*</td>
     <td>*What doesn't*</td>
  </tr>
  <tr>
     <td>*Canvas*</td>
     <td>It mostly works. You can alter QWidget::geometry property in order to obtain the arrangement you want. It passes `top` and `left` parameters to the <a href="http://demo.qooxdoo.org/current/apiviewer/#qx.ui.container.Composite~add">add</a> function from QWidget::geometry::Y and QWidget::geometry::X respectively.</td>
     <td>The `left` and `bottom` properties are not supported. Qt does not seem to support this form of arrangement. (I may be wrong) You can use fixed-size spacers to get the same effect.</td>
  </tr>
  <tr>
     <td>*VBox* and *HBox*</td>
     <td>They mostly work. You can set Horizontal and Vertical stretch coefficients under the QWidget::sizePolicy property to change the parameter that goes with `flex` when adding a widget inside a container with these two layouts.</td>
     <td>Horizontal and vertical alignment don't work as Qt Designer lacks those options in its user interface. (Qt itself supports alignment. see [http://doc.trolltech.com/4.5/qboxlayout.html#addWidget here]) You can use double spacers around what needs to be centered, as with the widget named `groupBox_centered` inside `test/source/xml/draw/Test.ui`</td>
  </tr>
  <tr>
     <td>*Grid*</td>
     <td>Again, it mostly works. You can set Horizontal and Vertical stretch coefficients under the QWidget::sizePolicy property to produce `[http://demo.qooxdoo.org/current/apiviewer/#qx.ui.layout.Grid~setRowFlex setRowFlex]` and `[http://demo.qooxdoo.org/current/apiviewer/#qx.ui.layout.Grid~setColumnFlex setColumnFlex]` calls in the factory function. (see</td>
     <td>Same comments about alignment apply. Use spacers or override and extend the factory classes to your liking.</td>
  </tr>
  <tr>
     <td>*QFormLayout*</td>
     <td>It's not supported.</td>
     <td>Qooxdoo does not seem to have a direct equivalent.</td>
  </tr>
</table>

==Core Widgets and Containers==

|| *Class*               || *Property*                || *Works* ||
|| QWidget               || enabled                   ||         ||
||                       || geometry                  ||  *X*    ||
||                       || sizePolicy                ||  *X*    ||
||                       || minimumSize               ||  *X*    ||
||                       || maximumSize               ||  *X*    ||
||                       || sizeIncrement             ||         ||
||                       || baseSize                  ||         ||
||                       || palette                   ||         ||
||                       || font                      ||         ||
||                       || cursor                    ||         ||
||                       || mouseTracking             ||         ||
||                       || focusPolicy               ||         ||
||                       || contextMenuPolicy         ||         ||
||                       || acceptDrops               ||         ||
||                       || toolTip                   ||         ||
||                       || statusTip                 ||         ||
||                       || whatsThis                 ||         ||
||                       || accessibleName            ||         ||
||                       || accessibleDescription     ||         ||
||                       || layoutDirection           ||         ||
||                       || autoFillBackground        ||         ||
||                       || styleSheet                ||         ||
||                       || locale                    ||         ||
|| *Class*               || *Property*                || *Works* ||
|| QFrame                || frameShape                ||         ||
||                       || frameShadow               ||         ||
||                       || lineWidth                 ||         ||
||                       || midLineWidth              ||         ||
|| *Class*               || *Property*                || *Works* ||
|| QAbstractScrollArea   || verticalScrollBarPolicy   ||         ||
||                       || horizontalScrollBarPolicy ||         ||
|| *Class*               || *Property*                || *Works* ||
||  QScrollArea          || widgetResizable           ||         ||
||                       || alignment                 ||         ||

==QAbstractItemView and children==

|| *Class*               || *Property*                || *Works* ||
||  QAbstractItemView    || autoScroll                ||         ||
||                       || autoScrollMargin          ||         ||
||                       || editTriggers              ||         ||
||                       || tabKeyNavigation          ||         ||
||                       || showDropIndicator         ||         ||
||                       || dragEnabled               ||         ||
||                       || dragDropOverwriteMode     ||         ||
||                       || dragDropMode              ||         ||
||                       || alternatingRowColors      ||         ||
||                       || selectionMode             ||         ||
||                       || selectionBehavior         ||         ||
||                       || iconSize                  ||         ||
||                       || textElideMode             ||         ||
||                       || verticalScrollMode        ||         ||
||                       || horizontalScrollMode      ||         ||

===QTableWidget===
|| *Class*               || *Property*                || *Works* ||
||  QTableView           || showGrid                  ||         ||
||                       || gridStyle                 ||         ||
||                       || sortingEnabled            ||         ||
||                       || wordWrap                  ||         ||
||                       || cornerButtonEnabled       ||         ||
|| *Class*               || *Property*                || *Works* ||
||  QTableWidget         || rowCount                  ||         ||
||                       || columnCount               ||         ||

===QListWidget===
|| *Class*               || *Property*                || *Works* ||
|| QListView             || movement                  ||         ||
||                       || flow                      ||         ||
||                       || isWrapping                ||         ||
||                       || resizeMode                ||         ||
||                       || layoutMode                ||         ||
||                       || spacing                   ||         ||
||                       || gridSize                  ||         ||
||                       || viewMode                  ||         ||
||                       || modelColumn               ||         ||
||                       || uniformItemSizes          ||         ||
||                       || batchSize                 ||         ||
||                       || wordWrap                  ||         ||
||                       || selectionRectVisible      ||         ||
|| *Class*               || *Property*                || *Works* ||
|| QListWidget           || currentRow                ||         ||
||                       || sortingEnabled            ||         ||

== Bar Widgets ==
|| *Class*               || *Property*                || *Works* ||
|| QToolBar              || movable                   ||         ||
||                       || allowedAreas              ||         ||
||                       || orientation               ||         ||
||                       || iconSize                  ||         ||
||                       || toolButtonStyle           ||         ||
||                       || floating                  ||         ||
||                       || floatable                 ||         ||
||                       || toolBarArea               ||   *X*   ||

Other bar widgets (toolbar.Button, menubar.MenuBar, menubar.Button, menu.Button, etc.) have no explicit representation in Qt Designer

== Form Widgets ==

===QPushButton===
A derivative of QAbstractButton, which in turn is a derivative of QWidget

|| *Class*               || *Property*                || *Works* ||
|| QAbstractButton       || text                      ||   *X*   ||
||                       || icon                      ||         ||
||                       || iconSize                  ||         ||
||                       || shortcut                  ||         ||
||                       || checkable                 ||         ||
||                       || checked                   ||         ||
||                       || autoRepeat                ||         ||
||                       || autoExclusive             ||         ||
||                       || autoRepeatDelay           ||         ||
||                       || autoRepeatInterval        ||         ||
||                       || down                      ||         ||
|| *Class*               || *Property*                || *Works* ||
|| QPushButton           || autoDefault               ||         ||
||                       || default                   ||         ||
||                       || flat                      ||         ||

===QSpinBox===
A derivative of QAbstractSpinBox, which in turn is a derivative of QWidget

|| *Class*               || *Property*                || *Works* ||
|| QAbstractSpinBox      || wrapping                  ||         ||
||                       || frame                     ||         ||
||                       || alignment                 ||         ||
||                       || readOnly                  ||         ||
||                       || buttonSymbols             ||         ||
||                       || specialValueText          ||         ||
||                       || text                      ||         ||
||                       || accelerated               ||         ||
||                       || correctionMode            ||         ||
||                       || acceptableInput           ||         ||
||                       || keyboardTracking          ||         ||
|| *Class*               || *Property*                || *Works* ||
|| QSpinBox              || suffix                    ||         ||
||                       || prefix                    ||         ||
||                       || minimum                   ||   *X*   ||
||                       || maximum                   ||   *X*   ||
||                       || singleStep                ||   *X*   ||
||                       || value                     ||   *X*   ||

===QDateEdit===
A derivative of QDateTimeEdit, which in turn is a derivative of QAbstractSpinBox.

|| *Class*               || *Property*                || *Works* ||
|| QDateTimeEdit         || dateTime                  ||         ||
||                       || time                      ||         ||
||                       || maximumDateTime           ||         ||
||                       || minimumDateTime           ||         ||
||                       || maximumDate               ||         ||
||                       || minimumDate               ||         ||
||                       || maximumTime               ||         ||
||                       || minimumTime               ||         ||
||                       || currentSection            ||         ||
||                       || displayFormat             ||         ||
||                       || calendarPopup             ||         ||
||                       || currentSectionIndex       ||         ||
||                       || timeSpec                  ||         ||
||                       || time                      ||         ||
|| *Class*               || *Property*                || *Works* ||
|| QDateEdit             || date                      ||         ||

===QLineEdit===
A derivative of QWidget.

|| *Class*               || *Property*                || *Works* ||
|| QLineEdit             || inputMask                 ||         ||
||                       || text                      ||   *X*   ||
||                       || maxLength                 ||         ||
||                       || frame                     ||         ||
||                       || echoMode                  ||         ||
||                       || cursorPosition            ||         ||
||                       || alignment                 ||         ||
||                       || dragEnabled               ||         ||
||                       || readOnly                  ||         ||

===QTextEdit===
A derivative of QAbstractScrollArea.

|| *Class*               || *Property*                || *Works* ||
|| QTextEdit             || autoFormatting            ||         ||
||                       || tabChangesFocus           ||         ||
||                       || documentTitle             ||         ||
||                       || undoRedoEnabled           ||         ||
||                       || lineWrapMode              ||         ||
||                       || lineWrapColumnOrWidth     ||         ||
||                       || readOnly                  ||         ||
||                       || html                      ||         ||
||                       || plainText                 ||         ||
||                       || overwriteMode             ||         ||
||                       || tabStopWidth              ||         ||
||                       || acceptRichText            ||         ||
||                       || cursorWidth               ||         ||
||                       || textInteractionFlags      ||         ||

===QComboBox===
A derivative of QWidget.

|| *Class*               || *Property*                || *Works* ||
|| QComboBox             || editable                  ||         ||
||                       || currentIndex              ||         ||
||                       || maxVisibleItems           ||         ||
||                       || maxCount                  ||         ||
||                       || insertPolicy              ||         ||
||                       || sizeAdjustPolicy          ||         ||
||                       || minimumContentsLength     ||         ||
||                       || iconSize                  ||         ||
||                       || duplicatesEnabled         ||         ||
||                       || frame                     ||         ||
||                       || modelColumn               ||         ||

===QCheckBox===
A derivative of QAbstractButton

|| *Class*               || *Property*                || *Works* ||
|| QCheckBox             || tristate                  ||         ||

===QRadioButton===
A derivative of QAbstractButton. It supports grouping only via QGroupBox. It can't be grouped "virtually" (i.e. without using a non-visual grouping mechanism) using Qt Designer. See the [http://doc.trolltech.com/qbuttongroup.html#details documentation] of QButtonGroup and [http://lists.trolltech.com/qt-interest/2006-12/thread00131-0.html this thread] for relevant information.

<No own properties>

===QLabel===
A derivative of QFrame.

|| *Class*               || *Property*                || *Works* ||
|| QLabel                || text                      ||   *X*   ||
||                       || textFormat                ||         ||
||                       || pixmap                    ||         ||
||                       || scaledContents            ||         ||
||                       || alignment                 ||         ||
||                       || wordWrap                  ||         ||
||                       || margin                    ||         ||
||                       || indent                    ||         ||
||                       || openExternalLinks         ||         ||
||                       || textInteractionFlags      ||         ||
||                       || buddy                     ||         ||

== No Equivalents ==
The following widgets, among others, have no Qooxdoo equivalent: 
 * QDateTimeEdit
 * QTimeEdit