from ixnetwork_restpy.base import Base
from ixnetwork_restpy.errors import IxNetworkError


class Sessions(Base):
    """Access the /sessions hierarchy.
    
    Provides the following functionality:
        get /sessions instances
        get/set properties on /sessions instances
        execute methods on /sessions instances
        get /sessions child nodes.

    Example:
        TestPlatform('localhost').add_Sessions()
    """
    _SDM_NAME = 'sessions'
    
    def __init__(self, parent):
        """The current session"""
        super(Sessions, self).__init__(parent)

    @property
    def Ixnetwork(self):
        """The root object of the configuration hierarchy
        
        Returns: 
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork.Ixnetwork)
        
        Raises:
            ServerError:
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
        ixnetwork = Ixnetwork(self)
        ixnetwork._set_properties(ixnetwork._connection._read('%s/%s' % (self.href, Ixnetwork._SDM_NAME)))
        return ixnetwork
    
    @property
    def State(self):
        """The state of the session

        Returns:
            str
        """
        return self._properties['state'].upper()
    
    @property
    def ApplicationType(self):
        """The application type of the session

        Returns:
            str
        """
        return self._properties['applicationType']
    
    @property
    def Id(self):
        """The id of the session

        Returns:
            number
        """
        return self._properties['id']
    
    @property
    def UserId(self):
        """The user id of the session

        Returns:
            str
        """
        return self._properties['userId']
    
    @property
    def UserName(self):
        """The user name of the session

        Returns:
            str
        """
        return self._properties['userName']

    def _start(self):
        """Starts the session

        Returns:
            None
        """
        if self.State == 'INITIAL':
            self._execute('start', payload={'applicationType': self.ApplicationType})
    
    def find(self, Id=None):
        """Finds all child instances of Sessions on the server.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        sessions = self._connection._read('%s/%s' % (self.parent.href, self._SDM_NAME))
        self._clear()
        for session in sessions:
            if Id is not None:
                if session['id'] == Id:
                    self._set_properties(session)
            else:
                self._set_properties(session)
        return self

    def add(self):
        """Adds a child instance of Sessions on the server.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes a child instance of Sessions on the server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        try:
            self._execute('stop?deleteAfterStop=true')
        except IxNetworkError as e:
            if e._status_code not in [404, 405]:
                raise e