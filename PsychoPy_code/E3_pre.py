#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.1),
    on 十二月 19, 2023, at 20:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.1'
expName = 'VisualExp1'  # from the Builder filename that created this script
expInfo = {
    'participant ID': '',
    '性别': ['男','女'],
    '年龄': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}

# Run 'Before Experiment' code from code_init
import write_test_excel

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s_FB_40loop_ExpTest' % (expInfo['participant ID'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\xdan\\Documents\\E3_pilot\\PsychoPy\\E3_pre.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
    # return log file
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1463, 914], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='dkl',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0000, 0.0000, 0.0000]
        win.colorSpace = 'dkl'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "blank_for_code" ---
    # Run 'Begin Experiment' code from code_init
    #exp_idx = expInfo['实验编号']
    E1_instro1='Normal blank'
    #exp_id = int(exp_idx)
    dt_practice =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName='practice.xlsx', colums1_name='Pic0', colums2_name='correct_key0',loopNum=3, total_file_num=150)
    dt_practice.write()
    loop1_filename = 'task1_40.xlsx'
    loop2_filename = 'task2_40.xlsx'
    
    dt_loop1 =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName=loop1_filename, colums1_name='Pic1', colums2_name='correct_key1',loopNum=15, total_file_num=150)
    dt_loop1.write()
    
    dt_loop2 =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName=loop2_filename, colums1_name='Pic2', colums2_name='correct_key2',loopNum=15, total_file_num=150)
    
    dt_loop2.write()
    task1_time = 2
    task2_time = 2
    task1_score = 0
    task2_score = 0
    E1_instro1_filename = 'withoutP_instro1.txt'
    with open(E1_instro1_filename, 'r',encoding='UTF-8') as file:
        E1_instro1 = file.read()
        print(data)
    
    
    # --- Initialize components for Routine "instr1" ---
    instr_start = visual.TextStim(win=win, name='instr_start',
        text=E1_instro1,
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instr_start_key = keyboard.Keyboard()
    image_eg = visual.ImageStim(
        win=win,
        name='image_eg', 
        image='example_noprompt.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "practice_pic" ---
    fixation_practice = visual.TextStim(win=win, name='fixation_practice',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    pic_practice = visual.ImageStim(
        win=win,
        name='pic_practice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.8),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_practice = keyboard.Keyboard()
    text_left_4 = visual.TextStim(win=win, name='text_left_4',
        text='左\n(S键)',
        font='Open Sans',
        pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_right_4 = visual.TextStim(win=win, name='text_right_4',
        text='右\n(K键)',
        font='Open Sans',
        pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_6 = visual.TextStim(win=win, name='text_6',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "practice2task1" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='练习结束了，接下来是正式实验\n请在保证正确率的前提下尽快反应。\nS键表示左边红点分布更多，K键表示右边更多。\n每对1题，你将获得0.2元报酬，共计60题\n如果你已经准备好，按空格键开始测试1。',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_next_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "task1_with_P" ---
    fixation = visual.TextStim(win=win, name='fixation',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    task1_withP = visual.ImageStim(
        win=win,
        name='task1_withP', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.8),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_task1 = keyboard.Keyboard()
    text_left_2 = visual.TextStim(win=win, name='text_left_2',
        text='左\n(S键)',
        font='Open Sans',
        pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_right_2 = visual.TextStim(win=win, name='text_right_2',
        text='右\n(K键)',
        font='Open Sans',
        pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_7 = visual.TextStim(win=win, name='text_7',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "judge_task1" ---
    # Run 'Begin Experiment' code from code_judge_task1
    feedback = "" #建立名为feedback的变量，等号的左右两边均有空格(接下)
                  #（接上）等号右边为英文引号(内无空格)，会有文字赋值到该变量
    a = []  #建立名为a的变量，变量类型为列表，等号右边为中括号（内无空格）
    
    # --- Initialize components for Routine "task1_to_2" ---
    text = visual.TextStim(win=win, name='text',
        text='恭喜你完成测试1，\n你可以短暂休息几秒\n或直接按空格键开始测试2\n测试2与测试1内容一致\n做相同按键的判断即可\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_next = keyboard.Keyboard()
    
    # --- Initialize components for Routine "task2_without_P" ---
    fixation2 = visual.TextStim(win=win, name='fixation2',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    task2_noP = visual.ImageStim(
        win=win,
        name='task2_noP', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.8),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_task2 = keyboard.Keyboard()
    text_left_5 = visual.TextStim(win=win, name='text_left_5',
        text='左\n(S键)',
        font='Open Sans',
        pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_right_5 = visual.TextStim(win=win, name='text_right_5',
        text='右\n(K键)',
        font='Open Sans',
        pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_8 = visual.TextStim(win=win, name='text_8',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "judge_task2" ---
    # Run 'Begin Experiment' code from code_judge_task2
    feedback = "" #建立名为feedback的变量，等号的左右两边均有空格(接下)
                  #（接上）等号右边为英文引号(内无空格)，会有文字赋值到该变量
    a2 = []  #建立名为a的变量，变量类型为列表，等号右边为中括号（内无空格）
    
    # --- Initialize components for Routine "thanks_gen" ---
    
    # --- Initialize components for Routine "Thanks" ---
    thanks = visual.TextStim(win=win, name='thanks',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "blank_for_code" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blank_for_code.started', globalClock.getTime())
    # keep track of which components have finished
    blank_for_codeComponents = []
    for thisComponent in blank_for_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank_for_code" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_for_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank_for_code" ---
    for thisComponent in blank_for_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank_for_code.stopped', globalClock.getTime())
    # the Routine "blank_for_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr1.started', globalClock.getTime())
    instr_start_key.keys = []
    instr_start_key.rt = []
    _instr_start_key_allKeys = []
    # keep track of which components have finished
    instr1Components = [instr_start, instr_start_key, image_eg]
    for thisComponent in instr1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_start* updates
        
        # if instr_start is starting this frame...
        if instr_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_start.frameNStart = frameN  # exact frame index
            instr_start.tStart = t  # local t and not account for scr refresh
            instr_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_start, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_start.status = STARTED
            instr_start.setAutoDraw(True)
        
        # if instr_start is active this frame...
        if instr_start.status == STARTED:
            # update params
            pass
        
        # *instr_start_key* updates
        waitOnFlip = False
        
        # if instr_start_key is starting this frame...
        if instr_start_key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instr_start_key.frameNStart = frameN  # exact frame index
            instr_start_key.tStart = t  # local t and not account for scr refresh
            instr_start_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_start_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_start_key.started')
            # update status
            instr_start_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_start_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_start_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_start_key.status == STARTED and not waitOnFlip:
            theseKeys = instr_start_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instr_start_key_allKeys.extend(theseKeys)
            if len(_instr_start_key_allKeys):
                instr_start_key.keys = _instr_start_key_allKeys[-1].name  # just the last key pressed
                instr_start_key.rt = _instr_start_key_allKeys[-1].rt
                instr_start_key.duration = _instr_start_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *image_eg* updates
        
        # if image_eg is starting this frame...
        if image_eg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg.frameNStart = frameN  # exact frame index
            image_eg.tStart = t  # local t and not account for scr refresh
            image_eg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg.started')
            # update status
            image_eg.status = STARTED
            image_eg.setAutoDraw(True)
        
        # if image_eg is active this frame...
        if image_eg.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr1" ---
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr1.stopped', globalClock.getTime())
    # the Routine "instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_practive = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice.xlsx'),
        seed=None, name='trials_practive')
    thisExp.addLoop(trials_practive)  # add the loop to the experiment
    thisTrials_practive = trials_practive.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practive.rgb)
    if thisTrials_practive != None:
        for paramName in thisTrials_practive:
            globals()[paramName] = thisTrials_practive[paramName]
    
    for thisTrials_practive in trials_practive:
        currentLoop = trials_practive
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_practive.rgb)
        if thisTrials_practive != None:
            for paramName in thisTrials_practive:
                globals()[paramName] = thisTrials_practive[paramName]
        
        # --- Prepare to start Routine "practice_pic" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice_pic.started', globalClock.getTime())
        fixation_practice.setText('+')
        pic_practice.setImage(Pic0)
        key_resp_practice.keys = []
        key_resp_practice.rt = []
        _key_resp_practice_allKeys = []
        # keep track of which components have finished
        practice_picComponents = [fixation_practice, pic_practice, key_resp_practice, text_left_4, text_right_4, text_6]
        for thisComponent in practice_picComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_pic" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_practice* updates
            
            # if fixation_practice is starting this frame...
            if fixation_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_practice.frameNStart = frameN  # exact frame index
                fixation_practice.tStart = t  # local t and not account for scr refresh
                fixation_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_practice.started')
                # update status
                fixation_practice.status = STARTED
                fixation_practice.setAutoDraw(True)
            
            # if fixation_practice is active this frame...
            if fixation_practice.status == STARTED:
                # update params
                pass
            
            # if fixation_practice is stopping this frame...
            if fixation_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_practice.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_practice.tStop = t  # not accounting for scr refresh
                    fixation_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_practice.stopped')
                    # update status
                    fixation_practice.status = FINISHED
                    fixation_practice.setAutoDraw(False)
            
            # *pic_practice* updates
            
            # if pic_practice is starting this frame...
            if pic_practice.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                pic_practice.frameNStart = frameN  # exact frame index
                pic_practice.tStart = t  # local t and not account for scr refresh
                pic_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pic_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pic_practice.started')
                # update status
                pic_practice.status = STARTED
                pic_practice.setAutoDraw(True)
            
            # if pic_practice is active this frame...
            if pic_practice.status == STARTED:
                # update params
                pass
            
            # if pic_practice is stopping this frame...
            if pic_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pic_practice.tStartRefresh + task1_time-frameTolerance:
                    # keep track of stop time/frame for later
                    pic_practice.tStop = t  # not accounting for scr refresh
                    pic_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pic_practice.stopped')
                    # update status
                    pic_practice.status = FINISHED
                    pic_practice.setAutoDraw(False)
            
            # *key_resp_practice* updates
            
            # if key_resp_practice is starting this frame...
            if key_resp_practice.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_practice.frameNStart = frameN  # exact frame index
                key_resp_practice.tStart = t  # local t and not account for scr refresh
                key_resp_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('key_resp_practice.started', t)
                # update status
                key_resp_practice.status = STARTED
                # keyboard checking is just starting
                key_resp_practice.clock.reset()  # now t=0
                key_resp_practice.clearEvents(eventType='keyboard')
            if key_resp_practice.status == STARTED:
                theseKeys = key_resp_practice.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_practice_allKeys.extend(theseKeys)
                if len(_key_resp_practice_allKeys):
                    key_resp_practice.keys = _key_resp_practice_allKeys[-1].name  # just the last key pressed
                    key_resp_practice.rt = _key_resp_practice_allKeys[-1].rt
                    key_resp_practice.duration = _key_resp_practice_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_practice.keys == str(correct_key0)) or (key_resp_practice.keys == correct_key0):
                        key_resp_practice.corr = 1
                    else:
                        key_resp_practice.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_left_4* updates
            
            # if text_left_4 is starting this frame...
            if text_left_4.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_left_4.frameNStart = frameN  # exact frame index
                text_left_4.tStart = t  # local t and not account for scr refresh
                text_left_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_left_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_left_4.started')
                # update status
                text_left_4.status = STARTED
                text_left_4.setAutoDraw(True)
            
            # if text_left_4 is active this frame...
            if text_left_4.status == STARTED:
                # update params
                pass
            
            # *text_right_4* updates
            
            # if text_right_4 is starting this frame...
            if text_right_4.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_right_4.frameNStart = frameN  # exact frame index
                text_right_4.tStart = t  # local t and not account for scr refresh
                text_right_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_right_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_right_4.started')
                # update status
                text_right_4.status = STARTED
                text_right_4.setAutoDraw(True)
            
            # if text_right_4 is active this frame...
            if text_right_4.status == STARTED:
                # update params
                pass
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_picComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_pic" ---
        for thisComponent in practice_picComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practice_pic.stopped', globalClock.getTime())
        # check responses
        if key_resp_practice.keys in ['', [], None]:  # No response was made
            key_resp_practice.keys = None
            # was no response the correct answer?!
            if str(correct_key0).lower() == 'none':
               key_resp_practice.corr = 1;  # correct non-response
            else:
               key_resp_practice.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_practive (TrialHandler)
        trials_practive.addData('key_resp_practice.keys',key_resp_practice.keys)
        trials_practive.addData('key_resp_practice.corr', key_resp_practice.corr)
        if key_resp_practice.keys != None:  # we had a response
            trials_practive.addData('key_resp_practice.rt', key_resp_practice.rt)
            trials_practive.addData('key_resp_practice.duration', key_resp_practice.duration)
        # the Routine "practice_pic" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_practive'
    
    
    # --- Prepare to start Routine "practice2task1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice2task1.started', globalClock.getTime())
    space_next_2.keys = []
    space_next_2.rt = []
    _space_next_2_allKeys = []
    # keep track of which components have finished
    practice2task1Components = [text_2, space_next_2]
    for thisComponent in practice2task1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice2task1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # *space_next_2* updates
        waitOnFlip = False
        
        # if space_next_2 is starting this frame...
        if space_next_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            space_next_2.frameNStart = frameN  # exact frame index
            space_next_2.tStart = t  # local t and not account for scr refresh
            space_next_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_next_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_next_2.started')
            # update status
            space_next_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_next_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_next_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_next_2.status == STARTED and not waitOnFlip:
            theseKeys = space_next_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _space_next_2_allKeys.extend(theseKeys)
            if len(_space_next_2_allKeys):
                space_next_2.keys = _space_next_2_allKeys[-1].name  # just the last key pressed
                space_next_2.rt = _space_next_2_allKeys[-1].rt
                space_next_2.duration = _space_next_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2task1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice2task1" ---
    for thisComponent in practice2task1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice2task1.stopped', globalClock.getTime())
    # the Routine "practice2task1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(loop1_filename),
        seed=None, name='trials1')
    thisExp.addLoop(trials1)  # add the loop to the experiment
    thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            globals()[paramName] = thisTrials1[paramName]
    
    for thisTrials1 in trials1:
        currentLoop = trials1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
        if thisTrials1 != None:
            for paramName in thisTrials1:
                globals()[paramName] = thisTrials1[paramName]
        
        # --- Prepare to start Routine "task1_with_P" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('task1_with_P.started', globalClock.getTime())
        fixation.setText('+')
        task1_withP.setImage(Pic1)
        key_resp_task1.keys = []
        key_resp_task1.rt = []
        _key_resp_task1_allKeys = []
        # keep track of which components have finished
        task1_with_PComponents = [fixation, task1_withP, key_resp_task1, text_left_2, text_right_2, text_7]
        for thisComponent in task1_with_PComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task1_with_P" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *task1_withP* updates
            
            # if task1_withP is starting this frame...
            if task1_withP.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                task1_withP.frameNStart = frameN  # exact frame index
                task1_withP.tStart = t  # local t and not account for scr refresh
                task1_withP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task1_withP, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task1_withP.started')
                # update status
                task1_withP.status = STARTED
                task1_withP.setAutoDraw(True)
            
            # if task1_withP is active this frame...
            if task1_withP.status == STARTED:
                # update params
                pass
            
            # if task1_withP is stopping this frame...
            if task1_withP.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task1_withP.tStartRefresh + task1_time-frameTolerance:
                    # keep track of stop time/frame for later
                    task1_withP.tStop = t  # not accounting for scr refresh
                    task1_withP.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task1_withP.stopped')
                    # update status
                    task1_withP.status = FINISHED
                    task1_withP.setAutoDraw(False)
            
            # *key_resp_task1* updates
            
            # if key_resp_task1 is starting this frame...
            if key_resp_task1.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_task1.frameNStart = frameN  # exact frame index
                key_resp_task1.tStart = t  # local t and not account for scr refresh
                key_resp_task1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_task1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('key_resp_task1.started', t)
                # update status
                key_resp_task1.status = STARTED
                # keyboard checking is just starting
                key_resp_task1.clock.reset()  # now t=0
                key_resp_task1.clearEvents(eventType='keyboard')
            if key_resp_task1.status == STARTED:
                theseKeys = key_resp_task1.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_task1_allKeys.extend(theseKeys)
                if len(_key_resp_task1_allKeys):
                    key_resp_task1.keys = _key_resp_task1_allKeys[-1].name  # just the last key pressed
                    key_resp_task1.rt = _key_resp_task1_allKeys[-1].rt
                    key_resp_task1.duration = _key_resp_task1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_task1.keys == str(correct_key1)) or (key_resp_task1.keys == correct_key1):
                        key_resp_task1.corr = 1
                    else:
                        key_resp_task1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_left_2* updates
            
            # if text_left_2 is starting this frame...
            if text_left_2.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_left_2.frameNStart = frameN  # exact frame index
                text_left_2.tStart = t  # local t and not account for scr refresh
                text_left_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_left_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_left_2.started')
                # update status
                text_left_2.status = STARTED
                text_left_2.setAutoDraw(True)
            
            # if text_left_2 is active this frame...
            if text_left_2.status == STARTED:
                # update params
                pass
            
            # *text_right_2* updates
            
            # if text_right_2 is starting this frame...
            if text_right_2.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_right_2.frameNStart = frameN  # exact frame index
                text_right_2.tStart = t  # local t and not account for scr refresh
                text_right_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_right_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_right_2.started')
                # update status
                text_right_2.status = STARTED
                text_right_2.setAutoDraw(True)
            
            # if text_right_2 is active this frame...
            if text_right_2.status == STARTED:
                # update params
                pass
            
            # *text_7* updates
            
            # if text_7 is starting this frame...
            if text_7.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.started')
                # update status
                text_7.status = STARTED
                text_7.setAutoDraw(True)
            
            # if text_7 is active this frame...
            if text_7.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task1_with_PComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task1_with_P" ---
        for thisComponent in task1_with_PComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('task1_with_P.stopped', globalClock.getTime())
        # check responses
        if key_resp_task1.keys in ['', [], None]:  # No response was made
            key_resp_task1.keys = None
            # was no response the correct answer?!
            if str(correct_key1).lower() == 'none':
               key_resp_task1.corr = 1;  # correct non-response
            else:
               key_resp_task1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials1 (TrialHandler)
        trials1.addData('key_resp_task1.keys',key_resp_task1.keys)
        trials1.addData('key_resp_task1.corr', key_resp_task1.corr)
        if key_resp_task1.keys != None:  # we had a response
            trials1.addData('key_resp_task1.rt', key_resp_task1.rt)
            trials1.addData('key_resp_task1.duration', key_resp_task1.duration)
        # the Routine "task1_with_P" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge_task1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judge_task1.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_judge_task1
        a.append(key_resp_task1.corr)     #变量a是个列表，.append()函数把括号内key_resp.corr的值添加到a中
        b = sum(a[0:])  #建立变量b,使用sum()函数计算列表a中从0开始到结尾（包含结尾最后一个值）的总和
        task1_score = b
        # keep track of which components have finished
        judge_task1Components = []
        for thisComponent in judge_task1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judge_task1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judge_task1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judge_task1" ---
        for thisComponent in judge_task1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judge_task1.stopped', globalClock.getTime())
        # the Routine "judge_task1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials1'
    
    
    # --- Prepare to start Routine "task1_to_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('task1_to_2.started', globalClock.getTime())
    space_next.keys = []
    space_next.rt = []
    _space_next_allKeys = []
    # Run 'Begin Routine' code from code_7
    a = []
    # keep track of which components have finished
    task1_to_2Components = [text, space_next]
    for thisComponent in task1_to_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task1_to_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *space_next* updates
        waitOnFlip = False
        
        # if space_next is starting this frame...
        if space_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            space_next.frameNStart = frameN  # exact frame index
            space_next.tStart = t  # local t and not account for scr refresh
            space_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_next.started')
            # update status
            space_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_next.status == STARTED and not waitOnFlip:
            theseKeys = space_next.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _space_next_allKeys.extend(theseKeys)
            if len(_space_next_allKeys):
                space_next.keys = _space_next_allKeys[-1].name  # just the last key pressed
                space_next.rt = _space_next_allKeys[-1].rt
                space_next.duration = _space_next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task1_to_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task1_to_2" ---
    for thisComponent in task1_to_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('task1_to_2.stopped', globalClock.getTime())
    # the Routine "task1_to_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(loop2_filename),
        seed=None, name='trials2')
    thisExp.addLoop(trials2)  # add the loop to the experiment
    thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            globals()[paramName] = thisTrials2[paramName]
    
    for thisTrials2 in trials2:
        currentLoop = trials2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
        if thisTrials2 != None:
            for paramName in thisTrials2:
                globals()[paramName] = thisTrials2[paramName]
        
        # --- Prepare to start Routine "task2_without_P" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('task2_without_P.started', globalClock.getTime())
        task2_noP.setImage(Pic2)
        key_resp_task2.keys = []
        key_resp_task2.rt = []
        _key_resp_task2_allKeys = []
        # keep track of which components have finished
        task2_without_PComponents = [fixation2, task2_noP, key_resp_task2, text_left_5, text_right_5, text_8]
        for thisComponent in task2_without_PComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task2_without_P" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation2* updates
            
            # if fixation2 is starting this frame...
            if fixation2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation2.frameNStart = frameN  # exact frame index
                fixation2.tStart = t  # local t and not account for scr refresh
                fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.started')
                # update status
                fixation2.status = STARTED
                fixation2.setAutoDraw(True)
            
            # if fixation2 is active this frame...
            if fixation2.status == STARTED:
                # update params
                pass
            
            # if fixation2 is stopping this frame...
            if fixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation2.tStop = t  # not accounting for scr refresh
                    fixation2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation2.stopped')
                    # update status
                    fixation2.status = FINISHED
                    fixation2.setAutoDraw(False)
            
            # *task2_noP* updates
            
            # if task2_noP is starting this frame...
            if task2_noP.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                task2_noP.frameNStart = frameN  # exact frame index
                task2_noP.tStart = t  # local t and not account for scr refresh
                task2_noP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task2_noP, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task2_noP.started')
                # update status
                task2_noP.status = STARTED
                task2_noP.setAutoDraw(True)
            
            # if task2_noP is active this frame...
            if task2_noP.status == STARTED:
                # update params
                pass
            
            # if task2_noP is stopping this frame...
            if task2_noP.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task2_noP.tStartRefresh + task2_time-frameTolerance:
                    # keep track of stop time/frame for later
                    task2_noP.tStop = t  # not accounting for scr refresh
                    task2_noP.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task2_noP.stopped')
                    # update status
                    task2_noP.status = FINISHED
                    task2_noP.setAutoDraw(False)
            
            # *key_resp_task2* updates
            
            # if key_resp_task2 is starting this frame...
            if key_resp_task2.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_task2.frameNStart = frameN  # exact frame index
                key_resp_task2.tStart = t  # local t and not account for scr refresh
                key_resp_task2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_task2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('key_resp_task2.started', t)
                # update status
                key_resp_task2.status = STARTED
                # keyboard checking is just starting
                key_resp_task2.clock.reset()  # now t=0
                key_resp_task2.clearEvents(eventType='keyboard')
            if key_resp_task2.status == STARTED:
                theseKeys = key_resp_task2.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_task2_allKeys.extend(theseKeys)
                if len(_key_resp_task2_allKeys):
                    key_resp_task2.keys = _key_resp_task2_allKeys[-1].name  # just the last key pressed
                    key_resp_task2.rt = _key_resp_task2_allKeys[-1].rt
                    key_resp_task2.duration = _key_resp_task2_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_task2.keys == str(correct_key1)) or (key_resp_task2.keys == correct_key1):
                        key_resp_task2.corr = 1
                    else:
                        key_resp_task2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_left_5* updates
            
            # if text_left_5 is starting this frame...
            if text_left_5.status == NOT_STARTED and tThisFlip >= task2_time-frameTolerance:
                # keep track of start time/frame for later
                text_left_5.frameNStart = frameN  # exact frame index
                text_left_5.tStart = t  # local t and not account for scr refresh
                text_left_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_left_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_left_5.started')
                # update status
                text_left_5.status = STARTED
                text_left_5.setAutoDraw(True)
            
            # if text_left_5 is active this frame...
            if text_left_5.status == STARTED:
                # update params
                pass
            
            # *text_right_5* updates
            
            # if text_right_5 is starting this frame...
            if text_right_5.status == NOT_STARTED and tThisFlip >= task2_time-frameTolerance:
                # keep track of start time/frame for later
                text_right_5.frameNStart = frameN  # exact frame index
                text_right_5.tStart = t  # local t and not account for scr refresh
                text_right_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_right_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_right_5.started')
                # update status
                text_right_5.status = STARTED
                text_right_5.setAutoDraw(True)
            
            # if text_right_5 is active this frame...
            if text_right_5.status == STARTED:
                # update params
                pass
            
            # *text_8* updates
            
            # if text_8 is starting this frame...
            if text_8.status == NOT_STARTED and tThisFlip >= task2_time-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.started')
                # update status
                text_8.status = STARTED
                text_8.setAutoDraw(True)
            
            # if text_8 is active this frame...
            if text_8.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task2_without_PComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task2_without_P" ---
        for thisComponent in task2_without_PComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('task2_without_P.stopped', globalClock.getTime())
        # check responses
        if key_resp_task2.keys in ['', [], None]:  # No response was made
            key_resp_task2.keys = None
            # was no response the correct answer?!
            if str(correct_key1).lower() == 'none':
               key_resp_task2.corr = 1;  # correct non-response
            else:
               key_resp_task2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials2 (TrialHandler)
        trials2.addData('key_resp_task2.keys',key_resp_task2.keys)
        trials2.addData('key_resp_task2.corr', key_resp_task2.corr)
        if key_resp_task2.keys != None:  # we had a response
            trials2.addData('key_resp_task2.rt', key_resp_task2.rt)
            trials2.addData('key_resp_task2.duration', key_resp_task2.duration)
        # the Routine "task2_without_P" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge_task2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judge_task2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_judge_task2
        a2.append(key_resp_task2.corr)     #变量a是个列表，.append()函数把括号内key_resp.corr的值添加到a中
        b = sum(a2[0:])  #建立变量b,使用sum()函数计算列表a中从0开始到结尾（包含结尾最后一个值）的总和
        task2_score = b
        # keep track of which components have finished
        judge_task2Components = []
        for thisComponent in judge_task2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judge_task2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judge_task2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judge_task2" ---
        for thisComponent in judge_task2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judge_task2.stopped', globalClock.getTime())
        # the Routine "judge_task2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials2'
    
    
    # --- Prepare to start Routine "thanks_gen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks_gen.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_thanks
    txt_thanks = "恭喜你完成了本次实验所有任务！\n 感谢你的参与！\n 在测试1中，您答对了: " + str(task1_score) + "\n在测试2中，您答对了："+str(task2_score) 
    # keep track of which components have finished
    thanks_genComponents = []
    for thisComponent in thanks_genComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks_gen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanks_genComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks_gen" ---
    for thisComponent in thanks_genComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('thanks_gen.stopped', globalClock.getTime())
    # the Routine "thanks_gen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Thanks.started', globalClock.getTime())
    thanks.setText(txt_thanks)
    # keep track of which components have finished
    ThanksComponents = [thanks]
    for thisComponent in ThanksComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Thanks" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thanks* updates
        
        # if thanks is starting this frame...
        if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks.frameNStart = frameN  # exact frame index
            thanks.tStart = t  # local t and not account for scr refresh
            thanks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks.started')
            # update status
            thanks.status = STARTED
            thanks.setAutoDraw(True)
        
        # if thanks is active this frame...
        if thanks.status == STARTED:
            # update params
            pass
        
        # if thanks is stopping this frame...
        if thanks.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thanks.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                thanks.tStop = t  # not accounting for scr refresh
                thanks.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thanks.stopped')
                # update status
                thanks.status = FINISHED
                thanks.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThanksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Thanks" ---
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Thanks.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            eyetracker.setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
