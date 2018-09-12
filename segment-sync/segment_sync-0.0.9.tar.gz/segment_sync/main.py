import sys
import os
import fnmatch
import json
import shutil
from PyQt5 import QtWidgets, QtCore
from segment_sync import mainwindow


class SyncThread(QtCore.QThread):
    progress_changed = QtCore.pyqtSignal(int, int)
    sync_aborted = QtCore.pyqtSignal(str)
    sync_finished = QtCore.pyqtSignal()

    def __init__(self, src, dst, files, parent=None):
        super(SyncThread, self).__init__(parent)
        self.src = src
        self.dst = dst
        self.files = files

    def __del__(self):
        self.wait()

    def run(self):
        index = 0
        size = len(self.files)
        for file in self.files:
            src_path = os.path.join(self.src, file)
            dst_path = os.path.join(self.dst, file)
            try:
                shutil.copyfile(src_path, dst_path)
            except Exception as e:
                self.sync_aborted.emit(str(e))
                return
            index += 1
            self.progress_changed.emit(index, size)
        self.sync_finished.emit()


class SegmentSyncApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, config):
        super().__init__()
        self.setupUi(self)
        self.refreshListPushButton.clicked.connect(self.on_refresh_list_clicked)
        self.syncSelectedPushButton.clicked.connect(self.on_sync_selected_clicked)

        self.sync_thread = None
        self.config = config

        if not self.config:
            self.set_enable_ui(False)
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Config file not allowed!')
        else:
            self.src_share_url = self.config['ProductionShare']
            self.dst_share_urls = self.config['TestShares']
            for item in self.dst_share_urls:
                self.comboBox.addItem(item)

        self.metadata = []
        self.on_refresh_list_clicked()

        self.comboBox.currentIndexChanged.connect(self.on_combobox_current_index_changed)
        self.selected_dst_share_url = None

    def load_metadata(self):
        self.metadata.clear()
        segments_metadata_files_list = fnmatch.filter(os.listdir(self.src_share_url), '*.json')
        for segment_metadata in segments_metadata_files_list:
            with open(os.path.join(self.src_share_url, segment_metadata), encoding="utf-8") as f:
                metadata = json.load(f)
                self.metadata.append(metadata)

    def set_enable_ui(self, flag):
        self.syncSelectedPushButton.setEnabled(flag)
        self.getSegmentsListPushButton.setEnabled(flag)

    def on_refresh_list_clicked(self):
        self.load_metadata()
        self.listWidget.clear()
        for metadata in self.metadata:
            self.listWidget.addItem(metadata['segment_name'])
        self.listWidget.sortItems()

    def on_sync_selected_clicked(self):
        if not self.listWidget.currentItem():
            return

        selected_segment_name = self.listWidget.currentItem().text()

        files_list = []
        for metadata in self.metadata:
            if metadata['segment_name'] == selected_segment_name:
                files_list.append(metadata['segment_name_lat'] + '.json')
                files_list.append(metadata['segment_name_lat'] + '.zip')
                files_list.append(metadata['segment_name_lat'] + '.data.sqlite')
                files_list.append(metadata['segment_name_lat'] + 'versions.data.sqlite')

        self.set_enable_ui(False)

        self.sync_thread = SyncThread(self.src_share_url, self.selected_dst_share_url, files_list, self)
        self.sync_thread.progress_changed.connect(self.progress_changed)
        self.sync_thread.sync_finished.connect(self.sync_finished)
        self.sync_thread.sync_aborted.connect(self.sync_aborted)
        self.sync_thread.start()

    def on_combobox_current_index_changed(self, index):
        self.selected_dst_share_url = self.comboBox.currentText()

    def progress_changed(self, index, size):
        self.progressBar.setRange(0, size)
        self.progressBar.setValue(index)

    def sync_finished(self):
        QtWidgets.QMessageBox.about(self, 'Done', 'Sync complete!')
        self.progressBar.setValue(0)
        self.set_enable_ui(True)

    def sync_aborted(self, message):
        QtWidgets.QMessageBox.critical(self, 'Error', message)
        self.progressBar.setValue(0)
        self.set_enable_ui(True)


def main():
    qt_app = QtWidgets.QApplication(sys.argv)
    config_path = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else \
        os.path.join(os.path.expanduser('~'), 'SegmentSync', 'segment_sync_conf.json')

    try:
        with open(config_path) as json_config_file:
            config = json.load(json_config_file)
    except Exception as e:
        config = None

    window = SegmentSyncApp(config)
    window.show()
    qt_app.exec_()
