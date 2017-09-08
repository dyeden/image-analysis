# -*- coding: utf-8 -*-


class AgreeLayout(object):

    def __init__(self):
        self.combobox_names = None

    def config_default(self):
        self.combobox_names = ["mapbiomas", "ucsb", "terraclass", "custom"]

        self.comparisons = {
            "mapbiomas": {
                "ucsb": [[1, 2]]
            }
        }
