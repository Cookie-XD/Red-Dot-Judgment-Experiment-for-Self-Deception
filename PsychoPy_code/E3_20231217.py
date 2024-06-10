#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.1),
    on 十二月 22, 2023, at 11:36
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
    '你的实验编号': ['1','2','3','4'],
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}

# Run 'Before Experiment' code from code_init
import write_test_excel
# Run 'Before Experiment' code from code_wr



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
    filename = u'data/%s_%s_%s_FB_40loop_ExpTest%s' % (expInfo['participant ID'], expName, expInfo['date'], expInfo['你的实验编号'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\xdan\\Documents\\E3_pilot\\PsychoPy\\E3_20231217.py',
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
            size=[2048, 1152], fullscr=True, screen=0,
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
    exp_idx = expInfo['你的实验编号']
    E1_instro1='Normal blank'
    exp_id = int(exp_idx)
    pic_num = 15
    loop1_filename = 'withPtask1.xlsx'
    task1_time = 2
    dt_prompt1 =  write_test_excel.WriteExcel(pathNamPrefix='withP40/With_prompt_40', excelFileName='./withPtask1.xlsx', colums1_name='Pic1', colums2_name='correct_key1',loopNum=pic_num, total_file_num=150)
    dt_prompt1.write()
    dt_prompt3 =  write_test_excel.WriteExcel(pathNamPrefix='withP40/With_prompt_40', excelFileName='./withPtask3.xlsx', colums1_name='Pic3', colums2_name='correct_key3',loopNum=pic_num, total_file_num=150)
    dt_prompt3.write()
    dt_noprompt1 =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName='./withoutPtask1.xlsx', colums1_name='Pic1', colums2_name='correct_key1',loopNum=pic_num, total_file_num=150)
    dt_noprompt1.write()
    dt_noprompt2 =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName='./withoutPtask2.xlsx', colums1_name='Pic2', colums2_name='correct_key2',loopNum=pic_num, total_file_num=150)
    dt_noprompt2.write()
    dt_noprompt3 =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName='./withoutPtask3.xlsx', colums1_name='Pic3', colums2_name='correct_key3',loopNum=pic_num, total_file_num=150)
    dt_noprompt3.write()
    dt_noprompt4 =  write_test_excel.WriteExcel(pathNamPrefix='withoutP40/No_prompt_40', excelFileName='./withoutPtask4.xlsx', colums1_name='Pic4', colums2_name='correct_key4',loopNum=pic_num, total_file_num=150)
    dt_noprompt4.write()
    # 需要的变量
    is_anser_at1 = 1
    is_feedback = 1
    E1_instro1_filename = './Error.txt'
    example_task1 = './instruction_text/example_noprompt.png'
    example_task2 = './instruction_text/example_noprompt.png'
    example_task3 = './instruction_text/example_noprompt.png'
    example_task4 = './instruction_text/example_noprompt.png'
    task1_corr = 0
    task2_corr = 0
    task3_corr = 0
    task4_corr = 0
    txt_last_thanks=""
    E3_instro1_filename = './instruction_text/Exp_intro.txt'
    T1_predict_filename = "./instruction_text/T1_predict.txt"
    T3_predict_filename = "./instruction_text/T3_predict.txt"
    if exp_id < 3:
        T1_predict_filename = './instruction_text/T1_predict_12.txt'
        loop1_filename = './withPtask1.xlsx' 
        example_task1 = './instruction_text/example_prompt.png'
        loop3_filename = 'withoutPtask3.xlsx'
        example_task3 = './instruction_text/example_noprompt.png'
    elif exp_id < 5:
        T3_predict_filename = './instruction_text/T3_predict_34.txt'
        loop1_filename = 'withoutPtask1.xlsx'
        example_task1 = './instruction_text/example_noprompt.png'
        loop3_filename = './withPtask3.xlsx'   
        example_task3 = './instruction_text/example_prompt.png'
    else:
        E3_instro1_filename = './Error.txt'
    
    loop2_filename = 'withoutPtask2.xlsx'
    loop4_filename = 'withoutPtask4.xlsx'
    
    with open(E3_instro1_filename, 'r',encoding='UTF-8') as file:
        E3_instro1 = file.read()
        
    T1_predict = "看到此文字说明程序错误"
    with open(T1_predict_filename, 'r', encoding='UTF-8') as file:
        T1_predict = file.read()
        
    T2_predict = "看到此文字说明程序错误"
    with open('./instruction_text/T2_predict.txt', 'r', encoding='UTF-8') as file:
        T2_predict = file.read()
        
    T3_predict = "看到此文字说明程序错误"
    with open(T3_predict_filename, 'r', encoding='UTF-8') as file:
        T3_predict = file.read()
        
    T4_predict = "看到此文字说明程序错误"
    with open('./instruction_text/T4_predict.txt', 'r', encoding='UTF-8') as file:
        T4_predict = file.read()
        
    Last_predict = "看到此文字说明程序错误"
    with open('./instruction_text/Last_predict.txt', 'r', encoding='UTF-8') as file:
        Last_predict = file.read()
     
    feedback_type = exp_id % 2
    
    
    # --- Initialize components for Routine "instr1" ---
    instr_start = visual.TextStim(win=win, name='instr_start',
        text=E3_instro1,
        font='Open Sans',
        pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instr_start_key = keyboard.Keyboard()
    image_eg_intro = visual.ImageStim(
        win=win,
        name='image_eg_intro', 
        image=example_task2, mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "practice_pic" ---
    fixation_2 = visual.TextStim(win=win, name='fixation_2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    taskpractice = visual.ImageStim(
        win=win,
        name='taskpractice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.8),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_practice = keyboard.Keyboard()
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
    text_answer_prompt_5 = visual.TextStim(win=win, name='text_answer_prompt_5',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "predict_task1" ---
    image_eg_predict_task1 = visual.ImageStim(
        win=win,
        name='image_eg_predict_task1', 
        image=example_task1, mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    txt_predict_task1 = visual.TextStim(win=win, name='txt_predict_task1',
        text='你的预测值：\n（两位数）',
        font='Open Sans',
        pos=(-0.1, -0.06), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_predict_task1 = keyboard.Keyboard()
    txt_question_predict_task1 = visual.TextStim(win=win, name='txt_question_predict_task1',
        text=T1_predict
    ,
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    txt_disp_input_predict_task1 = visual.TextStim(win=win, name='txt_disp_input_predict_task1',
        text='',
        font='Open Sans',
        pos=(0.1, -0.03), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_taskID1 = visual.TextStim(win=win, name='text_taskID1',
        text='测试1（共4个）',
        font='Open Sans',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "task1" ---
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
    key_resp1 = keyboard.Keyboard()
    text_left = visual.TextStim(win=win, name='text_left',
        text='左\n(S键)',
        font='Open Sans',
        pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_right = visual.TextStim(win=win, name='text_right',
        text='右\n(K键)',
        font='Open Sans',
        pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_answer_prompt = visual.TextStim(win=win, name='text_answer_prompt',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "judge_task1" ---
    # Run 'Begin Experiment' code from code_judje_task1
    feedback = "" #建立名为feedback的变量，等号的左右两边均有空格(接下)
                  #（接上）等号右边为英文引号(内无空格)，会有文字赋值到该变量
    a = []  #建立名为a的变量，变量类型为列表，等号右边为中括号（内无空格）
    
    # --- Initialize components for Routine "fb_string_gen" ---
    
    # --- Initialize components for Routine "fb_current" ---
    txt_fb = visual.TextStim(win=win, name='txt_fb',
        text='',
        font='Open Sans',
        pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_next = keyboard.Keyboard()
    txt_fb2 = visual.TextStim(win=win, name='txt_fb2',
        text='',
        font='Open Sans',
        pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "predict_task2" ---
    image_eg_predict_task2 = visual.ImageStim(
        win=win,
        name='image_eg_predict_task2', 
        image=example_task2, mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    txt_predict_task2 = visual.TextStim(win=win, name='txt_predict_task2',
        text='你的预测值：\n（两位数）',
        font='Open Sans',
        pos=(-0.1, -0.06), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_predict_task2 = keyboard.Keyboard()
    txt_question_predict_task2 = visual.TextStim(win=win, name='txt_question_predict_task2',
        text=T2_predict,
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    txt_disp_input_predict_task2 = visual.TextStim(win=win, name='txt_disp_input_predict_task2',
        text='',
        font='Open Sans',
        pos=(0.1, -0.03), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_taskID2 = visual.TextStim(win=win, name='text_taskID2',
        text='测试2（共4个）',
        font='Open Sans',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "task2" ---
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
    key_resp2 = keyboard.Keyboard()
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
    text_answer_prompt_2 = visual.TextStim(win=win, name='text_answer_prompt_2',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "judge_task2" ---
    # Run 'Begin Experiment' code from code_judje_task2
    feedback = "" #建立名为feedback的变量，等号的左右两边均有空格(接下)
                  #（接上）等号右边为英文引号(内无空格)，会有文字赋值到该变量
    a = []  #建立名为a的变量，变量类型为列表，等号右边为中括号（内无空格）
    
    
    # --- Initialize components for Routine "fb_string_gen" ---
    
    # --- Initialize components for Routine "fb_current" ---
    txt_fb = visual.TextStim(win=win, name='txt_fb',
        text='',
        font='Open Sans',
        pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_next = keyboard.Keyboard()
    txt_fb2 = visual.TextStim(win=win, name='txt_fb2',
        text='',
        font='Open Sans',
        pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "predict_task3" ---
    image_eg_predict_task3 = visual.ImageStim(
        win=win,
        name='image_eg_predict_task3', 
        image=example_task3, mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    txt_predict_task3 = visual.TextStim(win=win, name='txt_predict_task3',
        text='你的预测值：\n（两位数）',
        font='Open Sans',
        pos=(-0.1, -0.06), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_predict_task3 = keyboard.Keyboard()
    txt_question_predict_task3 = visual.TextStim(win=win, name='txt_question_predict_task3',
        text=T3_predict,
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    txt_disp_input_predict_task3 = visual.TextStim(win=win, name='txt_disp_input_predict_task3',
        text='',
        font='Open Sans',
        pos=(0.1, -0.03), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_taskID3 = visual.TextStim(win=win, name='text_taskID3',
        text='测试3（共4个）',
        font='Open Sans',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "task3" ---
    fixation3 = visual.TextStim(win=win, name='fixation3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    task3_pic = visual.ImageStim(
        win=win,
        name='task3_pic', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.8),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp3 = keyboard.Keyboard()
    text_left_3 = visual.TextStim(win=win, name='text_left_3',
        text='左\n(S键)',
        font='Open Sans',
        pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_right_3 = visual.TextStim(win=win, name='text_right_3',
        text='右\n(K键)',
        font='Open Sans',
        pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_answer_prompt_3 = visual.TextStim(win=win, name='text_answer_prompt_3',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "judge_task3" ---
    # Run 'Begin Experiment' code from code_judje_task3
    feedback = "" #建立名为feedback的变量，等号的左右两边均有空格(接下)
                  #（接上）等号右边为英文引号(内无空格)，会有文字赋值到该变量
    a = []  #建立名为a的变量，变量类型为列表，等号右边为中括号（内无空格）
    
    
    # --- Initialize components for Routine "fb_string_gen" ---
    
    # --- Initialize components for Routine "fb_current" ---
    txt_fb = visual.TextStim(win=win, name='txt_fb',
        text='',
        font='Open Sans',
        pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_next = keyboard.Keyboard()
    txt_fb2 = visual.TextStim(win=win, name='txt_fb2',
        text='',
        font='Open Sans',
        pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "predict_task4" ---
    image_eg_predict_task4 = visual.ImageStim(
        win=win,
        name='image_eg_predict_task4', 
        image=example_task4, mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    txt_predict_task4 = visual.TextStim(win=win, name='txt_predict_task4',
        text='你的预测值：\n（两位数）',
        font='Open Sans',
        pos=(-0.1, -0.06), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_predict_task4 = keyboard.Keyboard()
    txt_question_predict_task4 = visual.TextStim(win=win, name='txt_question_predict_task4',
        text=T4_predict,
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    txt_disp_input_predict_task4 = visual.TextStim(win=win, name='txt_disp_input_predict_task4',
        text='',
        font='Open Sans',
        pos=(0.1, -0.03), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_taskID4 = visual.TextStim(win=win, name='text_taskID4',
        text='测试4（共4个）',
        font='Open Sans',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "task4" ---
    fixation4 = visual.TextStim(win=win, name='fixation4',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    task34_pic = visual.ImageStim(
        win=win,
        name='task34_pic', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.8),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp4 = keyboard.Keyboard()
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
    text_answer_prompt_4 = visual.TextStim(win=win, name='text_answer_prompt_4',
        text='请作答',
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "judge_task4" ---
    # Run 'Begin Experiment' code from code_judje_task4
    feedback = "" #建立名为feedback的变量，等号的左右两边均有空格(接下)
                  #（接上）等号右边为英文引号(内无空格)，会有文字赋值到该变量
    a = []  #建立名为a的变量，变量类型为列表，等号右边为中括号（内无空格）
    
    
    # --- Initialize components for Routine "fb_string_gen" ---
    
    # --- Initialize components for Routine "fb_current" ---
    txt_fb = visual.TextStim(win=win, name='txt_fb',
        text='',
        font='Open Sans',
        pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_next = keyboard.Keyboard()
    txt_fb2 = visual.TextStim(win=win, name='txt_fb2',
        text='',
        font='Open Sans',
        pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "last_fb_and_predict" ---
    image_eg_predict_task5 = visual.ImageStim(
        win=win,
        name='image_eg_predict_task5', 
        image=example_task4, mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    txt_predict_task5 = visual.TextStim(win=win, name='txt_predict_task5',
        text='你的预测值：\n（两位数）',
        font='Open Sans',
        pos=(-0.1, -0.06), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_predict_task5 = keyboard.Keyboard()
    txt_question_predict_task5 = visual.TextStim(win=win, name='txt_question_predict_task5',
        text=Last_predict,
        font='Open Sans',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    txt_disp_input_predict_task5 = visual.TextStim(win=win, name='txt_disp_input_predict_task5',
        text='',
        font='Open Sans',
        pos=(0.1, -0.03), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
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
    instr1Components = [instr_start, instr_start_key, image_eg_intro]
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
        
        # *image_eg_intro* updates
        
        # if image_eg_intro is starting this frame...
        if image_eg_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg_intro.frameNStart = frameN  # exact frame index
            image_eg_intro.tStart = t  # local t and not account for scr refresh
            image_eg_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg_intro.started')
            # update status
            image_eg_intro.status = STARTED
            image_eg_intro.setAutoDraw(True)
        
        # if image_eg_intro is active this frame...
        if image_eg_intro.status == STARTED:
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
    trials_practice = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice.xlsx'),
        seed=None, name='trials_practice')
    thisExp.addLoop(trials_practice)  # add the loop to the experiment
    thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            globals()[paramName] = thisTrials_practice[paramName]
    
    for thisTrials_practice in trials_practice:
        currentLoop = trials_practice
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
        if thisTrials_practice != None:
            for paramName in thisTrials_practice:
                globals()[paramName] = thisTrials_practice[paramName]
        
        # --- Prepare to start Routine "practice_pic" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice_pic.started', globalClock.getTime())
        fixation_2.setText('+')
        taskpractice.setImage(Pic0)
        key_resp_practice.keys = []
        key_resp_practice.rt = []
        _key_resp_practice_allKeys = []
        # keep track of which components have finished
        practice_picComponents = [fixation_2, taskpractice, key_resp_practice, text_left_5, text_right_5, text_answer_prompt_5]
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
            
            # *fixation_2* updates
            
            # if fixation_2 is starting this frame...
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.started')
                # update status
                fixation_2.status = STARTED
                fixation_2.setAutoDraw(True)
            
            # if fixation_2 is active this frame...
            if fixation_2.status == STARTED:
                # update params
                pass
            
            # if fixation_2 is stopping this frame...
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                    # update status
                    fixation_2.status = FINISHED
                    fixation_2.setAutoDraw(False)
            
            # *taskpractice* updates
            
            # if taskpractice is starting this frame...
            if taskpractice.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                taskpractice.frameNStart = frameN  # exact frame index
                taskpractice.tStart = t  # local t and not account for scr refresh
                taskpractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taskpractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'taskpractice.started')
                # update status
                taskpractice.status = STARTED
                taskpractice.setAutoDraw(True)
            
            # if taskpractice is active this frame...
            if taskpractice.status == STARTED:
                # update params
                pass
            
            # if taskpractice is stopping this frame...
            if taskpractice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taskpractice.tStartRefresh + task1_time-frameTolerance:
                    # keep track of stop time/frame for later
                    taskpractice.tStop = t  # not accounting for scr refresh
                    taskpractice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taskpractice.stopped')
                    # update status
                    taskpractice.status = FINISHED
                    taskpractice.setAutoDraw(False)
            
            # *key_resp_practice* updates
            
            # if key_resp_practice is starting this frame...
            if key_resp_practice.status == NOT_STARTED and t >= 0.4-frameTolerance:
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
            
            # *text_left_5* updates
            
            # if text_left_5 is starting this frame...
            if text_left_5.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
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
            if text_right_5.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
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
            
            # *text_answer_prompt_5* updates
            
            # if text_answer_prompt_5 is starting this frame...
            if text_answer_prompt_5.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_answer_prompt_5.frameNStart = frameN  # exact frame index
                text_answer_prompt_5.tStart = t  # local t and not account for scr refresh
                text_answer_prompt_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_prompt_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_prompt_5.started')
                # update status
                text_answer_prompt_5.status = STARTED
                text_answer_prompt_5.setAutoDraw(True)
            
            # if text_answer_prompt_5 is active this frame...
            if text_answer_prompt_5.status == STARTED:
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
        # store data for trials_practice (TrialHandler)
        trials_practice.addData('key_resp_practice.keys',key_resp_practice.keys)
        trials_practice.addData('key_resp_practice.corr', key_resp_practice.corr)
        if key_resp_practice.keys != None:  # we had a response
            trials_practice.addData('key_resp_practice.rt', key_resp_practice.rt)
            trials_practice.addData('key_resp_practice.duration', key_resp_practice.duration)
        # the Routine "practice_pic" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_practice'
    
    
    # --- Prepare to start Routine "predict_task1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('predict_task1.started', globalClock.getTime())
    key_predict_task1.keys = []
    key_predict_task1.rt = []
    _key_predict_task1_allKeys = []
    # Run 'Begin Routine' code from code_input_predict_task1
    respDisplay_task1 = ""
    maxDigits = 6
    
    #key logger defaults
    last_len = 0
    key_list = []
    fb_string = "您已完成测试1"
    a = []
    
    # keep track of which components have finished
    predict_task1Components = [image_eg_predict_task1, txt_predict_task1, key_predict_task1, txt_question_predict_task1, txt_disp_input_predict_task1, text_taskID1]
    for thisComponent in predict_task1Components:
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
    
    # --- Run Routine "predict_task1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_eg_predict_task1* updates
        
        # if image_eg_predict_task1 is starting this frame...
        if image_eg_predict_task1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg_predict_task1.frameNStart = frameN  # exact frame index
            image_eg_predict_task1.tStart = t  # local t and not account for scr refresh
            image_eg_predict_task1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg_predict_task1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg_predict_task1.started')
            # update status
            image_eg_predict_task1.status = STARTED
            image_eg_predict_task1.setAutoDraw(True)
        
        # if image_eg_predict_task1 is active this frame...
        if image_eg_predict_task1.status == STARTED:
            # update params
            pass
        
        # *txt_predict_task1* updates
        
        # if txt_predict_task1 is starting this frame...
        if txt_predict_task1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_predict_task1.frameNStart = frameN  # exact frame index
            txt_predict_task1.tStart = t  # local t and not account for scr refresh
            txt_predict_task1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_predict_task1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_predict_task1.started')
            # update status
            txt_predict_task1.status = STARTED
            txt_predict_task1.setAutoDraw(True)
        
        # if txt_predict_task1 is active this frame...
        if txt_predict_task1.status == STARTED:
            # update params
            pass
        
        # *key_predict_task1* updates
        waitOnFlip = False
        
        # if key_predict_task1 is starting this frame...
        if key_predict_task1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_predict_task1.frameNStart = frameN  # exact frame index
            key_predict_task1.tStart = t  # local t and not account for scr refresh
            key_predict_task1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_predict_task1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_predict_task1.started')
            # update status
            key_predict_task1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_predict_task1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_predict_task1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_predict_task1.status == STARTED and not waitOnFlip:
            theseKeys = key_predict_task1.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return','backspace'], ignoreKeys=["escape"], waitRelease=False)
            _key_predict_task1_allKeys.extend(theseKeys)
            if len(_key_predict_task1_allKeys):
                key_predict_task1.keys = [key.name for key in _key_predict_task1_allKeys]  # storing all keys
                key_predict_task1.rt = [key.rt for key in _key_predict_task1_allKeys]
                key_predict_task1.duration = [key.duration for key in _key_predict_task1_allKeys]
        
        # *txt_question_predict_task1* updates
        
        # if txt_question_predict_task1 is starting this frame...
        if txt_question_predict_task1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_question_predict_task1.frameNStart = frameN  # exact frame index
            txt_question_predict_task1.tStart = t  # local t and not account for scr refresh
            txt_question_predict_task1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_question_predict_task1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_question_predict_task1.started')
            # update status
            txt_question_predict_task1.status = STARTED
            txt_question_predict_task1.setAutoDraw(True)
        
        # if txt_question_predict_task1 is active this frame...
        if txt_question_predict_task1.status == STARTED:
            # update params
            pass
        
        # *txt_disp_input_predict_task1* updates
        
        # if txt_disp_input_predict_task1 is starting this frame...
        if txt_disp_input_predict_task1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_disp_input_predict_task1.frameNStart = frameN  # exact frame index
            txt_disp_input_predict_task1.tStart = t  # local t and not account for scr refresh
            txt_disp_input_predict_task1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_disp_input_predict_task1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_disp_input_predict_task1.started')
            # update status
            txt_disp_input_predict_task1.status = STARTED
            txt_disp_input_predict_task1.setAutoDraw(True)
        
        # if txt_disp_input_predict_task1 is active this frame...
        if txt_disp_input_predict_task1.status == STARTED:
            # update params
            txt_disp_input_predict_task1.setText(respDisplay_task1
            , log=False)
        # Run 'Each Frame' code from code_input_predict_task1
        #if a new key has been pressed since last time
        if(len(key_predict_task1.keys) > last_len):
            
            #increment the key logger length
            last_len = len(key_predict_task1.keys)
            
            #grab the last key added to the keys list
            key_list.append(key_predict_task1.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
        
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 2):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            respDisplay_task1 = ''.join(key_list)
        
        # *text_taskID1* updates
        
        # if text_taskID1 is starting this frame...
        if text_taskID1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_taskID1.frameNStart = frameN  # exact frame index
            text_taskID1.tStart = t  # local t and not account for scr refresh
            text_taskID1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_taskID1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_taskID1.started')
            # update status
            text_taskID1.status = STARTED
            text_taskID1.setAutoDraw(True)
        
        # if text_taskID1 is active this frame...
        if text_taskID1.status == STARTED:
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
        for thisComponent in predict_task1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "predict_task1" ---
    for thisComponent in predict_task1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('predict_task1.stopped', globalClock.getTime())
    # check responses
    if key_predict_task1.keys in ['', [], None]:  # No response was made
        key_predict_task1.keys = None
    thisExp.addData('key_predict_task1.keys',key_predict_task1.keys)
    if key_predict_task1.keys != None:  # we had a response
        thisExp.addData('key_predict_task1.rt', key_predict_task1.rt)
        thisExp.addData('key_predict_task1.duration', key_predict_task1.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_input_predict_task1
    thisExp.addData('subjResponse', respDisplay_task1)
    # the Routine "predict_task1" was not non-slip safe, so reset the non-slip timer
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
        
        # --- Prepare to start Routine "task1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('task1.started', globalClock.getTime())
        fixation.setText('+')
        task1_withP.setImage(Pic1)
        key_resp1.keys = []
        key_resp1.rt = []
        _key_resp1_allKeys = []
        # keep track of which components have finished
        task1Components = [fixation, task1_withP, key_resp1, text_left, text_right, text_answer_prompt]
        for thisComponent in task1Components:
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
        
        # --- Run Routine "task1" ---
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
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
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
            
            # *key_resp1* updates
            
            # if key_resp1 is starting this frame...
            if key_resp1.status == NOT_STARTED and t >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_resp1.frameNStart = frameN  # exact frame index
                key_resp1.tStart = t  # local t and not account for scr refresh
                key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('key_resp1.started', t)
                # update status
                key_resp1.status = STARTED
                # keyboard checking is just starting
                key_resp1.clock.reset()  # now t=0
                key_resp1.clearEvents(eventType='keyboard')
            if key_resp1.status == STARTED:
                theseKeys = key_resp1.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp1_allKeys.extend(theseKeys)
                if len(_key_resp1_allKeys):
                    key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                    key_resp1.rt = _key_resp1_allKeys[-1].rt
                    key_resp1.duration = _key_resp1_allKeys[-1].duration
                    # was this correct?
                    if (key_resp1.keys == str(correct_key1)) or (key_resp1.keys == correct_key1):
                        key_resp1.corr = 1
                    else:
                        key_resp1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_left* updates
            
            # if text_left is starting this frame...
            if text_left.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_left.frameNStart = frameN  # exact frame index
                text_left.tStart = t  # local t and not account for scr refresh
                text_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_left.started')
                # update status
                text_left.status = STARTED
                text_left.setAutoDraw(True)
            
            # if text_left is active this frame...
            if text_left.status == STARTED:
                # update params
                pass
            
            # *text_right* updates
            
            # if text_right is starting this frame...
            if text_right.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_right.frameNStart = frameN  # exact frame index
                text_right.tStart = t  # local t and not account for scr refresh
                text_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_right.started')
                # update status
                text_right.status = STARTED
                text_right.setAutoDraw(True)
            
            # if text_right is active this frame...
            if text_right.status == STARTED:
                # update params
                pass
            
            # *text_answer_prompt* updates
            
            # if text_answer_prompt is starting this frame...
            if text_answer_prompt.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_answer_prompt.frameNStart = frameN  # exact frame index
                text_answer_prompt.tStart = t  # local t and not account for scr refresh
                text_answer_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_prompt.started')
                # update status
                text_answer_prompt.status = STARTED
                text_answer_prompt.setAutoDraw(True)
            
            # if text_answer_prompt is active this frame...
            if text_answer_prompt.status == STARTED:
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
            for thisComponent in task1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task1" ---
        for thisComponent in task1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('task1.stopped', globalClock.getTime())
        # check responses
        if key_resp1.keys in ['', [], None]:  # No response was made
            key_resp1.keys = None
            # was no response the correct answer?!
            if str(correct_key1).lower() == 'none':
               key_resp1.corr = 1;  # correct non-response
            else:
               key_resp1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials1 (TrialHandler)
        trials1.addData('key_resp1.keys',key_resp1.keys)
        trials1.addData('key_resp1.corr', key_resp1.corr)
        if key_resp1.keys != None:  # we had a response
            trials1.addData('key_resp1.rt', key_resp1.rt)
            trials1.addData('key_resp1.duration', key_resp1.duration)
        # the Routine "task1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge_task1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judge_task1.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_judje_task1
        a.append(key_resp1.corr)     #变量a是个列表，.append()函数把括号内key_resp.corr的值添加到a中
        b = sum(a[0:])  #建立变量b,使用sum()函数计算列表a中从0开始到结尾（包含结尾最后一个值）的总和
        task1_corr = b
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
    
    
    # --- Prepare to start Routine "fb_string_gen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_string_gen.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_fb_string
    if feedback_type == 1:
        fb_string = "刚刚的测试中测试你判断正确了" + str(b) + "个图片 \n (共30个图片)"
        pmt_loc = (0, 0.15)
        
    # keep track of which components have finished
    fb_string_genComponents = []
    for thisComponent in fb_string_genComponents:
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
    
    # --- Run Routine "fb_string_gen" ---
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
        for thisComponent in fb_string_genComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_string_gen" ---
    for thisComponent in fb_string_genComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_string_gen.stopped', globalClock.getTime())
    # the Routine "fb_string_gen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fb_current" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_current.started', globalClock.getTime())
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # keep track of which components have finished
    fb_currentComponents = [txt_fb, key_next, txt_fb2]
    for thisComponent in fb_currentComponents:
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
    
    # --- Run Routine "fb_current" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_fb* updates
        
        # if txt_fb is starting this frame...
        if txt_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb.frameNStart = frameN  # exact frame index
            txt_fb.tStart = t  # local t and not account for scr refresh
            txt_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb.started')
            # update status
            txt_fb.status = STARTED
            txt_fb.setAutoDraw(True)
        
        # if txt_fb is active this frame...
        if txt_fb.status == STARTED:
            # update params
            txt_fb.setText(fb_string, log=False)
        
        # *key_next* updates
        waitOnFlip = False
        
        # if key_next is starting this frame...
        if key_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            # update status
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                key_next.duration = _key_next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *txt_fb2* updates
        
        # if txt_fb2 is starting this frame...
        if txt_fb2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb2.frameNStart = frameN  # exact frame index
            txt_fb2.tStart = t  # local t and not account for scr refresh
            txt_fb2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb2.started')
            # update status
            txt_fb2.status = STARTED
            txt_fb2.setAutoDraw(True)
        
        # if txt_fb2 is active this frame...
        if txt_fb2.status == STARTED:
            # update params
            txt_fb2.setText('请按空格进入下一阶段\n', log=False)
        
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
        for thisComponent in fb_currentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_current" ---
    for thisComponent in fb_currentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_current.stopped', globalClock.getTime())
    # the Routine "fb_current" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "predict_task2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('predict_task2.started', globalClock.getTime())
    key_predict_task2.keys = []
    key_predict_task2.rt = []
    _key_predict_task2_allKeys = []
    # Run 'Begin Routine' code from code_input_predict_task2
    respDisplay_task2 = ""
    maxDigits = 6
    
    #key logger defaults
    last_len = 0
    key_list = []
    fb_string = "您已完成测试2"
    a = []
    
    # keep track of which components have finished
    predict_task2Components = [image_eg_predict_task2, txt_predict_task2, key_predict_task2, txt_question_predict_task2, txt_disp_input_predict_task2, text_taskID2]
    for thisComponent in predict_task2Components:
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
    
    # --- Run Routine "predict_task2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_eg_predict_task2* updates
        
        # if image_eg_predict_task2 is starting this frame...
        if image_eg_predict_task2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg_predict_task2.frameNStart = frameN  # exact frame index
            image_eg_predict_task2.tStart = t  # local t and not account for scr refresh
            image_eg_predict_task2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg_predict_task2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg_predict_task2.started')
            # update status
            image_eg_predict_task2.status = STARTED
            image_eg_predict_task2.setAutoDraw(True)
        
        # if image_eg_predict_task2 is active this frame...
        if image_eg_predict_task2.status == STARTED:
            # update params
            pass
        
        # *txt_predict_task2* updates
        
        # if txt_predict_task2 is starting this frame...
        if txt_predict_task2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_predict_task2.frameNStart = frameN  # exact frame index
            txt_predict_task2.tStart = t  # local t and not account for scr refresh
            txt_predict_task2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_predict_task2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_predict_task2.started')
            # update status
            txt_predict_task2.status = STARTED
            txt_predict_task2.setAutoDraw(True)
        
        # if txt_predict_task2 is active this frame...
        if txt_predict_task2.status == STARTED:
            # update params
            pass
        
        # *key_predict_task2* updates
        waitOnFlip = False
        
        # if key_predict_task2 is starting this frame...
        if key_predict_task2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_predict_task2.frameNStart = frameN  # exact frame index
            key_predict_task2.tStart = t  # local t and not account for scr refresh
            key_predict_task2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_predict_task2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_predict_task2.started')
            # update status
            key_predict_task2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_predict_task2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_predict_task2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_predict_task2.status == STARTED and not waitOnFlip:
            theseKeys = key_predict_task2.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return','backspace'], ignoreKeys=["escape"], waitRelease=False)
            _key_predict_task2_allKeys.extend(theseKeys)
            if len(_key_predict_task2_allKeys):
                key_predict_task2.keys = [key.name for key in _key_predict_task2_allKeys]  # storing all keys
                key_predict_task2.rt = [key.rt for key in _key_predict_task2_allKeys]
                key_predict_task2.duration = [key.duration for key in _key_predict_task2_allKeys]
        
        # *txt_question_predict_task2* updates
        
        # if txt_question_predict_task2 is starting this frame...
        if txt_question_predict_task2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_question_predict_task2.frameNStart = frameN  # exact frame index
            txt_question_predict_task2.tStart = t  # local t and not account for scr refresh
            txt_question_predict_task2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_question_predict_task2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_question_predict_task2.started')
            # update status
            txt_question_predict_task2.status = STARTED
            txt_question_predict_task2.setAutoDraw(True)
        
        # if txt_question_predict_task2 is active this frame...
        if txt_question_predict_task2.status == STARTED:
            # update params
            pass
        
        # *txt_disp_input_predict_task2* updates
        
        # if txt_disp_input_predict_task2 is starting this frame...
        if txt_disp_input_predict_task2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_disp_input_predict_task2.frameNStart = frameN  # exact frame index
            txt_disp_input_predict_task2.tStart = t  # local t and not account for scr refresh
            txt_disp_input_predict_task2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_disp_input_predict_task2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_disp_input_predict_task2.started')
            # update status
            txt_disp_input_predict_task2.status = STARTED
            txt_disp_input_predict_task2.setAutoDraw(True)
        
        # if txt_disp_input_predict_task2 is active this frame...
        if txt_disp_input_predict_task2.status == STARTED:
            # update params
            txt_disp_input_predict_task2.setText(respDisplay_task2
            , log=False)
        # Run 'Each Frame' code from code_input_predict_task2
        #if a new key has been pressed since last time
        if(len(key_predict_task2.keys) > last_len):
            
            #increment the key logger length
            last_len = len(key_predict_task2.keys)
            
            #grab the last key added to the keys list
            key_list.append(key_predict_task2.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
        
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 2):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            respDisplay_task2 = ''.join(key_list)
        
        # *text_taskID2* updates
        
        # if text_taskID2 is starting this frame...
        if text_taskID2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_taskID2.frameNStart = frameN  # exact frame index
            text_taskID2.tStart = t  # local t and not account for scr refresh
            text_taskID2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_taskID2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_taskID2.started')
            # update status
            text_taskID2.status = STARTED
            text_taskID2.setAutoDraw(True)
        
        # if text_taskID2 is active this frame...
        if text_taskID2.status == STARTED:
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
        for thisComponent in predict_task2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "predict_task2" ---
    for thisComponent in predict_task2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('predict_task2.stopped', globalClock.getTime())
    # check responses
    if key_predict_task2.keys in ['', [], None]:  # No response was made
        key_predict_task2.keys = None
    thisExp.addData('key_predict_task2.keys',key_predict_task2.keys)
    if key_predict_task2.keys != None:  # we had a response
        thisExp.addData('key_predict_task2.rt', key_predict_task2.rt)
        thisExp.addData('key_predict_task2.duration', key_predict_task2.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_input_predict_task2
    thisExp.addData('subjResponse', respDisplay_task2)
    # the Routine "predict_task2" was not non-slip safe, so reset the non-slip timer
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
        
        # --- Prepare to start Routine "task2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('task2.started', globalClock.getTime())
        task2_noP.setImage(Pic2)
        key_resp2.keys = []
        key_resp2.rt = []
        _key_resp2_allKeys = []
        # keep track of which components have finished
        task2Components = [fixation2, task2_noP, key_resp2, text_left_2, text_right_2, text_answer_prompt_2]
        for thisComponent in task2Components:
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
        
        # --- Run Routine "task2" ---
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
                if tThisFlipGlobal > fixation2.tStartRefresh + 0.5-frameTolerance:
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
                if tThisFlipGlobal > task2_noP.tStartRefresh + task1_time-frameTolerance:
                    # keep track of stop time/frame for later
                    task2_noP.tStop = t  # not accounting for scr refresh
                    task2_noP.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task2_noP.stopped')
                    # update status
                    task2_noP.status = FINISHED
                    task2_noP.setAutoDraw(False)
            
            # *key_resp2* updates
            waitOnFlip = False
            
            # if key_resp2 is starting this frame...
            if key_resp2.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_resp2.frameNStart = frameN  # exact frame index
                key_resp2.tStart = t  # local t and not account for scr refresh
                key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp2.started')
                # update status
                key_resp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp2.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp2_allKeys.extend(theseKeys)
                if len(_key_resp2_allKeys):
                    key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
                    key_resp2.rt = _key_resp2_allKeys[-1].rt
                    key_resp2.duration = _key_resp2_allKeys[-1].duration
                    # was this correct?
                    if (key_resp2.keys == str(correct_key2)) or (key_resp2.keys == correct_key2):
                        key_resp2.corr = 1
                    else:
                        key_resp2.corr = 0
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
            
            # *text_answer_prompt_2* updates
            
            # if text_answer_prompt_2 is starting this frame...
            if text_answer_prompt_2.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_answer_prompt_2.frameNStart = frameN  # exact frame index
                text_answer_prompt_2.tStart = t  # local t and not account for scr refresh
                text_answer_prompt_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_prompt_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_prompt_2.started')
                # update status
                text_answer_prompt_2.status = STARTED
                text_answer_prompt_2.setAutoDraw(True)
            
            # if text_answer_prompt_2 is active this frame...
            if text_answer_prompt_2.status == STARTED:
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
            for thisComponent in task2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task2" ---
        for thisComponent in task2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('task2.stopped', globalClock.getTime())
        # check responses
        if key_resp2.keys in ['', [], None]:  # No response was made
            key_resp2.keys = None
            # was no response the correct answer?!
            if str(correct_key2).lower() == 'none':
               key_resp2.corr = 1;  # correct non-response
            else:
               key_resp2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials2 (TrialHandler)
        trials2.addData('key_resp2.keys',key_resp2.keys)
        trials2.addData('key_resp2.corr', key_resp2.corr)
        if key_resp2.keys != None:  # we had a response
            trials2.addData('key_resp2.rt', key_resp2.rt)
            trials2.addData('key_resp2.duration', key_resp2.duration)
        # the Routine "task2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge_task2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judge_task2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_judje_task2
        a.append(key_resp2.corr)     #变量a是个列表，.append()函数把括号内key_resp.corr的值添加到a中
        b = sum(a[0:])  #建立变量b,使用sum()函数计算列表a中从0开始到结尾（包含结尾最后一个值）的总和
        task2_corr = b
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
    
    
    # --- Prepare to start Routine "fb_string_gen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_string_gen.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_fb_string
    if feedback_type == 1:
        fb_string = "刚刚的测试中测试你判断正确了" + str(b) + "个图片 \n (共30个图片)"
        pmt_loc = (0, 0.15)
        
    # keep track of which components have finished
    fb_string_genComponents = []
    for thisComponent in fb_string_genComponents:
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
    
    # --- Run Routine "fb_string_gen" ---
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
        for thisComponent in fb_string_genComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_string_gen" ---
    for thisComponent in fb_string_genComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_string_gen.stopped', globalClock.getTime())
    # the Routine "fb_string_gen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fb_current" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_current.started', globalClock.getTime())
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # keep track of which components have finished
    fb_currentComponents = [txt_fb, key_next, txt_fb2]
    for thisComponent in fb_currentComponents:
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
    
    # --- Run Routine "fb_current" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_fb* updates
        
        # if txt_fb is starting this frame...
        if txt_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb.frameNStart = frameN  # exact frame index
            txt_fb.tStart = t  # local t and not account for scr refresh
            txt_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb.started')
            # update status
            txt_fb.status = STARTED
            txt_fb.setAutoDraw(True)
        
        # if txt_fb is active this frame...
        if txt_fb.status == STARTED:
            # update params
            txt_fb.setText(fb_string, log=False)
        
        # *key_next* updates
        waitOnFlip = False
        
        # if key_next is starting this frame...
        if key_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            # update status
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                key_next.duration = _key_next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *txt_fb2* updates
        
        # if txt_fb2 is starting this frame...
        if txt_fb2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb2.frameNStart = frameN  # exact frame index
            txt_fb2.tStart = t  # local t and not account for scr refresh
            txt_fb2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb2.started')
            # update status
            txt_fb2.status = STARTED
            txt_fb2.setAutoDraw(True)
        
        # if txt_fb2 is active this frame...
        if txt_fb2.status == STARTED:
            # update params
            txt_fb2.setText('请按空格进入下一阶段\n', log=False)
        
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
        for thisComponent in fb_currentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_current" ---
    for thisComponent in fb_currentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_current.stopped', globalClock.getTime())
    # the Routine "fb_current" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "predict_task3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('predict_task3.started', globalClock.getTime())
    key_predict_task3.keys = []
    key_predict_task3.rt = []
    _key_predict_task3_allKeys = []
    # Run 'Begin Routine' code from code_input_predict_task3
    respDisplay_task3 = ""
    maxDigits = 6
    
    #key logger defaults
    last_len = 0
    key_list = []
    fb_string = "您已完成测试3"
    a = []
    
    # keep track of which components have finished
    predict_task3Components = [image_eg_predict_task3, txt_predict_task3, key_predict_task3, txt_question_predict_task3, txt_disp_input_predict_task3, text_taskID3]
    for thisComponent in predict_task3Components:
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
    
    # --- Run Routine "predict_task3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_eg_predict_task3* updates
        
        # if image_eg_predict_task3 is starting this frame...
        if image_eg_predict_task3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg_predict_task3.frameNStart = frameN  # exact frame index
            image_eg_predict_task3.tStart = t  # local t and not account for scr refresh
            image_eg_predict_task3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg_predict_task3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg_predict_task3.started')
            # update status
            image_eg_predict_task3.status = STARTED
            image_eg_predict_task3.setAutoDraw(True)
        
        # if image_eg_predict_task3 is active this frame...
        if image_eg_predict_task3.status == STARTED:
            # update params
            pass
        
        # *txt_predict_task3* updates
        
        # if txt_predict_task3 is starting this frame...
        if txt_predict_task3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_predict_task3.frameNStart = frameN  # exact frame index
            txt_predict_task3.tStart = t  # local t and not account for scr refresh
            txt_predict_task3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_predict_task3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_predict_task3.started')
            # update status
            txt_predict_task3.status = STARTED
            txt_predict_task3.setAutoDraw(True)
        
        # if txt_predict_task3 is active this frame...
        if txt_predict_task3.status == STARTED:
            # update params
            pass
        
        # *key_predict_task3* updates
        waitOnFlip = False
        
        # if key_predict_task3 is starting this frame...
        if key_predict_task3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_predict_task3.frameNStart = frameN  # exact frame index
            key_predict_task3.tStart = t  # local t and not account for scr refresh
            key_predict_task3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_predict_task3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_predict_task3.started')
            # update status
            key_predict_task3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_predict_task3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_predict_task3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_predict_task3.status == STARTED and not waitOnFlip:
            theseKeys = key_predict_task3.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return','backspace'], ignoreKeys=["escape"], waitRelease=False)
            _key_predict_task3_allKeys.extend(theseKeys)
            if len(_key_predict_task3_allKeys):
                key_predict_task3.keys = [key.name for key in _key_predict_task3_allKeys]  # storing all keys
                key_predict_task3.rt = [key.rt for key in _key_predict_task3_allKeys]
                key_predict_task3.duration = [key.duration for key in _key_predict_task3_allKeys]
        
        # *txt_question_predict_task3* updates
        
        # if txt_question_predict_task3 is starting this frame...
        if txt_question_predict_task3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_question_predict_task3.frameNStart = frameN  # exact frame index
            txt_question_predict_task3.tStart = t  # local t and not account for scr refresh
            txt_question_predict_task3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_question_predict_task3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_question_predict_task3.started')
            # update status
            txt_question_predict_task3.status = STARTED
            txt_question_predict_task3.setAutoDraw(True)
        
        # if txt_question_predict_task3 is active this frame...
        if txt_question_predict_task3.status == STARTED:
            # update params
            pass
        
        # *txt_disp_input_predict_task3* updates
        
        # if txt_disp_input_predict_task3 is starting this frame...
        if txt_disp_input_predict_task3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_disp_input_predict_task3.frameNStart = frameN  # exact frame index
            txt_disp_input_predict_task3.tStart = t  # local t and not account for scr refresh
            txt_disp_input_predict_task3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_disp_input_predict_task3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_disp_input_predict_task3.started')
            # update status
            txt_disp_input_predict_task3.status = STARTED
            txt_disp_input_predict_task3.setAutoDraw(True)
        
        # if txt_disp_input_predict_task3 is active this frame...
        if txt_disp_input_predict_task3.status == STARTED:
            # update params
            txt_disp_input_predict_task3.setText(respDisplay_task3, log=False)
        # Run 'Each Frame' code from code_input_predict_task3
        #if a new key has been pressed since last time
        if(len(key_predict_task3.keys) > last_len):
            
            #increment the key logger length
            last_len = len(key_predict_task3.keys)
            
            #grab the last key added to the keys list
            key_list.append(key_predict_task3.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
        
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 2):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            respDisplay_task3 = ''.join(key_list)
        
        # *text_taskID3* updates
        
        # if text_taskID3 is starting this frame...
        if text_taskID3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_taskID3.frameNStart = frameN  # exact frame index
            text_taskID3.tStart = t  # local t and not account for scr refresh
            text_taskID3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_taskID3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_taskID3.started')
            # update status
            text_taskID3.status = STARTED
            text_taskID3.setAutoDraw(True)
        
        # if text_taskID3 is active this frame...
        if text_taskID3.status == STARTED:
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
        for thisComponent in predict_task3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "predict_task3" ---
    for thisComponent in predict_task3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('predict_task3.stopped', globalClock.getTime())
    # check responses
    if key_predict_task3.keys in ['', [], None]:  # No response was made
        key_predict_task3.keys = None
    thisExp.addData('key_predict_task3.keys',key_predict_task3.keys)
    if key_predict_task3.keys != None:  # we had a response
        thisExp.addData('key_predict_task3.rt', key_predict_task3.rt)
        thisExp.addData('key_predict_task3.duration', key_predict_task3.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_input_predict_task3
    thisExp.addData('subjResponse', respDisplay_task3)
    # the Routine "predict_task3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(loop3_filename),
        seed=None, name='trials3')
    thisExp.addLoop(trials3)  # add the loop to the experiment
    thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3:
            globals()[paramName] = thisTrials3[paramName]
    
    for thisTrials3 in trials3:
        currentLoop = trials3
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
        if thisTrials3 != None:
            for paramName in thisTrials3:
                globals()[paramName] = thisTrials3[paramName]
        
        # --- Prepare to start Routine "task3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('task3.started', globalClock.getTime())
        task3_pic.setImage(Pic3)
        key_resp3.keys = []
        key_resp3.rt = []
        _key_resp3_allKeys = []
        # keep track of which components have finished
        task3Components = [fixation3, task3_pic, key_resp3, text_left_3, text_right_3, text_answer_prompt_3]
        for thisComponent in task3Components:
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
        
        # --- Run Routine "task3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation3* updates
            
            # if fixation3 is starting this frame...
            if fixation3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation3.frameNStart = frameN  # exact frame index
                fixation3.tStart = t  # local t and not account for scr refresh
                fixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation3.started')
                # update status
                fixation3.status = STARTED
                fixation3.setAutoDraw(True)
            
            # if fixation3 is active this frame...
            if fixation3.status == STARTED:
                # update params
                pass
            
            # if fixation3 is stopping this frame...
            if fixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation3.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation3.tStop = t  # not accounting for scr refresh
                    fixation3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation3.stopped')
                    # update status
                    fixation3.status = FINISHED
                    fixation3.setAutoDraw(False)
            
            # *task3_pic* updates
            
            # if task3_pic is starting this frame...
            if task3_pic.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                task3_pic.frameNStart = frameN  # exact frame index
                task3_pic.tStart = t  # local t and not account for scr refresh
                task3_pic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task3_pic, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task3_pic.started')
                # update status
                task3_pic.status = STARTED
                task3_pic.setAutoDraw(True)
            
            # if task3_pic is active this frame...
            if task3_pic.status == STARTED:
                # update params
                pass
            
            # if task3_pic is stopping this frame...
            if task3_pic.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task3_pic.tStartRefresh + task1_time-frameTolerance:
                    # keep track of stop time/frame for later
                    task3_pic.tStop = t  # not accounting for scr refresh
                    task3_pic.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task3_pic.stopped')
                    # update status
                    task3_pic.status = FINISHED
                    task3_pic.setAutoDraw(False)
            
            # *key_resp3* updates
            waitOnFlip = False
            
            # if key_resp3 is starting this frame...
            if key_resp3.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_resp3.frameNStart = frameN  # exact frame index
                key_resp3.tStart = t  # local t and not account for scr refresh
                key_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp3.started')
                # update status
                key_resp3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp3.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp3_allKeys.extend(theseKeys)
                if len(_key_resp3_allKeys):
                    key_resp3.keys = _key_resp3_allKeys[-1].name  # just the last key pressed
                    key_resp3.rt = _key_resp3_allKeys[-1].rt
                    key_resp3.duration = _key_resp3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp3.keys == str(correct_key3)) or (key_resp3.keys == correct_key3):
                        key_resp3.corr = 1
                    else:
                        key_resp3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_left_3* updates
            
            # if text_left_3 is starting this frame...
            if text_left_3.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_left_3.frameNStart = frameN  # exact frame index
                text_left_3.tStart = t  # local t and not account for scr refresh
                text_left_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_left_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_left_3.started')
                # update status
                text_left_3.status = STARTED
                text_left_3.setAutoDraw(True)
            
            # if text_left_3 is active this frame...
            if text_left_3.status == STARTED:
                # update params
                pass
            
            # *text_right_3* updates
            
            # if text_right_3 is starting this frame...
            if text_right_3.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_right_3.frameNStart = frameN  # exact frame index
                text_right_3.tStart = t  # local t and not account for scr refresh
                text_right_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_right_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_right_3.started')
                # update status
                text_right_3.status = STARTED
                text_right_3.setAutoDraw(True)
            
            # if text_right_3 is active this frame...
            if text_right_3.status == STARTED:
                # update params
                pass
            
            # *text_answer_prompt_3* updates
            
            # if text_answer_prompt_3 is starting this frame...
            if text_answer_prompt_3.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_answer_prompt_3.frameNStart = frameN  # exact frame index
                text_answer_prompt_3.tStart = t  # local t and not account for scr refresh
                text_answer_prompt_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_prompt_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_prompt_3.started')
                # update status
                text_answer_prompt_3.status = STARTED
                text_answer_prompt_3.setAutoDraw(True)
            
            # if text_answer_prompt_3 is active this frame...
            if text_answer_prompt_3.status == STARTED:
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
            for thisComponent in task3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task3" ---
        for thisComponent in task3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('task3.stopped', globalClock.getTime())
        # check responses
        if key_resp3.keys in ['', [], None]:  # No response was made
            key_resp3.keys = None
            # was no response the correct answer?!
            if str(correct_key3).lower() == 'none':
               key_resp3.corr = 1;  # correct non-response
            else:
               key_resp3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials3 (TrialHandler)
        trials3.addData('key_resp3.keys',key_resp3.keys)
        trials3.addData('key_resp3.corr', key_resp3.corr)
        if key_resp3.keys != None:  # we had a response
            trials3.addData('key_resp3.rt', key_resp3.rt)
            trials3.addData('key_resp3.duration', key_resp3.duration)
        # the Routine "task3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge_task3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judge_task3.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_judje_task3
        a.append(key_resp3.corr)     #变量a是个列表，.append()函数把括号内key_resp.corr的值添加到a中
        b = sum(a[0:])  #建立变量b,使用sum()函数计算列表a中从0开始到结尾（包含结尾最后一个值）的总和
        task3_corr = b
        # keep track of which components have finished
        judge_task3Components = []
        for thisComponent in judge_task3Components:
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
        
        # --- Run Routine "judge_task3" ---
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
            for thisComponent in judge_task3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judge_task3" ---
        for thisComponent in judge_task3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judge_task3.stopped', globalClock.getTime())
        # the Routine "judge_task3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials3'
    
    
    # --- Prepare to start Routine "fb_string_gen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_string_gen.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_fb_string
    if feedback_type == 1:
        fb_string = "刚刚的测试中测试你判断正确了" + str(b) + "个图片 \n (共30个图片)"
        pmt_loc = (0, 0.15)
        
    # keep track of which components have finished
    fb_string_genComponents = []
    for thisComponent in fb_string_genComponents:
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
    
    # --- Run Routine "fb_string_gen" ---
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
        for thisComponent in fb_string_genComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_string_gen" ---
    for thisComponent in fb_string_genComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_string_gen.stopped', globalClock.getTime())
    # the Routine "fb_string_gen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fb_current" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_current.started', globalClock.getTime())
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # keep track of which components have finished
    fb_currentComponents = [txt_fb, key_next, txt_fb2]
    for thisComponent in fb_currentComponents:
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
    
    # --- Run Routine "fb_current" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_fb* updates
        
        # if txt_fb is starting this frame...
        if txt_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb.frameNStart = frameN  # exact frame index
            txt_fb.tStart = t  # local t and not account for scr refresh
            txt_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb.started')
            # update status
            txt_fb.status = STARTED
            txt_fb.setAutoDraw(True)
        
        # if txt_fb is active this frame...
        if txt_fb.status == STARTED:
            # update params
            txt_fb.setText(fb_string, log=False)
        
        # *key_next* updates
        waitOnFlip = False
        
        # if key_next is starting this frame...
        if key_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            # update status
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                key_next.duration = _key_next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *txt_fb2* updates
        
        # if txt_fb2 is starting this frame...
        if txt_fb2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb2.frameNStart = frameN  # exact frame index
            txt_fb2.tStart = t  # local t and not account for scr refresh
            txt_fb2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb2.started')
            # update status
            txt_fb2.status = STARTED
            txt_fb2.setAutoDraw(True)
        
        # if txt_fb2 is active this frame...
        if txt_fb2.status == STARTED:
            # update params
            txt_fb2.setText('请按空格进入下一阶段\n', log=False)
        
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
        for thisComponent in fb_currentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_current" ---
    for thisComponent in fb_currentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_current.stopped', globalClock.getTime())
    # the Routine "fb_current" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "predict_task4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('predict_task4.started', globalClock.getTime())
    key_predict_task4.keys = []
    key_predict_task4.rt = []
    _key_predict_task4_allKeys = []
    # Run 'Begin Routine' code from code_input_predict_task4
    respDisplay_task4 = ""
    maxDigits = 6
    
    #key logger defaults
    last_len = 0
    key_list = []
    fb_string = "您已完成测试4"
    a = []
    
    # keep track of which components have finished
    predict_task4Components = [image_eg_predict_task4, txt_predict_task4, key_predict_task4, txt_question_predict_task4, txt_disp_input_predict_task4, text_taskID4]
    for thisComponent in predict_task4Components:
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
    
    # --- Run Routine "predict_task4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_eg_predict_task4* updates
        
        # if image_eg_predict_task4 is starting this frame...
        if image_eg_predict_task4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg_predict_task4.frameNStart = frameN  # exact frame index
            image_eg_predict_task4.tStart = t  # local t and not account for scr refresh
            image_eg_predict_task4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg_predict_task4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg_predict_task4.started')
            # update status
            image_eg_predict_task4.status = STARTED
            image_eg_predict_task4.setAutoDraw(True)
        
        # if image_eg_predict_task4 is active this frame...
        if image_eg_predict_task4.status == STARTED:
            # update params
            pass
        
        # *txt_predict_task4* updates
        
        # if txt_predict_task4 is starting this frame...
        if txt_predict_task4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_predict_task4.frameNStart = frameN  # exact frame index
            txt_predict_task4.tStart = t  # local t and not account for scr refresh
            txt_predict_task4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_predict_task4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_predict_task4.started')
            # update status
            txt_predict_task4.status = STARTED
            txt_predict_task4.setAutoDraw(True)
        
        # if txt_predict_task4 is active this frame...
        if txt_predict_task4.status == STARTED:
            # update params
            pass
        
        # *key_predict_task4* updates
        waitOnFlip = False
        
        # if key_predict_task4 is starting this frame...
        if key_predict_task4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_predict_task4.frameNStart = frameN  # exact frame index
            key_predict_task4.tStart = t  # local t and not account for scr refresh
            key_predict_task4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_predict_task4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_predict_task4.started')
            # update status
            key_predict_task4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_predict_task4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_predict_task4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_predict_task4.status == STARTED and not waitOnFlip:
            theseKeys = key_predict_task4.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return','backspace'], ignoreKeys=["escape"], waitRelease=False)
            _key_predict_task4_allKeys.extend(theseKeys)
            if len(_key_predict_task4_allKeys):
                key_predict_task4.keys = [key.name for key in _key_predict_task4_allKeys]  # storing all keys
                key_predict_task4.rt = [key.rt for key in _key_predict_task4_allKeys]
                key_predict_task4.duration = [key.duration for key in _key_predict_task4_allKeys]
        
        # *txt_question_predict_task4* updates
        
        # if txt_question_predict_task4 is starting this frame...
        if txt_question_predict_task4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_question_predict_task4.frameNStart = frameN  # exact frame index
            txt_question_predict_task4.tStart = t  # local t and not account for scr refresh
            txt_question_predict_task4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_question_predict_task4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_question_predict_task4.started')
            # update status
            txt_question_predict_task4.status = STARTED
            txt_question_predict_task4.setAutoDraw(True)
        
        # if txt_question_predict_task4 is active this frame...
        if txt_question_predict_task4.status == STARTED:
            # update params
            pass
        
        # *txt_disp_input_predict_task4* updates
        
        # if txt_disp_input_predict_task4 is starting this frame...
        if txt_disp_input_predict_task4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_disp_input_predict_task4.frameNStart = frameN  # exact frame index
            txt_disp_input_predict_task4.tStart = t  # local t and not account for scr refresh
            txt_disp_input_predict_task4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_disp_input_predict_task4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_disp_input_predict_task4.started')
            # update status
            txt_disp_input_predict_task4.status = STARTED
            txt_disp_input_predict_task4.setAutoDraw(True)
        
        # if txt_disp_input_predict_task4 is active this frame...
        if txt_disp_input_predict_task4.status == STARTED:
            # update params
            txt_disp_input_predict_task4.setText(respDisplay_task4, log=False)
        # Run 'Each Frame' code from code_input_predict_task4
        #if a new key has been pressed since last time
        if(len(key_predict_task4.keys) > last_len):
            
            #increment the key logger length
            last_len = len(key_predict_task4.keys)
            
            #grab the last key added to the keys list
            key_list.append(key_predict_task4.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
        
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 2):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            respDisplay_task4 = ''.join(key_list)
        
        # *text_taskID4* updates
        
        # if text_taskID4 is starting this frame...
        if text_taskID4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_taskID4.frameNStart = frameN  # exact frame index
            text_taskID4.tStart = t  # local t and not account for scr refresh
            text_taskID4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_taskID4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_taskID4.started')
            # update status
            text_taskID4.status = STARTED
            text_taskID4.setAutoDraw(True)
        
        # if text_taskID4 is active this frame...
        if text_taskID4.status == STARTED:
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
        for thisComponent in predict_task4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "predict_task4" ---
    for thisComponent in predict_task4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('predict_task4.stopped', globalClock.getTime())
    # check responses
    if key_predict_task4.keys in ['', [], None]:  # No response was made
        key_predict_task4.keys = None
    thisExp.addData('key_predict_task4.keys',key_predict_task4.keys)
    if key_predict_task4.keys != None:  # we had a response
        thisExp.addData('key_predict_task4.rt', key_predict_task4.rt)
        thisExp.addData('key_predict_task4.duration', key_predict_task4.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_input_predict_task4
    thisExp.addData('subjResponse', respDisplay_task4)
    # the Routine "predict_task4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials4 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(loop4_filename),
        seed=None, name='trials4')
    thisExp.addLoop(trials4)  # add the loop to the experiment
    thisTrials4 = trials4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
    if thisTrials4 != None:
        for paramName in thisTrials4:
            globals()[paramName] = thisTrials4[paramName]
    
    for thisTrials4 in trials4:
        currentLoop = trials4
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
        if thisTrials4 != None:
            for paramName in thisTrials4:
                globals()[paramName] = thisTrials4[paramName]
        
        # --- Prepare to start Routine "task4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('task4.started', globalClock.getTime())
        task34_pic.setImage(Pic4)
        key_resp4.keys = []
        key_resp4.rt = []
        _key_resp4_allKeys = []
        # keep track of which components have finished
        task4Components = [fixation4, task34_pic, key_resp4, text_left_4, text_right_4, text_answer_prompt_4]
        for thisComponent in task4Components:
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
        
        # --- Run Routine "task4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation4* updates
            
            # if fixation4 is starting this frame...
            if fixation4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation4.frameNStart = frameN  # exact frame index
                fixation4.tStart = t  # local t and not account for scr refresh
                fixation4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation4.started')
                # update status
                fixation4.status = STARTED
                fixation4.setAutoDraw(True)
            
            # if fixation4 is active this frame...
            if fixation4.status == STARTED:
                # update params
                pass
            
            # if fixation4 is stopping this frame...
            if fixation4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation4.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation4.tStop = t  # not accounting for scr refresh
                    fixation4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation4.stopped')
                    # update status
                    fixation4.status = FINISHED
                    fixation4.setAutoDraw(False)
            
            # *task34_pic* updates
            
            # if task34_pic is starting this frame...
            if task34_pic.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                task34_pic.frameNStart = frameN  # exact frame index
                task34_pic.tStart = t  # local t and not account for scr refresh
                task34_pic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task34_pic, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task34_pic.started')
                # update status
                task34_pic.status = STARTED
                task34_pic.setAutoDraw(True)
            
            # if task34_pic is active this frame...
            if task34_pic.status == STARTED:
                # update params
                pass
            
            # if task34_pic is stopping this frame...
            if task34_pic.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task34_pic.tStartRefresh + task1_time-frameTolerance:
                    # keep track of stop time/frame for later
                    task34_pic.tStop = t  # not accounting for scr refresh
                    task34_pic.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task34_pic.stopped')
                    # update status
                    task34_pic.status = FINISHED
                    task34_pic.setAutoDraw(False)
            
            # *key_resp4* updates
            waitOnFlip = False
            
            # if key_resp4 is starting this frame...
            if key_resp4.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                key_resp4.frameNStart = frameN  # exact frame index
                key_resp4.tStart = t  # local t and not account for scr refresh
                key_resp4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp4.started')
                # update status
                key_resp4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp4.getKeys(keyList=['s','k'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp4_allKeys.extend(theseKeys)
                if len(_key_resp4_allKeys):
                    key_resp4.keys = _key_resp4_allKeys[-1].name  # just the last key pressed
                    key_resp4.rt = _key_resp4_allKeys[-1].rt
                    key_resp4.duration = _key_resp4_allKeys[-1].duration
                    # was this correct?
                    if (key_resp4.keys == str(correct_key4)) or (key_resp4.keys == correct_key4):
                        key_resp4.corr = 1
                    else:
                        key_resp4.corr = 0
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
            
            # *text_answer_prompt_4* updates
            
            # if text_answer_prompt_4 is starting this frame...
            if text_answer_prompt_4.status == NOT_STARTED and tThisFlip >= task1_time-frameTolerance:
                # keep track of start time/frame for later
                text_answer_prompt_4.frameNStart = frameN  # exact frame index
                text_answer_prompt_4.tStart = t  # local t and not account for scr refresh
                text_answer_prompt_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_answer_prompt_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_answer_prompt_4.started')
                # update status
                text_answer_prompt_4.status = STARTED
                text_answer_prompt_4.setAutoDraw(True)
            
            # if text_answer_prompt_4 is active this frame...
            if text_answer_prompt_4.status == STARTED:
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
            for thisComponent in task4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task4" ---
        for thisComponent in task4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('task4.stopped', globalClock.getTime())
        # check responses
        if key_resp4.keys in ['', [], None]:  # No response was made
            key_resp4.keys = None
            # was no response the correct answer?!
            if str(correct_key4).lower() == 'none':
               key_resp4.corr = 1;  # correct non-response
            else:
               key_resp4.corr = 0;  # failed to respond (incorrectly)
        # store data for trials4 (TrialHandler)
        trials4.addData('key_resp4.keys',key_resp4.keys)
        trials4.addData('key_resp4.corr', key_resp4.corr)
        if key_resp4.keys != None:  # we had a response
            trials4.addData('key_resp4.rt', key_resp4.rt)
            trials4.addData('key_resp4.duration', key_resp4.duration)
        # the Routine "task4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judge_task4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judge_task4.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_judje_task4
        a.append(key_resp4.corr)     #变量a是个列表，.append()函数把括号内key_resp.corr的值添加到a中
        b = sum(a[0:])  #建立变量b,使用sum()函数计算列表a中从0开始到结尾（包含结尾最后一个值）的总和
        task4_corr = b
        # keep track of which components have finished
        judge_task4Components = []
        for thisComponent in judge_task4Components:
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
        
        # --- Run Routine "judge_task4" ---
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
            for thisComponent in judge_task4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judge_task4" ---
        for thisComponent in judge_task4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judge_task4.stopped', globalClock.getTime())
        # the Routine "judge_task4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials4'
    
    
    # --- Prepare to start Routine "fb_string_gen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_string_gen.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_fb_string
    if feedback_type == 1:
        fb_string = "刚刚的测试中测试你判断正确了" + str(b) + "个图片 \n (共30个图片)"
        pmt_loc = (0, 0.15)
        
    # keep track of which components have finished
    fb_string_genComponents = []
    for thisComponent in fb_string_genComponents:
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
    
    # --- Run Routine "fb_string_gen" ---
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
        for thisComponent in fb_string_genComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_string_gen" ---
    for thisComponent in fb_string_genComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_string_gen.stopped', globalClock.getTime())
    # the Routine "fb_string_gen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fb_current" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fb_current.started', globalClock.getTime())
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # keep track of which components have finished
    fb_currentComponents = [txt_fb, key_next, txt_fb2]
    for thisComponent in fb_currentComponents:
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
    
    # --- Run Routine "fb_current" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_fb* updates
        
        # if txt_fb is starting this frame...
        if txt_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb.frameNStart = frameN  # exact frame index
            txt_fb.tStart = t  # local t and not account for scr refresh
            txt_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb.started')
            # update status
            txt_fb.status = STARTED
            txt_fb.setAutoDraw(True)
        
        # if txt_fb is active this frame...
        if txt_fb.status == STARTED:
            # update params
            txt_fb.setText(fb_string, log=False)
        
        # *key_next* updates
        waitOnFlip = False
        
        # if key_next is starting this frame...
        if key_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            # update status
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                key_next.duration = _key_next_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *txt_fb2* updates
        
        # if txt_fb2 is starting this frame...
        if txt_fb2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_fb2.frameNStart = frameN  # exact frame index
            txt_fb2.tStart = t  # local t and not account for scr refresh
            txt_fb2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_fb2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_fb2.started')
            # update status
            txt_fb2.status = STARTED
            txt_fb2.setAutoDraw(True)
        
        # if txt_fb2 is active this frame...
        if txt_fb2.status == STARTED:
            # update params
            txt_fb2.setText('请按空格进入下一阶段\n', log=False)
        
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
        for thisComponent in fb_currentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fb_current" ---
    for thisComponent in fb_currentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fb_current.stopped', globalClock.getTime())
    # the Routine "fb_current" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "last_fb_and_predict" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('last_fb_and_predict.started', globalClock.getTime())
    key_predict_task5.keys = []
    key_predict_task5.rt = []
    _key_predict_task5_allKeys = []
    # Run 'Begin Routine' code from code_input_predict_task5
    respDisplay_task5 = ""
    maxDigits = 6
    
    #key logger defaults
    last_len = 0
    key_list = []
    fb_string = "您已完成测试4"
    a = []
    
    # keep track of which components have finished
    last_fb_and_predictComponents = [image_eg_predict_task5, txt_predict_task5, key_predict_task5, txt_question_predict_task5, txt_disp_input_predict_task5]
    for thisComponent in last_fb_and_predictComponents:
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
    
    # --- Run Routine "last_fb_and_predict" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_eg_predict_task5* updates
        
        # if image_eg_predict_task5 is starting this frame...
        if image_eg_predict_task5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_eg_predict_task5.frameNStart = frameN  # exact frame index
            image_eg_predict_task5.tStart = t  # local t and not account for scr refresh
            image_eg_predict_task5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_eg_predict_task5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_eg_predict_task5.started')
            # update status
            image_eg_predict_task5.status = STARTED
            image_eg_predict_task5.setAutoDraw(True)
        
        # if image_eg_predict_task5 is active this frame...
        if image_eg_predict_task5.status == STARTED:
            # update params
            pass
        
        # *txt_predict_task5* updates
        
        # if txt_predict_task5 is starting this frame...
        if txt_predict_task5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_predict_task5.frameNStart = frameN  # exact frame index
            txt_predict_task5.tStart = t  # local t and not account for scr refresh
            txt_predict_task5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_predict_task5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_predict_task5.started')
            # update status
            txt_predict_task5.status = STARTED
            txt_predict_task5.setAutoDraw(True)
        
        # if txt_predict_task5 is active this frame...
        if txt_predict_task5.status == STARTED:
            # update params
            pass
        
        # *key_predict_task5* updates
        waitOnFlip = False
        
        # if key_predict_task5 is starting this frame...
        if key_predict_task5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_predict_task5.frameNStart = frameN  # exact frame index
            key_predict_task5.tStart = t  # local t and not account for scr refresh
            key_predict_task5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_predict_task5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_predict_task5.started')
            # update status
            key_predict_task5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_predict_task5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_predict_task5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_predict_task5.status == STARTED and not waitOnFlip:
            theseKeys = key_predict_task5.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return','backspace'], ignoreKeys=["escape"], waitRelease=False)
            _key_predict_task5_allKeys.extend(theseKeys)
            if len(_key_predict_task5_allKeys):
                key_predict_task5.keys = [key.name for key in _key_predict_task5_allKeys]  # storing all keys
                key_predict_task5.rt = [key.rt for key in _key_predict_task5_allKeys]
                key_predict_task5.duration = [key.duration for key in _key_predict_task5_allKeys]
        
        # *txt_question_predict_task5* updates
        
        # if txt_question_predict_task5 is starting this frame...
        if txt_question_predict_task5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_question_predict_task5.frameNStart = frameN  # exact frame index
            txt_question_predict_task5.tStart = t  # local t and not account for scr refresh
            txt_question_predict_task5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_question_predict_task5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_question_predict_task5.started')
            # update status
            txt_question_predict_task5.status = STARTED
            txt_question_predict_task5.setAutoDraw(True)
        
        # if txt_question_predict_task5 is active this frame...
        if txt_question_predict_task5.status == STARTED:
            # update params
            pass
        
        # *txt_disp_input_predict_task5* updates
        
        # if txt_disp_input_predict_task5 is starting this frame...
        if txt_disp_input_predict_task5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_disp_input_predict_task5.frameNStart = frameN  # exact frame index
            txt_disp_input_predict_task5.tStart = t  # local t and not account for scr refresh
            txt_disp_input_predict_task5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_disp_input_predict_task5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'txt_disp_input_predict_task5.started')
            # update status
            txt_disp_input_predict_task5.status = STARTED
            txt_disp_input_predict_task5.setAutoDraw(True)
        
        # if txt_disp_input_predict_task5 is active this frame...
        if txt_disp_input_predict_task5.status == STARTED:
            # update params
            txt_disp_input_predict_task5.setText(respDisplay_task5, log=False)
        # Run 'Each Frame' code from code_input_predict_task5
        #if a new key has been pressed since last time
        if(len(key_predict_task5.keys) > last_len):
            
            #increment the key logger length
            last_len = len(key_predict_task5.keys)
            
            #grab the last key added to the keys list
            key_list.append(key_predict_task5.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
        
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 2):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            respDisplay_task5 = ''.join(key_list)
        
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
        for thisComponent in last_fb_and_predictComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "last_fb_and_predict" ---
    for thisComponent in last_fb_and_predictComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('last_fb_and_predict.stopped', globalClock.getTime())
    # check responses
    if key_predict_task5.keys in ['', [], None]:  # No response was made
        key_predict_task5.keys = None
    thisExp.addData('key_predict_task5.keys',key_predict_task5.keys)
    if key_predict_task5.keys != None:  # we had a response
        thisExp.addData('key_predict_task5.rt', key_predict_task5.rt)
        thisExp.addData('key_predict_task5.duration', key_predict_task5.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_input_predict_task5
    thisExp.addData('subjResponse', respDisplay_task5)
    # the Routine "last_fb_and_predict" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "thanks_gen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks_gen.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_last_thanks_2
    txt_last_thanks = "恭喜你完成了本次实验所有任务！\n 感谢你的参与！\n在四个测试中，\n你一共答对题数目为：" + str(task1_corr + task2_corr + task3_corr + task4_corr) 
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
    while continueRoutine:
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
            thanks.setText(txt_last_thanks, log=False)
        
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
    # the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
