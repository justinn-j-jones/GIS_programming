# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(displyName = 'Work GDB folder path', name = 'GDBfolderpath', datatype = 'DEfolder', parameterType = 'Required', direction = 'Input')
        # param1 = arcpy.Parameter(displyName = 'Work GDB Name', name = 'GDB_name', datatype = 'GPString', parameterType = 'Required', direction = 'Input')
        # param2 = arcpy.Parameter(displyName = 'garage CSV path', name = 'garageCSVfileaddress', datatype = 'DEfile', parameterType = 'Required', direction = 'Input')
        # param3 = arcpy.Parameter(displyName = 'garage name', name = 'garage_name', datatype = 'GPString', parameterType = 'Required', direction = 'Input')
        # param4 = arcpy.Parameter(displyName = 'campus GDB folder path', name = 'campusGDBfolderpath', datatype = 'DEfolder', parameterType = 'Required', direction = 'Input')
        # param5 = arcpy.Parameter(displyName = 'selected garage name', name = 'selectedgaragename', datatype = 'GPString', parameterType = 'Required', direction = 'Input')
        # param6 = arcpy.Parameter(displyName = 'buffer radius', name = 'bufferradius', datatype = 'GPDouble', parameterType = 'Required', direction = 'Input')
        # params = [param0, param1, param2, param3, param4, param5, param6]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
