from subprocess import run, PIPE, STDOUT, CalledProcessError
import os
import webbrowser

from foliant.utils import spinner
from foliant.backends.pandoc import Backend

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Backend(Backend):

    targets = ('gdoc')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gdoc_config = self.config.get('backend_config', {}).get('gdoc', {})
        self._slug = f'{self._pandoc_config.get("slug", self.get_slug())}'

        self.logger = self.logger.getChild('gdoc')
        self.logger.debug(f'Backend inited: {self.__dict__}')

    def _create_the_doc(self):
        with spinner('Making docx with Pandoc', self.logger, self.quiet):
            try:
                command = self._get_docx_command()
                self.logger.debug('Creating the doc.')
                run(command, shell=True, check=True, stdout=PIPE, stderr=STDOUT)

            except CalledProcessError as exception:
                raise RuntimeError(f'Build failed: {exception.output.decode()}')

            except Exception as exception:
                raise type(exception)(f'Build failed: {exception}')

    def _gdrive_auth(self):
        gauth = GoogleAuth()

        if True:  # Used while debugging to reduce amount of new tabs
            gauth.LocalWebserverAuth()
            self._gdrive = GoogleDrive(gauth)
        else:
            gauth.LoadCredentialsFile('client_creds.txt')

            if gauth.credentials is None:
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
                gauth.Refresh()
            else:
                gauth.Authorize()

            gauth.SaveCredentialsFile('client_creds.txt')
            self._gdrive = GoogleDrive(gauth)

    def _create_gdrive_folder(self):

        if not self._gdoc_config['gdrive_folder_id']:
            folder = self._gdrive.CreateFile({'title': self._gdoc_config['gdrive_folder_name'], 'mimeType': 'application/vnd.google-apps.folder'})
            folder.Upload()
            self._gdoc_config['gdrive_folder_id'] = folder['id']


    def _upload_file(self):
        if self._gdoc_config['gdoc_title']:
            title = self._gdoc_config['gdoc_title']
        else:
            title = self._slug
        
        if self._gdoc_config['gdoc_id']:
            upload_file = self._gdrive.CreateFile({'title': title, 'id': self._gdoc_config['gdoc_id'], 'parents': [{'id': self._gdoc_config['gdrive_folder_id']}], 'mimeType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})
        else:
            upload_file = self._gdrive.CreateFile({'title': title, 'parents': [{'id': self._gdoc_config['gdrive_folder_id']}], 'mimeType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})

        upload_file.SetContentFile('/'.join((os.getcwd(), f'{self._slug}.docx')))
        upload_file.Upload(param={'convert': True})

        self._gdoc_config['gdoc_id'] = upload_file['id']
        self._gdoc_link = upload_file['alternateLink']

        webbrowser.open(self._gdoc_link)

    def make(self, target):
        self._create_the_doc()

        self._gdrive_auth()

        self._create_gdrive_folder()

        self._upload_file()

        return f"\nDoc link: {self._gdoc_link}\n\
Google drive folder ID: {self._gdoc_config['gdrive_folder_id']}\n\
Google document ID: {self._gdoc_config['gdoc_id']}"
