# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/wk/Tresors/VPT/Open eQuarter/Development/oeq_git/mole/view/ui_main_process_dock.ui'
#
# Created: Tue Dec  8 16:35:36 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainProcess_dock(object):
    def setupUi(self, MainProcess_dock):
        MainProcess_dock.setObjectName(_fromUtf8("MainProcess_dock"))
        MainProcess_dock.resize(374, 516)
        MainProcess_dock.setMinimumSize(QtCore.QSize(374, 500))
        MainProcess_dock.setStyleSheet(_fromUtf8("QStackedWidget QWidget {\n"
"    text-align: left;\n"
"}\n"
"\n"
"QStackedWidget QAbstractButton {\n"
"    border: none;\n"
"    margin-left: 2px;\n"
"    min-width: 261px;\n"
"    max-width: 320px;\n"
"    min-height: 32px;\n"
"    max-height: 40px;\n"
"    qproperty-icon: url(\":/Controls/icons/openmark.png\") off,\n"
"                            url(\":/Controls/icons/checkmark.png\") on ;\n"
"    qproperty-iconSize: 17px;\n"
"    qproperty-flat: true;\n"
"    qproperty-checkable: true;\n"
"}\n"
"\n"
"QStackedWidget QAbstractButton:active {\n"
"    border: none;\n"
"}\n"
"\n"
"QListView {\n"
"    text-align: left;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"#menu_bar {\n"
"    padding: -10px;\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.menu_bar = QtGui.QWidget(self.dockWidgetContents)
        self.menu_bar.setMinimumSize(QtCore.QSize(60, 0))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.menu_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.settings_dropdown_btn = QtGui.QToolButton(self.menu_bar)
        self.settings_dropdown_btn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Controls/icons/gearwheel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_dropdown_btn.setIcon(icon)
        self.settings_dropdown_btn.setIconSize(QtCore.QSize(17, 17))
        self.settings_dropdown_btn.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.settings_dropdown_btn.setObjectName(_fromUtf8("settings_dropdown_btn"))
        self.horizontalLayout.addWidget(self.settings_dropdown_btn)
        self.tools_dropdown_btn = QtGui.QToolButton(self.menu_bar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Controls/icons/tools.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tools_dropdown_btn.setIcon(icon1)
        self.tools_dropdown_btn.setIconSize(QtCore.QSize(17, 17))
        self.tools_dropdown_btn.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.tools_dropdown_btn.setObjectName(_fromUtf8("tools_dropdown_btn"))
        self.horizontalLayout.addWidget(self.tools_dropdown_btn)
        self.horizontalLayout_3.addWidget(self.menu_bar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.active_page_dropdown = QtGui.QComboBox(self.dockWidgetContents)
        self.active_page_dropdown.setObjectName(_fromUtf8("active_page_dropdown"))
        self.active_page_dropdown.addItem(_fromUtf8(""))
        self.active_page_dropdown.addItem(_fromUtf8(""))
        self.active_page_dropdown.addItem(_fromUtf8(""))
        self.active_page_dropdown.addItem(_fromUtf8(""))
        self.active_page_dropdown.addItem(_fromUtf8(""))
        self.active_page_dropdown.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.active_page_dropdown)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.process_page = QtGui.QStackedWidget(self.dockWidgetContents)
        self.process_page.setEnabled(True)
        self.process_page.setMinimumSize(QtCore.QSize(350, 280))
        self.process_page.setMaximumSize(QtCore.QSize(16777215, 280))
        self.process_page.setFocusPolicy(QtCore.Qt.NoFocus)
        self.process_page.setAutoFillBackground(False)
        self.process_page.setStyleSheet(_fromUtf8(""))
        self.process_page.setFrameShape(QtGui.QFrame.StyledPanel)
        self.process_page.setFrameShadow(QtGui.QFrame.Plain)
        self.process_page.setLineWidth(2)
        self.process_page.setMidLineWidth(1)
        self.process_page.setObjectName(_fromUtf8("process_page"))
        self.oeq_requirements = QtGui.QWidget()
        self.oeq_requirements.setEnabled(True)
        self.oeq_requirements.setAccessibleDescription(_fromUtf8(""))
        self.oeq_requirements.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.oeq_requirements.setStyleSheet(_fromUtf8(""))
        self.oeq_requirements.setObjectName(_fromUtf8("oeq_requirements"))
        self.Requirements = QtGui.QVBoxLayout(self.oeq_requirements)
        self.Requirements.setObjectName(_fromUtf8("Requirements"))
        self.ol_plugin_installed = QProcessButton(self.oeq_requirements)
        self.ol_plugin_installed.setShortcut(_fromUtf8(""))
        self.ol_plugin_installed.setChecked(False)
        self.ol_plugin_installed.setAutoRepeat(False)
        self.ol_plugin_installed.setAutoExclusive(False)
        self.ol_plugin_installed.setAutoDefault(False)
        self.ol_plugin_installed.setDefault(False)
        self.ol_plugin_installed.setFlat(True)
        self.ol_plugin_installed.setObjectName(_fromUtf8("ol_plugin_installed"))
        self.Requirements.addWidget(self.ol_plugin_installed)
        self.pst_plugin_installed = QProcessButton(self.oeq_requirements)
        self.pst_plugin_installed.setObjectName(_fromUtf8("pst_plugin_installed"))
        self.Requirements.addWidget(self.pst_plugin_installed)
        self.real_centroid_plugin_installed = QProcessButton(self.oeq_requirements)
        self.real_centroid_plugin_installed.setObjectName(_fromUtf8("real_centroid_plugin_installed"))
        self.Requirements.addWidget(self.real_centroid_plugin_installed)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.Requirements.addItem(spacerItem2)
        self.process_page.addWidget(self.oeq_requirements)
        self.oeq_project_basics = QtGui.QWidget()
        self.oeq_project_basics.setAccessibleDescription(_fromUtf8(""))
        self.oeq_project_basics.setObjectName(_fromUtf8("oeq_project_basics"))
        self.Project = QtGui.QVBoxLayout(self.oeq_project_basics)
        self.Project.setObjectName(_fromUtf8("Project"))
        self.project_created = QProcessButton(self.oeq_project_basics)
        self.project_created.setObjectName(_fromUtf8("project_created"))
        self.Project.addWidget(self.project_created)
        self.project_saved = QProcessButton(self.oeq_project_basics)
        self.project_saved.setObjectName(_fromUtf8("project_saved"))
        self.Project.addWidget(self.project_saved)
        self.investigationarea_defined = QProcessButton(self.oeq_project_basics)
        self.investigationarea_defined.setObjectName(_fromUtf8("investigationarea_defined"))
        self.Project.addWidget(self.investigationarea_defined)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.Project.addItem(spacerItem3)
        self.process_page.addWidget(self.oeq_project_basics)
        self.oeq_informationsources = QtGui.QWidget()
        self.oeq_informationsources.setObjectName(_fromUtf8("oeq_informationsources"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.oeq_informationsources)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.import_ext_selected = QProcessButton(self.oeq_informationsources)
        self.import_ext_selected.setEnabled(False)
        self.import_ext_selected.setObjectName(_fromUtf8("import_ext_selected"))
        self.verticalLayout_6.addWidget(self.import_ext_selected)
        self.building_outlines_acquired = QProcessButton(self.oeq_informationsources)
        self.building_outlines_acquired.setObjectName(_fromUtf8("building_outlines_acquired"))
        self.verticalLayout_6.addWidget(self.building_outlines_acquired)
        self.building_coordinates_acquired = QProcessButton(self.oeq_informationsources)
        self.building_coordinates_acquired.setObjectName(_fromUtf8("building_coordinates_acquired"))
        self.verticalLayout_6.addWidget(self.building_coordinates_acquired)
        self.information_layers_loaded = QProcessButton(self.oeq_informationsources)
        self.information_layers_loaded.setObjectName(_fromUtf8("information_layers_loaded"))
        self.verticalLayout_6.addWidget(self.information_layers_loaded)
        self.needle_request_done = QProcessButton(self.oeq_informationsources)
        self.needle_request_done.setObjectName(_fromUtf8("needle_request_done"))
        self.verticalLayout_6.addWidget(self.needle_request_done)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.process_page.addWidget(self.oeq_informationsources)
        self.oeq_building_evaluation = QtGui.QWidget()
        self.oeq_building_evaluation.setAccessibleDescription(_fromUtf8(""))
        self.oeq_building_evaluation.setObjectName(_fromUtf8("oeq_building_evaluation"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.oeq_building_evaluation)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.database_created = QProcessButton(self.oeq_building_evaluation)
        self.database_created.setEnabled(True)
        self.database_created.setObjectName(_fromUtf8("database_created"))
        self.verticalLayout_3.addWidget(self.database_created)
        self.eval_ext_selected = QProcessButton(self.oeq_building_evaluation)
        self.eval_ext_selected.setEnabled(False)
        self.eval_ext_selected.setObjectName(_fromUtf8("eval_ext_selected"))
        self.verticalLayout_3.addWidget(self.eval_ext_selected)
        self.disp_ext_selected = QProcessButton(self.oeq_building_evaluation)
        self.disp_ext_selected.setEnabled(False)
        self.disp_ext_selected.setObjectName(_fromUtf8("disp_ext_selected"))
        self.verticalLayout_3.addWidget(self.disp_ext_selected)
        self.buildings_evaluated = QProcessButton(self.oeq_building_evaluation)
        self.buildings_evaluated.setObjectName(_fromUtf8("buildings_evaluated"))
        self.verticalLayout_3.addWidget(self.buildings_evaluated)
        self.quarter_evaluated = QProcessButton(self.oeq_building_evaluation)
        self.quarter_evaluated.setEnabled(False)
        self.quarter_evaluated.setObjectName(_fromUtf8("quarter_evaluated"))
        self.verticalLayout_3.addWidget(self.quarter_evaluated)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.process_page.addWidget(self.oeq_building_evaluation)
        self.oeq_reports = QtGui.QWidget()
        self.oeq_reports.setAccessibleDescription(_fromUtf8(""))
        self.oeq_reports.setObjectName(_fromUtf8("oeq_reports"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.oeq_reports)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.statistics_created = QProcessButton(self.oeq_reports)
        self.statistics_created.setEnabled(False)
        self.statistics_created.setObjectName(_fromUtf8("statistics_created"))
        self.verticalLayout_4.addWidget(self.statistics_created)
        self.building_reports_created = QProcessButton(self.oeq_reports)
        self.building_reports_created.setEnabled(False)
        self.building_reports_created.setObjectName(_fromUtf8("building_reports_created"))
        self.verticalLayout_4.addWidget(self.building_reports_created)
        self.investigationarea_report_created = QProcessButton(self.oeq_reports)
        self.investigationarea_report_created.setEnabled(False)
        self.investigationarea_report_created.setObjectName(_fromUtf8("investigationarea_report_created"))
        self.verticalLayout_4.addWidget(self.investigationarea_report_created)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.process_page.addWidget(self.oeq_reports)
        self.oeq_export = QtGui.QWidget()
        self.oeq_export.setAccessibleDescription(_fromUtf8(""))
        self.oeq_export.setObjectName(_fromUtf8("oeq_export"))
        self.verticalLayout_41 = QtGui.QVBoxLayout(self.oeq_export)
        self.verticalLayout_41.setObjectName(_fromUtf8("verticalLayout_41"))
        self.json_export_done = QProcessButton(self.oeq_export)
        self.json_export_done.setEnabled(True)
        self.json_export_done.setObjectName(_fromUtf8("json_export_done"))
        self.verticalLayout_41.addWidget(self.json_export_done)
        self.sqlite_export_done = QProcessButton(self.oeq_export)
        self.sqlite_export_done.setEnabled(True)
        self.sqlite_export_done.setObjectName(_fromUtf8("sqlite_export_done"))
        self.verticalLayout_41.addWidget(self.sqlite_export_done)
        self.csv_export_done = QProcessButton(self.oeq_export)
        self.csv_export_done.setEnabled(True)
        self.csv_export_done.setObjectName(_fromUtf8("csv_export_done"))
        self.verticalLayout_41.addWidget(self.csv_export_done)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_41.addItem(spacerItem7)
        self.process_page.addWidget(self.oeq_export)
        self.verticalLayout_5.addWidget(self.process_page)
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.setSpacing(5)
        self.button_layout.setObjectName(_fromUtf8("button_layout"))
        self.automode = QtGui.QCheckBox(self.dockWidgetContents)
        self.automode.setEnabled(True)
        self.automode.setObjectName(_fromUtf8("automode"))
        self.button_layout.addWidget(self.automode)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem8)
        self.run_button = QtGui.QPushButton(self.dockWidgetContents)
        self.run_button.setEnabled(False)
        self.run_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Controls/icons/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_button.setIcon(icon2)
        self.run_button.setIconSize(QtCore.QSize(16, 16))
        self.run_button.setObjectName(_fromUtf8("run_button"))
        self.button_layout.addWidget(self.run_button)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem9)
        self.process_button_next = QtGui.QPushButton(self.dockWidgetContents)
        self.process_button_next.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.process_button_next.setIcon(icon2)
        self.process_button_next.setIconSize(QtCore.QSize(16, 16))
        self.process_button_next.setObjectName(_fromUtf8("process_button_next"))
        self.button_layout.addWidget(self.process_button_next)
        self.verticalLayout_5.addLayout(self.button_layout)
        spacerItem10 = QtGui.QSpacerItem(20, 32, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.logo_layout = QtGui.QHBoxLayout()
        self.logo_layout.setObjectName(_fromUtf8("logo_layout"))
        self.oeq_clickable_logo = QClickableLabel(self.dockWidgetContents)
        self.oeq_clickable_logo.setMinimumSize(QtCore.QSize(350, 57))
        self.oeq_clickable_logo.setText(_fromUtf8(""))
        self.oeq_clickable_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/Brands/icons/OeQ_logo_footer.png")))
        self.oeq_clickable_logo.setObjectName(_fromUtf8("oeq_clickable_logo"))
        self.logo_layout.addWidget(self.oeq_clickable_logo)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.logo_layout.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.logo_layout)
        MainProcess_dock.setWidget(self.dockWidgetContents)

        self.retranslateUi(MainProcess_dock)
        self.process_page.setCurrentIndex(0)
        QtCore.QObject.connect(self.active_page_dropdown, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.process_page.setCurrentIndex)
        QtCore.QObject.connect(self.automode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.run_button.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainProcess_dock)
        MainProcess_dock.setTabOrder(self.ol_plugin_installed, self.pst_plugin_installed)
        MainProcess_dock.setTabOrder(self.pst_plugin_installed, self.real_centroid_plugin_installed)
        MainProcess_dock.setTabOrder(self.real_centroid_plugin_installed, self.process_button_next)
        MainProcess_dock.setTabOrder(self.process_button_next, self.settings_dropdown_btn)
        MainProcess_dock.setTabOrder(self.settings_dropdown_btn, self.tools_dropdown_btn)
        MainProcess_dock.setTabOrder(self.tools_dropdown_btn, self.active_page_dropdown)
        MainProcess_dock.setTabOrder(self.active_page_dropdown, self.building_outlines_acquired)
        MainProcess_dock.setTabOrder(self.building_outlines_acquired, self.building_coordinates_acquired)
        MainProcess_dock.setTabOrder(self.building_coordinates_acquired, self.eval_ext_selected)
        MainProcess_dock.setTabOrder(self.eval_ext_selected, self.disp_ext_selected)
        MainProcess_dock.setTabOrder(self.disp_ext_selected, self.csv_export_done)
        MainProcess_dock.setTabOrder(self.csv_export_done, self.project_created)
        MainProcess_dock.setTabOrder(self.project_created, self.investigationarea_defined)
        MainProcess_dock.setTabOrder(self.investigationarea_defined, self.project_saved)

    def retranslateUi(self, MainProcess_dock):
        MainProcess_dock.setWindowTitle(_translate("MainProcess_dock", "Open eQuarter Mole", None))
        self.tools_dropdown_btn.setText(_translate("MainProcess_dock", "...", None))
        self.label.setText(_translate("MainProcess_dock", "Currently viewing:", None))
        self.active_page_dropdown.setAccessibleName(_translate("MainProcess_dock", "Information Sources", None))
        self.active_page_dropdown.setItemText(0, _translate("MainProcess_dock", "Requirements", None))
        self.active_page_dropdown.setItemText(1, _translate("MainProcess_dock", "Project Basics", None))
        self.active_page_dropdown.setItemText(2, _translate("MainProcess_dock", "Information Sources", None))
        self.active_page_dropdown.setItemText(3, _translate("MainProcess_dock", "Evaluation", None))
        self.active_page_dropdown.setItemText(4, _translate("MainProcess_dock", "Reports", None))
        self.active_page_dropdown.setItemText(5, _translate("MainProcess_dock", "Export", None))
        self.process_page.setAccessibleName(_translate("MainProcess_dock", "jkiiuuu", None))
        self.oeq_requirements.setAccessibleName(_translate("MainProcess_dock", "Requirements", None))
        self.ol_plugin_installed.setText(_translate("MainProcess_dock", "Check if \'OpenLayers\' Plugin is available", None))
        self.pst_plugin_installed.setText(_translate("MainProcess_dock", "Check if \'Point Sampling Tool\' Plugin is available", None))
        self.real_centroid_plugin_installed.setText(_translate("MainProcess_dock", "Check if \'realcentriod\'  Plugin is available", None))
        self.oeq_project_basics.setAccessibleName(_translate("MainProcess_dock", "Project Basics", None))
        self.project_created.setText(_translate("MainProcess_dock", "Define Project Location and Parameters", None))
        self.project_saved.setText(_translate("MainProcess_dock", "Save Project", None))
        self.investigationarea_defined.setText(_translate("MainProcess_dock", "Define Investigation Area", None))
        self.oeq_informationsources.setAccessibleName(_translate("MainProcess_dock", "Information Sources", None))
        self.import_ext_selected.setText(_translate("MainProcess_dock", "Select Import Extensions", None))
        self.building_outlines_acquired.setText(_translate("MainProcess_dock", "Acquire Building Outlines", None))
        self.building_coordinates_acquired.setText(_translate("MainProcess_dock", "Acquire Building Coordinates", None))
        self.information_layers_loaded.setText(_translate("MainProcess_dock", "Load Information Layers", None))
        self.needle_request_done.setText(_translate("MainProcess_dock", "Perform Needle Request", None))
        self.oeq_building_evaluation.setAccessibleName(_translate("MainProcess_dock", "Evaluation", None))
        self.database_created.setText(_translate("MainProcess_dock", "Create Database", None))
        self.eval_ext_selected.setText(_translate("MainProcess_dock", "Select Evaluation Extensions", None))
        self.disp_ext_selected.setText(_translate("MainProcess_dock", "Select Display Extensions", None))
        self.buildings_evaluated.setText(_translate("MainProcess_dock", "Evaluate Buildings", None))
        self.quarter_evaluated.setText(_translate("MainProcess_dock", "Evaluate Quarter", None))
        self.oeq_reports.setAccessibleName(_translate("MainProcess_dock", "Reports", None))
        self.statistics_created.setText(_translate("MainProcess_dock", "Create reports of selected buildings", None))
        self.building_reports_created.setText(_translate("MainProcess_dock", "Create reports of the investigation area", None))
        self.investigationarea_report_created.setText(_translate("MainProcess_dock", "Create statistics", None))
        self.oeq_export.setAccessibleName(_translate("MainProcess_dock", "Export", None))
        self.json_export_done.setText(_translate("MainProcess_dock", "Export database as GeoJSON file", None))
        self.sqlite_export_done.setText(_translate("MainProcess_dock", "Export database as SQLite file", None))
        self.csv_export_done.setText(_translate("MainProcess_dock", "Export database as CSV file", None))
        self.automode.setText(_translate("MainProcess_dock", "Automode", None))
        self.run_button.setText(_translate("MainProcess_dock", "Run", None))
        self.process_button_next.setText(_translate("MainProcess_dock", "Step", None))

from oeq_ui_classes import QClickableLabel, QProcessButton
import resources_rc
