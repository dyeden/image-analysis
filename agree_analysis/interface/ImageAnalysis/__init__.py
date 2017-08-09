# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImageAnalysis
                                 A QGIS plugin
 this plugin will analyse raster images
                             -------------------
        begin                : 2017-08-02
        copyright            : (C) 2017 by Image Analysis
        email                : dyedenm@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ImageAnalysis class from file ImageAnalysis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .image_analysis import ImageAnalysis
    return ImageAnalysis(iface)
