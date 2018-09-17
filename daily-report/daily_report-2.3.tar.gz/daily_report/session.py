import logging
from collections import namedtuple

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Some custom exceptions:

class RewardSideNotFound(Exception):
    pass

class EmptySession(Exception):
    pass
# ------------------------------------------------------------------------------

class Session:
    """
    This class is a data holder for a single animal training session, designed to 
    parse a CSV coming from a BPOD device. It contains the following public attributes:
        · metadata (namedtuple): information about the session, like animal name, date, 
                                 stage number, etc.
        · raw_data (namedtuple): data and vectors extracted directly from the CSV file.
        · performance (namedtuple): calculations relative to the performance of the animal.
        · psych_curve (namedtuple): if applicable, contains the data relative to the
                                    psychometric curve that fits the session.
        · poke_histogram (np.array): contains data to plot a center poke time histogram.
    It also contains the following properties:
        · has_poke_histogram
        · has_psych_curve
        · has_response_time
    which return a boolean.
    """

    # Named tuples to contain the data:
    performance = namedtuple('performance', 
                            ['valids_total',
                            'valids_R', 
                            'valids_L',
                            'corrects_total',
                            'corrects_R', 
                            'corrects_L',
                            'valids_R_per_cent',
                            'valids_L_per_cent',
                            'corrects_per_cent',
                            'corrects_R_per_cent',
                            'corrects_L_per_cent',
                            'absolute_total',
                            'absolute_R', 
                            'absolute_L',
                            'ra_total', 
                            'ra_R', 
                            'ra_L',
                            'water', 
                            'invalids_total',
                            'invalids_per_cent'])

    metadata = namedtuple('metadata', 
                            ['box', 
                            'session_name', 
                            'subject_name', 
                            'time', 
                            'day',
                            'stage_number'])

    raw_data = namedtuple('raw_data', 
                            ['hithistory', 
                            'reward_side',
                            'response_time', 
                            'coherences',
                            'stimulus_duration',
                            'transitions', 
                            'invalid_indices',
                            'valid_indices',
                            'R_indices',
                            'L_indices',
                            'R_values',
                            'L_values'])    

    psych_curve = namedtuple('psych_curve',
                            ['xdata', 
                            'ydata', 
                            'fit', 
                            'params', 
                            'err'])

    def __init__(self, path):
        self._path = path
        self._df = None #  holds the pandas dataframe
        self._length = None 
        self.has_invalids = True
        # Four namedtuples which contain the main pieces of session information:
        self.metadata = None  
        self.raw_data = None
        self.performances = None
        self.psych_curve = None
        self.poke_histogram = None    

        # Read the dataframe and populate the namedtuples:
        self._read_dataframe()
        self._compute_metadata()
        self._compute_raw_data()
        self._compute_performances()  
        if self.has_psych_curve:
            self._compute_psych_curve()
        if self.has_cpoke_histogram:
            self._compute_histogram()

    def __len__(self):
        """
        Returns the total number of trials (valids and invalids) of the session.
        """
        return self._length

    def _read_dataframe(self):
        """
        Take the path of a CSV file and read it as a pandas dataframe.
        """
        try:
            dataframe = pd.read_csv(self._path, skiprows=6, sep=';')
        except FileNotFoundError:
            logger.critical("Error: CSV file not found. Exiting...")
            raise
        else:
            self._df = dataframe

    def _compute_metadata(self):
        """
        This function extracts metadata from the pandas dataframe and saves it into 
        a namedtuple. 
        """

        try:
            box = self._df[self._df.MSG == 'SETUP-NAME']['+INFO'].iloc[0]
        except IndexError:
            box = "Unknown box"
            logger.warning("Box name not found.")
            
        try:
            session_name = self._df[self._df.MSG == 'SESSION-NAME']['+INFO'].iloc[0]
        except IndexError:
            session_name = "Unknown session"
            logger.warning("Session name not found. Saving as 'Unknown session'.")

        try:
            subject_name = self._df[self._df.MSG == 'SUBJECT-NAME']['+INFO'].iloc[0]
            subject_name = subject_name[1:-1].split(',')[0].strip("'")
        except IndexError:
            subject_name = "Unknown subject"
            logger.warning("Subject name not found.")
            
        try:
            session_started = self._df[self._df.MSG == 'SESSION-STARTED']['+INFO'].iloc[0]
            date = session_started.split() #  f.e. ['2018-08-13', '11:25:18.238172']
            time = date[1][0:8]
            day = date[0]
        except IndexError:
            time = "??"
            day = "??"
            logger.warning("Session start time not found.")
            
        try:
            stage_number = self._df[self._df.MSG == 'STAGE_NUMBER']['+INFO'].iloc[0]
            stage_number = int(stage_number)
        except IndexError:
            stage_number = np.nan
            logger.warning("Stage number not found.")

        self.metadata = Session.metadata(box=box, 
                                        session_name=session_name, 
                                        subject_name=subject_name,
                                        time=time, 
                                        day=day,
                                        stage_number=stage_number)

        logger.info(f"{subject_name}, ({day} - {time})")
        logger.info("Session metadata loaded.")


    def _compute_raw_data(self):
        """
        Extracts the main vectors and data from the CSV file: reward_side,
        hithistory, session length, response time, coherences and transition 
        information (for the poke histogram).
        """

        # -----------------------------------------------------------------------------
        # Extract the main states of the session. They contain a value if the trial passed
        # through that state, NaN otherwise. Here, the main states are punish,
        # invalids and reward.

        punish_data = self._df.query("TYPE=='STATE' and MSG=='Punish'")['BPOD-FINAL-TIME'].astype(float)
        invalids = self._df.query("TYPE=='STATE' and MSG=='Invalid'")['BPOD-FINAL-TIME'].astype(float)
        reward_data = self._df.query("TYPE=='STATE' and MSG=='Reward'")['BPOD-FINAL-TIME'].astype(float)

        # Since the state machines are designed so that the main states are mutually exclusive in a single trial, we 
        # can compute the total session length as the sum of all the values that are not NaN:
        self._length = punish_data.dropna().size + reward_data.dropna().size + invalids.dropna().size

        if not self._length:
            raise EmptySession("Session results not found; report can't be generated. Exiting...")

        invalid_indices = np.where(~np.isnan(invalids))[0]
        valid_indices = np.where(np.isnan(invalids))[0]

        if not invalid_indices.size and not valid_indices.size:
            self.has_invalids = False

        # Compute hithistory vector; it will now contain True if the answer 
        # was correct, False otherwise:
        hithistory = np.isnan(punish_data.values)[:self._length]

        # -----------------------------------------------------------------------------
        # REWARD_SIDE contains a 1 if the correct answer was the (R)ight side, 0 otherwise.
        # It is received as a string from the CSV: "[0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1]"...
        # and there can be more than one in the file. We always take THE LAST (iloc[-1]).
        try:
            reward_side_str = self._df[self._df.MSG == "REWARD_SIDE"]['+INFO'].iloc[-1][1:-1].split(',')[:self._length]
        except IndexError: #  Compatibility with old files, when REWARD_SIDE was called VECTOR_CHOICE.
            logger.warning("REWARD_SIDE vector not found. Trying old VECTOR_CHOICE...")
            try:
                reward_side_str = self._df[self._df.MSG == 'VECTOR_CHOICE']['+INFO'].iloc[-1][1:-1].split(',')[:self._length]
            except IndexError:
                raise RewardSideNotFound("Neither REWARD_SIDE nor VECTOR_CHOICE found. Exiting...")
        else:
            # Cast to int from str:
            reward_side = np.array(reward_side_str, dtype=int)
        
        # Indices of left and right trials, omitting invalid trials:
        R_indices = np.where(np.delete(reward_side, invalid_indices))[0]
        L_indices = np.where(np.delete(reward_side, invalid_indices) == 0)[0]
        # Contains 1 for correct and valid trials, 0 otherwise, only for right side:
        R_values = np.take(hithistory, R_indices)
        # Same for left side:
        L_values = np.take(hithistory, L_indices)

        # -----------------------------------------------------------------------------
        # Response times for the session and their mean:
        response_time = self._df[self._df.MSG == "WaitResponse"]['+INFO'].values[:self._length].astype(float)
        
        if response_time.size:
            if self.has_invalids:
                # Don't take invalid trials into account:
                response_time = np.delete(response_time, invalid_indices)
            # Take NaNs out:
            response_time =  response_time[~np.isnan(response_time)]
            # Remove outliers higher than 1 second or negative:
            response_time = response_time[(response_time > 0) & (response_time < 1)]
            # Convert to ms and return an int:
            response_time = int(np.mean(response_time) * 1000) 
        else:
            logger.warning("No response time found, it is undefined from now on.")

        # -----------------------------------------------------------------------------
        # coherences vector, from 0 to 1 (later it will be converted 
        # into evidences from -1 to 1):
        coherences =  self._df[self._df['MSG'] == 'coherence01']['+INFO'].values[:self._length].astype(float)
        # Delete invalid trials:
        coherences = np.delete(coherences, invalid_indices)
        if not coherences.size:
            logger.warning("This trial doesn't use coherences.")  

        # -----------------------------------------------------------------------------
        # Stimulus duration section, not needed for now.
        """
        startSound = df.query("TYPE == 'STATE' and MSG == 'StartSound'")['+INFO'].values[:length]

        if startSound.size:
            startSound = [round(float(elem) * 1000, 1) for elem in startSound]
        else:
            startSound = []

        # Stimulus duration for the staircase plot inside the daily report:
        stimulus_duration = df.query("TYPE == 'STATE' and MSG=='KeepSoundOn'")['+INFO'].values[:length]
        if not stimulus_duration.size:
            logger.info("Stimulus duration info not found.")
            stimulus_duration = []
        else:
            stimulus_duration = parse_stimulus_duration(stimulus_duration)
            if startSound.size:
                stimulus_duration = list(map(sum, zip(stimulus_duration, startSound)))
        """
        stimulus_duration = []    

        # -----------------------------------------------------------------------------
        # Transition information for the daily report histogram, if available:

        trans = self._df[self._df.TYPE=='TRANSITION'].copy(deep=True)
        if trans.size:
            trans['fixtime'] = np.nan
            trans=trans.reset_index()
            trans.drop(['index'], axis=1, inplace=True)
        else:
            logger.warning("Transition information not found.")

        # -----------------------------------------------------------------------------
        # Now that we have calculated all the indices, we can remove the invalids
        # from reward_side and hithistory:
        hithistory = np.delete(hithistory, invalid_indices)
        reward_side = np.delete(reward_side, invalid_indices)

        self.raw_data = Session.raw_data(hithistory=hithistory, 
                                        reward_side=reward_side, 
                                        response_time=response_time, 
                                        coherences=coherences, 
                                        stimulus_duration=stimulus_duration, 
                                        transitions=trans, 
                                        invalid_indices=invalid_indices,
                                        valid_indices=valid_indices,
                                        R_indices=R_indices,
                                        L_indices=L_indices,
                                        R_values=R_values,
                                        L_values=L_values)

        logger.info("Session raw data loaded.")


    def _compute_performances(self):
        """ 
        Computes information relative to performances. We have three main categories:
        total performance, left performance, and right performance. For each of these, 
        we need two pieces of information: the absolute performance (as % of valid trials) 
        and the windowed (20 samples) performance. We also compute here useful percentages.
        """

        def compute_window(data):
            """ 
            Computes a rolling average with a length of 20 samples.
            """
            performance = []
            for i in range(len(data)):
                if i < 20: 
                    performance.append(round(np.mean(data[0:i+1]), 2))
                else:
                    performance.append(round(np.mean(data[i-20:i]), 2))

            return performance
        
        percentage = lambda part, total: np.around(part * 100 / total, 1)
        
        # For the performance display, take into account that invalid trials do not count towards
        # overall performance; hence, the indices of the valid trials must be tracked for the displays
        # and calculations.

        # Total number of invalid trials:
        invalids_total = len(self.raw_data.invalid_indices)
        # Total number of valid trials:
        valids_total = len(self) - invalids_total
        valids_R = len(self.raw_data.R_values)
        valids_L = valids_total - valids_R
        # Total number of correct trials:
        corrects_total = np.count_nonzero(self.raw_data.hithistory)
        corrects_R = np.count_nonzero(self.raw_data.R_values)
        corrects_L = corrects_total - corrects_R
        # Percentage calculation. Invalids % is relative to total trials; valids on R and L and total
        # corrects are relative to total valids; corrects on R and L are relative to valids on R and L.
        invalids_per_cent = percentage(invalids_total, len(self))
        valids_R_per_cent = percentage(valids_R, valids_total)
        valids_L_per_cent = percentage(valids_L, valids_total)
        corrects_per_cent = percentage(corrects_total, valids_total) # AKA, accuracy
        corrects_R_per_cent = percentage(corrects_R, valids_R)
        corrects_L_per_cent = percentage(corrects_L, valids_L)
        # Total (absolute) performances:
        absolute_total = np.around(np.mean(self.raw_data.hithistory), 2)
        absolute_R = np.mean(self.raw_data.R_values)
        absolute_L = np.mean(self.raw_data.L_values)        
        # Rolling averages:
        ra_total = compute_window(self.raw_data.hithistory)
        ra_R = compute_window(self.raw_data.R_values)
        ra_L = compute_window(self.raw_data.L_values)

        # Each correct trial implies 24 uL of water; we display it in mL in the report:
        water = np.around(corrects_total * 0.024, 3)
        
        # Save the data in the biggest namedtuple you've ever seen:
        self.performance = Session.performance(valids_total=valids_total,
                                               valids_R=valids_R, 
                                               valids_L=valids_L,
                                               corrects_total=corrects_total,
                                               corrects_R=corrects_R, 
                                               corrects_L=corrects_L,
                                               valids_R_per_cent=valids_R_per_cent,
                                               valids_L_per_cent=valids_L_per_cent,
                                               corrects_per_cent=corrects_per_cent,
                                               corrects_R_per_cent=corrects_R_per_cent,
                                               corrects_L_per_cent=corrects_L_per_cent,
                                               absolute_total=absolute_total,
                                               absolute_R=absolute_R, 
                                               absolute_L=absolute_L,
                                               ra_total=ra_total, 
                                               ra_R=ra_R, 
                                               ra_L=ra_L,
                                               water=water, 
                                               invalids_total=invalids_total,
                                               invalids_per_cent=invalids_per_cent)

        logger.info("Session performances loaded.")

    def _compute_psych_curve(self):
        """
        If the session has coherences, this method will fit a psychometric curve.
        """

        def sigmoid_MME(fit_params: tuple):
            """
            This function is used by the minimizer to compute the fit parameters.
            """
            k, x0, B, P = fit_params
            # Function to fit:
            yPred = B + (1 - B - P)/(1 + np.exp(-k * (xdata - x0)))
            # Calculate negative log likelihood:
            LL = - np.sum(stats.norm.logpdf(ydata, loc=yPred))

            return LL
        
        evidences = self.raw_data.coherences * 2 - 1
        # R_resp contains True if the response was on the right side, whether correct or incorrect.
        R_resp = np.logical_not(np.logical_xor(self.raw_data.reward_side, self.raw_data.hithistory))
        a = {'R_resp': R_resp, 'evidence': evidences, 'coh': self.raw_data.coherences}
        coherence_dataframe = pd.DataFrame(a)

        info = coherence_dataframe.groupby(['evidence'])['R_resp'].mean()
        ydata = [np.around(elem, 3) for elem in info.values]
        xdata = info.index.values
        err = [np.around(elem, 3) for elem in coherence_dataframe.groupby(['coh'])['R_resp'].sem().values]

        # Run the minimizer:
        LL = minimize(sigmoid_MME, [1, 1, 0, 0])
        
        # Fit parameters:
        k, x0, B, P = LL['x']
        # Compute the fit with 30 points:
        fit = B + (1 - B - P)/(1 + np.exp(-k * (np.linspace(-1, 1, 30) - x0)))
        fit = [np.around(elem, 3) for elem in fit]

        self.psych_curve = Session.psych_curve(xdata=xdata, 
                                            ydata=ydata,
                                            fit=fit, 
                                            params=LL['x'],
                                            err=err)

        logger.info("Session psychometric curve done loaded.")

    def _compute_histogram(self):
        """
        Uses a dataframe made with the TRANSITION rows to compute the necessary
        values for a centerpoke time histogram.
        """
        transition_df = self.raw_data.transitions
        for index in self.raw_data.transitions[:-2].index:
            try:
                if transition_df.loc[index, 'MSG'] == 'Fixation' and transition_df.loc[index+1, 'MSG'] == 'Invalid':
                    transition_df.loc[index, 'fixtime'] = transition_df.loc[index+1, 'BPOD-INITIAL-TIME'] - transition_df.loc[index, 'BPOD-INITIAL-TIME']
                elif transition_df.loc[index, 'MSG'] == 'Fixation':
                    transition_df.loc[index, 'fixtime'] = transition_df.loc[index+2, 'BPOD-INITIAL-TIME'] - transition_df.loc[index, 'BPOD-INITIAL-TIME']
            except:
                logger.critical("An error in the histogram ocurred.")
                raise
        transition_df['fixtime'] *= 1000
        # remove outliers
        toplot = transition_df['fixtime'].dropna().values
    
        self.poke_histogram = toplot

        logger.info("Session transition information loaded.")

    @property
    def has_psych_curve(self) -> bool:
        return bool(self.raw_data.coherences.size)

    @property
    def has_cpoke_histogram(self) -> bool:
        return bool(self.raw_data.transitions.size)
    
    @property
    def has_response_time(self) -> bool:
        return bool(self.raw_data.response_time)
