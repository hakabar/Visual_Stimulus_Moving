#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Fri 07 Jul 2017 01:55:04 PM PDT
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'patternMoving4'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/riffell-lab/Desktop/python_stimulus_moving/stimulusMoving.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1, -1], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
#Parameters to use along the experiment
#Constants
RAD=0.9
CTE_ANGLE=180       #Used to set the starting point of the stimulus in the screen
ANGLES= [0, 45, 90] #Angles for the stimulus
SIZE= len(ANGLES)   #Num. of angles used (valid for trial loop counter) 
COUNTER_LOOP= 5     #Num. of repeats for each stimulus movement loop
STEP= 0.01          #Velocity of the stimulus
#Variables
index= 0            #Index for the ANGLES list
position_ptrn=[0,0] #Position of the stimulus

# Initialize components for Routine "left_to_right"
left_to_rightClock = core.Clock()


polygon = visual.Rect(win=win, name='polygon',
    width=[0.2, 4][0], height=[0.2, 4][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "right_to_left"
right_to_leftClock = core.Clock()

polygon_2 = visual.Rect(win=win, name='polygon_2',
    width=[0.2, 3][0], height=[0.2, 3][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1,interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=SIZE, method='random', 
    extraInfo=expInfo, originPath=u'/home/riffell-lab/Desktop/python_stimulus_moving/stimulusMoving.psyexp',
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    angle= ANGLES[index]            #Used to find initial position & inclination angle of stimulus
    stimulus_angle= CTE_ANGLE-angle #Angle assigned to the stimulus
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    index+=1
    
    # set up handler to look after randomisation of conditions etc
    left_to_right_loop = data.TrialHandler(nReps=COUNTER_LOOP, method='random', 
        extraInfo=expInfo, originPath=u'/home/riffell-lab/Desktop/python_stimulus_moving/stimulusMoving.psyexp',
        trialList=[None],
        seed=None, name='left_to_right_loop')
    thisExp.addLoop(left_to_right_loop)  # add the loop to the experiment
    thisLeft_to_right_loop = left_to_right_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisLeft_to_right_loop.rgb)
    if thisLeft_to_right_loop != None:
        for paramName in thisLeft_to_right_loop.keys():
            exec(paramName + '= thisLeft_to_right_loop.' + paramName)
    
    for thisLeft_to_right_loop in left_to_right_loop:
        currentLoop = left_to_right_loop
        # abbreviate parameter names if possible (e.g. rgb = thisLeft_to_right_loop.rgb)
        if thisLeft_to_right_loop != None:
            for paramName in thisLeft_to_right_loop.keys():
                exec(paramName + '= thisLeft_to_right_loop.' + paramName)
        
        #------Prepare to start Routine "left_to_right"-------
        t = 0
        left_to_rightClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        #Calculate the initial positions of the stimulus
        x= RAD*np.cos(np.deg2rad(CTE_ANGLE+angle))
        y= RAD*np.sin(np.deg2rad(CTE_ANGLE+angle))
        position_ptrn= [x,y]
        #Calculate the increment for x & y in function of stimulus angle
        if (angle == 0): 
            speed_x= STEP
            speed_y= 0
        elif (angle == 90):
            speed_x= 0
            speed_y= STEP
        else:
            #Valid only for a stimulus angle of 45 degrees
            speed_x= STEP*np.tan(np.deg2rad(CTE_ANGLE+angle))
            speed_y= STEP*np.tan(np.deg2rad(CTE_ANGLE+angle))
        polygon.setOri(stimulus_angle)
        # keep track of which components have finished
        left_to_rightComponents = []
        left_to_rightComponents.append(polygon)
        for thisComponent in left_to_rightComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "left_to_right"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = left_to_rightClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #Update the stimulus position in the screen
            position_ptrn[0]+= speed_x
            position_ptrn[1]+= speed_y
            
            # *polygon* updates
            if t >= 0.0 and polygon.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon.tStart = t  # underestimates by a little under one frame
                polygon.frameNStart = frameN  # exact frame index
                polygon.setAutoDraw(True)
            elif polygon.status == STARTED and t >= (0.0 + 3.5):
                polygon.setAutoDraw(False)
            if polygon.status == STARTED:  # only update if being drawn
                polygon.setPos(position_ptrn, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in left_to_rightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "left_to_right"-------
        for thisComponent in left_to_rightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed COUNTER_LOOP repeats of 'left_to_right_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    right_to_left_loop = data.TrialHandler(nReps=COUNTER_LOOP, method='random', 
        extraInfo=expInfo, originPath=u'/home/riffell-lab/Desktop/python_stimulus_moving/stimulusMoving.psyexp',
        trialList=[None],
        seed=None, name='right_to_left_loop')
    thisExp.addLoop(right_to_left_loop)  # add the loop to the experiment
    thisRight_to_left_loop = right_to_left_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisRight_to_left_loop.rgb)
    if thisRight_to_left_loop != None:
        for paramName in thisRight_to_left_loop.keys():
            exec(paramName + '= thisRight_to_left_loop.' + paramName)
    
    for thisRight_to_left_loop in right_to_left_loop:
        currentLoop = right_to_left_loop
        # abbreviate parameter names if possible (e.g. rgb = thisRight_to_left_loop.rgb)
        if thisRight_to_left_loop != None:
            for paramName in thisRight_to_left_loop.keys():
                exec(paramName + '= thisRight_to_left_loop.' + paramName)
        
        #------Prepare to start Routine "right_to_left"-------
        t = 0
        right_to_leftClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        #Calculate the initial positions of the stimulus
        x= RAD*np.cos(np.deg2rad(2*CTE_ANGLE+angle))
        y= RAD*np.sin(np.deg2rad(2*CTE_ANGLE+angle))
        position_ptrn= [x,y]
        #Calculate the increment for x & y in function of stimulus angle
        if (angle == 0): 
            speed_x= STEP*(-1)
            speed_y= 0
        elif (angle == 90):
            speed_x= 0
            speed_y= STEP*(-1)
        else:
            #Valid only for a stimulus angle of 45 degrees
            speed_x= STEP*np.tan(np.deg2rad(CTE_ANGLE-angle))
            speed_y= STEP*np.tan(np.deg2rad(CTE_ANGLE-angle))
        polygon_2.setOri(stimulus_angle)
        # keep track of which components have finished
        right_to_leftComponents = []
        right_to_leftComponents.append(polygon_2)
        for thisComponent in right_to_leftComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "right_to_left"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = right_to_leftClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #Update the stimulus position in the screen
            position_ptrn[0]+= speed_x
            position_ptrn[1]+= speed_y
            
            # *polygon_2* updates
            if t >= 0.0 and polygon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_2.tStart = t  # underestimates by a little under one frame
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.setAutoDraw(True)
            elif polygon_2.status == STARTED and t >= (0.0 + 3.5):
                polygon_2.setAutoDraw(False)
            if polygon_2.status == STARTED:  # only update if being drawn
                polygon_2.setPos(position_ptrn, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in right_to_leftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "right_to_left"-------
        for thisComponent in right_to_leftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed COUNTER_LOOP repeats of 'right_to_left_loop'
    
    thisExp.nextEntry()
    
# completed SIZE repeats of 'trials'




win.close()
core.quit()
