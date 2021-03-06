# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImageAnalysis
                                 A QGIS plugin
 this plugin will analyse raster images
                              -------------------
        begin                : 2017-08-02
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Image Analysis
        email                : dyedenm@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QTableWidgetItem
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from engine.agree.agree_layout import AgreeLayout
from image_analysis_dialog import ImageAnalysisDialog
import os.path


class ImageAnalysis:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ImageAnalysis_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = ImageAnalysisDialog()
        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Image Analysis')
        # TODO: We are going to let the user set this up in a future iteration
        self.agreelayout = AgreeLayout()
        self.toolbar = self.iface.addToolBar(u'ImageAnalysis')
        self.toolbar.setObjectName(u'ImageAnalysis')
        
    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ImageAnalysis', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = ImageAnalysisDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/ImageAnalysis/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow())
        
        self.init_plugin()

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Image Analysis'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def select_output_file(self):
        # filename = QFileDialog.getSaveFileName(self.dlg, "Select output file ", "", "*.txt")
        filename = QFileDialog.getExistingDirectory(self.dlg, "Select output file ", "")
        self.dlg.lineEdit_input_s1.setText(filename)
        self.dlg.comboBox_s1.addItems(["Java", "C#", "Python"])
        self.dlg.tableWidget_comparison.setRowCount(4)
        self.dlg.tableWidget_comparison.setColumnCount(2) 
        self.dlg.tableWidget_comparison.setItem(0,0, QTableWidgetItem("Item (1,1)"))
        self.dlg.tableWidget_comparison.show()

    def set_config_options(self):
        print "working set_config_options"
        sourcename1 = self.dlg.comboBox_s1.currentText()
        sourcename2 = self.dlg.comboBox_s2.currentText()

        if sourcename1 == sourcename2:
            self.dlg.tableWidget_comparison.clear()
            return None

        self.dlg.tableWidget_comparison.setRowCount(4)
        self.dlg.tableWidget_comparison.setColumnCount(2) 

        self.dlg.tableWidget_comparison.setHorizontalHeaderItem(0, QTableWidgetItem(sourcename1))
        self.dlg.tableWidget_comparison.setHorizontalHeaderItem(1, QTableWidgetItem(sourcename2))


        self.dlg.tableWidget_comparison.setItem(0,0, QTableWidgetItem(sourcename1))
        self.dlg.tableWidget_comparison.setItem(0,1, QTableWidgetItem(sourcename2))
        self.dlg.tableWidget_comparison.show()


    def set_default_config(self):

        #combo box source 1 e source 2
        self.agreelayout.config_default()
        self.dlg.comboBox_s1.addItems(self.agreelayout.combobox_names)
        self.dlg.comboBox_s2.addItems(self.agreelayout.combobox_names)



    def validate_config(self):
        pass

        

    def init_plugin(self):
        self.set_default_config()
        self.dlg.comboBox_s1.currentIndexChanged.connect(self.set_config_options)
        self.dlg.comboBox_s2.currentIndexChanged.connect(self.set_config_options)
        self.set_config_options()
 

    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()

        # See if OK was pressed
        if result:
            print("ok working")
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
