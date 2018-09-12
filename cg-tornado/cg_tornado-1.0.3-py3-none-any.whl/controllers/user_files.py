# employees_logic
import os
from base64 import encodebytes

from cg_tornado import CgDbLogic
from cg_tornado.models.data_models import UserFile
from cg_tornado.errors import ExceptionWithMessage, RequiredFieldMissing


class UserFiles(CgDbLogic):

    def prepare(self):
        self.Model = UserFile
        self.PublicMethods = ['Upload', 'List', 'Delete']

        super().prepare()

    def _returnFileTypeThroughMimeType(self, mimetype):
        fileType = 'other'
        if 'image' in mimetype:
            fileType = 'image'
        elif 'application' in mimetype:
            fileType = 'application'
        elif 'video' in mimetype:
            fileType = 'video'
        elif 'audio' in mimetype:
            fileType = 'audio'

        return fileType

    def _makeFileName(self, fileId):

        fName = encodebytes(bytes(str(fileId), 'utf-8'))
        fName = fName.decode('utf-8')
        fName = fName.replace('=', '')
        fName = fName.replace('\n', '')
        return fName

    def Upload(self):
        upFile = self.request.files['UserFile'][0]
        userFile = UserFile()
        userFile.user_id = self.User.user_id
        userFile.file_name = upFile['filename']
        userFile.file_size = len(upFile['body'])
        userFile.file_type = self._returnFileTypeThroughMimeType(upFile['content_type'])
        self.gdb.add(userFile)
        self.gdb.flush()

        destinationFolder = "{}/{}/".format(
            self.application.UserFilesRoot,
            self.User.user_id
        )

        if not os.path.exists(destinationFolder):
            os.makedirs(destinationFolder)

        fName = "{}{}".format(
            self._makeFileName(userFile.file_id),
            (os.path.splitext(userFile.file_name)[-1]).lower()
        )

        file_only_name, file_extension = os.path.splitext(userFile.file_name)
        userFile.file_ext = file_extension

        destinationFile = "{}/{}".format(destinationFolder, fName)

        with open(destinationFile, 'wb') as f:
            f.write(upFile['body'])

        userFile.file_url = "{}/files/{}/{}".format(self.application.BaseUrl, self.User.user_id, fName)

        data = {'oid': userFile.file_id, 'columns': ['file_id', 'file_name', 'file_ext',
                                                     'file_size', 'file_type', 'file_url']}

        ctrl = self._loadController(slug='user_files', data=data)
        resp = ctrl.Single()
        return resp

    def List(self):
        self.addTopWhere(column='user_id', value=self.User.user_id)
        return super().List()

    def Delete(self):
        if 'oid' not in self.Data:
            raise RequiredFieldMissing('oid')

        oids = self.Data['oid']

        if not isinstance(oids, list):
            oids = [oids]

        for oid in oids:
            query = self.gdb.query(UserFile).filter(UserFile.file_id == oid)
            query = query.filter(UserFile.user_id == self.User.user_id)
            file = query.one_or_none()

            if file is not None:

                srcFolder = "{}/{}".format(
                    self.application.UserFilesRoot,
                    self.User.user_id
                )

                srcFile = "{}/{}{}".format(srcFolder,
                                           self._makeFileName(file.file_id),
                                           (os.path.splitext(file.file_name)[-1]).lower())

                if os.path.isfile(srcFile):
                    os.unlink(srcFile)
                    self.gdb.delete(file)

                else:
                    print("File Not Found to Delete", srcFile)
                    self.gdb.delete(file)  # remove redundant entry from database

            else:
                raise ExceptionWithMessage('File id: {} not found!'.format(oid))

        return self.Data['oid']
