# -*- coding: utf-8 -*-


class AgreeLayout(object):

    def __init__(self):
        self.combobox_names = None

    def config_default(self):
        self.combobox_names = ["mapbiomas", "ucsb", "terraclass", "custom"]

        self.comparisons = {
            "mapbiomas": {
                "ucsb" : [[10,1],[3,2],[21,3],[8,5],[26,6],[22,7]],
                "hansen" : [[1,1],[2,1],[3,1],[4,1],[-1,0]],
                "terraclass" : [[0,2],[3,5],[8,14],[8,15],[10,9],[14,1],[14,4],[14,12],[14,13],[21,1],[21,4],[21,12],
                        [21,13],[22,3],[22,7],[22,8],[22,11],[26,6],[27,2]]
            }
        }

        self.legendas = {
            1:["Forests", "#008940"],
            2:["Natural Forest Formations", "#058e75"],
            3:["Dense Forest", "#058e75"],
            4:["Open Forest", "#058e75"],
            5:["Mangrove", "#058e75"],
            6:["Floored Forest", "#058e75"],
            7:["Degraded Forest", "#058e75"],
            8:["Secoundary Forest", "#00ff19"],
            9:["Silviculture", "#058e75"],
            10:["Non-Forest Natural Formations", "#ff9d00"],
            11:["Non-Forest Formations in Wetlands", "#058e75"],
            12:["Grasslands", "#058e75"],
            13:["Other nof forest formations", "#058e75"],
            14:["Farming", "#058e75"],
            15:["Pasture", "#058e75"],
            16:["Pasture in Natural Fields", "#058e75"],
            17:["Other Pasture", "#058e75"],
            18:["Agriculture", "#058e75"],
            19:["Annual Crops", "#058e75"],
            20:["Semi-permanent Crops", "#058e75"],
            21:["Agriculture or Pasture", "#ffffa5"],
            22:["Non-Vegeted Areas", "#ff65b5"],
            23:["Beaches", "#058e75"],
            24:["Urban Infrastructure", "#058e75"],
            25:["Other non vegetated areas", "#058e75"],
            26:["Water bodies", "#0000ff"],
            27:["Not Observed", "#058e75"],
            28:["Mosaic of Crops", "#058e75"],
        } 
