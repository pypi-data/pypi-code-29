import multiprocessing
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import configparser
from collections import OrderedDict
import EPIC
from EPIC import sim_objects
from EPIC.cosmology import a_of_z, cosmic_objects as cosmo
from EPIC.utils import io_tools
from EPIC.utils.numbers import speedoflight
from EPIC.utils.plots import make_plots
from EPIC.gui import custom_widgets as EPIC_widgets
import os
from shutil import copy2
from numpy import ceil, logspace, linspace, log10

class Application(object):

    WIDTH = 1257
    MINHEIGHT = 731
    HEIGHT = 781
    LEFT_FRAME_WIDTH = 476
    CORNER_WIDTH = 160
    #BOTTOM_CENTER_FRAME_WIDTH = 182
    BOTTOM_RIGHT_FRAME_HEIGHT = 150
    STATUS_BAR_HEIGHT = 56

    PADX = 10
    PADY = 10
    RIGHT_FRAME_WIDTH = WIDTH-2*PADX-LEFT_FRAME_WIDTH

    IPADX = 4
    IPADY = 4
    default_padding = {'padx': PADX, 'pady': PADY}
    default_xpadding = {'padx': PADX}
    default_ypadding = {'pady': PADY}
    default_ipadding = {'ipadx': IPADX, 'ipady': IPADY}
    default_ixpadding = {'ipadx': PADX}
    default_iypadding = {'ipady': PADY}

    list_of_solved_models = []
    please_select_model = '(Select a model...)'
    please_select_species = '(Select...)'
    please_select_style = 'Plot style'
    models_list_notice = \
            '\n'.join([
                'Models will be added to the',
                'list on the right if you include',
                'Distances. You can double',
                'click any entry to rename it.',
                ])

    distances_to_compare = [
            'Comoving distance $\chi(z)$',
            'Angular diameter $d_A(z)$',
            #'Volume averaged $d_V(z)$',
            'Hubble $d_H(z)$', 
            'Lookback time $c\,t(z)$',
            'Luminosity $d_L(z)$',
        ]

    styles_list = [style.replace('_', ' ') for style \
            in EPIC.pyplot_available_styles]

    mcmc_styles_list = [style.replace('_', ' ') for style \
            in EPIC.pyplot_grid_styles]

    fs_list = range(8, 19, 2)
    tex_options = {}

    texprefix = 'TeX with'
    for mode, av_fonts in [
            ('regular', io_tools.available_fonts),
            ('MCMC', io_tools.pdf_fonts)
            ]:
        tex_options[mode] = ['Do not use TeX']

        for font in av_fonts.keys():
            tex_options[mode].append(' '.join([texprefix, font]))

    matplotlib_fonts = dict(zip(tex_options['regular'], 
        [None, 'Computer Modern Roman', 'Times New Roman', 'Charter',
            'Palatino']))

    tempfile_name = 'temp_ini.ini'

    def __init__(self, run_parser, analyze_parser, plot_parser,
            analyze_function, master=None, theme='clam'):
        self.rccustom()
        self.run_parser = run_parser
        self.analyze_parser = analyze_parser
        self.plot_parser = plot_parser
        self.analyze = analyze_function
        self.master = master
        self.master.title("EPIC's Cosmology Calculator")
        #self.master.minsize(height=self.MINHEIGHT)
        icon = tk.Image("photo", file=os.path.join(EPIC.root, 'gui_files',
            'iconepic.gif'))
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)
        self.frame_bg, self.foreground_text = EPIC_widgets.configure_ttk(
                theme=theme)
        self.master.config(background=self.frame_bg)
        self.create_widgets()

    def rccustom(self):
        try:
            fsize = self.fontsize_choice.var.get()
        except AttributeError:
            fsize = 12

        plt.rcParams.update({
            'grid.linewidth': 0.5,
            'grid.linestyle': '-',
            'font.size': fsize or 12,
        #    'legend.handlelength': 2.2,
        #    'legend.framealpha': 1.0,
        })

    def set_tex_option(self, update_other=True):
        option = self.tex_options['regular'][self.tex_choice.var.get()]
        if option != self.current_tex_option:
            self.current_tex_option = option
            if update_other and option in self.tex_options['MCMC']:
                self.mcmc_tex_choice.var.set(self.tex_options['MCMC'].index(option))
                self.set_mcmc_tex_option(update_other=False)
            if self.texprefix in option:
                plt.rcParams.update({'text.usetex': True})
                font_preamble = io_tools.tex_packages(
                        io_tools.available_fonts[option[len(self.texprefix)+1:]]
                        )
                plt.rcParams.update({
                    'text.latex.preamble': font_preamble,
                    'text.latex.unicode' : True,
                    'text.latex.preview' : True,
                    'font.size': self.fontsize_choice.var.get() or 14,
                    'font.family': 'serif',
                    'font.serif': self.matplotlib_fonts[option]
                    })
                self.remake_plots()
            else:
                # this guarantees tex will be reset to False, since plot_style
                # selection preserves it
                plt.rcdefaults()
                if self.style_choice.var.get() == 0:
                    self.rccustom()
                    self.remake_plots()
                else:
                    self.current_style = -1 #to force remake plots next
                    # this will preserve selected style
                    self.set_chosen_plot_style()

    def set_mcmc_tex_option(self, update_other=True):
        option = self.tex_options['MCMC'][self.mcmc_tex_choice.var.get()]
        if option != self.current_mcmc_tex_option:
            self.current_mcmc_tex_option = option
            if update_other and option in self.tex_options['regular']:
                self.tex_choice.var.set(self.tex_options['regular'].index(option))
                self.set_tex_option(update_other=False)
            self.check_and_remake_mcmc_plot()

    def set_font_size(self, menubutton, otherbutton,
            updating_from_other=True):
        if not updating_from_other:
            current_size = plt.rcParams['font.size'] 
            new_size = getattr(self, menubutton).var.get()
            if new_size != current_size:
                getattr(self, otherbutton).var.set(new_size)
                plt.rcParams['font.size'] = new_size
                self.check_and_remake_mcmc_plot()
                self.remake_plots()

    def check_and_remake_mcmc_plot(self):
        if not getattr(self, 'sim', None):
            return None
        plot_args = self.get_plot_args(autorange=True)
        self.MCMC_output.start()
        print('')
        self.remake_mcmc_plot(plot_args, self.plot_parser, self.sim)
        self.MCMC_output.stop()
    
    def set_chosen_plot_style(self, update_other=True):
        style = self.style_choice.var.get()
        if style != self.current_style:
            self.current_style = int(style)
            style = self.styles_list[style]
            # update the other plots 
            if update_other and style in self.mcmc_styles_list:
                self.mcmc_style_choice.var.set(self.mcmc_styles_list.index(style))
                self.set_mcmc_style(update_other=False)
            preserve_tex_options = dict(
                    (key, plt.rcParams[key]) for key in [
                        'text.usetex',
                        'text.latex.preamble',
                        'text.latex.unicode',
                        'text.latex.preview',
                        'font.family',
                        'font.size'
                        ]
                    )
            plt.rcdefaults()
            plt.style.use(style.replace(' ', '_'))
            self.rccustom()
            plt.rcParams.update(preserve_tex_options)

            self.remake_plots()

    def remake_plots(self):
        self.master.config(cursor='exchange')
        self.master.update()

        viewing = getattr(self, 'viewing', None)
        if viewing == 'plots':
            self.show_densities()
        elif viewing == 'dist':
            self.compare_distances(models=self.all_models,
                    labels=self.all_labels)
        else:
            pass

        self.master.config(cursor='left_ptr')

    def get_plot_args(self, autorange=False):
        plot_args_list = []
        if self.mcmc_tex_choice.var.get():
            plot_args_list.append('--use-tex')
            font = list(io_tools.pdf_fonts.keys())[self.mcmc_tex_choice.var.get()-1]
            plot_args_list.extend(['--font', font])
        if self.png_var.get():
            plot_args_list.append('--png')
        if not autorange:
            plot_args_list.append('--no-auto-range')
        plot_args_list.extend([
                '--font-size', str(self.mcmc_fontsize_choice.var.get()),
                '--levels', *[str(i) for i in range(1, 1+self.CL_var.get())], 
                '--style', self.mcmc_styles_list[self.mcmc_style_choice.var.get()].replace(' ', '_'),
                ])
        plot_args_list = [self.wdir,] + plot_args_list
        plot_args = self.plot_parser.parse_args(args=plot_args_list)
        return plot_args

    def set_mcmc_style(self, update_other=True):
        style = self.mcmc_style_choice.var.get()
        if style != self.current_mcmc_style:
            self.current_mcmc_style = int(style)
            style = self.mcmc_styles_list[style]
            # update the other plots 
            if update_other and style in self.styles_list:
                self.style_choice.var.set(self.styles_list.index(style))
                self.set_chosen_plot_style(update_other=False)
            preserve_tex_options = dict(
                    (key, plt.rcParams[key]) for key in [
                        'text.usetex',
                        'text.latex.preamble',
                        'text.latex.unicode',
                        'text.latex.preview',
                        'font.family',
                        'font.size'
                        ]
                    )
            plt.rcdefaults()
            plt.style.use(style.replace(' ', '_'))
            plt.rcParams.update(preserve_tex_options)
            plt.setp(self.MCMCplot_tab.fig, 'facecolor',
                    plt.rcParams['figure.facecolor'])
            self.check_and_remake_mcmc_plot()

    def remake_mcmc_plot(self, args, parser, sim, include_defaults=False):
        self.master.config(cursor='exchange')
        self.master.update()
        print(' '.join(io_tools.get_parsed_args(args, parser,
            include_defaults=include_defaults, command='plot')))
        make_plots([sim], external_fig=self.MCMCplot_tab, args=args)
        print('Done.')
        self.master.config(cursor='left_ptr')

    def create_widgets(self):
        self.available_models = configparser.ConfigParser()
        self.available_models.read([
            os.path.join(EPIC.root, 'cosmology', 'model_recipes.ini'),
            os.path.join(EPIC.user_folder, 'modifications', 'cosmology',
                'model_recipes.ini'),
            ])
        self.available_species = configparser.ConfigParser()
        self.available_species.read([
            os.path.join(EPIC.root, 'cosmology', 'available_species.ini'),
            os.path.join(EPIC.user_folder, 'modifications', 'cosmology',
                'available_species.ini'),
            ])
        self.models = self.available_models.sections()
        self.models = OrderedDict((model, self.available_models[model]['name']) \
                for model in self.models if 'name' in self.available_models[model])

        # map models label and name
        self.map_model = {self.please_select_model: self.please_select_model}
        for model in self.models:
            if 'name' in self.available_models[model]:
                self.map_model[model] = self.available_models[model]['name'].replace(
                        r'$\Lambda$', 'Λ').replace('$w$CDM', 'wCDM') 
        remap(self.map_model)

        # map parameters label and tex
        self.map_parameters = {'h': 'h', 'H0': 'H_0', 'xi': r'\xi'}
        for section in ['density parameter', 'physical density parameter']:
            for key, par_label in self.available_species[section].items():
                self.map_parameters[par_label] = self.available_species['tex '+ section][key]
        for key, lparams in self.available_species['EoS parameters'].items():
            for par, tex in zip(eval(lparams), eval(self.available_species['tex EoS parameters'][key])):
                self.map_parameters[par] = tex

        # Status bar
        self.status_bar = tk.Label(self.master, bg=self.foreground_text,
                fg='white', anchor=tk.W, relief=tk.FLAT,
                **self.default_padding) 
        self.status_bar.config(text="Welcome to the EPIC's Cosmology Calculator. " \
                + "Choose a model to start, then specify the parameters " \
                + "and make some plots.")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # bottom ttk Notebook
        self.parameters_setup_notebook = ttk.Notebook(self.master,
                height=self.BOTTOM_RIGHT_FRAME_HEIGHT-self.PADY)
        self.parameters_setup_notebook.pack(side=tk.BOTTOM, fill=tk.X, #expand=1,
                **self.default_iypadding, **self.default_padding)

        parameter_space_frame = ttk.Frame(self.parameters_setup_notebook)
        self.parameters_setup_notebook.add(parameter_space_frame,
                text='Specify parameters')

        constrain_parameters_frame = ttk.Frame(self.parameters_setup_notebook)
        self.parameters_setup_notebook.add(constrain_parameters_frame,
                text='Constrain with MCMC')

        self.MCMC_terminal = EPIC_widgets.TwoPanes(self.parameters_setup_notebook, 
                pack=False, orient=tk.HORIZONTAL)
        #self.MCMC_terminal.bind("<Visibility>", self.MCMC_visible)
        self.MCMC_output = EPIC_widgets.ConsoleText(self.MCMC_terminal.main,
                relief=tk.FLAT)
        self.MCMC_output.pack(fill=tk.BOTH, expand=1)

        self.MCMC_simulation_info = {}
        for labelframe, w in [
                ('Acceptance rates', 16),
                ('# of accepted states', 16),
                ('Marginalized fits', 34),
                ]:
            lf = ttk.LabelFrame(self.MCMC_terminal.second, relief=tk.FLAT,
                    text=labelframe+':')
            lf.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, **self.default_padding)
            scrolltext = EPIC_widgets.ScrollableText(lf, width=w,
                    highlightthickness=0, state=tk.DISABLED)
            scrolltext.pack(fill=tk.BOTH, expand=1)
            scrolltext.tag_config('right', justify=tk.RIGHT)
            self.MCMC_simulation_info[labelframe] = scrolltext

        #self.MCMC_simulation_info['Marginalized fits'].tag_config('underlined',
        #        font=('underline',))
        self.parameters_setup_notebook.pack_propagate(False)

        left_frame = ttk.Frame(parameter_space_frame,
                width=self.LEFT_FRAME_WIDTH)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        left_frame.pack_propagate(False)

        left_frame_MCMC = ttk.Frame(constrain_parameters_frame,
                width=self.WIDTH//2 + 20)
        #        #width=self.WIDTH//3 + 90)
        left_frame_MCMC.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.W, expand=1)
        left_frame_MCMC.pack_propagate(False)

        self.parameter_values = ttk.Frame(left_frame)
        self.parameter_values.pack(fill=tk.BOTH, expand=1)

        self.parameter_priors = ttk.LabelFrame(left_frame_MCMC,
                #relief=tk.FLAT, 
                text='Priors  |  Diagonal covariance matrix for proposal function (Multivariate Gaussian)  |  Unit:')
        self.parameter_priors.pack(fill=tk.BOTH, expand=1,
                **self.default_padding)
        self.parameter_priors_baseframe = ttk.Frame(self.parameter_priors)
        self.parameter_priors_baseframe.pack(side=tk.LEFT, fill=tk.X, expand=1)

        datasets_label_frame = ttk.LabelFrame(constrain_parameters_frame,
                text='Datasets:', width=480)
        datasets_label_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1,
                anchor=tk.W, **self.default_padding)
        datasets_label_frame.pack_propagate(False)
        datasets_frame = EPIC_widgets.ScrollableFrame(datasets_label_frame,
                self.frame_bg)
        self.data_cosmic_chrono = tk.IntVar()
        self.data_cosmic_chrono.set(1)
        ttk.Checkbutton(datasets_frame.frame, text='Cosmic chronometer H(z)',
                variable=self.data_cosmic_chrono).pack(anchor=tk.W,
                        **self.default_padding)
        self.data_local_Hubble = tk.IntVar()
        self.data_local_Hubble.set(1)
        ttk.Checkbutton(datasets_frame.frame, text='Hubble local Measurement H(z=0)',
                variable=self.data_local_Hubble).pack(anchor=tk.W,
                        **self.default_padding)
        SNe_frame = ttk.LabelFrame(datasets_frame.frame,
                text='SNe Ia Joint Light-curve Analysis:', relief=tk.FLAT)
        SNe_frame.pack(anchor=tk.W, **self.default_padding)
        self.data_JLA_simple = tk.IntVar()
        self.data_JLA_simple.set(0)
        self.data_JLA_full = tk.IntVar()
        self.data_JLA_full.set(0)
        ttk.Checkbutton(SNe_frame, text='Simple',
                variable=self.data_JLA_simple,
                command=self.sne_simple_toggle).pack(anchor=tk.W)
        self.jla_simple_nuisance_par = EPIC_widgets.PriorLineSetup(SNe_frame,
                'M', 'M', background=self.frame_bg, par_label_width=6,
                cb_width=14, xpadding=self.default_xpadding)
        config_all_widgets(self.jla_simple_nuisance_par.frame, state=tk.DISABLED)

        ttk.Checkbutton(SNe_frame, text='Full',
                variable=self.data_JLA_full,
                command=self.sne_full_toggle).pack(anchor=tk.W)
        self.jla_full_nuisance_pars = [EPIC_widgets.PriorLineSetup(SNe_frame,
            label[0], label[1], row=i, background=self.frame_bg, par_label_width=6,
            cb_width=14, xpadding=self.default_xpadding) for i, label \
                    in enumerate([
                        (r'\alpha', 'alpha'),
                        (r'\beta', 'beta'),
                        ('M_B', 'M_B'),
                        ('\Delta{M}', 'DeltaM'),
                        ])]
        for par in self.jla_full_nuisance_pars:
            config_all_widgets(par.frame, state=tk.DISABLED)

        self.BAO_frame = ttk.LabelFrame(datasets_frame.frame, text='BAO:', relief=tk.FLAT)
        self.BAO_frame.pack(anchor=tk.W, **self.default_padding)
        self.BAO_dict = OrderedDict()
        self.BAO_dict_check = OrderedDict()
        bao_list = [
            '6dF+SDSS_MGS',
            'SDSS_BOSS_CMASS',
            'SDSS_BOSS_LOWZ',
            'SDSS_BOSS_QuasarLyman',
            'SDSS_BOSS_Lyalpha-Forests',
            'SDSS_BOSS_consensus',
            'WiggleZ',
            ]

        for bao_set in bao_list:
            self.BAO_dict[bao_set] = tk.IntVar()
            self.BAO_dict_check[bao_set] = ttk.Checkbutton(self.BAO_frame,
                    text=bao_set, variable=self.BAO_dict[bao_set])
            if bao_set.startswith('SDSS_BOSS'):
                self.BAO_dict_check[bao_set].config(command=self.bao_sdss_boss_toggle)
            elif bao_set == 'WiggleZ':
                self.BAO_dict_check[bao_set].config(command=self.bao_wigglez_toggle)
            self.BAO_dict_check[bao_set].pack(anchor=tk.W)

        self.read_bao_states()
        """
        for bao_set in bao_list:
            self.BAO_dict[bao_set].set(0 if bao_set == 'WiggleZ' else 1)
            if bao_set.startswith('SDSS_BOSS'):
                self.bao_sdss_boss_toggle()
            elif bao_set == 'WiggleZ':
                self.bao_wigglez_toggle()
        """

        self.CMB_frame = ttk.LabelFrame(datasets_frame.frame, 
                text='CMB distance priors:', relief=tk.FLAT)
        self.CMB_frame.pack(anchor=tk.W, **self.default_padding)
        self.data_CMB_LCDM = OrderedDict((
                (2015, tk.IntVar()),
                (2018, tk.IntVar())
                ))
        self.data_CMB_wCDM = OrderedDict((
                (2015, tk.IntVar()),
                (2018, tk.IntVar())
                ))
        self.data_CMB_LCDM_check = OrderedDict((
            (2015, ttk.Checkbutton(self.CMB_frame, text='Planck 2015 ΛCDM',
                variable=self.data_CMB_LCDM[2015],
                command=lambda: self.cmb_lcdm_toggle(2015))),
            (2018, ttk.Checkbutton(self.CMB_frame, text='Planck 2018 ΛCDM',
                variable=self.data_CMB_LCDM[2018],
                command=lambda: self.cmb_lcdm_toggle(2018)))
            ))
        self.data_CMB_wCDM_check = OrderedDict((
            (2015, ttk.Checkbutton(self.CMB_frame, text='Planck 2015 wCDM',
                variable=self.data_CMB_wCDM[2015], 
                command=lambda: self.cmb_wcdm_toggle(2015))),
            (2018, ttk.Checkbutton(self.CMB_frame, text='Planck 2018 wCDM',
                variable=self.data_CMB_wCDM[2018],
                command=lambda: self.cmb_wcdm_toggle(2018)))
            ))
        self.data_CMB_LCDM_check[2015].pack(anchor=tk.W)
        self.data_CMB_wCDM_check[2015].pack(anchor=tk.W)
        self.data_CMB_LCDM_check[2018].pack(anchor=tk.W)
        self.data_CMB_wCDM_check[2018].pack(anchor=tk.W)

        simulation_grid = ttk.Frame(constrain_parameters_frame)
        simulation_grid.pack(anchor=tk.W, fill=tk.BOTH, expand=1,
                **self.default_padding)
        simulation_labelframe = ttk.LabelFrame(simulation_grid,
                text='Simulation:')
        sim_buttons = ttk.Frame(simulation_grid)
        sim_buttons.pack(side=tk.BOTTOM, fill=tk.X, anchor=tk.S, expand=1)
        simulation_labelframe.pack(side=tk.TOP, anchor=tk.N, fill=tk.BOTH,
                expand=1)
        self.load_button = ttk.Button(sim_buttons, text='Load', width=4,
                command=self.load_sim)
        self.load_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.export_ini = ttk.Button(sim_buttons, text='Export', width=4,
                #style='Flat.TButton',
                command=self.export_ini_only)
        self.export_ini.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.MCMC_button = ttk.Button(sim_buttons, text='Start', width=4,
                #style='Flat.TButton',
                command=self.export_ini_and_run_MCMC)
        self.MCMC_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        sim_options_frame = EPIC_widgets.ScrollableFrame(simulation_labelframe,
                background=self.frame_bg, width=147)
        #sim_options_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        nlines = 0
        for (label, attribute, vartype, value, width, values) in [
            ('Tag:', 'tag_var', tk.StringVar, '(optional)', 10, None),
            ('# of chains:', 'chains_var', tk.IntVar,
                multiprocessing.cpu_count(), 4, (2, 128, 1)),
            ('# of steps:', 'steps_var', tk.IntVar, 5000, 5, None),
            ('Check every:', 'check_interval_var', tk.StringVar, 
                io_tools.revert_TimeString(EPIC._defaults_['check_interval']), 5,
                None),
            ('Tolerance:', 'tol_var', tk.DoubleVar,
                EPIC._defaults_['tolerance'], 5, None),
            ('Acc. range:', 'acc_range', tk.DoubleVar,
                EPIC._defaults_['acceptance_limits'], 3, [0, 1]),
            ('Sigma levels:', 'CL_var', tk.IntVar,
                EPIC._defaults_['sigma_levels'][-1], 4, (1, 4, 1)),
            ('# of bins:', 'bins_var', tk.IntVar, EPIC._defaults_['bins'], 4, (10,
                60, 5)),
            ('Save rejected states:', 'rejected_var', tk.IntVar, 0, None, None),
            ('Final plot with KDE:', 'kde_var', tk.IntVar, 1, None, None),
            ('Save .png too:', 'png_var', tk.IntVar, 0, None, None),
            ('Import covariance...', 'cov_loaded', tk.IntVar, 0,
                'proposal_cov_file', 'choose_proposal_cov_file')
            ]:
            nlines += 1
            fr = ttk.Frame(sim_options_frame.frame)
            fr.pack(fill=tk.X, expand=1)
            ttk.Label(fr, text=label).pack(side=tk.LEFT, anchor=tk.W)
            if isinstance(value, list):
                widget = None
                setattr(self, attribute, EPIC_widgets.TwoValues(fr, vartype,
                    value, values, width=width))
            else:
                setattr(self, attribute, vartype())
                getattr(self, attribute).set(value)
            if isinstance(values, tuple):
                from_, to_, delta = values
                widget = tk.Spinbox(fr, from_=from_, to_=to_, increment=delta,
                        width=width-1, textvariable=getattr(self, attribute),
                        buttonbackground=self.frame_bg,
                        buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT)
            elif isinstance(values, str):
                widget = ttk.Checkbutton(
                        fr, text='', variable=getattr(self, attribute),
                        command=getattr(self, values)
                        )
                if isinstance(width, str):
                    setattr(self, width, tk.StringVar())
                    getattr(self, width).set('' if not value else str(value))
            elif isinstance(values, list):
                pass
            else:
                if width is None:
                    widget = ttk.Checkbutton(fr, text='',
                            variable=getattr(self, attribute))
                else:
                    widget = ttk.Entry(fr, width=width, textvariable=getattr(self,
                        attribute))

            if widget:
                widget.pack(side=tk.RIGHT, anchor=tk.E)
        nlines += 1

        mcmcplotcfg = ttk.Frame(sim_options_frame.frame)
        mcmcplotcfg.pack(fill=tk.X, expand=1)

        self.current_mcmc_style = 0
        self.current_mcmc_tex_option = self.tex_options['MCMC'][0]

        for menubtn, text, menutitle, options, current, command, imgfile in [
                ('mcmc_style_choice', 'Style', self.please_select_style,
                    self.mcmc_styles_list, self.current_mcmc_style, self.set_mcmc_style, None),
                ('mcmc_tex_choice', None, 'TeX options',
                    self.tex_options['MCMC'], self.current_mcmc_tex_option,
                    self.set_mcmc_tex_option, 'menu-tex.png'),
                ('mcmc_fontsize_choice', None, 'Font size', self.fs_list, 12,
                    lambda: self.set_font_size('mcmc_fontsize_choice',
                        'fontsize_choice', updating_from_other=False), 'fontsize.png'),
                ]:
            img_path = os.path.join(EPIC.root, 'gui_files', 'images', imgfile) \
                    if imgfile else None
            setattr(self, menubtn, EPIC_widgets.MenuButtonOptions(
                mcmcplotcfg,
                text=text,
                tearoff=0,
                menutitle=menutitle,
                options=options,
                current=current,
                command=command,
                menubackground=self.frame_bg,
                image=img_path,
                style='Flat.TMenubutton'
                ))
            var_value = self.fs_list.index(current) \
                    if menubtn == 'mcmc_fontsize_choice' else current
            getattr(self, menubtn).menu.invoke(var_value)

        self.mcmc_tex_choice.btn.grid(row=0, column=0, sticky='nws')
        self.mcmc_fontsize_choice.btn.grid(row=0, column=1, sticky='nws')
        self.mcmc_style_choice.btn.grid(row=0, column=2, sticky='news')
        for i in range(3):
            mcmcplotcfg.columnconfigure(i, weight=1)
        nlines += 1

        for i in range(nlines):
            sim_options_frame.frame.rowconfigure(i, weight=1)

        self.frame_scroll_priors = EPIC_widgets.ScrollableFrame(
                self.parameter_priors_baseframe, self.frame_bg)

        right_frame = ttk.Frame(parameter_space_frame,
                width=self.RIGHT_FRAME_WIDTH)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        right_frame.pack_propagate(False)
        
        model_setup_notebook = ttk.Notebook(self.master)
        model_setup_LF = ttk.Frame(model_setup_notebook)
        model_setup_notebook.add(model_setup_LF, text='Cosmology')
        model_setup_notebook.pack(side=tk.LEFT, fill=tk.Y, 
                **self.default_padding)
        model_setup_notebook.pack_propagate(False)

        self.plots_notebook = ttk.Notebook(self.master)
        self.model_solution_tabs_dict = OrderedDict()
        for plot, xlabel, ylabel, xscale, yscale, xtoggle, ytoggle in [
                ('Density parameters', r'$a$', r'$\Omega$', 'log', 'linear',
                    True, False),
                ('Energy densities', r'$a$', r'$\rho \, [\rm{kg}/\rm{m}^3]$',
                    'log', 'log', True, False),
                #('Comoving distances', r'$z$', r'$d(z) \, [\rm{Mpc}]$', 'log',
                #    'log', True, True),
                ('Distances', r'$z$', r'$d(z) \, [\rm{Mpc}]$', 'log',
                    'log', True, True),
                #('Adimensional distances', r'$z$', r'$d(z)/d_H(z)$', 'log',
                #    'log', True, True),
                ('Lookback time', r'$z$', r'$t(z) \, [\rm{Gyr}]$', 'log',
                    'linear', True, True),
                ('Equation of state', r'$a$', r'$w(a)$', 'log', 'linear',
                    False, False),
                ]:
            self.model_solution_tabs_dict[plot] = EPIC_widgets.FigureFrame(
                    self.plots_notebook, plot_name=plot, xlabel=xlabel,
                    ylabel=ylabel, yscale=yscale,
                    xscale_toggle=xtoggle, yscale_toggle=ytoggle,
                    difference_toggle=False,
                    )
            self.plots_notebook.add(self.model_solution_tabs_dict[plot],
                    text=plot, padding=EPIC_widgets.PlotNotebook_padding)

        self.distance_comparison_tabs_dict = OrderedDict(
                ((name, EPIC_widgets.FigureFrame(
                    self.plots_notebook, plot_name=name, xlabel=r'$z$', 
                    ylabel=io_tools.split_last(name)[1].rstrip('$') + r'\, [\rm{Mpc}]$',
                    yscale='log', difference_toggle=True,
                    xscale_toggle=True, yscale_toggle=True,
                    #name == 'Lookback time',
                    )) for name in self.distances_to_compare)
            )
        for name in self.distances_to_compare:
            self.plots_notebook.add(self.distance_comparison_tabs_dict[name],
                    text=io_tools.split_last(name)[0],
                    padding=EPIC_widgets.PlotNotebook_padding)

        self.MCMCplot_tab = EPIC_widgets.BasicFigureFrame(self.plots_notebook,
                plot_name='MCMC', customize_plot_buttons=False)
        self.plots_notebook.add(self.MCMCplot_tab, text='MCMC',
                padding=EPIC_widgets.PlotNotebook_padding)

        for tab in self.plots_notebook.tabs():
            self.plots_notebook.hide(tab)
        self.plots_notebook.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, **self.default_padding)

        include_plots_frame = ttk.Frame(right_frame)
        include_plots_frame.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.Y,
                expand=1)

        include_plots_LF = ttk.LabelFrame(include_plots_frame, relief=tk.FLAT,
                #width=(self.RIGHT_FRAME_WIDTH-8*self.PADX)//4,
                text='Include plots of:')
        include_plots_LF.pack(anchor=tk.NW, fill=tk.Y, expand=1,
                **self.default_padding)
        #include_plots_LF.pack_propagate(False)

        corner_frame = ttk.Frame(right_frame, 
                width=(self.RIGHT_FRAME_WIDTH-0*self.PADX)//4)
        corner_frame.pack(side=tk.LEFT, fill=tk.Y, expand=1,
                **self.default_padding)
        corner_frame.pack_propagate(False)

        self.corner_frame_buttons = ttk.Frame(corner_frame)
        self.corner_frame_buttons.pack(fill=tk.X, expand=1, anchor=tk.NW)

        self.solve_button = ttk.Button(self.corner_frame_buttons, state=tk.DISABLED,
                text='Solve background\ncosmology',# height=5,
                command=self.get_cosmo_solution)
        self.solve_button.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E)
        #self.solve_button.grid_propagate(False)

        calc_at_z_btn = ttk.Button(self.corner_frame_buttons, #padding='2 3 2 3',
                text='Calculate at:', state=tk.DISABLED,
                command=self.calculate_at_z)
        calc_at_z_btn.grid(row=1, column=0, sticky=tk.NW+tk.SW)
        EPIC_widgets.MyTextLabel(self.corner_frame_buttons, 'z', width=4,
                background=self.frame_bg).grid(row=1, column=1, sticky=tk.W+tk.E,
                        **self.default_xpadding)
        self.z_var = tk.DoubleVar()
        self.z_var.set(1.0)
        at_z_entry = ttk.Entry(self.corner_frame_buttons, width=4, font=('Times',
            14-EPIC_widgets.platform_reduce_font_parameter), state=tk.DISABLED,
            textvariable=self.z_var)
        at_z_entry.grid(row=1, column=2, sticky=tk.NW+tk.SE)

        self.age_label = ttk.Label(corner_frame, justify=tk.LEFT, anchor=tk.SW,
                text='')
        self.age_label.pack(anchor=tk.SW, expand=1)

        self.saved_models_frame = ttk.Frame(right_frame)
        #width=(self.RIGHT_FRAME_WIDTH-8*self.PADX)//4)
        self.saved_models_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1,
                **self.default_padding)

        select_buttons_frame = ttk.Frame(self.saved_models_frame)
        select_buttons_frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        n_select_btns = 6
        columns_iter = iter(range(n_select_btns))
        ttk.Button(select_buttons_frame, style='Flat.TButton',
                command=self.rename_active, text='Rename').grid(row=0,
                        column=next(columns_iter), sticky=tk.NW+tk.SE)
        ttk.Label(select_buttons_frame, text='Select:', anchor=tk.E).grid(
                row=0, column=next(columns_iter), sticky=tk.NW+tk.SE)
        ttk.Button(select_buttons_frame, text='All', width=4,
                command=self.comparison_select_all,
                style='Flat.TButton').grid(row=0, column=next(columns_iter),
                        sticky=tk.NW+tk.SE)
        ttk.Button(select_buttons_frame, width=4,
                command=self.comparison_clear_selection, style='Flat.TButton',
                text='None').grid(row=0, column=next(columns_iter),
                        sticky=tk.NW+tk.SE)
        ttk.Button(select_buttons_frame, width=4,
                command=self.comparison_invert_selection, style='Flat.TButton',
                text='Invert').grid(row=0, column=next(columns_iter),
                        sticky=tk.NW+tk.SE)
        ttk.Button(select_buttons_frame, width=1, command=self.empty_list,
                style='Flat.TButton', text='\u274C').grid(row=0,
                        column=next(columns_iter), sticky=tk.NW+tk.SE)
        ttk.Button(self.saved_models_frame, text='Compare distances',
                command=self.new_comparison).pack(side=tk.BOTTOM, fill=tk.BOTH,
                        expand=1)

        for i in range(n_select_btns):
            select_buttons_frame.columnconfigure(i, weight=1)
        select_buttons_frame.pack_propagate(False)

        listbox_frame = ttk.Frame(self.saved_models_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=1)
        listbox_frame.pack_propagate(False)

        self.saved_models_listbox = EPIC_widgets.ListboxEditable(
                listbox_frame, selectmode=tk.EXTENDED)
        self.saved_models_listbox.grid(row=0, column=0, sticky=tk.NW+tk.SE)
        saved_scroll = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        saved_scroll.grid(row=0, column=1, sticky=tk.N+tk.S)
        listbox_frame.columnconfigure(0, weight=1)
        listbox_frame.rowconfigure(0, weight=1)
        self.saved_models_listbox.config(yscrollcommand=saved_scroll.set)
        saved_scroll.config(command=self.saved_models_listbox.yview)

        config_all_widgets(self.saved_models_frame, state=tk.DISABLED)

        self.model_results_tabs_states = OrderedDict([
                ('Density parameters', 1),
                ('Energy densities', 1),
                ('Distances', 0),
                ('Equation of state', 0)
                ])

        self.model_results_checkbuttons_dict = {}
        self.model_results_checkbuttons_var = {}

        for i, tab in enumerate(self.model_results_tabs_states.keys()):
            self.model_results_checkbuttons_var[tab] = tk.IntVar()
            self.model_results_checkbuttons_dict[tab] = ttk.Checkbutton(
                    include_plots_LF, text=tab,
                    variable=self.model_results_checkbuttons_var[tab],
                    command=getattr(self, 'show_hide_%s' % tab.replace(' ', '_'))
                    ) #borderwidth=0, highlightthickness=0, 
            self.model_results_checkbuttons_dict[tab].grid(row=i, column=0,
                    columnspan=1 if tab == 'Distances' else 4,
                    sticky=tk.NW+tk.SW)
            #pack(anchor=tk.W, fill=tk.Y, expand=1)

        ttk.Label(include_plots_LF, text='(z max:').grid(row=2, column=1, sticky=tk.E)
        self.zrange_combobox = EPIC_widgets.ReadonlyCombobox(include_plots_LF,
                values=['5', '100', '10³', '10\u2074'], width=3, state=tk.DISABLED)
        self.zrange_combobox.current(3)
        self.zrange_combobox.grid(row=2, column=2, sticky=tk.W+tk.E) 
        ttk.Label(include_plots_LF, text=')').grid(row=2, column=3,
                sticky=tk.W)

        self.reset_model_results_states()

        self.model_results_checkbuttons_dict['Equation of state'].config(
                state=tk.DISABLED)

        textcfg = ttk.Frame(include_plots_frame)
        textcfg.pack(anchor=tk.SW, fill=tk.Y, expand=1, **self.default_xpadding)

        self.current_tex_option = self.tex_options['regular'][0]
        self.current_style = 0

        for menubtn, text, menutitle, options, current, command, imgfile in [
                ('style_choice', self.please_select_style,
                    self.please_select_style, self.styles_list,
                    self.current_style, self.set_chosen_plot_style, None),
                ('tex_choice', None, 'TeX options',
                    self.tex_options['regular'], 0, self.set_tex_option,
                    'menu-tex.png'),
                ('fontsize_choice', None, 'Font size', self.fs_list, 12,
                    lambda: self.set_font_size('fontsize_choice',
                        'mcmc_fontsize_choice', updating_from_other=False), 'fontsize.png'),
                ]:
            img_path = os.path.join(EPIC.root, 'gui_files', 'images', imgfile) \
                    if imgfile else None
            setattr(self, menubtn, EPIC_widgets.MenuButtonOptions(
                textcfg,
                text=text,
                menutitle=menutitle,
                options=options,
                current=current,
                command=command,
                menubackground=self.frame_bg,
                image=img_path
                ))

        self.tex_choice.btn.grid(row=0, column=0, sticky='nws')
        self.fontsize_choice.btn.grid(row=0, column=1, sticky='nws')
        self.style_choice.btn.grid(row=0, column=2, sticky='nws')

        #for i in range(2):
        #    self.fontsize_choice.btn.columnconfigure(i, weight=0)

        iter_rows = iter(range(7))

        cb_model_values = [self.please_select_model,] \
                + [self.map_model[model] for model in self.models.keys()]
        self.model_options_combobox = EPIC_widgets.ReadonlyCombobox(model_setup_LF, 
                width=round(210/EPIC_widgets.pixels_to_char_size),
                values=cb_model_values)
        self.model_options_combobox.current(0)

        next_row = next(iter_rows)
        ttk.Label(model_setup_LF, text='Model:').grid(row=next_row, column=0,
                sticky=tk.E, **self.default_padding)
        self.model_options_combobox.grid(row=next_row, column=1, sticky=tk.W,
                **self.default_padding)
        self.model_options_combobox.bind("<<ComboboxSelected>>",
                func=self.show_optional_species, add='+')

        next_row = next(iter_rows)
        ttk.Label(model_setup_LF, text='Mandatory species:').grid(row=next_row,
                column=0, sticky=tk.E, **self.default_padding)
        self.mandatory_msg = ttk.Label(model_setup_LF,
                width=round(230/EPIC_widgets.pixels_to_char_size),
                text=self.please_select_model+'\n', padding=self.PADX)
        self.mandatory_msg.grid(row=next_row, column=1, sticky=tk.W,
                **self.default_ypadding)

        next_row = next(iter_rows)
        self.optional_species_listbox = tk.Listbox(model_setup_LF,
                selectmode=tk.MULTIPLE, height=2, exportselection=0)
        ttk.Label(model_setup_LF, text='Add optional species:').grid(
                row=next_row, column=0, sticky=tk.E, **self.default_padding)
        self.optional_species_listbox.grid(row=next_row, column=1, 
                sticky=tk.W, **self.default_padding)

        cb_frame = ttk.Frame(model_setup_LF)
        cb_frame.grid(row=next(iter_rows), column=0, columnspan=2, sticky=tk.NW+tk.SE)

        self.combined_var = tk.IntVar()
        self.combined_var.set(0)
        self.combined_option = ttk.Checkbutton(cb_frame,
                variable=self.combined_var, state=tk.DISABLED,
                text='Use combined matter\nfluid (cdm+baryons)'
                )
        self.combined_option.pack(side=tk.LEFT, expand=1,
                anchor=tk.CENTER, **self.default_padding)

        self.physical_var = tk.IntVar()
        self.physical_var.set(1)
        ttk.Checkbutton(cb_frame, text='Use physical\ndensities',
                variable=self.physical_var).pack(side=tk.LEFT, expand=1,
                        anchor=tk.CENTER, **self.default_padding)

        next_row = next(iter_rows)
        self.derived_lbl = ttk.Label(model_setup_LF, justify=tk.RIGHT,
                state=tk.DISABLED,
                text='Use density of this fluid\nas derived parameter:')
        self.derived_lbl.grid(row=next_row, column=0, sticky=tk.E,
                **self.default_padding)
        self.derived_combobox = EPIC_widgets.ReadonlyCombobox(model_setup_LF,
                state=tk.DISABLED, values=[self.please_select_species,],
                width=8)
        self.derived_combobox.current(0)
        self.derived_combobox.grid(row=next_row, column=1, sticky=tk.W,
                **self.default_padding)

        next_row = next(iter_rows)
        self.int_frame = ttk.Frame(model_setup_LF)
        self.int_frame.grid(row=next_row, column=1, sticky=tk.W+tk.E)
        self.interaction_propto_options = EPIC_widgets.ReadonlyCombobox(
                self.int_frame, width=8, values=[self.please_select_species,])
        self.int_propto_label = ttk.Label(model_setup_LF, justify=tk.RIGHT,
                text='Interaction setup -\nProportional to density of:', state=tk.DISABLED)
        self.int_propto_label.grid(row=next_row, column=0, sticky=tk.E,
                **self.default_padding)
        self.interaction_propto_options.current(0)
        self.interaction_propto_options.pack(side=tk.LEFT, anchor=tk.W,
                **self.default_padding)

        self.int_sign_combobox = EPIC_widgets.ReadonlyCombobox(self.int_frame,
                width=5, values=['(sign)', '+1', '-1'])
        self.int_sign_combobox.current(1)
        self.int_sign_combobox.pack(side=tk.LEFT, anchor=tk.CENTER,
                **self.default_padding)

        ttk.Button(self.int_frame, style='Flat.TButton', text='Set', width=5,
                command=self.set_and_update_gif).pack(side=tk.LEFT,
                        anchor=tk.W, **self.default_padding)

        config_all_widgets(self.int_frame, state=tk.DISABLED)

        self.darksector_and_build_frame = ttk.Frame(model_setup_LF)
        self.darksector_and_build_frame.grid(row=next(iter_rows), column=0,
                columnspan=2)

        img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files', 'blank.gif'))
        img_lbl_text = ttk.LabelFrame(self.darksector_and_build_frame,
                text='Dark sector:')
        img_lbl_text.pack(side=tk.LEFT, **self.default_padding)

        self.img_lbl = ttk.Label(img_lbl_text, style='Image.TLabel', image=img)
        self.img_lbl.image = img
        self.img_lbl.pack() 

        ttk.Button(self.darksector_and_build_frame, text='Build\nnew\nmodel',
                width=5, command=self.build_model).pack(side=tk.RIGHT, expand=1,
                        anchor=tk.S, **self.default_ipadding,
                        **self.default_padding)

        config_all_widgets(self.darksector_and_build_frame, state=tk.DISABLED)

        for x in range(8):
            model_setup_LF.rowconfigure(x, weight=1)
        for y in range(2):
            model_setup_LF.columnconfigure(y, weight=0)

    def reset_model_results_states(self):
        for tab, state in self.model_results_tabs_states.items():
            self.model_results_checkbuttons_var[tab].set(1-state if \
                    not tk.DISABLED in self.model_results_checkbuttons_dict[tab].state() else state)
            self.model_results_checkbuttons_dict[tab].invoke()

    """
    def specify_visible(self, event):
        for tab in self.plots_notebook.tabs():
            self.plots_notebook.hide(tab)
        self.reset_model_results_states()
        self.viewing = 'plots'
    """

    def MCMC_visible(self, event):
        self.plots_notebook.add(self.MCMCplot_tab,
                padding=EPIC_widgets.PlotNotebook_padding)
        select_first_visible(self.plots_notebook, order=-1)
        #self.viewing = 'MCMC'

    def cmb_lcdm_toggle(self, year):
        if self.data_CMB_LCDM[year].get():
            self.data_CMB_LCDM[2015+2018-year].set(0)
            self.data_CMB_wCDM[2015].set(0)
            self.data_CMB_wCDM[2018].set(0)

    def cmb_wcdm_toggle(self, year):
        if self.data_CMB_wCDM[year].get():
            self.data_CMB_wCDM[2015+2018-year].set(0)
            self.data_CMB_LCDM[2015].set(0)
            self.data_CMB_LCDM[2018].set(0)

    def sne_simple_toggle(self):
        if self.data_JLA_simple.get():
            self.data_JLA_full.set(0)
            for par in self.jla_full_nuisance_pars:
                config_all_widgets(par.frame, state=tk.DISABLED)
            config_all_widgets(self.jla_simple_nuisance_par.frame, state=tk.NORMAL)
            self.jla_simple_nuisance_par.par_states_with_prior_type()
        else:
            config_all_widgets(self.jla_simple_nuisance_par.frame, state=tk.DISABLED)

    def sne_full_toggle(self):
        if self.data_JLA_full.get():
            self.data_JLA_simple.set(0)
            for par in self.jla_full_nuisance_pars:
                config_all_widgets(par.frame, state=tk.NORMAL)
                par.par_states_with_prior_type()
            config_all_widgets(self.jla_simple_nuisance_par.frame, state=tk.DISABLED)
        else:
            for par in self.jla_full_nuisance_pars:
                config_all_widgets(par.frame, state=tk.DISABLED)

    def has_baryons_and_radiation(self):
        assert hasattr(self, 'cosmo_model')
        return 'baryons' in self.cosmo_model.species and 'radiation' in self.cosmo_model.species

    def read_bao_states(self):
        self.BAO_states = OrderedDict()
        for bao_set, check in self.BAO_dict_check.items():
            self.BAO_states[bao_set] = not tk.DISABLED in check.state()

    def bao_sdss_boss_toggle(self):
        use = any([check.get() for k, check in self.BAO_dict.items() \
                if not k in ['WiggleZ', '6dF+SDSS_MGS']])
        self.BAO_dict_check['WiggleZ'].config(state=tk.DISABLED if use \
                or not self.has_baryons_and_radiation() else tk.NORMAL)
        self.read_bao_states()

    def bao_wigglez_toggle(self):
        use = self.BAO_dict['WiggleZ'].get()
        for k, check in self.BAO_dict_check.items():
            if not k in ['WiggleZ', '6dF+SDSS_MGS']:
                check.config(state=tk.DISABLED if use or not \
                        self.has_baryons_and_radiation() else tk.NORMAL)
        self.read_bao_states()

    def comparison_select_all(self, func='selection_set'):
        getattr(self.saved_models_listbox, func)(0, last=tk.END)

    def comparison_clear_selection(self):
        self.comparison_select_all(func='selection_clear')

    def empty_list(self):
        self.list_of_solved_models = []
        self.saved_models_listbox.delete(0, tk.END)

    def comparison_invert_selection(self):
        for i in range(self.saved_models_listbox.size()):
            if self.saved_models_listbox.selection_includes(i):
                self.saved_models_listbox.selection_clear(i)
            else:
                self.saved_models_listbox.selection_set(i)

    def rename_active(self):
        if len(self.saved_models_listbox.curselection()) != 1:
            self.saved_models_listbox.selection_set(tk.ACTIVE)
        self.saved_models_listbox.edit()

    def show_hide_tabs(self, which_tabs):
        show = self.model_results_checkbuttons_var[which_tabs].get()
        if which_tabs == 'Distances':
            which_tabs = [
                    #'Comoving distances', 
                    'Distances', 
                    'Lookback time'
                    ]
            self.zrange_combobox.config(state='readonly' if show else tk.DISABLED)
        else:
            which_tabs = [which_tabs,]
        set_of_tabs = self.model_solution_tabs_dict
        for tab in which_tabs:
            if show:
                #self.hide_distance_comparison_tabs()
                self.plots_notebook.add(set_of_tabs[tab],
                        padding=EPIC_widgets.PlotNotebook_padding)
                #, text=tab,
            else:
                current = self.plots_notebook.select()
                hide_tab(self.plots_notebook, set_of_tabs[tab])
                if current not in self.plots_notebook.tabs():
                    select_first_visible(self.plots_notebook)

        self.determine_solve_btn_state()

    def determine_solve_btn_state(self):
        if hasattr(self, 'cosmo_model') and any([check.get() \
                for check in self.model_results_checkbuttons_var.values()]):
            state = tk.NORMAL
        else:
            state = tk.DISABLED
        self.solve_button.config(state=state)

    def show_hide_Distances(self):
        return self.show_hide_tabs('Distances')

    def show_hide_Density_parameters(self):
        return self.show_hide_tabs('Density parameters')

    def show_hide_Energy_densities(self):
        return self.show_hide_tabs('Energy densities')

    def show_hide_Equation_of_state(self):
        return self.show_hide_tabs('Equation of state')

    def new_comparison(self):
        if len(self.saved_models_listbox.curselection()) < 1:
            messagebox.showerror('Error', 'At least one model must be selected.')
            return None

        self.master.config(cursor='exchange')
        self.master.update()
        self.compare_distances()
        self.master.config(cursor='left_ptr')

    def compare_distances(self, models=None, labels=None):

        if models is None:
            models = [self.list_of_solved_models[i] \
                    for i in self.saved_models_listbox.curselection()] 
        if labels is None:
            labels = self.saved_models_listbox.get(0, tk.END)
            labels = [labels[i].replace('Λ', r'$\Lambda$').replace('wCDM',
                r'$w$CDM') for i in self.saved_models_listbox.curselection()]

        self.status_bar.config(text='Plotting...')
        self.status_bar.update()

        if self.viewing != 'dist':
            for key, cb in self.model_results_checkbuttons_dict.items():
                if self.model_results_checkbuttons_var[key].get():
                    cb.invoke()

        for plot_name in self.distances_to_compare:
            instructions = [model.results['Distances'] \
                    for model in models]
            self.distance_comparison_tabs_dict[plot_name].add_distance_comparison_to_widget(
                    plot_name, instructions, labels)

        if self.viewing != 'dist':
            for plot_name in self.distances_to_compare:
                self.plots_notebook.add(self.distance_comparison_tabs_dict[plot_name],
                        padding=EPIC_widgets.PlotNotebook_padding)
                # text=io_tools.split_last(plot_name)[0],

        if self.viewing != 'dist':
            select_first_visible(self.plots_notebook)

        self.viewing = 'dist'
        self.all_models = list(models)
        self.all_labels = list(labels)
        self.status_bar.config(text='Done.')

    def visible_tab(self, tab):
        return tab in self.plots_notebook.tabs() \
                and self.plots_notebook.tab(tab)['state'] == 'normal'

    def add_prior_config(self, baseframe, i, par):
        par.prior_setup = EPIC_widgets.PriorLineSetup(baseframe,
                self.map_parameters[par.label], par.label, row=i,
                background=self.frame_bg, xpadding=self.default_xpadding)
        if par.label == 'T_CMB':
            par.prior_setup.prior_dist.current(0)
        par.prior_setup.prior_dist.bind("<<ComboboxSelected>>",
                func=par.set_default_priors, add='+')
        par.prior_setup.par_states_with_prior_type()
        par.set_default_priors()

    def get_optional_species(self):
        optional = self.optional_species_listbox.curselection()
        optional = [self.optional_species[i] for i in optional]
        return optional

    def write_if_non_empty(self, f, key):
        attribute = '_' + key.replace(' ', '_') + '_chosen'
        _list = getattr(self.cosmo_model, attribute)
        if len(_list) > 0:
            f.write(' = '.join([key, str(_list) + '\n']))

    def write_dictionary(self, f, d, key, _break_list=False, ident=2):
        f.write(key + ' = ')
        if len(d) > 0: 
            f.write('{\n')
            for k, v in d.items():
                if isinstance(v, list):
                    if _break_list:
                        value = break_list(v, ident=ident)
                    else:
                        value = quote(v)
                else:
                    value = quote(v)
                f.write("    '" + k + "' : " + value + ",\n")
            f.write('    }\n')
        else:
            f.write('\n')

    def choose_proposal_cov_file(self):
        filename = filedialog.askopenfilename(
                initialdir=EPIC.user_folder,
                defaultextension='.txt', 
                filetypes=[
                    ('TXT file', '*.txt'),
                    ('All files', '*.*'),
                    ]
                )
        self.proposal_cov_file.set(filename)
        self.cov_loaded.set(int(bool(filename)))
        self.status_bar.config(
                text='Proposal covariance file {0} loaded. Click the load button again and click Cancel to unload.'.format(filename) \
                        if filename else 'No file was loaded.'
                )

    def export_ini_only(self, run=False):
        if not hasattr(self, 'cosmo_model'):
            messagebox.showerror('Error', 'Please, set up a model first.')
            return None
        self.inifile = filedialog.asksaveasfilename(title='Export ini file...', 
                defaultextension='.ini',
                filetypes=[('INI file', '*.ini')], initialdir=EPIC.user_folder,
                initialfile='{0}.ini'.format(self.cosmo_model.model)
                )
        if not self.inifile:
            return None
        if EPIC._OS == 'Windows':
            self.inifile = io_tools.unixify_path(self.inifile)
        self.args_list = self.get_args_list()
        if self.prepare_sim_ini():
            # file exported, instructions in the header
            if not run:
                self.status_bar.config(text='File %s exported. You can start a MCMC simulation following instructions given in the header of this file.' % self.inifile)
        setattr(self, 'exported', self.inifile)

    def get_args_list(self):
        args_list = [
                self.inifile, 
                str(self.chains_var.get()), # number of chains
                str(self.steps_var.get()), # number of steps
                '-c', self.check_interval_var.get(), # check interval
                '--tolerance', str(self.tol_var.get()), # tolerance
                '--acceptance-limits', *[str(v) for v in self.acc_range.get()],
                '--bins', str(self.bins_var.get()),
                ] # only parser_run args
        if self.rejected_var.get():
            args_list.append('--save-rejected')
        tag = self.tag_var.get()
        if tag and tag != '(optional)':
            args_list.extend(['--sim-tag', self.tag_var.get()])
        if self.proposal_cov_file.get():
            args_list.extend(['--proposal-covariance', self.proposal_cov_file.get()])
        return args_list

    def export_ini_and_run_MCMC(self):
        if not getattr(self, 'inifile', None):
            # this function defines self.inifile and self.exported
            self.export_ini_only(run=True)

        if not getattr(self, 'exported', None):
            return None

        self.start_simulation()

    def load_sim(self):
        load = filedialog.askdirectory(initialdir=EPIC.user_folder)
        if load:
            self.inifile = load
            self.start_simulation(load_previous=load)

    def start_simulation(self, load_previous=None):
        for info in self.MCMC_simulation_info.values():
            info.clear_text()
        self.MCMC_visible(None)
        self.args_list = self.get_args_list()
        args = self.run_parser.parse_args(args=self.args_list)
        self.parameters_setup_notebook.add(self.MCMC_terminal, text='Output')
        tabId = '.' + self.parameters_setup_notebook.winfo_name() \
                + '.' + self.MCMC_terminal.winfo_name()
        self.parameters_setup_notebook.select(tabId)
        self.MCMC_output.start()
        if load_previous:
            self.wdir = load_previous
            self.sim = sim_objects.load_existing_simulation(self.wdir)
        else:
            self.wdir, analysis = sim_objects.create_new_simulation(args)
            self.sim = sim_objects.load_existing_simulation(self.wdir, analysis)
        self.status_bar.config(text='MCMC started... Location: ' + self.wdir)
        self.status_bar.update()
        plot_args = self.get_plot_args()
        if self.sim.start(args, external_fig=self.MCMCplot_tab,
                external_texts=self.MCMC_simulation_info,
                plot_args=plot_args):
            rargs_list = [self.sim.working_dir, '--convergence', '--dont-plot']
            if self.kde_var.get():
                rargs_list.append('--kde')
            rargs = self.analyze_parser.parse_args(args=rargs_list)
            self.analyze(self.sim, args=rargs,
                    external_texts=self.MCMC_simulation_info)
            setattr(plot_args, 'kde', bool(self.kde_var.get()))
            setattr(plot_args, 'no_auto_range', False)
            print('')
            print('Making final plot:')
            self.remake_mcmc_plot(plot_args, self.plot_parser, self.sim)
            self.status_bar.config(text='Analysis finished. Location: ' + self.wdir)
        else:
            self.status_bar.config(text=':( Try again with a different covariance matrix for the proposal function.')
        self.MCMC_output.stop()
        self.proposal_cov_file.set('')
        self.cov_loaded.set(0)
        self.clear_info_exported_ini()


    def prepare_sim_ini(self):
        try:
            self.attempt_prepare_sim_ini()
        except tk.TclError:
            messagebox.showerror('Error', 'Invalid float value.')
            succeeded = False
        else:
            copy2(self.tempfile_name, self.inifile)
            succeeded = True
        finally:
            if os.path.isfile(self.tempfile_name):
                os.remove(self.tempfile_name)

        return succeeded

    def attempt_prepare_sim_ini(self):
        with open(self.tempfile_name, 'w') as f:
            if getattr(self, 'args_list') is not None:
                args = self.run_parser.parse_args(self.args_list)
                args = io_tools.get_parsed_args(args, self.run_parser, command='run')
                if '--check-interval' in args:
                    interval_index = args.index('--check-interval') + 1
                    args[interval_index] = io_tools.revert_TimeString(
                            int(args[interval_index])
                            )
                f.write('\n'.join([
                    '# This ini file was generated from EPIC GUI.',
                    '# To start a simulation with this configuration, open a terminal,',
                    '# activate the virtual environment in which you installed EPIC,',
                    '# cd into EPIC and then run:'
                    ]))
                f.write('\n')
                f.write('#    ' + ' '.join(args) + '\n')
                f.write('\n')
            f.write('[model]\n')
            f.write(' = '.join(['type', self.cosmo_model.model + '\n']))
            f.write(' = '.join(['physical', 
                ('yes'  if self.cosmo_model.physical_density_parameters \
                        else 'no') + '\n']))
            for key in [
                    'optional species',
                    'combined species',
                    'interaction setup',
                    ]:
                self.write_if_non_empty(f, key)
            f.write(' = '.join(['derived', self.cosmo_model._derived+'\n']))
            f.write('\n')

            priors_dict = OrderedDict()
            dist_dict = OrderedDict()
            fixed_dict = OrderedDict()
            all_free_parameters = list(self.free_parameters)
            if self.data_JLA_simple.get():
                all_free_parameters.append(self.jla_simple_nuisance_par)
            elif self.data_JLA_full.get():
                all_free_parameters.extend(self.jla_full_nuisance_pars)

            for par in all_free_parameters:
                # 0 is fixed, 1 is flat, 2 is Gaussian
                try:
                    p = par.prior_setup
                except AttributeError:
                    p = par
                dist = p.prior_dist.current()
                if dist == 0:
                    fixed_dict[p.label] = p.parameters_var[0].get()
                else:
                    priors_dict[p.label] = [p.parameters_var[0].get(),
                            p.parameters_var[1].get()]
                    if dist == 2:
                        dist_dict[p.label] = 'Gaussian'

            datasets_dict = OrderedDict()
            datasets_label = []
            if self.data_cosmic_chrono.get():
                datasets_dict['Hz'] = 'cosmic_chronometers'
                datasets_label.append('$H(z)$')
            if self.data_local_Hubble.get():
                datasets_dict['H0'] = 'HST_local_H0'
                datasets_label.append('$H_0$')
            if self.data_JLA_simple.get():
                datasets_dict['SNeIa'] = 'JLA_simplified'
                datasets_label.append('SNeIa')
            elif self.data_JLA_full.get():
                datasets_dict['SNeIa'] = 'JLA_full'
                datasets_label.append('SNeIa')
            BAO_list = []
            for bao_set, check in self.BAO_dict.items():
                if check.get() and \
                        not (tk.DISABLED in self.BAO_dict_check[bao_set].state()):
                    BAO_list.append(bao_set)
            if len(BAO_list) > 0:
                datasets_dict['BAO'] = BAO_list
                datasets_label.append('BAO')
            for year in [2015, 2018]:
                if self.data_CMB_LCDM[year].get() and \
                        not (tk.DISABLED in self.data_CMB_LCDM_check[year].state()):
                    datasets_dict['CMB'] = 'Planck%i_distances_LCDM' % year
                    datasets_label.append('CMB')
                    break
                elif self.data_CMB_wCDM[year].get() and \
                        not (tk.DISABLED in self.data_CMB_wCDM_check[year].state()):
                    datasets_dict['CMB'] = 'Planck%i_distances_wCDM' % year
                    datasets_label.append('CMB')
                    break

            f.write('[analysis]\n')
            f.write(' = '.join(['label', ' + '.join(datasets_label) + '\n']))
            self.write_dictionary(f, datasets_dict, 'datasets', _break_list=True)
            f.write('priors = {\n')
            for k, v in priors_dict.items():
                f.write("    '" + k + "' : " + str(v) + ",\n")
            f.write('    }\n')
            self.write_dictionary(f, dist_dict, 'prior distributions')
            self.write_dictionary(f, fixed_dict, 'fixed')
            f.write('\n')

            f.write('[simulation]\n')
            proposal_dict = OrderedDict()
            for par in all_free_parameters:
                if isinstance(par, EPIC_widgets.PriorLineSetup):
                    p = par
                else:
                    p = par.prior_setup
                if p.prior_dist.current() != 0:
                    proposal_dict[p.label] = p.sig_var.get()
            self.write_dictionary(f, proposal_dict, 'proposal covariance')
            f.write('\n')

    def clear_info_exported_ini(self):
        self.inifile = ''
        if hasattr(self, 'exported'):
            delattr(self, 'exported')

    def build_model(self):

        if hasattr(self, 'age_label'):
            self.age_label.config(text=self.models_list_notice)

        modelname = self.map_model[self.model_options_combobox.get()]
        if modelname == self.please_select_model:
            messagebox.showerror('Error', 'Please, select a model first.')
            return None

        self.clear_info_exported_ini()
        optional = self.get_optional_species()
        if 'cde' in modelname:
            if self.interaction_propto_options.get() == self.please_select_species \
                    or self.int_sign_combobox.get() == '(sign)':
                messagebox.showerror('Error', 'Please, make sure to set up correctly the interaction.')
                return None
            propto = self.map_species_abbrv[self.interaction_propto_options.get()]
            dependent_on_other = list(self.mandatory_species)
            dependent_on_other.remove(propto)
            propto_other = {dependent_on_other[0]: propto}
            sign = int(self.int_sign_combobox.get())
            int_setup = {
                'species': self.mandatory_species[:2],
                'propto_other': propto_other,
                'parameter': {propto: 'xi'},
                'tex': r'\xi',
                'sign': dict(zip(self.mandatory_species[:2], [sign, -sign]))
                }
            combined = []
        else:
            int_setup = {}
            combined = ['matter',] if self.combined_var.get() else []
        #print('combined species', combined)

        #print('interaction setup', int_setup)
        derived_opt = self.map_species_abbrv[self.derived_combobox.get()]
        self.cosmo_model = cosmo.CosmologicalSetup(
                modelname, 
                optional_species=optional,
                combined_species=combined,
                interaction_setup=int_setup,
                physical=bool(self.physical_var.get()),
                derived=derived_opt,
                a0=1
                )
        self.cosmo_model._combined_species_chosen = combined
        self.cosmo_model._interaction_setup_chosen = int_setup
        self.cosmo_model._optional_species_chosen = optional
        self.cosmo_model._derived = derived_opt

        for widget in self.parameter_values.winfo_children() \
                + self.frame_scroll_priors.frame.winfo_children():
            widget.destroy()
        default_units = configparser.ConfigParser()
        default_units.read([
            os.path.join(EPIC.root, 'cosmology', 'default_parameter_units.ini'),
            os.path.join(EPIC.user_folder, 'modifications', 'cosmology',
                'default_parameter_units.ini'),
            ])
        self.free_parameters = list(filter(lambda p: isinstance(p, cosmo.FreeParameter), 
            self.cosmo_model.parameters))
        sep = int(ceil(len(self.free_parameters)/2))
        for i, par in enumerate(self.free_parameters):
            col = 0 if i < sep else 2
            EPIC_widgets.MyTextLabel(self.parameter_values,
                    self.map_parameters[par.label], background=self.frame_bg
                    ).grid(row=i % sep, column=col, sticky=tk.E,
                            **self.default_xpadding)
            self.add_prior_config(self.frame_scroll_priors.frame, i, par)
            par.entry_var = tk.DoubleVar()
            par.entry_var.set(par.default)
            par.entry_frame = ttk.Frame(self.parameter_values)
            par.entry_frame.grid(row=i % sep, column=col+1, sticky=tk.W)
            ttk.Entry(par.entry_frame, width=6, font=('Times', 
                16-EPIC_widgets.platform_reduce_font_parameter),
                    textvariable=par.entry_var).pack(side=tk.LEFT, anchor=tk.W)

            if par.label in default_units['DEFAULT']:
                orig_unit_lbl = default_units['DEFAULT'][par.label]
                unit_label = io_tools.parse_unit(orig_unit_lbl, latex=True)
                for frame in [par.entry_frame, None]:
                    par.prior_setup.add_unit(unit_label, orig_unit_lbl,
                            frame=frame, xpadding=self.default_xpadding)

        for x in range(4):
            self.parameter_values.rowconfigure(x, weight=1)
        for y in range(4):
            self.parameter_values.columnconfigure(y, weight=1)

        self.variable_eos = {}
        for key, species in self.cosmo_model.species.items():
            if species.EoS.type == 'woa':
                self.variable_eos[key] = species

        if len(self.variable_eos):
            self.model_results_checkbuttons_dict['Equation of state'].config(
                    state=tk.NORMAL)
        else:
            if self.model_results_checkbuttons_var['Equation of state'].get():
                self.model_results_checkbuttons_dict['Equation of state'].invoke()
            self.model_results_checkbuttons_dict['Equation of state'].config(
                    state=tk.DISABLED)

        if self.has_baryons_and_radiation(): 
            config_all_widgets(self.CMB_frame, state=tk.NORMAL)
            for bao_set, check in self.BAO_dict_check.items():
                check.config(state=tk.NORMAL \
                        if self.BAO_states[bao_set] else tk.DISABLED)
        else:
            config_all_widgets(self.CMB_frame, state=tk.DISABLED)
            config_all_widgets(self.BAO_frame, state=tk.DISABLED)


        config_all_widgets(self.corner_frame_buttons, state=tk.DISABLED)
        self.determine_solve_btn_state()

    def hide_distance_comparison_tabs(self):
        for tab in self.distance_comparison_tabs_dict.values():
            hide_tab(self.plots_notebook, tab)
                
    def calculate_at_z(self):
        z = self.z_var.get()
        try:
            parameters = dict((par.label, par.entry_var.get()) \
                for par in self.free_parameters)
        except tk.TclError:
            messagebox.showerror('Error', 'Invalid float value.')
            return None

        da = self.cosmo_model.d_a(z, parameter_space=parameters)
        D_H = self.cosmo_model.D_H(z, parameter_space=parameters)
        Vave = (da**2 * z * D_H)**(1/3)
        age_z = self.cosmo_model.get_age_of_the_universe(z,
                parameter_space=parameters)
        sep = '; '
        self.status_bar.config(
                text=self.map_model[self.cosmo_model.model] \
                        + ' - ' + 'At z = %s: ' % str(z) +
                sep.join([
                    'Age of the universe: %.2f Gyr' % age_z,
                    'Comoving distance: %.2f Mpc' % da,
                    #'Comoving luminosity distance: %.2f Mpc' % (da * (1+z)**2),
                    #'Comoving Hubble distance: %.2f Mpc' % (D_H*(1+z)),
                    #'Comoving volume averaged distance: %.2f Mpc' % (Vave*(1+z)),
                    #'Volume averaged distance: %.2f Mpc' % Vave,
                    'Angular diameter distance: %.2f Mpc' % (da * self.cosmo_model.a0 / (1+z)),
                    'Luminosity distance: %.2f Mpc' % (da * (1+z) / self.cosmo_model.a0),
                    'Hubble distance: %.2f Mpc' % D_H,
                    ]) + '.'
                )

    def get_function_mp(self, model_d, key, shared_dict, z, **kwargs):
        factor = kwargs.pop('factor', 1)
        shared_dict[key] = factor \
                * getattr(self.cosmo_model, model_d)(z, **kwargs)

    def get_cosmo_solution(self):
        try:
            parameters = dict((par.label, par.entry_var.get()) \
                for par in self.free_parameters)
        except tk.TclError:
            messagebox.showerror('Error', 'Invalid float value.')
            return None

        self.status_bar.config(text='Calculating...')
        self.master.config(cursor='watch')
        self.master.update()

        self.hide_distance_comparison_tabs()

        # get results
        self.cosmo_model.solve_background(parameter_space=parameters)
        age = self.cosmo_model.get_age_of_the_universe(0,
                parameter_space=parameters)
        if age:
            self.age_label.config(
                    text='Age of the universe today:\n%.3f Gyr.' % age)

        hubble = self.cosmo_model.HubbleParameter.get_value(
                parameter_space=parameters)
        rho_cr0 = cosmo.rho_critical_SI(hubble * \
                (100 if self.cosmo_model.physical_density_parameters else 1)) 
        
        self.cosmo_model.results = OrderedDict()
        self.cosmo_model.model_solution_plots_shown = []
        title = ' '.join([
            self.available_models[self.cosmo_model.model].get('tex',
                self.map_model[self.cosmo_model.model]).replace('text', 'rm'),
            'model'
        ])

        if self.show_tab('Density parameters'):
            self.cosmo_model.results['Density parameters'] = { 
                    'x': self.cosmo_model.a_range,
                    'ydict': self.cosmo_model.background_solution_Omegas,
                    'title': title,
                    'map_species': self.map_species_abbrv,
                    }
            self.cosmo_model.model_solution_plots_shown.append(
                    self.model_solution_tabs_dict['Density parameters'].winfo_name()
                    )

        if self.show_tab('Energy densities'):
            self.cosmo_model.results['Energy densities'] = {
                    'x': self.cosmo_model.a_range,
                    'ydict': self.cosmo_model.background_solution_rhos,
                    'exclude': ['total',],
                    'factor': rho_cr0 * (hubble**-2 \
                            if self.cosmo_model.physical_density_parameters else 1),
                    'title': title,
                    'map_species': self.map_species_abbrv,
                    }
            self.cosmo_model.model_solution_plots_shown.append(
                    self.model_solution_tabs_dict['Energy densities'].winfo_name()
                    )

        man = multiprocessing.Manager()
        distances_mdict = man.dict()
        jobs = []

        if self.show_tab('Distances'):
            self.cosmo_model.model_solution_plots_shown.extend(
                    [self.model_solution_tabs_dict[w].winfo_name() \
                        for w in [
                            #'Comoving distances',
                            'Distances',
                            'Lookback time'
                            ]])
            logzmax = self.zrange_combobox.current()+1
            if logzmax == 1:
                z_range = linspace(0, 5, 500)
            else:
                z_range = logspace(-logzmax, min(logzmax, 
                    log10(cosmo.z_of_a(self.cosmo_model.a_range[0]))), 500)

            for function, key in [
                    ('d_a', 'Comoving angular distance'),
                    ('D_H', 'Hubble distance'),
                    ('get_lookback_time', 'Lookback time'),
                    ('get_age_of_various_z', 'Age of the universe'),
                    ]:
                kw = {'parameter_space': parameters}
                if function == 'get_age_of_various_z' and \
                        not self.cosmo_model.directly_solvable:
                    kw.update({
                        'a_zinf': a_of_z(z_range[-1]),
                        })
                if EPIC._OS == 'Windows':
                    self.get_function_mp(function, key, distances_mdict,
                            z_range, **kw)
                else:
                    jobs.append(
                            multiprocessing.Process(
                                target=self.get_function_mp,
                                args=(function, key, distances_mdict, z_range),
                                kwargs=kw,
                                )
                            )


        if self.show_tab('Equation of state'):
            self.cosmo_model.model_solution_plots_shown.append(
                    self.model_solution_tabs_dict['Equation of state'].winfo_name()
                    )
            eos_mdict = man.dict()
            for key, species in self.variable_eos.items():
                jobs.append(
                        multiprocessing.Process(
                            target=eos_get_function_mp,
                            args=(species.EoS.w_of_a, key, eos_mdict,
                                self.cosmo_model.a_range),
                            kwargs={'a0': self.cosmo_model.a0,
                                'parameter_space': parameters},
                            )
                        )

        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
                        
        if self.show_tab('Distances'):
            distances_mdict['Comoving luminosity distance'] = \
                    distances_mdict['Comoving angular distance'] * (1+z_range)**2

            #distances_mdict['Volume averaged distance'] = \
            #        (distances_mdict['Comoving angular distance']**2 * z_range \
            #        * distances_mdict['Hubble distance'])**(1/3)

            #distances_mdict['Comoving volume averaged distance'] = \
            #        distances_mdict['Volume averaged distance']*(1+z_range)

            #distances_mdict['Comoving Hubble distance'] = \
            #        distances_mdict['Hubble distance']*(1+z_range)

            #distances_mdict['Comoving lookback time'] = \
            #        distances_mdict['Lookback time']*(1+z_range)


            distances_mdict['Angular distance'] = \
                    distances_mdict['Comoving angular distance']/(1+z_range)

            distances_mdict['Luminosity distance'] = \
                    distances_mdict['Comoving luminosity distance']/(1+z_range)

            #######################

            #H0_distance = self.cosmo_model.HubbleParameter.entry_var.get() \
            #        * (100 if self.cosmo_model.physical_density_parameters else 1)
            #distances_mdict['Adimensional angular distance'] = \
            #        distances_mdict['Angular distance']\
            #        / H0_distance # /distances_mdict['Hubble distance']

            #distances_mdict['Adimensional luminosity distance'] = \
            #        distances_mdict['Luminosity distance'] \
            #        / H0_distance # /distances_mdict['Hubble distance']

            #distances_mdict['Adimensional volume averaged distance'] = \
            #        distances_mdict['Volume averaged distance'] \
            #        / H0_distance # /distances_mdict['Hubble distance']

            #distances_mdict['Adimensional lookback time'] = \
            #        distances_mdict['Lookback time'] \
            #        / H0_distance # /distances_mdict['Hubble distance']

            self.cosmo_model.results.update(
                    OrderedDict([
                        #('Comoving distances', {
                        #    'x' : z_range,
                        #    'ydict': OrderedDict([
                        #        ('Angular diameter $d_A(z)$',
                        #            distances_mdict['Comoving angular distance']),
                        #        #('Volume averaged $d_V(z)$',
                        #        #    distances_mdict['Comoving volume averaged distance']),
                        #        ('Hubble $d_H(z)$',
                        #            distances_mdict['Comoving Hubble distance']),
                        #        (r'Lookback time $c\,t(z)\left(1+z\right)$', 
                        #            distances_mdict['Comoving lookback time']\
                        #                    *speedoflight/1e3/976.480247152),
                        #        ]), 
                        #    'ysecond': OrderedDict([
                        #        ('Luminosity $d_L(z)$',
                        #            distances_mdict['Comoving luminosity distance']),
                        #        ]),
                        #    'title': title,
                        #    'map_species': self.map_species_abbrv,
                        #    'sec_weights': [2, 1],
                        #    }),
                        ('Distances', {
                            'x': z_range,
                            'ydict': OrderedDict([
                                ('Comoving distance $\chi(z)$',
                                    distances_mdict['Comoving angular distance']),
                                ('Angular diameter $d_A(z)$',
                                    distances_mdict['Angular distance']),
                                #('Volume averaged $d_V(z)$',
                                #    distances_mdict['Volume averaged distance']),
                                ('Hubble $d_H(z)$', 
                                    distances_mdict['Hubble distance']),
                                ('Lookback time $c\,t(z)$',
                                    distances_mdict['Lookback time']\
                                            *speedoflight/1e3/976.480247152),
                                ]),
                            'ysecond': OrderedDict([
                                ('Luminosity $d_L(z)$',
                                    distances_mdict['Luminosity distance']),
                                ]),
                            'title': title,
                            'map_species': self.map_species_abbrv,
                            'sec_weights': [2, 1],
                            }),
                        #('Adimensional distances', {
                        #    'x': z_range,
                        #    'ydict': OrderedDict([
                        #        ('Angular diameter $d_A(z)/d_H(z)$',
                        #            distances_mdict['Adimensional angular distance']),
                        #        ('Volume averaged $d_V(z)/d_H(z)$',
                        #            distances_mdict['Adimensional volume averaged distance']),
                        #        (r'Lookback time $c\,t(z)/d_H(z)$',
                        #            distances_mdict['Adimensional lookback time']\
                        #                    *speedoflight/1e3/976.480247152),
                        #        ]),
                        #    'ysecond': OrderedDict([
                        #        ('Luminosity $d_L(z)/d_H(z)$',
                        #            distances_mdict['Adimensional luminosity distance']),
                        #        ]),
                        #    'title': title,
                        #    'map_species': self.map_species_abbrv,
                        #    'sec_weights': [2, 1],
                        #    }),
                        ('Lookback time', {
                            'x': z_range, 
                            'ydict': OrderedDict([
                                ('Lookback time', distances_mdict['Lookback time']),
                                ('Age of the universe', distances_mdict['Age of the universe']),
                                ]),
                            'title': title,
                            }),
                        ])
                    )

        if self.show_tab('Equation of state'):
            self.cosmo_model.results.update(OrderedDict([
                ('Equation of state', {
                    'x': self.cosmo_model.a_range,
                    'ydict': eos_mdict,
                    'title': title,
                    'map_species': self.map_species_abbrv,
                    }),
                ]),
            )

        self.show_densities()
        config_all_widgets(self.corner_frame_buttons, state=tk.NORMAL)
        if self.show_tab('Distances'):
            self.add_model_to_list(self.cosmo_model, parameters)
        self.master.config(cursor='left_ptr')

    def add_model_to_list(self, model, parameter_space):
        model.calculated_point = parameter_space
        model_abbrv = model_abbrevation(self.map_model[model.model])
        if model in self.list_of_solved_models:
            i = self.list_of_solved_models.index(model)
            self.saved_models_listbox.delete(i)
            self.saved_models_listbox.insert(i, model_abbrv)
        else:
            config_all_widgets(self.saved_models_frame, state=tk.NORMAL)
            self.list_of_solved_models.append(model)
            self.saved_models_listbox.insert(tk.END, model_abbrv)

    def set_and_update_gif(self):
        model = self.map_model[self.model_options_combobox.get()]
        species = self.map_species_abbrv[self.interaction_propto_options.get()]
        sign = self.int_sign_combobox.get()
        if species == self.please_select_species or sign == '(sign)':
            img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                'blank.gif'))
            self.img_lbl.config(image=img)
            self.img_lbl.image = img
            return None
        if species == 'idm':
            if model == 'cde':
                img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                    'cde_propto_c_%s.gif' % sign))
            else:
                assert model == 'cde lambda'
                img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                    'ilambda_propto_c_%s.gif' % sign))
        elif species == 'ilambda':
            img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                'ilambda_propto_de_%s.gif' % sign))
        else:
            assert species == 'ide'
            img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                'cde_propto_de_%s.gif' % sign))
        self.img_lbl.config(image=img)
        self.img_lbl.image = img

    def show_optional_species(self, event):
        model = event.widget.get()
        model = self.map_model[model]
        self.mandatory_msg.config(text=self.please_select_model+'\n')
        self.optional_species_listbox.delete(0, tk.END)
        no_model = model == self.please_select_model
        cde_state = tk.NORMAL if 'cde' in model else tk.DISABLED
        cde_state_inverse = tk.DISABLED if 'cde' in model else tk.NORMAL
        config_all_widgets(self.darksector_and_build_frame,
                state=tk.DISABLED if no_model else tk.NORMAL)
        if no_model:
            img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                'blank.gif'))
            self.img_lbl.config(image=img)
            self.img_lbl.image = img
            self.derived_combobox['values'] = [self.please_select_species,]
            self.derived_combobox.current(0)
            self.derived_combobox.config(state=tk.DISABLED)
            self.derived_lbl.config(state=tk.DISABLED)
            return None

        # map species label and name
        self.map_species = OrderedDict([
                (self.please_select_model+'\n', self.please_select_model+'\n'),
                (self.please_select_species, self.please_select_species),
                ])
        self.map_species_abbrv = OrderedDict([
                (self.please_select_species, self.please_select_species),
                ])
        self.mandatory_species = eval(self.available_models[model]['mandatory species'])
        self.optional_species = eval(self.available_models[model]['supported optional species'])
        self.combined_species = eval(self.available_models[model].get('supported composed species', '[]'))
        for species in self.mandatory_species + self.optional_species + self.combined_species:
            name = self.available_species['name'].get(species)
            abbrv = self.available_species['abbreviation'].get(species, None)
            if abbrv:
                abbrv = abbrv.replace(r'$\Lambda$', 'Λ')
            self.map_species_abbrv[species] = abbrv or name
            abbrv = '' if abbrv is None else ' (%s)' % abbrv
            self.map_species[species] = name + abbrv
        remap(self.map_species_abbrv)
        remap(self.map_species)

        self.mandatory_msg.config(text='\n'.join([self.map_species[species] \
                for species in self.mandatory_species]))
        self.derived_combobox['values'] = [self.map_species_abbrv[species] for species in self.mandatory_species]
        self.derived_combobox.current(len(self.derived_combobox['values'])-1)
        self.derived_combobox.config(state='readonly')
        self.derived_lbl.config(state=tk.NORMAL)
        if 'cde' in model:
            self.combined_var.set(0)
            self.interaction_propto_options['values'] = [self.please_select_species,] + [self.map_species_abbrv[species] \
                    for species in self.mandatory_species]
        else:
            self.interaction_propto_options['values'] = [self.please_select_species,]
        self.interaction_propto_options.current(0)
        self.combined_option.config(state=cde_state_inverse)
        self.int_propto_label.config(state=cde_state)
        config_all_widgets(self.int_frame, state=cde_state)
        for option in self.optional_species:
            self.optional_species_listbox.insert(tk.END, self.map_species[option])

        img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files', 'blank.gif'))
        if model == 'lcdm':
            img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                'lcdm.gif'))
        elif model in ['wcdm', 'cpl', 'jbp', 'ba', 'lh', 'fnt2', 'fnt3']:
            img = tk.PhotoImage(file=os.path.join(EPIC.root, 'gui_files',
                'wde.gif'))
        self.img_lbl.config(image=img)
        self.img_lbl.image = img

    def show_tab(self, tab):
        return self.model_results_checkbuttons_var[tab].get() 

    def show_densities(self):

        if not hasattr(self, 'cosmo_model'):
            return None

        if not hasattr(self.cosmo_model, 'results'):
            return None 

        self.status_bar.config(text='Plotting...')
        self.status_bar.update()

        for plot_name, instructions in self.cosmo_model.results.items():
            self.model_solution_tabs_dict[plot_name].add_figure_to_widget(
                    **instructions)

        self.viewing = 'plots'
        self.status_bar.config(text='Done.')

