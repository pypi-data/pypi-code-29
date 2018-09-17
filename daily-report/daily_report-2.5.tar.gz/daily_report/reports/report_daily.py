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

# Plot parameters:
MARKERSIZE = 2
LINEWIDTH = .7
LABELSIZE = 9
FONTSIZE = 10

def plot(session_data, cumulative_data: list):
    """ Creates a daily report with the performance and psychometric plots, if necessary. """    
    
    logger.info("Starting daily report.")

    with PdfPages(session_data.metadata.session_name + '.pdf') as pdf:
            plt.figure(figsize=(11.7, 8.3))

            # ---------------------- First plot: rolling averages of performances -------------------------------------
            
            axes1 = plt.subplot2grid((2,3), (0,0), colspan=3)
            axes1.set_ylim([0,1.1])
            axes1.set_yticks(list(np.arange(0,1.1, 0.1)))
            axes1.set_yticklabels(['0', '', '','','','50', '','','','','100'])
            axes1.plot( range(len(session_data.performance.ra_total)), session_data.performance.ra_total, 
                        marker = 'o', markersize=MARKERSIZE, color='black', linewidth=LINEWIDTH)
            if session_data.raw_data.L_indices.size:
                axes1.plot(session_data.raw_data.L_indices, session_data.performance.ra_L, 
                            marker = 'o', markersize=MARKERSIZE, color='cyan', linewidth=LINEWIDTH)
            if session_data.raw_data.R_indices.size:
                axes1.plot(session_data.raw_data.R_indices, session_data.performance.ra_R, 
                            marker = 'o', markersize=MARKERSIZE, color='magenta', linewidth=LINEWIDTH)
            axes1.set_xlim([1, len(session_data) + 1])
            axes1.set_ylabel('Accuracy [%]')
            axes1.set_xlabel('Trials')
            axes1.yaxis.set_tick_params(labelsize=LABELSIZE)
            axes1.xaxis.set_tick_params(labelsize=LABELSIZE)
            axes1.spines['right'].set_visible(False)
            axes1.spines['top'].set_visible(False)
            # Custom legend:
            legend_elements = [Line2D([0], [0],color='black', label='Total'),
            Line2D([0], [0], color='cyan', label='Left'),
            Line2D([0], [0], color='magenta', label='Right')]
            leg = plt.legend(loc="lower right", handles=legend_elements, ncol=1, prop={'size': 8})
            leg.get_frame().set_alpha(0.5)

            # ---------------------------- Upper text -----------------------------------------------------------------
            if session_data.has_response_time:
                response_time_str = f"{session_data.raw_data.response_time} ms"
            else:
                response_time_str = "Not taken into account"

            if session_data.raw_data.L_indices.size:
                L_corrects_str = f"Corrects on left: {session_data.performance.corrects_L} " \
                                f"({session_data.performance.corrects_L_per_cent} %)"
            else:
                L_corrects_str = f"Corrects on left: N/A"
            
            if session_data.raw_data.R_indices.size:
                R_corrects_str = f"Corrects on right: {session_data.performance.corrects_R} " \
                                f"({session_data.performance.corrects_R_per_cent} %)"
            else:
                R_corrects_str = f"Corrects on right: N/A"
               
            if session_data.has_invalids:
                invalid_trials_str = f"{session_data.performance.invalids_total} ({session_data.performance.invalids_per_cent} %)"
            else:
                invalid_trials_str = "Not taken into account"
                
            s1 = f"Date: {session_data.metadata.day} {session_data.metadata.time}\n" 
            s2 = f"Subject name: {session_data.metadata.subject_name}\n" 
            s3 = f"Valid trials: {session_data.performance.valids_total} / Accuracy: {session_data.performance.corrects_per_cent} % / {L_corrects_str} / {R_corrects_str} / Invalid trials: {invalid_trials_str}\n"
            s4 = f"Water: {session_data.performance.water} mL / Mean response time: {response_time_str}"
            
            plt.text(0.1, 0.90, s1+s2+s3+s4, fontsize=8, transform=plt.gcf().transFigure)
            
            # ---------------------- Second plot: cpoke histogram ----------------------------------------------------

            if session_data.has_cpoke_histogram:
                axes3 = plt.subplot2grid((2,3),(1,0), colspan=2)
                axes3.hist(session_data.poke_histogram[np.where(session_data.poke_histogram < 1001)], bins=50)
                axes3.set_xlim([0,900])
                axes3.axvline(x=300, color='r', linestyle=':')
                axes3.set_title("Center poke time", fontsize=FONTSIZE)
                axes3.set_xlabel("Time [ms]")
                axes3.yaxis.set_tick_params(labelsize=LABELSIZE)
                axes3.xaxis.set_tick_params(labelsize=LABELSIZE)

            # ---------------------- Third plot: psychometric curve ---------------------------------------------------
            
            if session_data.has_psych_curve:
                if session_data.has_cpoke_histogram:
                    axes2 = plt.subplot2grid((2,3), (1,2), colspan=1)
                else:
                    axes2 = plt.subplot2grid((2,3), (1,1), colspan=1)
                axes2.plot([0,0], [0, 1], 'k-', lw=1, linestyle=':')
                axes2.plot([-1, 1], [0.5, 0.5], 'k-', lw=1, linestyle=':')
                axes2.errorbar(session_data.psych_curve.xdata, session_data.psych_curve.ydata, 
                                yerr=session_data.psych_curve.err, fmt='ro', elinewidth=1, markersize=3)
                axes2.plot(np.linspace(-1,1,30), session_data.psych_curve.fit, color='black', linewidth=1)
                axes2.set_yticks(np.arange(0, 1.1, step=0.1))
                axes2.set_xlabel('Evidence')
                axes2.set_ylabel('Probability of right')
                axes2.set_xlim([-1.05, 1.05])
                axes2.yaxis.set_tick_params(labelsize=9)
                axes2.xaxis.set_tick_params(labelsize=9)
                axes2.set_ylim([-0.05,1.05])
                axes2.tick_params(labelsize=9)
                axes2.annotate(str(round(session_data.psych_curve.ydata[0] ,2)), xy=(session_data.psych_curve.xdata[0], 
                             session_data.psych_curve.ydata[0]), xytext=(session_data.psych_curve.xdata[0] - 0.03, 
                                       session_data.psych_curve.ydata[0] + 0.05), fontsize=8)
                axes2.annotate(str(round(session_data.psych_curve.ydata[-1], 2)), xy=(session_data.psych_curve.xdata[-1], 
                             session_data.psych_curve.ydata[-1]), xytext=(session_data.psych_curve.xdata[-1] - 0.1, 
                                       session_data.psych_curve.ydata[-1] - 0.08), fontsize=8)
                S, B, LR_R, LR_L = session_data.psych_curve.params
                axes2.annotate("S = " + str(round(S, 2)) + "\n" + "B = " +
                             str(round(B, 2))+ "\n" + "LR_L = " + 
                             str(round(LR_R, 2))+ "\n" +"LR_R = " + 
                             str(round(LR_L, 2)), xy=(0, 0), xytext = (-1, 0.85), fontsize=7)
                plt.tight_layout()
                plt.subplots_adjust(top=0.85, hspace=0.3)
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1)             
            pdf.savefig(plt.gcf())  # saves the current figure into a pdf page
            plt.close()
