#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.00), May 26, 2015, at 12:54
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Biomarker Imaging Study'  # from the Builder filename that created this script
expInfo = {u'Gender': u'female', u'Handedness': u'Right', u'participant': u'SKY100', u'Trigger Pulse Button': u'*',u'Response Pad Button':u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + '%s/%s_%s_%s' %(expInfo['participant'], expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1600, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[-1.,-1.,-1.], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Start"
StartClock = core.Clock()
Welcome = visual.TextStim(win=win, ori=0, name='Welcome',
    text=u'Welcome to the Biomarker Imaging Study',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
'''
Total time to record MRI sequence:
    Seconds: 2196.44
    Minutes: 36.60733~
'''
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
#should be 600 (1320 frames = 22 seconds @ 60Hz refresh rate)
instrStopTime = 960
#should be 600 (1800 frames = 30 seconds @ 60Hz refresh rate)
instrStopTime2 = 960
#set this to whatever button is recorded on a trigger pulse,
# wrapped in apostrophes and seperated by commas for multiple
# buttons( e.g.: '6','^')
triggerButton = expInfo[u'Trigger Pulse Button']
responseButton = expInfo[u'Response Pad Button']
data_path = _thisDir + os.sep + '%s' %(expInfo['participant'])
try:
    os.makedirs(data_path)
except:
    pass
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
###################SETTINGS######################
#
#################################################
####################CSV Code#####################
def writeDataFile(csvDict, csvFileName, fieldNames, finalLine = {}):
    with open('%s.csv' % csvFileName, 'wb') as outfile:
        writer = csv.DictWriter(outfile, fieldnames = fieldNames)
        writer.writeheader()
        rowList = []
        for i in range(len(csvDict[fieldNames[0]])):
            rowDict = {}
            for key in csvDict.keys():
                try:
                    rowDict[key] = csvDict[key][i]
                except:
                    pass
            rowList.append(rowDict)
        if finalLine != {}:
            rowList.append(finalLine)
        writer.writerows(rowList)
####################CSV Code#####################
#################################################
#
#################################################
#################N-Back Code#####################
import csv
########
def n_backer():
    iRanWhat= 0
    continueRunning = True
    while continueRunning:
        corAns = 'none'
        nBackLetter = 'A'
        currentLetter = 'A'
        oldLets = []
        correctButtonList = []
        nBackLets = []
        position=0
        correctAns= 0
        nBack = 2
        #array of letters to sample from
        nBackLets = map(chr, range(65, 91))
        counter = 0
        howManyTimes = 24
        while(position<howManyTimes):
           #pick random number from 1-100 for determining if this is an nBack round or not
           bias = randint(1, 100)
           currentLetter = nBackLets[randint(0,25)]
           #check that enough rounds have passed to display an nBack
           if position-nBack >= 0:
              #determine if next letter will be new or a nBack match, currently 50/50 odds
              if bias < 50:
                 currentLetter = oldLets[position-nBack]
                 corAns = responseButton
                 counter += 1
              else:
                 corAns = 'none'
           # update component parameters for each repeat
           correctButtonList.append(corAns)
           oldLets.append(currentLetter)
           position = position + 1
        iRanWhat += 1
        if counter == (howManyTimes/2):
            continueRunning = False
            retList = [oldLets, correctButtonList]
            return retList

#csvDictionary = {'letters':, 'correctButton':}
moresoOldLets = []
moresoButtonList = []
for i in range(0, 4):
    temp_thing = n_backer()
    for item in temp_thing[0]:
        moresoOldLets.append(item)
    for item in temp_thing[1]:
        moresoButtonList.append(item)

csvDictionary={'letters': moresoOldLets, 'correctButton': moresoButtonList}

writeDataFile(csvDictionary, 'NbackStimOrder_all', ['letters', 'correctButton'])
##################N-Back Code####################
#################################################
#
#################################################
####################CPT Code#####################
##RANDOMIZATION OF STIMULI#####
###Randomization of X trials###
list1 = []
list2 = []
buttonList1 = []
buttonList2 = []

def make_x_list():
    # Array of letters to sample from
    lets = map(chr, range(65, 91))
    del lets[23]####Delete X from the list
    xPoolOfLetters = ["X" for i in range(24)]
    xPoolOfLetters += (2 * lets)
    xPoolOfLetters.append(lets[randint(0,24)])
    return xPoolOfLetters


def make_ax_list():
    # # Randomization of A-X trials
    lets = map(chr, range(65, 91))
    del lets[23]####Delete X from the list
    del lets[0]####Delete A from the list
    ############for ax, I'll just load the list with A's,
    ############and after sorting insert X after each A in the list
    axPoolOfLetters = ["A" for i in range(12)]
    axPoolOfLetters += (2 * lets)
    for i in range(3):
        axPoolOfLetters.append(lets[randint(0,23)])
    return axPoolOfLetters

def xRandomizer(pol):
    repeatAttempt = False
    for x in range(0,len(pol)):
        if x > 2:
            if pol[x] == pol[x-1]:
                if pol[x] == pol[x-2]:
                    if pol[x] == pol[x-3]:
                        shuffle(pol)
                        repeatAttempt = True
                        break
    if repeatAttempt == True:
        xRandomizer(pol)
    perfectPool = list(pol)
    return perfectPool

x_list1 = make_x_list()
x_list2 = make_x_list()
x_list3 = make_x_list()
x_list4 = make_x_list()
x_lists = [x_list1, x_list2, x_list3, x_list4]

for item in x_lists:
    temp_list = xRandomizer(item)
    for indItem in item:
        list1.append(indItem)

ax_list1 = make_ax_list()
ax_list2 = make_ax_list()
ax_list3 = make_ax_list()
ax_list4 = make_ax_list()
ax_lists = [ax_list1, ax_list2, ax_list3, ax_list4]

for item in ax_lists:
    temp_list = xRandomizer(item)
    for x in range(0, len(item)+12):##add new length here
        if item[x] == 'A':
            item.insert(x+1,'X')
    for indItem in item:
        list2.append(indItem)


def createButtonLists(alist):
    abuttonlist = []
    for i in alist:
        if i is 'X':
            abuttonlist.append(responseButton)
        else:
            abuttonlist.append('none')
    return abuttonlist

buttonList1 = createButtonLists(list1)
buttonList2 = createButtonLists(list2)

csvDictionary = {'CPT_letters': list1, 'correctButton':buttonList1}
writeDataFile(csvDictionary, 'CPTstimOrder1_all', ['CPT_letters', 'correctButton'])
csvDictionary = {'CPT_letters': list2, 'correctButton':buttonList2}
writeDataFile(csvDictionary, 'CPTstimOrder2_all', ['CPT_letters', 'correctButton'])

####################CPT Code#####################
#################################################

# Initialize components for Routine "AreYouSure"
AreYouSureClock = core.Clock()
Warning = visual.TextStim(win=win, ori=0, name='Warning',
    text=u"After this point we won't stop the experiment, unless there is a problem.\n\nAre you sure you are ready?",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "MRI_sync"
MRI_syncClock = core.Clock()
Waiting_For_Pulse = visual.TextStim(win=win, ori=0, name='Waiting_For_Pulse',
    text='Waiting for trigger pulse...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Welcome_CPT_X"
Welcome_CPT_XClock = core.Clock()
epoch_counter = 0
instr_duration_s = '0'
bgcolor = [-1.0, -1.0, 0.0]
stim_selection = {'round1':list(range(0,75)),'round2': list(range(75,150)), 'round3': list(range(150,225)),'round4': list(range(225,300))}
nback_stim_selection = {'round1':list(range(0,24)),'round2': list(range(24,48)), 'round3': list(range(48,72)),'round4': list(range(72,96))}
grating = visual.GratingStim(win=win, name='grating',units='norm', 
    tex=None, mask=None,
    ori=0, pos=[0, 0], size=2, sf=None, phase=0.0,
    color=[-0.5,0.,0.], colorSpace='rgb', opacity=1,
    texRes=512, interpolate=True, depth=-1.0)
Instructions_CPT_X = visual.TextStim(win=win, ori=0, name='Instructions_CPT_X',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "CPT_X"
CPT_XClock = core.Clock()
Letter_CPT_X = visual.TextStim(win=win, ori=0, name='Letter_CPT_X',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
CPT_X_responseList = []
CPT_X_correctList = []
CPT_X_accuracy = []
CPT_X_responseTimeList = []

# Initialize components for Routine "Welcome_CPT_AX"
Welcome_CPT_AXClock = core.Clock()
grating_2 = visual.GratingStim(win=win, name='grating_2',units='norm', 
    tex=None, mask=None,
    ori=0, pos=[0, 0], size=2, sf=None, phase=0.0,
    color=[-1,0,-.5], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
Instructions_CPT_AX = visual.TextStim(win=win, ori=0, name='Instructions_CPT_AX',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "CPT_AX"
CPT_AXClock = core.Clock()
Letter_CPT_AX = visual.TextStim(win=win, ori=0, name='Letter_CPT_AX',
    text='default text',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
CPT_AX_responseList = []
CPT_AX_responseToAList = []
CPT_AX_correctList = []
CPT_AX_accuracy = []
CPT_AX_responseTimeList = []

# Initialize components for Routine "Welcome_Nback"
Welcome_NbackClock = core.Clock()
Nback_Instructions = visual.ImageStim(win=win, name='Nback_Instructions',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1.125, 1.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Nback_Fixation"
Nback_FixationClock = core.Clock()
Fixation_Nback = visual.TextStim(win=win, ori=0, name='Fixation_Nback',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Nback_Stimulus"
Nback_StimulusClock = core.Clock()
Letter_Nback = visual.TextStim(win=win, ori=0, name='Letter_Nback',
    text='default text',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Nback_responseList = []
Nback_correctList = []
Nback_accuracy = []
Nback_responseTimeList = []

# Initialize components for Routine "End"
EndClock = core.Clock()
GoodBye = visual.TextStim(win=win, ori=0, name='GoodBye',
    text=u'Thank you, the study is complete. Please wait patiently for the technician to prompt you for the rest of the scanning.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Start"-------
t = 0
StartClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat

# keep track of which components have finished
StartComponents = []
StartComponents.append(Welcome)
for thisComponent in StartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Start"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if t >= 0.0 and Welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome.tStart = t  # underestimates by a little under one frame
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.setAutoDraw(True)
    if Welcome.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        Welcome.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "AreYouSure"-------
t = 0
AreYouSureClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
AreYouSureComponents = []
AreYouSureComponents.append(Warning)
for thisComponent in AreYouSureComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "AreYouSure"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = AreYouSureClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Warning* updates
    if t >= 0.0 and Warning.status == NOT_STARTED:
        # keep track of start time/frame for later
        Warning.tStart = t  # underestimates by a little under one frame
        Warning.frameNStart = frameN  # exact frame index
        Warning.setAutoDraw(True)
    if Warning.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        Warning.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AreYouSureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "AreYouSure"-------
for thisComponent in AreYouSureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "MRI_sync"-------
t = 0
MRI_syncClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Pulse_Next_Slide = event.BuilderKeyResponse()  # create an object of type KeyResponse
Pulse_Next_Slide.status = NOT_STARTED
# keep track of which components have finished
MRI_syncComponents = []
MRI_syncComponents.append(Waiting_For_Pulse)
MRI_syncComponents.append(Pulse_Next_Slide)
for thisComponent in MRI_syncComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "MRI_sync"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = MRI_syncClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Waiting_For_Pulse* updates
    if t >= 0.0 and Waiting_For_Pulse.status == NOT_STARTED:
        # keep track of start time/frame for later
        Waiting_For_Pulse.tStart = t  # underestimates by a little under one frame
        Waiting_For_Pulse.frameNStart = frameN  # exact frame index
        Waiting_For_Pulse.setAutoDraw(True)
    
    # *Pulse_Next_Slide* updates
    if t >= 0.0 and Pulse_Next_Slide.status == NOT_STARTED:
        # keep track of start time/frame for later
        Pulse_Next_Slide.tStart = t  # underestimates by a little under one frame
        Pulse_Next_Slide.frameNStart = frameN  # exact frame index
        Pulse_Next_Slide.status = STARTED
        # AllowedKeys looks like a variable named `triggerButton`
        if not 'triggerButton' in locals():
            logging.error('AllowedKeys variable `triggerButton` is not defined.')
            core.quit()
        if not type(triggerButton) in [list, tuple, np.ndarray]:
            if not isinstance(triggerButton, basestring):
                logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                core.quit()
            elif not ',' in triggerButton: triggerButton = (triggerButton,)
            else:  triggerButton = eval(triggerButton)
        # keyboard checking is just starting
        Pulse_Next_Slide.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if Pulse_Next_Slide.status == STARTED:
        theseKeys = event.getKeys(keyList=list(triggerButton))
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Pulse_Next_Slide.keys.extend(theseKeys)  # storing all keys
            Pulse_Next_Slide.rt.append(Pulse_Next_Slide.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MRI_syncComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "MRI_sync"-------
for thisComponent in MRI_syncComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Pulse_Next_Slide.keys in ['', [], None]:  # No response was made
   Pulse_Next_Slide.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('Pulse_Next_Slide.keys',Pulse_Next_Slide.keys)
if Pulse_Next_Slide.keys != None:  # we had a response
    thisExp.addData('Pulse_Next_Slide.rt', Pulse_Next_Slide.rt)
thisExp.nextEntry()
# the Routine "MRI_sync" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
epoch = data.TrialHandler(nReps=4, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='epoch')
thisExp.addLoop(epoch)  # add the loop to the experiment
thisEpoch = epoch.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisEpoch.rgb)
if thisEpoch != None:
    for paramName in thisEpoch.keys():
        exec(paramName + '= thisEpoch.' + paramName)

for thisEpoch in epoch:
    currentLoop = epoch
    # abbreviate parameter names if possible (e.g. rgb = thisEpoch.rgb)
    if thisEpoch != None:
        for paramName in thisEpoch.keys():
            exec(paramName + '= thisEpoch.' + paramName)
    
    #------Prepare to start Routine "Welcome_CPT_X"-------
    t = 0
    Welcome_CPT_XClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if epoch_counter == 0:
        instr_duration = 1320
        instr_duration2 = 1800
        splicer1 = epoch_counter
        splicer2 = splicer1 + 2
        instruction_image = 'N-back Instructions.jpg'
    else:
        instr_duration = instrStopTime
        instr_duration2 = instrStopTime2
        splicer1 = epoch_counter*2
        splicer2 = splicer1 + 2
        instruction_image = 'N-back Instructions short.jpg'
    
    instr_duration_s = str(int((instr_duration-120)/ 60))
    
    num_of_stim = stim_selection['round%s' % (epoch_counter + 1)]
    nback_num_of_stim = nback_stim_selection['round%s' % (epoch_counter + 1)]
    
    Instructions_CPT_X.setText("In this task, letters will be presented rapidly on the screen one at a time. Anytime you see the letter X, press button 1 as quickly as you can. Only press when you see letter X.\n\nThis screen will be up for " + instr_duration_s + " seconds.")
    Trigger_CPT_X_Instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_CPT_X_Instructions.status = NOT_STARTED
    # keep track of which components have finished
    Welcome_CPT_XComponents = []
    Welcome_CPT_XComponents.append(grating)
    Welcome_CPT_XComponents.append(Instructions_CPT_X)
    Welcome_CPT_XComponents.append(Trigger_CPT_X_Instructions)
    for thisComponent in Welcome_CPT_XComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Welcome_CPT_X"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Welcome_CPT_XClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *grating* updates
        if frameN >= 0 and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        if grating.status == STARTED and frameN >= instr_duration-120:
            grating.setAutoDraw(False)
        
        # *Instructions_CPT_X* updates
        if frameN >= 0 and Instructions_CPT_X.status == NOT_STARTED:
            # keep track of start time/frame for later
            Instructions_CPT_X.tStart = t  # underestimates by a little under one frame
            Instructions_CPT_X.frameNStart = frameN  # exact frame index
            Instructions_CPT_X.setAutoDraw(True)
        if Instructions_CPT_X.status == STARTED and frameN >= instr_duration-120:
            Instructions_CPT_X.setAutoDraw(False)
        
        # *Trigger_CPT_X_Instructions* updates
        if frameN >= 0.0 and Trigger_CPT_X_Instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_CPT_X_Instructions.tStart = t  # underestimates by a little under one frame
            Trigger_CPT_X_Instructions.frameNStart = frameN  # exact frame index
            Trigger_CPT_X_Instructions.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_CPT_X_Instructions.clock.reset()  # now t=0
        if Trigger_CPT_X_Instructions.status == STARTED and frameN >= instr_duration:
            Trigger_CPT_X_Instructions.status = STOPPED
        if Trigger_CPT_X_Instructions.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_CPT_X_Instructions.keys.extend(theseKeys)  # storing all keys
                Trigger_CPT_X_Instructions.rt.append(Trigger_CPT_X_Instructions.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_CPT_XComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Welcome_CPT_X"-------
    for thisComponent in Welcome_CPT_XComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    epoch_counter += 1
    # check responses
    if Trigger_CPT_X_Instructions.keys in ['', [], None]:  # No response was made
       Trigger_CPT_X_Instructions.keys=None
    # store data for epoch (TrialHandler)
    epoch.addData('Trigger_CPT_X_Instructions.keys',Trigger_CPT_X_Instructions.keys)
    if Trigger_CPT_X_Instructions.keys != None:  # we had a response
        epoch.addData('Trigger_CPT_X_Instructions.rt', Trigger_CPT_X_Instructions.rt)
    # the Routine "Welcome_CPT_X" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    CPT_X_Trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('CPTstimOrder1_all.csv', selection=num_of_stim),
        seed=None, name='CPT_X_Trials')
    thisExp.addLoop(CPT_X_Trials)  # add the loop to the experiment
    thisCPT_X_Trial = CPT_X_Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisCPT_X_Trial.rgb)
    if thisCPT_X_Trial != None:
        for paramName in thisCPT_X_Trial.keys():
            exec(paramName + '= thisCPT_X_Trial.' + paramName)
    
    for thisCPT_X_Trial in CPT_X_Trials:
        currentLoop = CPT_X_Trials
        # abbreviate parameter names if possible (e.g. rgb = thisCPT_X_Trial.rgb)
        if thisCPT_X_Trial != None:
            for paramName in thisCPT_X_Trial.keys():
                exec(paramName + '= thisCPT_X_Trial.' + paramName)
        
        #------Prepare to start Routine "CPT_X"-------
        t = 0
        CPT_XClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Letter_CPT_X.setText(CPT_letters)
        Response_CPT_X_X = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Response_CPT_X_X.status = NOT_STARTED
        Trigger_CPT_X_Stimulus = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Trigger_CPT_X_Stimulus.status = NOT_STARTED
        
        # keep track of which components have finished
        CPT_XComponents = []
        CPT_XComponents.append(Letter_CPT_X)
        CPT_XComponents.append(Response_CPT_X_X)
        CPT_XComponents.append(Trigger_CPT_X_Stimulus)
        for thisComponent in CPT_XComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "CPT_X"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CPT_XClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Letter_CPT_X* updates
            if frameN >= 0 and Letter_CPT_X.status == NOT_STARTED:
                # keep track of start time/frame for later
                Letter_CPT_X.tStart = t  # underestimates by a little under one frame
                Letter_CPT_X.frameNStart = frameN  # exact frame index
                Letter_CPT_X.setAutoDraw(True)
            if Letter_CPT_X.status == STARTED and frameN >= 6:
                Letter_CPT_X.setAutoDraw(False)
            
            # *Response_CPT_X_X* updates
            if frameN >= 0 and Response_CPT_X_X.status == NOT_STARTED:
                # keep track of start time/frame for later
                Response_CPT_X_X.tStart = t  # underestimates by a little under one frame
                Response_CPT_X_X.frameNStart = frameN  # exact frame index
                Response_CPT_X_X.status = STARTED
                # keyboard checking is just starting
                Response_CPT_X_X.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Response_CPT_X_X.status == STARTED and frameN >= 60:
                Response_CPT_X_X.status = STOPPED
            if Response_CPT_X_X.status == STARTED:
                theseKeys = event.getKeys(keyList=['1'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Response_CPT_X_X.keys = theseKeys[-1]  # just the last key pressed
                    Response_CPT_X_X.rt = Response_CPT_X_X.clock.getTime()
                    # was this 'correct'?
                    if (Response_CPT_X_X.keys == str(correctButton)) or (Response_CPT_X_X.keys == correctButton):
                        Response_CPT_X_X.corr = 1
                    else:
                        Response_CPT_X_X.corr = 0
            
            # *Trigger_CPT_X_Stimulus* updates
            if frameN >= 0 and Trigger_CPT_X_Stimulus.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trigger_CPT_X_Stimulus.tStart = t  # underestimates by a little under one frame
                Trigger_CPT_X_Stimulus.frameNStart = frameN  # exact frame index
                Trigger_CPT_X_Stimulus.status = STARTED
                # AllowedKeys looks like a variable named `triggerButton`
                if not 'triggerButton' in locals():
                    logging.error('AllowedKeys variable `triggerButton` is not defined.')
                    core.quit()
                if not type(triggerButton) in [list, tuple, np.ndarray]:
                    if not isinstance(triggerButton, basestring):
                        logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                        core.quit()
                    elif not ',' in triggerButton: triggerButton = (triggerButton,)
                    else:  triggerButton = eval(triggerButton)
                # keyboard checking is just starting
                Trigger_CPT_X_Stimulus.clock.reset()  # now t=0
            if Trigger_CPT_X_Stimulus.status == STARTED and frameN >= 60:
                Trigger_CPT_X_Stimulus.status = STOPPED
            if Trigger_CPT_X_Stimulus.status == STARTED:
                theseKeys = event.getKeys(keyList=list(triggerButton))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Trigger_CPT_X_Stimulus.keys.extend(theseKeys)  # storing all keys
                    Trigger_CPT_X_Stimulus.rt.append(Trigger_CPT_X_Stimulus.clock.getTime())
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CPT_XComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "CPT_X"-------
        for thisComponent in CPT_XComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Response_CPT_X_X.keys in ['', [], None]:  # No response was made
           Response_CPT_X_X.keys=None
           # was no response the correct answer?!
           if str(correctButton).lower() == 'none': Response_CPT_X_X.corr = 1  # correct non-response
           else: Response_CPT_X_X.corr = 0  # failed to respond (incorrectly)
        # store data for CPT_X_Trials (TrialHandler)
        CPT_X_Trials.addData('Response_CPT_X_X.keys',Response_CPT_X_X.keys)
        CPT_X_Trials.addData('Response_CPT_X_X.corr', Response_CPT_X_X.corr)
        if Response_CPT_X_X.keys != None:  # we had a response
            CPT_X_Trials.addData('Response_CPT_X_X.rt', Response_CPT_X_X.rt)
        # check responses
        if Trigger_CPT_X_Stimulus.keys in ['', [], None]:  # No response was made
           Trigger_CPT_X_Stimulus.keys=None
        # store data for CPT_X_Trials (TrialHandler)
        CPT_X_Trials.addData('Trigger_CPT_X_Stimulus.keys',Trigger_CPT_X_Stimulus.keys)
        if Trigger_CPT_X_Stimulus.keys != None:  # we had a response
            CPT_X_Trials.addData('Trigger_CPT_X_Stimulus.rt', Trigger_CPT_X_Stimulus.rt)
        #print 'Response_CPT_X_X.keys = %s' % Response_CPT_X_X.keys
        CPT_X_responseList.append(Response_CPT_X_X.keys)
        #print 'CPT_X_responseList = %s' % CPT_X_responseList
        CPT_X_correctList.append(Response_CPT_X_X.corr)
        if len(CPT_X_accuracy) > 0:
            CPT_X_accuracy.append(sum(CPT_X_correctList)/len(CPT_X_correctList))
        else:
            CPT_X_accuracy.append(Response_CPT_X_X.corr)
        if Response_CPT_X_X.keys != None:  # we had a response
            CPT_X_responseTimeList.append(Response_CPT_X_X.rt)
        else:
            CPT_X_responseTimeList.append(0)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'CPT_X_Trials'
    
    # get names of stimulus parameters
    if CPT_X_Trials.trialList in ([], [None], None):  params = []
    else:  params = CPT_X_Trials.trialList[0].keys()
    # save data for this loop
    CPT_X_Trials.saveAsExcel(filename + '.xlsx', sheetName='CPT_X_Trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    CPT_X_Trials.saveAsText(filename + 'CPT_X_Trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    #------Prepare to start Routine "Welcome_CPT_AX"-------
    t = 0
    Welcome_CPT_AXClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Instructions_CPT_AX.setText("This time press button 1 as quickly as you can when you see the letter X if it comes after letter A. Do not hit the button on letter A, only on letter X when it comes AFTER letter A.\n\nThis screen will be up for " + instr_duration_s + " seconds.")
    Trigger_CPT_AX_Instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_CPT_AX_Instructions.status = NOT_STARTED
    # keep track of which components have finished
    Welcome_CPT_AXComponents = []
    Welcome_CPT_AXComponents.append(grating_2)
    Welcome_CPT_AXComponents.append(Instructions_CPT_AX)
    Welcome_CPT_AXComponents.append(Trigger_CPT_AX_Instructions)
    for thisComponent in Welcome_CPT_AXComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Welcome_CPT_AX"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Welcome_CPT_AXClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating_2* updates
        if frameN >= 0.0 and grating_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_2.tStart = t  # underestimates by a little under one frame
            grating_2.frameNStart = frameN  # exact frame index
            grating_2.setAutoDraw(True)
        if grating_2.status == STARTED and frameN >= instr_duration-120:
            grating_2.setAutoDraw(False)
        
        # *Instructions_CPT_AX* updates
        if frameN >= 0 and Instructions_CPT_AX.status == NOT_STARTED:
            # keep track of start time/frame for later
            Instructions_CPT_AX.tStart = t  # underestimates by a little under one frame
            Instructions_CPT_AX.frameNStart = frameN  # exact frame index
            Instructions_CPT_AX.setAutoDraw(True)
        if Instructions_CPT_AX.status == STARTED and frameN >= instr_duration-120:
            Instructions_CPT_AX.setAutoDraw(False)
        
        # *Trigger_CPT_AX_Instructions* updates
        if frameN >= 0 and Trigger_CPT_AX_Instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_CPT_AX_Instructions.tStart = t  # underestimates by a little under one frame
            Trigger_CPT_AX_Instructions.frameNStart = frameN  # exact frame index
            Trigger_CPT_AX_Instructions.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_CPT_AX_Instructions.clock.reset()  # now t=0
        if Trigger_CPT_AX_Instructions.status == STARTED and frameN >= instr_duration:
            Trigger_CPT_AX_Instructions.status = STOPPED
        if Trigger_CPT_AX_Instructions.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_CPT_AX_Instructions.keys.extend(theseKeys)  # storing all keys
                Trigger_CPT_AX_Instructions.rt.append(Trigger_CPT_AX_Instructions.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_CPT_AXComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Welcome_CPT_AX"-------
    for thisComponent in Welcome_CPT_AXComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Trigger_CPT_AX_Instructions.keys in ['', [], None]:  # No response was made
       Trigger_CPT_AX_Instructions.keys=None
    # store data for epoch (TrialHandler)
    epoch.addData('Trigger_CPT_AX_Instructions.keys',Trigger_CPT_AX_Instructions.keys)
    if Trigger_CPT_AX_Instructions.keys != None:  # we had a response
        epoch.addData('Trigger_CPT_AX_Instructions.rt', Trigger_CPT_AX_Instructions.rt)
    # the Routine "Welcome_CPT_AX" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    CPT_AX_Trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('CPTstimOrder2_all.csv', selection=num_of_stim),
        seed=None, name='CPT_AX_Trials')
    thisExp.addLoop(CPT_AX_Trials)  # add the loop to the experiment
    thisCPT_AX_Trial = CPT_AX_Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisCPT_AX_Trial.rgb)
    if thisCPT_AX_Trial != None:
        for paramName in thisCPT_AX_Trial.keys():
            exec(paramName + '= thisCPT_AX_Trial.' + paramName)
    
    for thisCPT_AX_Trial in CPT_AX_Trials:
        currentLoop = CPT_AX_Trials
        # abbreviate parameter names if possible (e.g. rgb = thisCPT_AX_Trial.rgb)
        if thisCPT_AX_Trial != None:
            for paramName in thisCPT_AX_Trial.keys():
                exec(paramName + '= thisCPT_AX_Trial.' + paramName)
        
        #------Prepare to start Routine "CPT_AX"-------
        t = 0
        CPT_AXClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Letter_CPT_AX.setText(CPT_letters)
        Response_CPT_AX_X = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Response_CPT_AX_X.status = NOT_STARTED
        Response_CPT_AX_A = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Response_CPT_AX_A.status = NOT_STARTED
        Trigger_CPT_AX_Stimuls = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Trigger_CPT_AX_Stimuls.status = NOT_STARTED
        
        # keep track of which components have finished
        CPT_AXComponents = []
        CPT_AXComponents.append(Letter_CPT_AX)
        CPT_AXComponents.append(Response_CPT_AX_X)
        CPT_AXComponents.append(Response_CPT_AX_A)
        CPT_AXComponents.append(Trigger_CPT_AX_Stimuls)
        for thisComponent in CPT_AXComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "CPT_AX"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CPT_AXClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Letter_CPT_AX* updates
            if frameN >= 0 and Letter_CPT_AX.status == NOT_STARTED:
                # keep track of start time/frame for later
                Letter_CPT_AX.tStart = t  # underestimates by a little under one frame
                Letter_CPT_AX.frameNStart = frameN  # exact frame index
                Letter_CPT_AX.setAutoDraw(True)
            if Letter_CPT_AX.status == STARTED and frameN >= 6:
                Letter_CPT_AX.setAutoDraw(False)
            
            # *Response_CPT_AX_X* updates
            if frameN >= 0 and Response_CPT_AX_X.status == NOT_STARTED:
                # keep track of start time/frame for later
                Response_CPT_AX_X.tStart = t  # underestimates by a little under one frame
                Response_CPT_AX_X.frameNStart = frameN  # exact frame index
                Response_CPT_AX_X.status = STARTED
                # keyboard checking is just starting
                Response_CPT_AX_X.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Response_CPT_AX_X.status == STARTED and frameN >= 60:
                Response_CPT_AX_X.status = STOPPED
            if Response_CPT_AX_X.status == STARTED:
                theseKeys = event.getKeys(keyList=['1'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Response_CPT_AX_X.keys = theseKeys[-1]  # just the last key pressed
                    Response_CPT_AX_X.rt = Response_CPT_AX_X.clock.getTime()
                    # was this 'correct'?
                    if (Response_CPT_AX_X.keys == str(correctButton)) or (Response_CPT_AX_X.keys == correctButton):
                        Response_CPT_AX_X.corr = 1
                    else:
                        Response_CPT_AX_X.corr = 0
            
            # *Response_CPT_AX_A* updates
            if frameN >= 0 and Response_CPT_AX_A.status == NOT_STARTED:
                # keep track of start time/frame for later
                Response_CPT_AX_A.tStart = t  # underestimates by a little under one frame
                Response_CPT_AX_A.frameNStart = frameN  # exact frame index
                Response_CPT_AX_A.status = STARTED
                # keyboard checking is just starting
                Response_CPT_AX_A.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Response_CPT_AX_A.status == STARTED and frameN >= 60:
                Response_CPT_AX_A.status = STOPPED
            if Response_CPT_AX_A.status == STARTED:
                theseKeys = event.getKeys(keyList=['1'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Response_CPT_AX_A.keys = theseKeys[-1]  # just the last key pressed
                    Response_CPT_AX_A.rt = Response_CPT_AX_A.clock.getTime()
            
            # *Trigger_CPT_AX_Stimuls* updates
            if frameN >= 0 and Trigger_CPT_AX_Stimuls.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trigger_CPT_AX_Stimuls.tStart = t  # underestimates by a little under one frame
                Trigger_CPT_AX_Stimuls.frameNStart = frameN  # exact frame index
                Trigger_CPT_AX_Stimuls.status = STARTED
                # AllowedKeys looks like a variable named `triggerButton`
                if not 'triggerButton' in locals():
                    logging.error('AllowedKeys variable `triggerButton` is not defined.')
                    core.quit()
                if not type(triggerButton) in [list, tuple, np.ndarray]:
                    if not isinstance(triggerButton, basestring):
                        logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                        core.quit()
                    elif not ',' in triggerButton: triggerButton = (triggerButton,)
                    else:  triggerButton = eval(triggerButton)
                # keyboard checking is just starting
                Trigger_CPT_AX_Stimuls.clock.reset()  # now t=0
            if Trigger_CPT_AX_Stimuls.status == STARTED and frameN >= 60:
                Trigger_CPT_AX_Stimuls.status = STOPPED
            if Trigger_CPT_AX_Stimuls.status == STARTED:
                theseKeys = event.getKeys(keyList=list(triggerButton))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Trigger_CPT_AX_Stimuls.keys.extend(theseKeys)  # storing all keys
                    Trigger_CPT_AX_Stimuls.rt.append(Trigger_CPT_AX_Stimuls.clock.getTime())
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CPT_AXComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "CPT_AX"-------
        for thisComponent in CPT_AXComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Response_CPT_AX_X.keys in ['', [], None]:  # No response was made
           Response_CPT_AX_X.keys=None
           # was no response the correct answer?!
           if str(correctButton).lower() == 'none': Response_CPT_AX_X.corr = 1  # correct non-response
           else: Response_CPT_AX_X.corr = 0  # failed to respond (incorrectly)
        # store data for CPT_AX_Trials (TrialHandler)
        CPT_AX_Trials.addData('Response_CPT_AX_X.keys',Response_CPT_AX_X.keys)
        CPT_AX_Trials.addData('Response_CPT_AX_X.corr', Response_CPT_AX_X.corr)
        if Response_CPT_AX_X.keys != None:  # we had a response
            CPT_AX_Trials.addData('Response_CPT_AX_X.rt', Response_CPT_AX_X.rt)
        # check responses
        if Response_CPT_AX_A.keys in ['', [], None]:  # No response was made
           Response_CPT_AX_A.keys=None
        # store data for CPT_AX_Trials (TrialHandler)
        CPT_AX_Trials.addData('Response_CPT_AX_A.keys',Response_CPT_AX_A.keys)
        if Response_CPT_AX_A.keys != None:  # we had a response
            CPT_AX_Trials.addData('Response_CPT_AX_A.rt', Response_CPT_AX_A.rt)
        # check responses
        if Trigger_CPT_AX_Stimuls.keys in ['', [], None]:  # No response was made
           Trigger_CPT_AX_Stimuls.keys=None
        # store data for CPT_AX_Trials (TrialHandler)
        CPT_AX_Trials.addData('Trigger_CPT_AX_Stimuls.keys',Trigger_CPT_AX_Stimuls.keys)
        if Trigger_CPT_AX_Stimuls.keys != None:  # we had a response
            CPT_AX_Trials.addData('Trigger_CPT_AX_Stimuls.rt', Trigger_CPT_AX_Stimuls.rt)
        CPT_AX_responseList.append(Response_CPT_AX_X.keys)
        CPT_AX_correctList.append(Response_CPT_AX_X.corr)
        if (Response_CPT_AX_X.corr == 0) and (CPT_letters == 'A'):
            CPT_AX_responseToAList.append(1)
        else:
            CPT_AX_responseToAList.append(0)
        if len(CPT_AX_accuracy) > 0:
            CPT_AX_accuracy.append(sum(CPT_AX_correctList)/len(CPT_AX_correctList))
        else:
            CPT_AX_accuracy.append(Response_CPT_AX_X.corr)
        if Response_CPT_AX_X.keys != None:  # we had a response
            CPT_AX_responseTimeList.append(Response_CPT_AX_X.rt)
        else:
            CPT_AX_responseTimeList.append(0)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'CPT_AX_Trials'
    
    # get names of stimulus parameters
    if CPT_AX_Trials.trialList in ([], [None], None):  params = []
    else:  params = CPT_AX_Trials.trialList[0].keys()
    # save data for this loop
    CPT_AX_Trials.saveAsExcel(filename + '.xlsx', sheetName='CPT_AX_Trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    CPT_AX_Trials.saveAsText(filename + 'CPT_AX_Trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    #------Prepare to start Routine "Welcome_Nback"-------
    t = 0
    Welcome_NbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Trigger_Nback_Instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Trigger_Nback_Instructions.status = NOT_STARTED
    # keep track of which components have finished
    Welcome_NbackComponents = []
    Welcome_NbackComponents.append(Nback_Instructions)
    Welcome_NbackComponents.append(Trigger_Nback_Instructions)
    for thisComponent in Welcome_NbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Welcome_Nback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Welcome_NbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Nback_Instructions* updates
        if frameN >= 0 and Nback_Instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            Nback_Instructions.tStart = t  # underestimates by a little under one frame
            Nback_Instructions.frameNStart = frameN  # exact frame index
            Nback_Instructions.setAutoDraw(True)
        if Nback_Instructions.status == STARTED and frameN >= instr_duration2:
            Nback_Instructions.setAutoDraw(False)
        if Nback_Instructions.status == STARTED:  # only update if being drawn
            Nback_Instructions.setImage(instruction_image, log=False)
        
        # *Trigger_Nback_Instructions* updates
        if frameN >= 0 and Trigger_Nback_Instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trigger_Nback_Instructions.tStart = t  # underestimates by a little under one frame
            Trigger_Nback_Instructions.frameNStart = frameN  # exact frame index
            Trigger_Nback_Instructions.status = STARTED
            # AllowedKeys looks like a variable named `triggerButton`
            if not 'triggerButton' in locals():
                logging.error('AllowedKeys variable `triggerButton` is not defined.')
                core.quit()
            if not type(triggerButton) in [list, tuple, np.ndarray]:
                if not isinstance(triggerButton, basestring):
                    logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in triggerButton: triggerButton = (triggerButton,)
                else:  triggerButton = eval(triggerButton)
            # keyboard checking is just starting
            Trigger_Nback_Instructions.clock.reset()  # now t=0
        if Trigger_Nback_Instructions.status == STARTED and frameN >= instr_duration2:
            Trigger_Nback_Instructions.status = STOPPED
        if Trigger_Nback_Instructions.status == STARTED:
            theseKeys = event.getKeys(keyList=list(triggerButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Trigger_Nback_Instructions.keys.extend(theseKeys)  # storing all keys
                Trigger_Nback_Instructions.rt.append(Trigger_Nback_Instructions.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_NbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Welcome_Nback"-------
    for thisComponent in Welcome_NbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Trigger_Nback_Instructions.keys in ['', [], None]:  # No response was made
       Trigger_Nback_Instructions.keys=None
    # store data for epoch (TrialHandler)
    epoch.addData('Trigger_Nback_Instructions.keys',Trigger_Nback_Instructions.keys)
    if Trigger_Nback_Instructions.keys != None:  # we had a response
        epoch.addData('Trigger_Nback_Instructions.rt', Trigger_Nback_Instructions.rt)
    # the Routine "Welcome_Nback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Nback_Trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('NbackStimOrder_all.csv', selection=nback_num_of_stim),
        seed=None, name='Nback_Trials')
    thisExp.addLoop(Nback_Trials)  # add the loop to the experiment
    thisNback_Trial = Nback_Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisNback_Trial.rgb)
    if thisNback_Trial != None:
        for paramName in thisNback_Trial.keys():
            exec(paramName + '= thisNback_Trial.' + paramName)
    
    for thisNback_Trial in Nback_Trials:
        currentLoop = Nback_Trials
        # abbreviate parameter names if possible (e.g. rgb = thisNback_Trial.rgb)
        if thisNback_Trial != None:
            for paramName in thisNback_Trial.keys():
                exec(paramName + '= thisNback_Trial.' + paramName)
        
        #------Prepare to start Routine "Nback_Fixation"-------
        t = 0
        Nback_FixationClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Trigger_Nback_Fixation = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Trigger_Nback_Fixation.status = NOT_STARTED
        # keep track of which components have finished
        Nback_FixationComponents = []
        Nback_FixationComponents.append(Fixation_Nback)
        Nback_FixationComponents.append(Trigger_Nback_Fixation)
        for thisComponent in Nback_FixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Nback_Fixation"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Nback_FixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_Nback* updates
            if frameN >= 0 and Fixation_Nback.status == NOT_STARTED:
                # keep track of start time/frame for later
                Fixation_Nback.tStart = t  # underestimates by a little under one frame
                Fixation_Nback.frameNStart = frameN  # exact frame index
                Fixation_Nback.setAutoDraw(True)
            if Fixation_Nback.status == STARTED and frameN >= 60:
                Fixation_Nback.setAutoDraw(False)
            
            # *Trigger_Nback_Fixation* updates
            if frameN >= 0 and Trigger_Nback_Fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trigger_Nback_Fixation.tStart = t  # underestimates by a little under one frame
                Trigger_Nback_Fixation.frameNStart = frameN  # exact frame index
                Trigger_Nback_Fixation.status = STARTED
                # AllowedKeys looks like a variable named `triggerButton`
                if not 'triggerButton' in locals():
                    logging.error('AllowedKeys variable `triggerButton` is not defined.')
                    core.quit()
                if not type(triggerButton) in [list, tuple, np.ndarray]:
                    if not isinstance(triggerButton, basestring):
                        logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                        core.quit()
                    elif not ',' in triggerButton: triggerButton = (triggerButton,)
                    else:  triggerButton = eval(triggerButton)
                # keyboard checking is just starting
                Trigger_Nback_Fixation.clock.reset()  # now t=0
            if Trigger_Nback_Fixation.status == STARTED and frameN >= 60:
                Trigger_Nback_Fixation.status = STOPPED
            if Trigger_Nback_Fixation.status == STARTED:
                theseKeys = event.getKeys(keyList=list(triggerButton))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Trigger_Nback_Fixation.keys.extend(theseKeys)  # storing all keys
                    Trigger_Nback_Fixation.rt.append(Trigger_Nback_Fixation.clock.getTime())
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Nback_FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Nback_Fixation"-------
        for thisComponent in Nback_FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Trigger_Nback_Fixation.keys in ['', [], None]:  # No response was made
           Trigger_Nback_Fixation.keys=None
        # store data for Nback_Trials (TrialHandler)
        Nback_Trials.addData('Trigger_Nback_Fixation.keys',Trigger_Nback_Fixation.keys)
        if Trigger_Nback_Fixation.keys != None:  # we had a response
            Nback_Trials.addData('Trigger_Nback_Fixation.rt', Trigger_Nback_Fixation.rt)
        
        #------Prepare to start Routine "Nback_Stimulus"-------
        t = 0
        Nback_StimulusClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Letter_Nback.setText(letters)
        Response_Nback = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Response_Nback.status = NOT_STARTED
        Trigger_Nback_Stimulus = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Trigger_Nback_Stimulus.status = NOT_STARTED
        
        # keep track of which components have finished
        Nback_StimulusComponents = []
        Nback_StimulusComponents.append(Letter_Nback)
        Nback_StimulusComponents.append(Response_Nback)
        Nback_StimulusComponents.append(Trigger_Nback_Stimulus)
        for thisComponent in Nback_StimulusComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Nback_Stimulus"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Nback_StimulusClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Letter_Nback* updates
            if frameN >= 0 and Letter_Nback.status == NOT_STARTED:
                # keep track of start time/frame for later
                Letter_Nback.tStart = t  # underestimates by a little under one frame
                Letter_Nback.frameNStart = frameN  # exact frame index
                Letter_Nback.setAutoDraw(True)
            if Letter_Nback.status == STARTED and frameN >= 60:
                Letter_Nback.setAutoDraw(False)
            
            # *Response_Nback* updates
            if frameN >= 0 and Response_Nback.status == NOT_STARTED:
                # keep track of start time/frame for later
                Response_Nback.tStart = t  # underestimates by a little under one frame
                Response_Nback.frameNStart = frameN  # exact frame index
                Response_Nback.status = STARTED
                # keyboard checking is just starting
                Response_Nback.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Response_Nback.status == STARTED and frameN >= 60:
                Response_Nback.status = STOPPED
            if Response_Nback.status == STARTED:
                theseKeys = event.getKeys(keyList=['1'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Response_Nback.keys = theseKeys[-1]  # just the last key pressed
                    Response_Nback.rt = Response_Nback.clock.getTime()
                    # was this 'correct'?
                    if (Response_Nback.keys == str(correctButton)) or (Response_Nback.keys == correctButton):
                        Response_Nback.corr = 1
                    else:
                        Response_Nback.corr = 0
            
            # *Trigger_Nback_Stimulus* updates
            if frameN >= 0 and Trigger_Nback_Stimulus.status == NOT_STARTED:
                # keep track of start time/frame for later
                Trigger_Nback_Stimulus.tStart = t  # underestimates by a little under one frame
                Trigger_Nback_Stimulus.frameNStart = frameN  # exact frame index
                Trigger_Nback_Stimulus.status = STARTED
                # AllowedKeys looks like a variable named `triggerButton`
                if not 'triggerButton' in locals():
                    logging.error('AllowedKeys variable `triggerButton` is not defined.')
                    core.quit()
                if not type(triggerButton) in [list, tuple, np.ndarray]:
                    if not isinstance(triggerButton, basestring):
                        logging.error('AllowedKeys variable `triggerButton` is not string- or list-like.')
                        core.quit()
                    elif not ',' in triggerButton: triggerButton = (triggerButton,)
                    else:  triggerButton = eval(triggerButton)
                # keyboard checking is just starting
                Trigger_Nback_Stimulus.clock.reset()  # now t=0
            if Trigger_Nback_Stimulus.status == STARTED and frameN >= 60:
                Trigger_Nback_Stimulus.status = STOPPED
            if Trigger_Nback_Stimulus.status == STARTED:
                theseKeys = event.getKeys(keyList=list(triggerButton))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Trigger_Nback_Stimulus.keys.extend(theseKeys)  # storing all keys
                    Trigger_Nback_Stimulus.rt.append(Trigger_Nback_Stimulus.clock.getTime())
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Nback_StimulusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Nback_Stimulus"-------
        for thisComponent in Nback_StimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Response_Nback.keys in ['', [], None]:  # No response was made
           Response_Nback.keys=None
           # was no response the correct answer?!
           if str(correctButton).lower() == 'none': Response_Nback.corr = 1  # correct non-response
           else: Response_Nback.corr = 0  # failed to respond (incorrectly)
        # store data for Nback_Trials (TrialHandler)
        Nback_Trials.addData('Response_Nback.keys',Response_Nback.keys)
        Nback_Trials.addData('Response_Nback.corr', Response_Nback.corr)
        if Response_Nback.keys != None:  # we had a response
            Nback_Trials.addData('Response_Nback.rt', Response_Nback.rt)
        # check responses
        if Trigger_Nback_Stimulus.keys in ['', [], None]:  # No response was made
           Trigger_Nback_Stimulus.keys=None
        # store data for Nback_Trials (TrialHandler)
        Nback_Trials.addData('Trigger_Nback_Stimulus.keys',Trigger_Nback_Stimulus.keys)
        if Trigger_Nback_Stimulus.keys != None:  # we had a response
            Nback_Trials.addData('Trigger_Nback_Stimulus.rt', Trigger_Nback_Stimulus.rt)
        Nback_responseList.append(Response_Nback.keys)
        #print 'Response_Nback.keys = %s' % Response_Nback.keys
        #print 'Nback_responseList = %s' % Nback_responseList
        Nback_correctList.append(Response_Nback.corr)
        if len(Nback_accuracy) > 0:
            Nback_accuracy.append(sum(Nback_correctList)/len(Nback_correctList))
        else:
            Nback_accuracy.append(Response_Nback.corr)
        if Response_Nback.keys != None:  # we had a response
            Nback_responseTimeList.append(Response_Nback.rt)
        else:
            Nback_responseTimeList.append(0)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Nback_Trials'
    
    # get names of stimulus parameters
    if Nback_Trials.trialList in ([], [None], None):  params = []
    else:  params = Nback_Trials.trialList[0].keys()
    # save data for this loop
    Nback_Trials.saveAsExcel(filename + '.xlsx', sheetName='Nback_Trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    Nback_Trials.saveAsText(filename + 'Nback_Trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 4 repeats of 'epoch'

# get names of stimulus parameters
if epoch.trialList in ([], [None], None):  params = []
else:  params = epoch.trialList[0].keys()
# save data for this loop
epoch.saveAsExcel(filename + '.xlsx', sheetName='epoch',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
epoch.saveAsText(filename + 'epoch.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
EndComponents.append(GoodBye)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GoodBye* updates
    if frameN >= 0.0 and GoodBye.status == NOT_STARTED:
        # keep track of start time/frame for later
        GoodBye.tStart = t  # underestimates by a little under one frame
        GoodBye.frameNStart = frameN  # exact frame index
        GoodBye.setAutoDraw(True)
    if GoodBye.status == STARTED and frameN >= instrStopTime:
        GoodBye.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


CPT_X_responseListTotal = len([elem for elem in CPT_X_responseList if elem == '1'])
CPT_X_correctList_Total = sum(CPT_X_correctList)
try:
    CPT_X_responseTimeList_Average = (sum(CPT_X_responseTimeList)/len([elem for elem in CPT_X_responseTimeList if elem != 0]))
except:
    CPT_X_responseTimeList_Average = 0
csvDictionary = {'CPT_X_letters': list1, 'correctButton':buttonList1, 'Response':CPT_X_responseList, 'Correct':CPT_X_correctList, 'Accuracy':CPT_X_accuracy, 'Response_Time':CPT_X_responseTimeList}
finalLine = {'CPT_X_letters': 'Total:', 'correctButton':'-'*5, 'Response':CPT_X_responseListTotal, 'Correct':CPT_X_correctList_Total, 'Accuracy':'Average:', 'Response_Time':CPT_X_responseTimeList_Average}
writeDataFile(csvDictionary, data_path + os.sep + '%s_CPT_X_results' % expInfo['participant'], ['CPT_X_letters', 'correctButton', 'Response', 'Correct', 'Accuracy', 'Response_Time'], finalLine)
csvDictionary = {}
CPT_AX_responseListTotal = len([elem for elem in CPT_AX_responseList if elem == '1'])
CPT_AX_correctList_Total = sum(CPT_AX_correctList)
CPT_AX_responseToAList_Total = sum(CPT_AX_responseToAList)
try:
    CPT_AX_responseTimeList_Average = (sum(CPT_AX_responseTimeList)/len([elem for elem in CPT_AX_responseTimeList if elem > 0]))
except:
    CPT_AX_responseTimeList_Average = 0
csvDictionary = {'CPT_AX_letters': list2, 'correctButton':buttonList2, 'Response':CPT_AX_responseList, 'Response_To_A':CPT_AX_responseToAList, 'Correct':CPT_AX_correctList, 'Accuracy':CPT_AX_accuracy, 'Response_Time':CPT_AX_responseTimeList}
finalLine = {'CPT_AX_letters': 'Total:', 'correctButton':'-'*5, 'Response':CPT_AX_responseListTotal, 'Response_To_A': CPT_AX_responseToAList_Total,'Correct':CPT_X_correctList_Total, 'Accuracy':'Average:', 'Response_Time':CPT_X_responseTimeList_Average}
writeDataFile(csvDictionary, data_path + os.sep + '%s_CPT_AX_results' % expInfo['participant'], ['CPT_AX_letters', 'correctButton', 'Response', 'Response_To_A', 'Correct', 'Accuracy', 'Response_Time'], finalLine)
csvDictionary = {}
Nback_responseListTotal = len([elem for elem in Nback_responseList if elem == '1'])
Nback_correctList_Total = sum(Nback_correctList)
try:
    Nback_responseTimeList_Average = (sum(Nback_responseTimeList)/len(elem for elem in Nback_responseTimeList if elem != 0))
except:
    Nback_responseTimeList_Average = 0
csvDictionary = {'Nback_letters': moresoOldLets, 'correctButton':moresoButtonList, 'Response':Nback_responseList, 'Correct':Nback_correctList, 'Accuracy':Nback_accuracy, 'Response_Time':Nback_responseTimeList}
finalLine = {'Nback_letters': 'Total:', 'correctButton':'-'*5, 'Response':Nback_responseListTotal, 'Correct':Nback_correctList_Total, 'Accuracy':'Average:', 'Response_Time':Nback_responseTimeList_Average}
writeDataFile(csvDictionary, data_path + os.sep + '%s_Nback_results' % expInfo['participant'], ['Nback_letters', 'correctButton', 'Response', 'Correct', 'Accuracy', 'Response_Time'], finalLine)
win.close()
core.quit()
