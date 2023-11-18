# -*- coding: utf-8 -*-

from os import read
import arcpy
import time 

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [RenderTool]

class RenderTool(object):
    def __init__(self):
        """Define the toolbox ()."""
        self.label = "Tool"
        self.description = ''
        self.canRunInBackground = False 

    def getParameterInfo(self):
        """define"""
        param0 = arcpy.Parameter(
            displayName = 'Your working project', 
            name = 'workProject', 
            datatype = 'DEFile', 
            parameterType = 'Required', 
            direction = 'Input'
        )

        param1 = arcpy.Parameter(
            displayName = 'Name of layer to render', 
            name = 'layername', 
            datatype = 'GPString', 
            parameterType = 'Required', 
            direction = 'Input'
        )

        param2 = arcpy.Parameter(
            displayName = 'Folder of the new project', 
            name = 'newprojectfolder', 
            datatype = 'DEFolder', 
            parameterType = 'Required', 
            direction = 'Input'
        )

        param3 = arcpy.Parameter(
            displayName = 'Name of the new project', 
            name = 'newprojectname', 
            datatype = 'GPString', 
            parameterType = 'Required', 
            direction = 'Input'
        )

        params = [param0, param1, param2, param3]
        
        return params 
    
    def execute(self, parameters, messages):
        """The source code of the tool."""
        # define progressor variables 
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # setup the progressor 
        arcpy.SetProgressor('step', 'Checking project layer, please hold...', start, maximum, step)
        time.sleep(readTime)
        # add message to results pane 
        arcpy.AddMessage('Checking project layer, please hold...')

        # ref to our .aprx 
        aprxFileAddress = parameters[0].valueAsText 
        project = arcpy.mp.ArcGISProject(aprxFileAddress)
        layername = parameters[1].valueAsText
        # grab the layer in the aprx

        if layername == 'GarageParking':
            layer = project.listMaps('Map')[0].listLayers()[1]
            symbology = layer.symbology

            # increment the prog and change label, add message 
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel('Start to update render... :) ')
            time.sleep(readTime)
            arcpy.AddMessage('Start to update render... :) ')

            # update the copy's renderer to be gradcolors 
            symbology.updateRenderer('GraduatedColorsRenderer')
            # tell arcpy which field to base chloropleth off of 
            symbology.renderer.classificationField = 'Shape_Area'

            # increment the prog and change the label, add message 
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel('setting render...')
            time.sleep(readTime)
            arcpy.AddMessage('setting render...')

            # set how many classes 
            symbology.renderer.breakCount = 5
            # set the color ramp 
            symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
            # set the layer's actual sym equal to copy
            layer.symbology = symbology

            # increment the prog and change label
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel('Saving project... Almost done :D ')
            time.sleep(readTime)
            arcpy.AddMessage('Saving project... Almost done :D ')

        if layername == 'Structures':
            layer = project.listMaps('Map')[0].listLayers()[0]
            symbology = layer.symbology 

            # increment the prog and change label, add message 
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel('Start to update render... :) ')
            time.sleep(readTime)
            arcpy.AddMessage('Start to update render... :) ')

            # update the copy's renderer to be  
            symbology.updateRenderer('UniqueValueRenderer')

            # increment the prog and change the label, add message 
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel('setting render...')
            time.sleep(readTime)
            arcpy.AddMessage('setting render...')

            # tells arcpy that we want to use type as our unique values 
            symbology.renderer.fields = ['Type']
            # set the layer's actual sym equal to copy
            layer.symbology = symbology

            # increment the prog and change label
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel('Saving project... Almost done :D ')
            time.sleep(readTime)
            arcpy.AddMessage('Saving project... Almost done :D ')

        else: 
            arcpy.AddMessage('Not happening... ')

        newprojectpath = parameters[2].valueAsText + "\\" + parameters[3].valueAsText
        project.saveACopy(newprojectpath)
        arcpy.AddMessage('Done, hurray!!!')
        
        return


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
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
        # define progressor variables 
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # setup the progressor 
        arcpy.SetProgressor('step', 'Checking project layer, please hold...', start, maximum, step)
        time.sleep(readTime)
        # add message to results pane 
        arcpy.AddMessage('Checking project layer, please hold...')

        # ref to our .aprx 
        aprxFileAddress = parameters[0].valueAsText 
        project = arcpy.mp.ArcGISProject(aprxFileAddress)
        layername = parameters[1].valueAsText
        # grab the layer in the aprx

        if layername == 'GarageParking':
            layer = project.listMaps('Map')[0].listLayers()[1]
            symbology = layer.symbology

            # increment the prog and change label, add message 
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel('Start to update render... :) ')
            time.sleep(readTime)
            arcpy.AddMessage('Start to update render... :) ')

            # update the copy's renderer to be gradcolors 
            symbology.updateRenderer('GraduatedColorsRenderer')
            # tell arcpy which field to base chloropleth off of 
            symbology.renderer.classificationField = 'Shape_Area'

            # increment the prog and change the label, add message 
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel('setting render...')
            time.sleep(readTime)
            arcpy.AddMessage('setting render...')

            # set how many classes 
            symbology.renderer.breakcount = 5
            # set the color ramp 
            symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
            # set the layer's actual sym equal to copy
            layer.symbology = symbology

            # increment the prog and change label
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel('Saving project... Almost done :D ')
            time.sleep(readTime)
            arcpy.AddMessage('Saving project... Almost done :D ')

        if layername == 'Structures':
            layer = project.listMaps('Map')[0].listLayers()[0]
            symbology = layer.symbology 

            # increment the prog and change label, add message 
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel('Start to update render... :) ')
            time.sleep(readTime)
            arcpy.AddMessage('Start to update render... :) ')

            # update the copy's renderer to be  
            symbology.updateRenderer('UniqueValueRenderer')

            # increment the prog and change the label, add message 
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel('setting render...')
            time.sleep(readTime)
            arcpy.AddMessage('setting render...')

            # tells arcpy that we want to use type as our unique values 
            symbology.renderer.fields = ['Type']
            # set the layer's actual sym equal to copy
            layer.symbology = symbology

            # increment the prog and change label
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel('Saving project... Almost done :D ')
            time.sleep(readTime)
            arcpy.AddMessage('Saving project... Almost done :D ')

        else: 
            arcpy.AddMessage('Not happening... ')

        newprojectpath = parameters[2].valueAsText + '\\' + parameters[3].valueAsText
        project.saveACopy(newprojectpath)
        arcpy.AddMessage('Done, hurray!!!')
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
