import tkinter as tk
from tkinter import messagebox, Menu, font
from tkinter import BooleanVar, StringVar
from win32api import GetMonitorInfo, MonitorFromPoint
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from matplotlib.patches import Polygon, Rectangle
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os
import re
import math
import subprocess
def open_pdf():
    try:
        dir=pathlib.Path(__file__).parent.absolute()
        filename='StairIRC.pdf'
        path=os.path.join(dir, filename)
    finally:subprocess.Popen([path], shell=True)
def end():
    for widget in root.winfo_children(): # Cleanup All On Exit
        if isinstance(widget, tk.Canvas):widget.destroy()
        else:widget.destroy()
    os._exit(0)
def on_resize(event):
    if event.widget == root:
        if root_start.get():return
        if event.width>=event.height:root_fontsize= int(event.height/(default_hgt/rootdefault_fontsize))
        else:root_fontsize= int(event.width/(default_wid/rootdefault_fontsize))
        if root_fontsize<4: root_fontsize=4
        root.font['size'] = root_fontsize
        lbl_font['size'] = root_fontsize-2
    return
def menu_popup(event):
    try:popup.tk_popup(event.x_root, event.y_root)
    finally:popup.grab_release()
def about():
       messagebox.showinfo('About', 'Creator: Ross Waters\nEmail: RossWatersjr@gmail.com'\
              '\nProgram: Staircase Stringer Designer\nRevision: 2.4'\
              '\nLast Revision Date: 12/13/2023\nLanguage: Python 3.12.0 64-bit'\
              '\nOperating System: Windows 10/11')
def enterkey_pressed(event):
    try:
        if (event.keysym)=='Return':
            if event.widget['text']=='Stringer Height': 
                value=stgr_hgt.get()
                if value=='': raise Exception('Staircase Height Value Is Null.')
                valmin,valmax=14.00,150.00
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Staircase Height Range Is From\n'
                    msg2= '14 inches (2 Steps) to 150 inches (@20 Steps).'
                    messagebox.showwarning('Limit Violation', msg1+msg2)
                    if float(value)<valmin:stgr_hgt.set(str(valmin))
                    elif float(value)>valmax:stgr_hgt.set(str(valmax))
                    else:stgr_hgt.set(str(value))
            elif event.widget['text']=='Run Per Step':
                value=stgr_run.get()
                tread_overhang=float(tdoverhang.get())
                if float(value) <11.00 : #Examine Overhang >=0.75-1.25
                    if float(tread_overhang)< 0.75:
                        tread_overhang=0.75
                        tdoverhang.set(tread_overhang)
                if value=='': raise Exception('Run Per Step Value Is Null.')
                valmin,valmax=10.00,30.00
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Staircase Run Length Is From\n'
                    msg2= '10.00 inches to 30.00 inches.'
                    messagebox.showwarning('(Application Limit)', msg1+msg2)
                    if float(value)<valmin:stgr_run.set(str(valmin))
                    elif float(value)>valmax:stgr_run.set(str(valmax))
                    else:stgr_run.set(str(value))
                tread_depth=float(value)
                tddepth.set(tread_depth)
            elif event.widget['text']=='Toekick Angle':
                value=toekick.get()
                if value=='': raise Exception('Toe Kick Angle Value Is Null.')
                valmin,valmax=0.0,30.00
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Toe Kick Angel Is From\n'
                    msg2= '0 Degrees to 30 Degrees (I.R.C) Specs.'
                    messagebox.showwarning('(I.R.C) Spec. Violation', msg1+msg2)
                    toekick.set('30')
                    if float(value)<valmin:toekick.set(str(valmin))
                    elif float(value)>valmax:toekick.set(str(valmax))
                    else:toekick.set(str(value))
            elif event.widget['text']=='Tread Thickness':
                value=tdthickness.get()
                if value=='': raise Exception('Tread Thickness Value Is Null.')
                valmin,valmax=0.0,3.0
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Tread Thickness Is From\n'
                    msg2= '0 inches to 3 inches.'
                    messagebox.showwarning('Application Limit', msg1+msg2)
                    if float(value)<valmin:tdthickness.set(str(valmin))
                    elif float(value)>valmax:tdthickness.set(str(valmax))
                    else:tdthickness.set(str(value))
            elif event.widget['text']=='Top Tread Thickness':
                value=ttdthickness.get()
                if value=='': raise Exception('Top Tread Thickness Value Is Null.')
                valmin,valmax=0.0,3.0
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Top Tread Thickness Is From\n'
                    msg2= '0 inches to 3 inches.'
                    messagebox.showwarning('Application Limit', msg1+msg2)
                    if float(value)<valmin:ttdthickness.set(str(valmin))
                    elif float(value)>valmax:ttdthickness.set(str(valmax))
                    else:ttdthickness.set(str(value))
            elif event.widget['text']=='Tread Depth':
                run_per_step=float(stgr_run.get())
                tread_depth=float(tddepth.get())
                stgr_run.set(str(tread_depth))
                tread_overhang=float(tdoverhang.get())
                if tread_depth<11.00:
                    if float(tread_overhang)< 0.75:
                        tread_overhang=0.75
                        tdoverhang.set(tread_overhang)
                value=tddepth.get()
                if value=='': raise Exception('Tread Depth Value Is Null.')
                valmin,valmax=10.0,30.0
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Tread Depth Is '+str(valmin)+' inches\n'
                    msg2='To '+str(valmax)+' inches.'
                    messagebox.showwarning('(Application Limit)', msg1+msg2)
                    if float(value)<valmin:tddepth.set(str(valmin))
                    elif float(value)>valmax:tddepth.set(str(valmax))
                    else:tddepth.set(str(value))
            elif event.widget['text']=='Tread Overhang':
                value=tdoverhang.get()
                run_per_step=float(stgr_run.get())
                tread_depth=float(tddepth.get())
                if run_per_step>=11: valmin=0.0
                if run_per_step<11: valmin=0.75
                valmax=1.25       
                if value=='': raise Exception('Tread Overhang Value Is Null.')
                if float(value)<valmin or float(value)>valmax:
                    msg1='Allowable Tread Overhang Is From '+str(valmin)+' inches To\n'
                    msg2= str(valmax)+' inches (I.R.C) Specs.'
                    messagebox.showwarning('(I.R.C) Spec. Violation', msg1+msg2)
                    if float(value)<valmin:tdoverhang.set(str(valmin))
                    elif float(value)>valmax:tdoverhang.set(str(valmax))
                    else:tdoverhang.set(str(value))
        plot()
    except Exception as e:
            msg1='Exception occurred while code execution:\n'
            msg2= repr(e)+' '+event.widget['text']
            msg3='\nPlease Check Entry Values!'
            messagebox.showerror('Exeption Error', msg1+msg2+msg3)
