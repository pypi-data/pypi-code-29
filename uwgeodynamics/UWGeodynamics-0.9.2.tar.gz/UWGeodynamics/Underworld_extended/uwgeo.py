    def load(self, filename):
        """
        Load the swarm variable from disk. This must be called *after* the swarm.load().

        Parameters
        ----------
        filename : str
            The filename for the saved file. Relative or absolute paths may be
            used, but all directories must exist.

        Notes
        -----
        This method must be called collectively by all processes.


        Example
        -------
        Refer to example provided for 'save' method.

        """

        if not isinstance(filename, str):
            raise TypeError("'filename' parameter must be of type 'str'")

        if self.swarm._checkpointMapsToState != self.swarm.stateId:
            raise RuntimeError("'Swarm' associate with this 'SwarmVariable' does not appear to be in the correct state.\n" \
                               "Please ensure that you have loaded the swarm prior to loading any swarm variables.")
        gIds = self.swarm._local2globalMap

        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()

        # open hdf5 file
        h5f = h5py.File(name=filename, mode="r", driver='mpio', comm=MPI.COMM_WORLD)

        # get units
        try:
            units = h5f.attrs["units"]
        except KeyError:
            units = None

        if units and units != "None":
            units = u.parse_expression(units)
        else:
            units = None

        dset = h5f.get('data')
        if dset == None:
            raise RuntimeError("Can't find 'data' in file '{}'.\n".format(filename))

        if dset.shape[1] != self.data.shape[1]:
            raise RuntimeError("Cannot load file data on current swarm. Data in file '{0}', " \
                               "has {1} components -the particlesCoords has {2} components".format(filename, dset.shape[1], self.particleCoordinates.data.shape[1]))

        particleGobalCount = self.swarm.particleGlobalCount

        if dset.shape[0] != particleGobalCount:
            if rank == 0:
                import warnings
                warnings.warn("Warning, it appears {} particles were loaded, but this h5 variable has {} data points". format(particleGobalCount, dset.shape[0]), RuntimeWarning)

        size = len(gIds) # number of local2global mapped indices
        if size > 0:     # only if there is a non-zero local2global do we load
            if units:
                vals = dset[gIds,:]
                self.data[:] = nonDimensionalize(vals * units)
            else:
                self.data[:] = dset[gIds,:]
        
        # for efficiency, we want to load swarmvariable data in the largest stride chunks possible.
        # we need to determine where required data is contiguous.
        # first construct an array of gradients. the required data is contiguous
        # where the indices into the array are increasing by 1, ie have a gradient of 1.
        gradIds = np.zeros_like(gIds)            # creates array of zeros of same size & type
        if len(gIds) > 1:
            gradIds[:-1] = gIds[1:] - gIds[:-1]  # forward difference type gradient

        guy = 0
        while guy < len(gIds):

            # do contiguous
            start_guy = guy
            while gradIds[guy]==1:  # count run of contiguous. note bounds check not required as last element of gradIds is always zero.
                guy += 1
            # copy contiguous chunk if found.. note that we are copying 'plus 1' items
            if guy > start_guy:
                self.data[start_guy:guy+1] = dset[gIds[start_guy]:gIds[guy]+1]
                guy += 1

            # do non-contiguous
            start_guy = guy
            while guy<len(gIds) and gradIds[guy]!=1:  # count run of non-contiguous
                guy += 1
            # copy non-contiguous items (if found) using index array slice
            if guy > start_guy:
                self.data[start_guy:guy,:] = dset[gIds[start_guy:guy],:]
                
            # repeat process until all done

        h5f.close();
