import datetime
import logging
import os

import matplotlib as mpl 
if os.environ.get('DISPLAY','') == '':
    mpl.use('Agg')
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D

logger = logging.getLogger(__name__)

def plot(session_data, cumulative_data: list):
    """ 
    Creates an inter-session report with the data from 
    all previous sessions. 
    """
    def marker_color(stage_nums: list) -> list:
        """
        Returns a list of strings, each string representing a color for the marker 
        of a session. The colors indicate the session's stage.
        """
        default_color = 'black'
        marker_color = []
        # Colors for the different stages, 1 to 6. If the stage number 
        # is higher, the marker will be painted gold. Default color is black
        # (for those sessions where stage number was not specified).
        colors = ['blue', 'green', 'red', 'purple', 'orange', 'dodgerblue', 'violet']
        for number in stage_nums:
            if number is None:
                marker_color.append(default_color)
            elif np.isnan(number):
                marker_color.append(default_color)
            else:
                try:
                    marker_color.append(colors[number])
                except IndexError:
                    marker_color.append('gold')
        return marker_color

    def parse_dates(date_list: list) -> list:
        """
        Receives a list of all the dates in the session list and returns the same
        dates in a python date format and with the offset removed so that the
        first session is the zero (1) on the graph.
        """
        date_nums = []
        # First translate the dates into datetime objects:
        for elem in date_list:
            if "/" in elem: # This date contains time and day
                date_nums.append(datetime.datetime.strptime(
                    elem, "%Y-%m-%d/%H:%M:%S"))
            else: # This string only contains the day
                date_nums.append(datetime.datetime.strptime(
                    elem, "%Y-%m-%d"))
        # Translate dates into numbers for the plot:
        num_dates = [mdates.date2num(elem) for elem in date_nums]
        # The first date marks the start of the plot axis (1):
        offset = [elem - num_dates[0] + 1 for elem in num_dates]        

        return offset

    curve_indices = []
    response_times_plot = False
    
    # Calculate whether we will need some of the plots:
    for elem in cumulative_data:
        if not np.isnan(elem.get('response_time')):
            response_times_plot = True
            break

    # Calculate % of invalid trials for the first plot:
    invalids_per_cent = [round(elem.get('invalid_trials') / elem.get('trial_num'), 2) if not np.isnan(elem.get('invalid_trials')) else np.nan for elem in cumulative_data]

    # curve_indices contains the index of those plots that will need
    # a psych curve:
    for i, elem in enumerate(cumulative_data):
        if elem.get('xdata') is not None:
            curve_indices.append(i)

    logger.info("Starting inter-session report.")
    
    with PdfPages(session_data.metadata.subject_name + '_inter_session.pdf') as pdf:

        # Obtain the x-axis from the dates:
        dates = [session['day'] for session in cumulative_data]
        x_axis = parse_dates(dates)        

        # Give a bit of margin to the x-axis:
        higher_date = np.amax(x_axis)
        if higher_date <= 30:
            x_limit = 35
        else:
            x_limit = higher_date + 2
        
        # Labels for all the plots (x-axis) on first page,
        # showing a label every 5 sessions but showing all session ticks
        xlabels = [str(elem) if not elem % 5 else "" for elem in range(1, len(x_axis))]
        xlabels = ["1"] + xlabels

        # START OF FIRST PAGE
        # --------------------- Accuracy plot: -------------------------------------

        plt.figure(figsize=(11.7, 8.3)) # A4

        axes1 = plt.subplot2grid((4,8), (0,0), colspan=7)
        axes1.set_xlim([0, x_limit])
        axes1.set_ylim([0, 1.1])
        axes1.set_yticks(list(np.arange(0, 1.1, 0.1)))
        axes1.set_yticklabels(['0', '', '','','','50', '','','','','100'], fontsize=8)
                
        # Obtain the correct marker colors, if the stage numbers are available:
        total_color = marker_color(
            [session.get('stage_number') for session in cumulative_data])

        # Scatter and plot for total accuracy (black):
        total_acc = [session['total_perf'] for session in cumulative_data]
        axes1.plot(x_axis, total_acc, color = 'black', linewidth=0.7, zorder=1)
        axes1.scatter(x_axis, total_acc, c=total_color, s=3, zorder=2)    
        # Scatter and plot for right side performance:
        right_acc = [session['R_perf'] for session in cumulative_data]
        axes1.scatter(x_axis, right_acc, c=total_color, s=3, zorder=2)
        axes1.plot(x_axis, right_acc, color='magenta', linewidth=0.7, zorder=1)        
        # Scatter and plot for left side performance:
        left_acc = [session['L_perf'] for session in cumulative_data]
        axes1.scatter(x_axis, left_acc, c = total_color, s=3, zorder=2)
        axes1.plot(x_axis, left_acc, color = 'cyan',  linewidth=0.7, zorder=1)
        axes1.set_ylabel("Accuracy [%]", fontsize=9) 
        # Scatter and plot for invalid trials:
        axes1.scatter(x_axis, invalids_per_cent, c=total_color, s=3, zorder=2)
        axes1.plot(x_axis, invalids_per_cent, color='gray', zorder=1, linewidth=0.7, linestyle='dashed')

        # Remove the frame:
        axes1.spines['right'].set_visible(False)
        axes1.spines['top'].set_visible(False)
        # Do the custom legend:
        plt.text(0.1, 0.95, "Subject name: " + session_data.metadata.subject_name, fontsize=8, transform=plt.gcf().transFigure)
        legend_elements = [Line2D([0], [0],color='black', label='Total'),
        Line2D([0], [0], color='cyan', label='Left'),
        Line2D([0], [0], color='magenta', label='Right'),
        Line2D([0], [0], color='gray', label='Inv %', linestyle = 'dashed')]
        leg = plt.legend(handles=legend_elements, ncol=1, prop={'size': 7}, bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
        leg.get_frame().set_alpha(0.5) 
        plt.xticks(x_axis, xlabels, fontsize=8)
        
        # --------------------- Valid trials plot: --------------------------------

        axes4 = plt.subplot2grid((4,8), (1,0), colspan=7)   
        axes4.set_xlim([0,x_limit])
        plt.yticks(fontsize = 8)
        valid_trials = [session['trial_num'] - session['invalid_trials'] if not np.isnan(session['invalid_trials']) else session['trial_num'] for session in cumulative_data]
        max_value = np.amax([x if not np.isnan(x) else -1 for x in valid_trials])
        if max_value < 100:
            max_value = 100
        else:
            max_value = (max_value // 100) * 100 + 200
        axes4.set_ylim([0,max_value])
        
        axes4.plot(x_axis, valid_trials, color='black', linewidth=0.7, zorder=1)
        axes4.scatter(x_axis, valid_trials, c=total_color, s=3, zorder=2)
        axes4.set_ylabel('Valid trials', fontsize=9)
        if not curve_indices and not response_times_plot:
            axes4.set_xlabel("Session") 
        axes4.spines['right'].set_visible(False)
        axes4.spines['top'].set_visible(False)
        plt.xticks(x_axis, xlabels, fontsize=8)
        
        plot_number = 2

        # --------------------- Coherences 1 and -1 plot: -------------------------
        if curve_indices:
            
            coh_neg = []
            coh_pos = []
            
            for elem in cumulative_data:
                ydata = elem.get('ydata')
                if ydata is None:
                    coh_neg.append(np.nan)
                    coh_pos.append(np.nan)
                else:
                    coh_neg.append(1-ydata[0])
                    coh_pos.append(ydata[-1])
         
            axes2 = plt.subplot2grid((4,8), (plot_number,0), colspan=7)
    
            axes2.set_xlim([0, x_limit])
            axes2.set_ylim([0, 1.1])
            axes2.set_yticks(list(np.arange(0, 1.1, 0.1)))
            axes2.set_yticklabels(['0', '', '','','','50', '','','','','100'], fontsize = 8)
            if not response_times_plot:
                axes2.set_xlabel("Session") 

            axes2.plot(x_axis, coh_neg, color = 'cyan', linewidth=0.7, zorder = 1)
            axes2.scatter(x_axis, coh_neg, c = total_color, s = 3, zorder = 2)

            axes2.plot(x_axis, coh_pos, color = 'magenta', linewidth=0.7, zorder = 1)
            axes2.scatter(x_axis, coh_pos, c = total_color, s = 3, zorder = 2)

            axes2.spines['right'].set_visible(False)
            axes2.spines['top'].set_visible(False)
            axes2.set_ylabel('Acc. Coh = 1, -1 [%]', fontsize = 9)
            
            plt.xticks(x_axis, xlabels, fontsize = 8)

            plot_number += 1
        
        # --------------------- Response times plot: --------------------------------
        if response_times_plot:

            axes3 = plt.subplot2grid((4,8), (plot_number,0), colspan=7)

            axes3.set_xlim([0,x_limit])
            aux = [session['response_time'] for session in cumulative_data]
            max_value = np.amax([x if not np.isnan(x) else -1 for x in aux])
            if max_value < 400:
                axes3.set_ylim([0,500])
            else:
                axes3.set_ylim([0,max_value+100])
        
            response_time = [session['response_time'] for session in cumulative_data]
            axes3.plot(x_axis, response_time, color='black', linewidth=0.7, zorder=1)
            axes3.scatter(x_axis, response_time, c=total_color, s=3, zorder=2)
            axes3.set_ylabel('Response time [ms]', fontsize=9)
            axes3.set_xlabel('Session')
            axes3.spines['right'].set_visible(False)
            axes3.spines['top'].set_visible(False)
            plt.yticks(fontsize = 8)
            plt.xticks(x_axis, xlabels, fontsize = 8)

        plt.tight_layout()
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close() 

        # START OF SECOND PAGE
        # --------------------- Psychometric curves: --------------------------------
        # Psychometric plots in A4 paper, landscape, 12 plots a page.
        # Only the last 12 sessions.

        if curve_indices:        
            sessions_with_curve = []
            for elem in curve_indices:
                sessions_with_curve.append(cumulative_data[elem])  
            last_twelve = sessions_with_curve[-12:]
            curve_indices = curve_indices[-12:]             
            for ii, session in enumerate(last_twelve):
                if ii == 0:
                    plt.figure(figsize=(11.7, 8.3))
                plt.subplot2grid((3,4), ((ii % 12) // 4, ii % 4), colspan=1)
                params = session.get('params')
                if params is not None:
                    S, B, LR_L, LR_R = params
                    plt.annotate("S = " + str(round(S, 2)) + "\n" + "B = " +
                             str(round(B, 2))+ "\n" + "LR_L = " + 
                             str(round(LR_L, 2))+ "\n" +"LR_R = " + 
                             str(round(LR_R, 2)), xy =(0,0), xytext = (-1,0.81), fontsize = 6 )
                plt.plot(np.linspace(-1,1,30), session['fit'], linewidth=0.8, c = 'black')
                plt.errorbar(session['xdata'],
                             session['ydata'], 
                             yerr=session['err'], fmt='ro', markersize = 2, elinewidth = 0.7)
                plt.plot([0,0], [0, 1], 'k-', lw=1, linestyle=':')
                plt.plot([-1, 1], [0.5, 0.5], 'k-', lw=1, linestyle=':')
                plt.tick_params(axis = 'both', labelsize=7.5)
                plt.xlim([-1.05, 1.05])
                plt.ylim([-0.05,1.05])
                plt.xlabel('Evidence', fontsize = 8)
                if ii % 4 == 0: plt.ylabel('Probability of right', fontsize = 8)
                plt.title(' '.join((session['day'], '(Session', str(
                    curve_indices[ii]+1) + ')')), fontsize =8)
                if len(last_twelve) - 1 == ii: # If we finished the page or we reached the last plot
                    plt.tight_layout()
                    plt.subplots_adjust(left = 0.1, right = 0.9, bottom = 0.1, top = 0.9)
                    pdf.savefig(plt.gcf())  # saves the current figure into a pdf page
                    plt.close()