def remap(d):
    d.update({v: k for k, v in d.items() if k != v})
        
def launch_gui(args, run_parser, analyze_parser, plot_parser,
        analyze_function):
    plt.rcdefaults()
    master = tk.Tk()
    app = Application(run_parser, analyze_parser, plot_parser,
            analyze_function, master=master, theme=args.theme)
    master.update_idletasks()
    w = master.winfo_width()
    h = master.winfo_height()
    W = master.winfo_screenwidth()
    H = master.winfo_screenheight()
    x = W//2 - w//2
    y = H//2 - h//2
    master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    master.mainloop()

def eos_get_function_mp(model_d, key, shared_dict, z, **kwargs):
    factor = kwargs.pop('factor', 1)
    shared_dict[key] = factor * model_d(z, **kwargs)

def select_first_visible(nb, order=1):
    for tab in nb.tabs()[::order]:
        if nb.tab(tab)['state'] == 'normal':
            nb.select(tab)
            return None

def config_all_widgets(w, **kwargs):
    for widget in w.winfo_children():
        try:
            widget.config(**kwargs)
            if isinstance(widget, EPIC_widgets.ReadonlyCombobox):
                if kwargs.get('state') == tk.NORMAL:
                    widget.config(state='readonly')
            elif isinstance(widget, EPIC_widgets.MyTextLabel):
                if 'state' in kwargs:
                    widget.config(state=tk.DISABLED)
        except tk.TclError:
            pass
        config_all_widgets(widget, **kwargs)

def model_abbrevation(name):
    abbrv = name.split('(', 1)
    if len(abbrv) == 1:
        return abbrv[0]
    return abbrv[1].split(')')[0]

def quote(value):
    if isinstance(value, str):
        return value.join(["'", "'"])
    return str(value)

def break_list(_list, ident=1):
    return '\n'.join(['['] + [' '*4*ident + quote(e) + ',' for e in _list] + [' '*4*ident + ']'])

def hide_tab(nb, tab):
    nb.hide(nb._nametowidget(tab.winfo_name()))
