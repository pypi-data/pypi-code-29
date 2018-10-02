# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging

import pyforms as app
from confapp import conf
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pyforms.controls import ControlCheckBoxList
from pybpodgui_api.models.subject import Subject

logger = logging.getLogger(__name__)


class SubjectWindow(Subject, BaseWidget):
	"""
	Define here which fields from the board model should appear on the details section.

	The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

	You may also assign actions to these components.

	**Properties**

		name
			:class:`string`

			Name associated with this board. Returns the current value stored in the :py:attr:`_name` text field.

		serial_port
			:class:`string`

			Serial port associated with this board. Returns the current value stored in the :py:attr:`_serial_port` text field.


	**Private attributes**

		_name
			:class:`pyforms.controls.ControlText`

			Text field to edit board name. Editing this field fires the event :meth:`BoardWindow._BoardWindow__name_changed_evt`.

		_serial_port
			:class:`pyforms.controls.ControlText`

			Text field to edit serial port. Editing this field fires the event :meth:`BoardWindow._BoardWindow__serial_changed_evt`.

		_log_btn
			:class:`pyforms.controls.ControlButton`

			Button to show this board events on a console window. Pressing the button fires the event :class:`BoardDockWindow.open_log_window`.

		_formset
			Describe window fields organization to PyForms.

	**Methods**

	"""

	def __init__(self, project=None):
		"""

		:param project: project where this board belongs
		:type project: pycontrolgui.models.project.Project
		"""
		BaseWidget.__init__(self, 'Subject')
		self.layout().setContentsMargins(5,10,5,5)

		self._selected_setup = None

		self._name 	= ControlText('Name')
		self._setups = ControlCombo('Setup')
		self._run = ControlButton('Run',checkable = True, default=self.__run_task)
		self._stoptrial_btn = ControlButton('Stop trial', default=self._stop_trial_evt)
		self._pause_btn     = ControlButton('Pause', checkable=True, default=self._pause_evt)

		Subject.__init__(self, project)

		self._formset = [
			'_name',
			'_setups',
			'_run',
			('_stoptrial_btn','_pause_btn'),
			' ',
		]

		self._name.changed_event 		= self.__name_changed_evt
		self.reload_setups()

	def _stop_trial_evt(self):
		setup = self._setups.value
		if setup is not None:
			setup._stop_trial_evt()

	def _pause_evt(self):
		setup = self._setups.value
		if setup:
			setup._pause_evt()
			
	def _run_task(self):
		setup = self._setups.value
		if setup:
			setup.clear_subjects()
			setup += self
			setup._run_task()

	def __run_task(self):
		setup = self._setups.value
		if setup:
			if setup.status == setup.STATUS_READY:
				setup.clear_subjects()
				setup += self
			setup._run_task()
		else:
			self._run.checked = False

	#def _setup_changed_evt(self):
	#	self._selected_setup = self._setups.value

	def reload_setups(self):		
		self._setups.clear()
		self._setups.add_item('',0)
		#return
		for experiment in self.project.experiments:
			for setup in experiment.setups:
				self._setups.add_item(setup.name, setup)
		self._setups.current_index = 0

	def __name_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_name`.

		This methods is called every time the user changes the field.
		"""
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recursive calls when editing the name text field
		self._name.value = value
		self._update_name = False

# Execute the application
if __name__ == "__main__":
	app.start_app(SubjectWindow)