def validate_Entries(entry_text):
    result=re.match(r"^\d*[.,]?\d*$", entry_text) #  Positive Integers or Floats
    return (entry_text == '' 
    or (entry_text.count('.') <= 1 # allow only one period
        and result is not None
        and result.group(0) != ''))
def on_validate(P):
    return validate_Entries(P)
def plot():
    try:
        fig.clear(True) # Start Fresh
        viewport=fig.add_subplot(111) # Create The Figure
        viewport.set_facecolor('lightcyan')
        viewport.set_title('Staircase Stringer Calculator (I.R.C. Specs.)',
            ha='center', color='mediumblue', fontsize=14, weight='normal', style='italic')# Centered on graph
        # X and Y Axis Labels
        viewport.set_xlabel('Required Floor Space (inches)', ha='center', color='firebrick',
            fontsize=10, weight='normal', style='italic')
        viewport.set_ylabel('Distance To Top Landing (inches)', ha='center', color='firebrick',
        fontsize=10, weight='normal', style='italic')
        # Define and Set Plot Limits
        stringer_hgt=float(stgr_hgt.get())
        total_rise=stringer_hgt
        pos=top_position.get() #Returns Integer
        run_per_step=float(stgr_run.get())
        top_tread_thickness=float(ttdthickness.get())
        tread_depth=float(tddepth.get())
        finished_hgt=stringer_hgt+top_tread_thickness
        tread_thickness=float(tdthickness.get())
        num_of_steps=int(finished_hgt/7.5)
        toekick_angle=float(toekick.get())
        stringer_width=float(stgr_wid.get())
        tread_overhang=float(tdoverhang.get())
        if pos==0: # Flush With Top Sub-Floor
            num_of_risers=num_of_steps
            num_of_runners=num_of_risers
            rise_per_step=finished_hgt/num_of_risers
            # If Rise > Spec, Add Step To Reduce Rise
            if rise_per_step >7.75: #Max Riser Hgt
                num_of_risers += 1
                rise_per_step=finished_hgt/num_of_risers
                num_of_runners=num_of_risers
                rise_per_step=finished_hgt/num_of_risers
            num_of_steps=num_of_risers
            top_riser_rise=rise_per_step-top_tread_thickness+tread_thickness
            totalrise.set(total_rise)
            stringer_hgt=float(stgr_hgt.get())
            req_floor_space=run_per_step*num_of_steps
            xmax=req_floor_space+(run_per_step*2)
            ymax=xmax/aspect_ratio
            ylimits=0, ymax
            xlimits=0, xmax
            viewport.set(xlim=xlimits, ylim=ylimits, autoscale_on=False)
            x1=0.0
            x2=x1+run_per_step
            y1=stringer_hgt
            y2=y1
            # Upper Landing Annotation
            # Try Keeping Arrow Head Constant size
            arrow_x=(1.75*run_per_step)+tread_overhang
            viewport.arrow(arrow_x, stringer_hgt, -run_per_step*0.5, 0, 
                head_width=ymax/116, head_length=(xmax*2)/158, fc='k', ec='k')
            viewport.annotate('Upper Landing Subfloor = '+ str(stringer_hgt) +' in.',
                xy=(arrow_x+1, stringer_hgt-0.1), xycoords='data', fontsize=6, color='k')
        else: # 1 Step Down From Top Sub-Floor
            # Top Overhang
            viewport.add_patch(Rectangle((0, stringer_hgt), tread_overhang, top_tread_thickness,
            facecolor = 'lime', ec='darkgreen',lw=1,fill=True))
            rise_per_step=finished_hgt/num_of_steps
            num_of_runners=num_of_steps-1
            num_of_risers=num_of_steps-1  
            if rise_per_step >7.75: #Max Riser Hgt
                num_of_risers += 1
                num_of_steps=num_of_risers+1
                num_of_runners=num_of_steps-1
                rise_per_step=finished_hgt/num_of_steps
            req_floor_space=run_per_step*num_of_risers
            xmax=req_floor_space+(run_per_step*3)
            ymax=xmax/aspect_ratio
            ylimits=0, ymax
            xlimits=0, xmax
            viewport.set(xlim=xlimits, ylim=ylimits, autoscale_on=False)
            x1=0.0
            x2=x1+run_per_step
            total_rise=finished_hgt-rise_per_step-tread_thickness
            top_riser_rise=rise_per_step-top_tread_thickness+tread_thickness
            totalrise.set(round(total_rise,4))
            y1=total_rise
            y2=y1
            # Upper Landing Annotation
            # 116 And 158 Represents Viewport Height and Width
            # At a Standard 9 Feet Staircasing With Arrow Dimensions
            # At Approximately L=2, W=1
            viewport.arrow(run_per_step*0.85, stringer_hgt, -run_per_step*0.5, 0, 
                head_width=ymax/116, head_length=(xmax*2)/158, fc='k', ec='k')      
            viewport.annotate('Upper Landing Subfloor = '+ str(stringer_hgt) +' in.',
                xy=(run_per_step+1, stringer_hgt-0.1), xycoords='data', fontsize=6, 
                color='k', clip_on=True)
            # Total Rise Annotation
            arrow_x=(1.75*run_per_step)+tread_overhang
            viewport.arrow(arrow_x, total_rise, -run_per_step*0.5, 0, 
                head_width=ymax/116, head_length=(xmax*2)/158, fc='k', ec='k')      
            viewport.annotate('Stringer Rise = '+ str(round(total_rise,4)) +' in.',
                xy=(arrow_x+1, total_rise-0.1), xycoords='data', fontsize=6, 
                color='k', clip_on=True)
        # Set Tick Label Font Size And Grid/Ticks
        viewport.tick_params(axis='both', which='major', labelsize=8)
        # Change Major And Minor Ticks Depending On Height Of Staircase
        if stringer_hgt<=90:
            xmajor_tick=run_per_step
            ymajor_tick=rise_per_step
            xminor_tick=2
            yminor_tick=2
        elif stringer_hgt>90:
            xmajor_tick=run_per_step*2
            ymajor_tick=rise_per_step*2
            xminor_tick=2
            yminor_tick=2
        viewport.xaxis.set_major_locator(MultipleLocator(xmajor_tick))
        viewport.xaxis.set_minor_locator(AutoMinorLocator(xminor_tick))
        viewport.yaxis.set_major_locator(MultipleLocator(ymajor_tick))
        viewport.yaxis.set_minor_locator(AutoMinorLocator(yminor_tick))
        # Turn Both Major and Minor Ticks On
        viewport.grid(which='major', color='lightgray', linestyle='dashed')
        viewport.grid(which='minor', color='lightgray', linestyle='dashed')
        # Get Things Ready To Plot The Stringer Risers And Runners
        if toekick_angle > 0: # Toe Kick Angle > 0
            toekick_tan=math.tan(toekick_angle/(180/math.pi))
            run_diff=toekick_tan*rise_per_step #Correction For Runs With Riser Angle
            riser_len=math.sqrt(pow(rise_per_step,2)+pow(run_diff,2))
            runner_len=run_per_step+run_diff
            tread_top_adj = toekick_tan * tread_thickness
        else:
            run_diff=0
            riser_len=rise_per_step
            runner_len=run_per_step
            tread_top_adj=0
        while x1 < req_floor_space: # Plot The Stringer Risers And Runners
            viewport.plot([x1-run_diff,x2], [y1,y2],'saddlebrown', lw=2) #Plot Runners
            x1=x2
            y1=y2
            if y2==stringer_hgt:
                y2-=top_riser_rise
            else:        
                y2-=rise_per_step
            viewport.plot([x1,x2-run_diff], [y1,y2],'saddlebrown', lw=2) #Plot Risers
            y1=y2
            x2+=run_per_step
        # Get Things Ready To Plot Tread
        x1=0
        y1=total_rise
        x2=x1+tread_depth+tread_overhang
        y2=y1
        x3=x2
        y3=y2+tread_thickness
        if x1==0:
            x4=x1 # No toekick_angle For Top Step
            y3=y2+top_tread_thickness # Top Tread May Differ From Tread
            y4=y3
        else:
            x4=x1+tread_top_adj
            x1=0
            y1=total_rise
            y3=y2+tread_thickness
            y4=y3
        while y1 > 3: # Plot The Tread
            p = np.array([[x1-run_diff,y1], [x2,y2], [x3,y3], [x4,y4]])
            viewport.add_patch(Polygon(p, facecolor = 'lime',closed=True,
                ec='darkgreen',lw=1,fill=True))
            x1+=run_per_step
            y1-=rise_per_step
            x2=x1+tread_depth+tread_overhang
            if y2==stringer_hgt:y2-=top_riser_rise
            else:y2-=rise_per_step        
            y1=y2
            x3=x2
            y3=y2+tread_thickness
            x4=x1-run_diff+tread_top_adj
            y4=y3
        # Top Riser Rise Annotations
        if pos==0: arrow_y=stringer_hgt-(0.65*rise_per_step)
        else: arrow_y=stringer_hgt-(1.65*rise_per_step)
        arrow_x=(run_per_step*1.75)-0.75*run_diff 
        viewport.arrow(arrow_x, arrow_y, -run_per_step*0.5, 0, head_width=ymax/116, 
            head_length=(xmax*2)/158, fc='k', ec='k')      
        viewport.annotate('Top Riser Rise = '+ str(round(top_riser_rise,4)) +' in.',
            xy=(arrow_x+1, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        # Rise Per Step Annotations
        if num_of_risers>2:
            if pos==0: arrow_y=stringer_hgt-(1.65*rise_per_step)
            else: arrow_y=stringer_hgt-(2.65*rise_per_step)
            arrow_x=(run_per_step*2.75)-0.75*run_diff 
            viewport.arrow(arrow_x, arrow_y, -run_per_step*0.5, 0, head_width=ymax/116, 
                head_length=(xmax*2)/158, fc='k', ec='k')      
            viewport.annotate('Rise = '+ str(round(rise_per_step,4)) +' in.',
                xy=(arrow_x+1, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        # Bottom Riser Rise Annotations
        arrow_x=(req_floor_space-(run_per_step/aspect_ratio))-run_diff*0.75
        arrow_y=0.3*(rise_per_step-tread_thickness)
        viewport.arrow(arrow_x, arrow_y, 0.5*run_per_step, 0, head_width=ymax/116, 
            head_length=(xmax*2)/158, fc='k', ec='k')
        # This Annotation Is Used To Only Obtain Text Dimensions.
        # Will Be Removed And Replaced Below.      
        txt=viewport.annotate('Bottom Riser Rise = '+ str(round(rise_per_step-tread_thickness,4)) +' in.',
            xy=((xmax)*0.5, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        r = canvas.get_renderer()
        # Get Text Properties in Data Coords.
        bbox = viewport.transData.inverted().transform_bbox(txt.get_window_extent(renderer=r))
        x0=arrow_x-bbox.width-1
        txt.remove() # Remove Original Annotation And Replace With New
        # Place Annotation Along Left Side Of Arrow According To Data Dimensions
        txt=viewport.annotate('Bottom Riser Rise = '+ str(round(rise_per_step-tread_thickness,4)) +' in.',
            xy=(x0, arrow_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        # Set Variables To Move Arrows And Annotations According To Number Of Steps
        if num_of_risers<=7:
            redarrow_x=req_floor_space-run_per_step+tread_overhang
            redarrow_y=(3.2*rise_per_step)+1
            runarrow_x=req_floor_space+tread_overhang
            runarrow_y=(2.5*rise_per_step)+1
            runnotation_x=(req_floor_space-run_per_step)+2
            runnotation_y=(2.5*rise_per_step)+1.5
            overhang_x=(req_floor_space-run_per_step)+2
            overhang_y=(2.5*rise_per_step)+3.5
            tdarrow_x=(req_floor_space)-((run_per_step*2)-tread_overhang)
            tdarrow_y=(3.5*rise_per_step)+1
            tdannotation_x=(req_floor_space-((run_per_step*2)-tread_overhang))+1
            tdannotation_y=3.5*rise_per_step
            twarrow_x=(req_floor_space)-(run_per_step*2)-run_diff
            twarrow_y=(3.7*rise_per_step)
            twannotation_x=(req_floor_space-(run_per_step*2))-(run_diff-1)
            twannotation_y=(3.7*rise_per_step)
        elif num_of_risers<=12:
            redarrow_x=(req_floor_space-(2*run_per_step))+tread_overhang
            redarrow_y=(4.2*rise_per_step)+1
            runarrow_x=(req_floor_space-run_per_step)+tread_overhang
            runarrow_y=(3.5*rise_per_step)+1
            runnotation_x=(req_floor_space-(2*run_per_step))+2
            runnotation_y=(3.5*rise_per_step)+1.5
            overhang_x=(req_floor_space-(2*run_per_step))+2
            overhang_y=(4.5*rise_per_step)-3
            tdarrow_x=(req_floor_space)-((run_per_step*3)-tread_overhang)
            tdarrow_y=(4.5*rise_per_step)+1
            tdannotation_x=(req_floor_space-((run_per_step*3)-tread_overhang))+1
            tdannotation_y=4.5*rise_per_step
            twarrow_x=(req_floor_space)-(run_per_step*3)-run_diff
            twarrow_y=(4.8*rise_per_step)+1
            twannotation_x=(req_floor_space-(run_per_step*3))-(run_diff-1)
            twannotation_y=(4.8*rise_per_step)+1
        else: 
            redarrow_x=(req_floor_space-(3*run_per_step))+tread_overhang
            redarrow_y=(5.2*rise_per_step)+1
            runarrow_x=(req_floor_space-2*run_per_step)+tread_overhang
            runarrow_y=(4.5*rise_per_step)+1
            runnotation_x=(req_floor_space-(3*run_per_step))+2
            runnotation_y=(4.5*rise_per_step)+1.5
            overhang_x=(req_floor_space-(3*run_per_step))+2
            overhang_y=(5.5*rise_per_step)-2.5
            tdarrow_x=(req_floor_space)-((run_per_step*4)-tread_overhang)
            tdarrow_y=(5.5*rise_per_step)+1
            tdannotation_x=(req_floor_space-((run_per_step*4)-tread_overhang))+1
            tdannotation_y=5.5*rise_per_step
            twarrow_x=(req_floor_space)-(run_per_step*4)-run_diff
            twarrow_y=(5.8*rise_per_step)+1
            twannotation_x=(req_floor_space-(run_per_step*4))-(run_diff-1)
            twannotation_y=(5.8*rise_per_step)+1
        # Use The Variables And Move Arrows And Annotation Accordingly
        viewport.arrow(redarrow_x, redarrow_y, 0,
            (-1.2*rise_per_step)+tread_thickness, head_width=ymax/116,
            head_length=(xmax*2)/158, fc='k', ec='red')      
        # Run Per Step Arrow And Annotation             
        viewport.arrow(runarrow_x, runarrow_y, 0,
            (-rise_per_step*1.5)+tread_thickness, head_width=ymax/116,
            head_length=(xmax*2)/158, fc='k', ec='k')
        txt=viewport.annotate('Run Per Step = '+ str(round(run_per_step,3)) +' in.', xy=(runnotation_x,
            runnotation_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        # Overhang Annotation Only
        txt=viewport.annotate('Overhang = '+ str(round(tread_overhang,3)) +' in.', xy=(overhang_x,
            overhang_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        # Tread Depth Arrow And Annotation       
        viewport.arrow(tdarrow_x, tdarrow_y, 0, 
            (-rise_per_step*1.5)+tread_thickness, head_width=ymax/116, 
            head_length=(xmax*2)/158, fc='k', ec='k')
        txt=viewport.annotate('Tread Depth = '+ str(round(tread_depth,3)) +' in.', xy=(tdannotation_x,
            tdannotation_y), xycoords='data', fontsize=6, color='k', clip_on=True)
        if toekick_angle > 0:
            viewport.arrow(twarrow_x, twarrow_y, 0, 
                (-rise_per_step*1.8)+tread_thickness, head_width=ymax/116, 
                head_length=(xmax*2)/158, fc='k', ec='k')      
            txt=viewport.annotate('Tread Width = '+ str(round(runner_len+tread_overhang,3)) +' in.', 
                xy=(twannotation_x, twannotation_y),
                xycoords='data', fontsize=6, color='k', clip_on=True)
        # Draw The Strnger Material
        x1=0
        if pos==0: y1=stringer_hgt+rise_per_step
        if pos==1: y1=stringer_hgt
        # peaks_valleys, Top Cut Length, Floor Cut Length And Staircase Angle
        peaks_valleys=round(math.sqrt(pow(rise_per_step,2)+pow(run_per_step,2)),4)#Hyp
        topanglesin=run_per_step/peaks_valleys
        topcutlength= stringer_width/topanglesin
        x2,y2=x1,y1-topcutlength              
        stair_angle=math.atan(rise_per_step/run_per_step)*(180/math.pi)
        hyp=y2/math.sin(stair_angle/(180/math.pi))
        x3,y3=math.sqrt(pow(hyp,2)-pow(y2,2)),0
        floor_sin=rise_per_step/peaks_valleys
        floor_cutlength=stringer_width/floor_sin
        x4,y4=x3+floor_cutlength,0
        # Plot Stringer Material
        p = np.array([[x1,y1], [x2,y2], [x3,y3], [x4,y4]])
        viewport.add_patch(Polygon(p, closed=True,
            ec='saddlebrown',lw=1,ls='--', fill=False))
        # Stringer Length Required
        if pos==0: y1=stringer_hgt
        if pos==1: y1=stringer_hgt-rise_per_step
        stringer_len=math.sqrt(pow(y1,2)+pow(req_floor_space,2))
        tread_wid=runner_len+tread_overhang # Total Tread Width
        fig.canvas.draw() # Refresh The Canvas
        # Update Entry Widgets
        numrisers.set(num_of_risers)
        numsteps.set(num_of_steps)
        riseperstep.set(round(rise_per_step,4))
        numrunners.set(num_of_runners)
        totalrun.set(round(req_floor_space,4))
        runnerlength.set(round(runner_len,4))
        riserlength.set(round(riser_len,4))
        toprise.set(round(top_riser_rise,4))
        bot_riser_rise=rise_per_step-tread_thickness
        botrise.set(round(bot_riser_rise,4))
        stairangle.set(round(stair_angle,4))
        # Stringer Floor And Top Cut Angles
        floor_cutangle=90-stair_angle
        botangle.set(round(floor_cutangle,4))
        peakvalley.set(peaks_valleys)
        stringerlen.set(round(stringer_len,4))
        treadwid.set(round(tread_wid,4)) 
    except Exception as e:
        msg1='Exception occurred while code execution:\n'
        msg2= repr(e)
        msg3='\nPlease Check Entry Values!'
        messagebox.showerror('Exeption Error', msg1+msg2+msg3)
if __name__ == "__main__":
    root=tk.Tk()
    root_start=BooleanVar()
    root_start.set(True)
    dir=pathlib.Path(__file__).parent.absolute()
    filename='Stringer.ico'
    path=os.path.join(dir, filename)
    root.iconbitmap(path)  
    title='Staircase Stringer Designer'
    options='Right-Click Graph For Options'
    root.title(title + options.rjust(40+len(options)))
    monitor_info=GetMonitorInfo(MonitorFromPoint((0,0)))
    work_area= monitor_info.get("Work")
    screen_width=work_area[2]
    screen_height=work_area[3]
    root_hgt=int(screen_height/1.8)
    root_wid=int(screen_width/2.0)
    default_hgt=root_hgt 
    default_wid=root_wid 
    x=(screen_width/2)-(root_wid/2)
    y=(screen_height/2)-(root_hgt/2)
    root.configure(bg='lightgray') # Set main backcolor to aqua
    root.bind("<Configure>", on_resize)
    root.protocol("WM_DELETE_WINDOW", end)
    fig_width=700
    fig_height=500
    px = 1/plt.rcParams['figure.dpi'] # Create And Position The Figure
    fig=plt.figure(figsize=(fig_width*px, fig_height*px), dpi=113)
    aspect_ratio=fig_width/fig_height
    fig.patch.set_facecolor('lightgray')# Set the figure facecolor
    canvas=FigureCanvasTkAgg(fig, master=root) # Create The Canvas
    canvas.get_tk_widget().pack(side='top', anchor='nw')#place(x=0, y=0)
    toolbar=NavigationToolbar2Tk(canvas, root) # create Matplotlib toolbar
    tb_hgt=toolbar.winfo_reqheight()
    canvas.get_tk_widget().pack() # place oolbar on Tkinter window
    root.geometry('%dx%d+%d+%d' % (root_wid, root_hgt+tb_hgt, x, y, )) # Position Center Of Screen
    lbl_font=font.Font(family='lucidas', size=8, weight='bold', slant='italic')
    root.font=font.Font(family='lucidas', size=10, weight='normal', slant='italic')
    rootdefault_fontsize=10
    lbldefault_fontsize=8
    top_position = tk.IntVar() #PY_VAR3 Location Of Top Step, 0=Flush, 1=Down 1 Step
    stgr_hgt=StringVar(root,name='Stringer Height')
    stgr_run=StringVar(root,name='Run Per Step')
    toekick=StringVar(root,name='Toekick Angle')
    tdthickness=StringVar(root,name='Tread Thickness')
    ttdthickness=StringVar(root,name='Top Tread Thickness')
    tddepth=StringVar(root,name='Tread Depth')
    tdoverhang=StringVar(root,name='Tread Overhang')
    stgr_wid=StringVar(root,name='Stringer Width')
    treadwid=StringVar() # tread_wid
    totalrise=StringVar() # total_rise
    riseperstep=StringVar() # rise_per_step
    numrisers=StringVar() # num_of_risers
    toprise=StringVar() # top_riser_rise
    botrise=StringVar() # bot_riser_rise
    totalrun=StringVar() # req_floor_space
    numrunners=StringVar() # num_of_runners
    numsteps=StringVar() # num_of_steps
    runnerlength=StringVar() # runner_len
    riserlength=StringVar()
    stairangle=StringVar() # stair_angle
    botangle=StringVar() # floor_cutangle
    peakvalley=StringVar() # peaks_valleys
    stringerlen=StringVar() # stringer_len
    # Create Frame with Label and place 2 radio buttons inside
    fra_lbl=tk.Label(root, background='light gray', foreground='mediumblue', font=root.font,
        text="Stringer Position At Top")
    lbl_wid=fra_lbl.winfo_reqwidth()
    lbl_hgt=fra_lbl.winfo_reqheight()
    x= (root_wid-(lbl_wid+20)) / root_wid
    fra_lbl.place(relx=x, rely=0.008, relwidth=0.16, relheight=0.028892455858748)
    # Radio Buttons For Staircase Location At Top   
    top_position.set(0)  # initializing the choice, i.e. Python
    rdo1=tk.Radiobutton(root, text='Flush with Top Subfloor', indicatoron=0, activebackground='aqua',
        background='lightgray', font=lbl_font, padx=10, variable=top_position, command=plot, value=0)
    rdo1.place(relx=x, rely=0.04, relwidth=0.16, relheight=0.037)
    rdo2=tk.Radiobutton(root, text='Down 1 Step from Top', indicatoron=0, activebackground='aqua',
        background='lightgray', font=lbl_font, padx=10, variable=top_position, command=plot, value=1)
    rdo2.place(relx=x, rely=0.082, relwidth=0.16, relheight=0.037)
    #Height for calculations = 623 = root_hgt + tb_hgt = 573 + 50
    root.bind('<Return>', enterkey_pressed) # Enter Key Was Pressed On Entry Widgets
    lbl=[]
    x,y,wid,hgt=0.77604166,0.128410915,0.153125,0.0288
    text=['Staircase Height (in.)','Run per Step (in.)','Riser Toe Kick Angle','Tread Thickness (in.)',
        'Top Tread Thickness (in.)','Tread Depth (in.)','Tread Overhang (in.)','Stringer Width (in.)',
        'Tread Width (in.)','Stringer Total Rise (in.)','Rise per Step (in.)','Number of Risers',
        'Top Riser Rise (in.)','Bottom Riser Rise (in.)','Required Floor Space (in.)','Number of Runners',
        'Number of Steps','Runner Cut Length (in.)','Riser Cut Length (in.)','Staircase Angle',
        'Bottom Cut Angle','Peaks/Valleys (in.)','Stringer Length Req. (in.)']
    for index, element in enumerate(text):
        lbl.append([index])
        lbl[index]=tk.Label(root, background='lightgray', font=lbl_font, text=element, justify='left', anchor='e')
        lbl[index].place(relx=x, rely=y, relwidth=wid, relheight=hgt)
        y+=0.033707865
    text.clear()    
    txtbx=[]
    cmd=[]    
    x,y,wid,hgt=0.929166666,0.128410915,0.067,0.0288
    strvars=[stgr_hgt,stgr_run,toekick,tdthickness,ttdthickness,tddepth,tdoverhang,stgr_wid]
    text=['60.0','10.25','0.0','1.0','1.0','10.25','1.0','11.5']
    for index, element in enumerate(strvars):
        txtbx.append([index])
        cmd.append([index])
        txtbx[index]=tk.Entry(root, background='lightcyan', textvariable=element, font=root.font,)
        txtbx[index]['validatecommand']=(txtbx[index].register(validate_Entries),'%P','%d')
        cmd[index]=(txtbx[index].register(on_validate), '%P')
        txtbx[index].config(validate="key", validatecommand=cmd[index])
        txtbx[index].place(relx=x, rely=y, relwidth=wid, relheight=hgt)
        txtbx[index].insert(0, text[index])
        y+=0.033707865
    strvars.clear()
    text.clear()    
    lbl2=[]
    wid,hgt=0.067,0.0288
    strvars=[treadwid,totalrise,riseperstep,numrisers,toprise,botrise,totalrun,numrunners,numsteps,
        runnerlength,riserlength,stairangle,botangle,peakvalley,stringerlen]
    for index, element in enumerate(strvars):
        lbl2.append([index])
        lbl2[index]=tk.Label(root, background='whitesmoke', font=root.font, textvariable=element, 
            anchor='w', justify='right', borderwidth=1, relief="ridge")
        lbl2[index].place(relx=x, rely=y, relwidth=wid, relheight=hgt)
        y+=0.033707865
    strvars.clear()
    text.clear()
    popup=Menu(root, tearoff=0)
    #Add PopUp Menu Items
    popup.add_command(label="View I.R.C. pdf File", background='aqua', command=lambda:open_pdf())
    popup.add_separator(background='lightgray')
    popup.add_command(label="About", background='aqua', command=lambda:about())
    popup.add_separator(background='lightgray')
    popup.add_command(label="Exit Program", background='aqua', command=lambda:end())
    root.bind("<Button-3>", menu_popup)
    root.update()
    root_start.set(False)
    plot()
    root.mainloop()
