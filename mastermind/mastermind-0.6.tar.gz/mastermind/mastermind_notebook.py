# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @author: Nicolas Houlier

import random
import ipywidgets as wd
from IPython.display import display
from notebook_toggle_code import ToggleCode
import os


class MastermindNotebook:
    """
    Play a game of mastermind directly into a jupyter notebook !
    """

    def __init__(self, answer: list = None):
        """
        This constructor will display the gui of the mastermid game

        Args:
            answer (list, optional): Defaults to None. The list of 4 digit corresponding to the good answer. 
            If None, the code will choose a combination randomly
        """

        ToggleCode().add_js()

        self.answer = [
            random.randint(1, 4) for j in range(4)] if not answer else answer

        answer_colors_list = list()
        arrows_list = list()

        for _ in range(4):
            mystery = wd.Button(disabled=True, button_style='primary')
            mystery.icon = 'question'
            mystery.style.button_color = '#4B4A4E'
            answer_colors_list.append(mystery)

            arrow = wd.Button(disabled=True)
            arrow.icon = 'arrow-up'
            arrow.style.button_color = 'white'
            arrows_list.append(arrow)

        path_logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img/logo_notebook.png')
        self.logo_widget = wd.Image(value=open(path_logo, 'rb').read(), layout={
            'width': '197px', 'height': '69px', 'margin': '0px 0px 0px 70px'})

        self.answer_box = wd.HBox(answer_colors_list, layout={
                                  'margin': '20px 0px 0px 0px'})

        self.arrows_box = wd.HBox(arrows_list)

        self.trials = wd.VBox([wd.HBox([wd.VBox([self.answer_box, self.arrows_box]), self.logo_widget], layout={
                              'margin': '0px 0px 20px 0px'})], layout={'margin': '20px 0px 0px 0px'})
        self.selectors = wd.HBox()
        self.user_interact = wd.HBox(layout={'margin': '20px 0px 20px 0px'})
        self.console = wd.HBox()
        self.game_container = wd.VBox(
            [self.trials, self.user_interact, self.console])

        self.mastermind_container = wd.Tab(children=[self.game_container])
        self.mastermind_container.set_title(0, 'Mastermind')

        self.confirm_button = wd.Button(description='Confirm combination', layout={
                                        'width': '252px', 'margin': '2px 0px 0px 50px'}, button_style='primary')
        self.confirm_button.icon = 'check'

        self.new_game_button = wd.Button(description='New game', layout={
                                         'margin': '0px 0px 0px 20px'})
        self.new_game_button.icon = 'refresh'

        self.new_game_button.on_click(self.new_game_function())

        self.turn = 0
        self.duplicate = []
        self.avoid = []
        self.already_checked = []
        self.try_return = {'well_placed': 0, 'misplaced': 0}

        self.mapping_colors = {1: 'warning',
                               2: 'danger', 3: 'primary', 4: 'success'}

        self.create_gui()

        display(self.mastermind_container)

    def create_gui(self):
        """
        This function create all ipywidgets necessary to the game
        """

        selectors_widgets = list()

        for n in range(4):

            selectors_widgets.append(wd.Dropdown(
                options={'': 0, 'Orange': 1, 'Red': 2, 'Blue': 3, 'Green': 4},
                value=0,
                disabled=False,
                layout={'width': '148px'}
            ))

        self.confirm_button.on_click(
            self.create_combination_and_rate_function())
        self.user_interact.children = [self.selectors, self.confirm_button]

        self.selectors.children = selectors_widgets

    def check_combination(self, combination):
        """
        This function will compute haw many digits are misplaced and well placed
        in a combination proposed by the user compared to the true answer

        Args:
            combination (list): a list containing the 4 digits proposed by the user
        """

        # we first check if there are any pieces of the right value well placed.
        for j in range(0, 4):
            if combination[j] == self.answer[j]:
                self.try_return['well_placed'] += 1
                self.already_checked += [combination[j]]
                self.avoid += [j]

        for p in range(0, 4):
            for s in range(0, 4):
                if not p in self.avoid:
                    if combination[s] == self.answer[p] and not combination[s] in self.already_checked:

                        self.try_return['misplaced'] += 1
                        self.duplicate += [combination[s]]
                        if self.duplicate.count(combination[s]) > 1:
                            self.try_return['misplaced'] -= 1

    def new_game_function(self):
        """
        Return a function that will be assigned to a button

        Returns:
           new_game (function) : Create a new game by setting to default all changed attributes of the class
        """

        def new_game(_):

            self.console.children = []

            self.answer = [random.randint(1, 4) for j in range(4)]

            self.trials.children = [wd.HBox([wd.VBox(
                [self.answer_box, self.arrows_box]), self.logo_widget], layout={'margin': '0px 0px 20px 0px'})]
            self.turn = 0
            for selector in self.selectors.children:
                selector.disabled = False
            self.confirm_button.disabled = False
            self.try_return = {'well_placed': 0, 'misplaced': 0}

            for button in self.answer_box.children:
                button.icon = 'question'
                button.style.button_color = '#4B4A4E'

        return new_game

    def create_combination_and_rate_function(self):
        """
        Return a function that will be assigned to a button

        Returns:
            create_combination_and_rate (function): this function create a combination of colors from 
            the for dropdowns of the game and rate this combination following the rules of the mastermind
        """

        def create_combination_and_rate(_):

            self.console.children = []

            selection = wd.HBox()

            selection_widgets = list()
            if not 0 in (dropdown.value for dropdown in self.selectors.children):

                self.turn += 1

                user_try = list()

                for selector in self.selectors.children:

                    color = wd.Button(
                        disabled=True, button_style=self.mapping_colors[selector.value])
                    color.icon = 'user-o'

                    selection_widgets.append(color)

                    user_try.append(selector.value)
                    selector.value = 0

                self.duplicate = []
                self.avoid = []
                self.already_checked = []

                self.check_combination(combination=user_try)

                info = wd.Button(description='Turn {0} - Well placed: {1} \n - Misplaced: {2}'.format(self.turn,
                                                                                                      self.try_return['well_placed'], self.try_return['misplaced']),
                                 disabled=True,
                                 layout={'width': 'auto',
                                         'margin': '0px 0px 0px 50px'}
                                 )

                info.icon = 'hashtag'

                selection_widgets.append(info)

                # see if the player wins.
                if self.try_return == {'well_placed': 4, 'misplaced': 0}:

                    self.console.children = [
                        wd.Label(value='You won !'), self.new_game_button]

                    self.display_correct_answer(failed=False)

                    for selector in self.selectors.children:
                        selector.disabled = True
                    self.confirm_button.disabled = True

                else:  # if the player has not won, we reset the counter of well/misplaced checkers and wait 7 seconds
                    # before asking for another attempt.
                    if self.turn == 12:

                        self.console.children = [
                            wd.Label(value='You loose !'),  self.new_game_button]

                        self.display_correct_answer()

                        for selector in self.selectors.children:
                            selector.disabled = True
                        self.confirm_button.disabled = True

                    else:
                        self.try_return = {'well_placed': 0, 'misplaced': 0}

            else:
                self.console.children = [
                    wd.Label(value='Please choose a color for every positions !')]

            selection.children = selection_widgets

            trials_children = list(self.trials.children)
            trials_children.insert(1, selection)

            self.trials.children = trials_children

        return create_combination_and_rate

    def display_correct_answer(self, failed: bool = True):

        new_answer_widgets = list()

        for position, _ in enumerate(self.answer_box.children):
            revealed = wd.Button(
                disabled=True, button_style=self.mapping_colors[self.answer[position]])
            if failed:
                revealed.icon = 'close'
            else:
                revealed.icon = 'check-square-o'
            new_answer_widgets.append(revealed)

        self.answer_box.children = new_answer_widgets
