#!/usr/bin/env python3

import sys

from mlprocessors.registry import registry, register_processor

registry.namespace = "spyking_circus"

from mlprocessors.core import Input, Output, Processor, IntegerParameter, FloatParameter, StringParameter, IntegerListParameter

import os
from shutil import copyfile
import subprocess, shlex
import h5py
from mountainlab_pytools import mdaio
import numpy as np

def sc_results_to_firings(hdf5_path):
    X=h5py.File(hdf5_path,'r');
    spiketimes=X.get('spiketimes')
    names=list(spiketimes.keys())
    clusters=[]
    for j in range(len(names)):
        times0=spiketimes.get(names[j])
        clusters.append(dict(
            k=j+1,
            times=times0
        ))
    times_list=[]
    labels_list=[]
    for cluster in clusters:
        times0=cluster['times']
        k=cluster['k']
        times_list.append(times0)
        labels_list.append(np.ones(times0.shape)*k)
    times=np.concatenate(times_list)
    labels=np.concatenate(labels_list)
    
    sort_inds=np.argsort(times)
    times=times[sort_inds]
    labels=labels[sort_inds]
    
    L=len(times)
    firings=np.zeros((3,L))
    firings[1,:]=times
    firings[2,:]=labels
    return firings

@register_processor(registry)
class sort(Processor):
    """
        Spike sorting using SpyKING Circus
    """
    VERSION='0.1.2'

    timeseries = Input('Input timeseries .mda file (MxN) M=number of channels, N=number of timepoints')
    geom       = Input('Probe geometry .csv file')
    firings_out = Output('Output firings .mda file (3xL) where 3 is number of events. Second and third rows are the times and labels.')

    samplerate = FloatParameter('Sample rate of the timeseries (Hz)')
    spike_thresh = FloatParameter('Threshold for detection',optional=True,default=6)
    detect_sign = IntegerParameter('Polarity of the spikes, -1, 0, or 1')
    adjacency_radius = IntegerParameter('Channel neighborhood adjacency radius corresponding to geom file')
    template_width_ms = FloatParameter('Spyking circus parameter',optional=True,default=3)
    whitening_max_elts = IntegerParameter('Spyking circus parameter - I believe it relates to subsampling and affects compute time',optional=True,default=1000)
    clustering_max_elts = IntegerParameter('Spyking circus parameter - I believe it relates to subsampling and affects compute time',optional=True,default=10000)
    
    def _read_text_file(self,fname):
        with open(fname) as f:
            return f.read()
        
    def _write_text_file(self,fname,str):
        with open(fname,'w') as f:
            f.write(str)
            
    def _run_command_and_print_output(self,command):
        with subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            while True:
                output_stdout= process.stdout.readline()
                output_stderr = process.stderr.readline()
                if (not output_stdout) and (not output_stderr) and (process.poll() is not None):
                    break
                if output_stdout:
                    print(output_stdout.decode())
                if output_stderr:
                    print(output_stderr.decode())
            rc = process.poll()
            return rc

    def run(self):
        tmpdir=os.environ.get('ML_PROCESSOR_TEMPDIR')
        if not tmpdir:
            raise Exception('Environment variable not set: ML_PROCESSOR_TEMPDIR')
        
        source_dir=os.path.dirname(os.path.realpath(__file__))
        
        ## todo: link rather than copy
        print('Copying timeseries file: {} -> {}'.format(self.timeseries,tmpdir+'/raw.mda'))
        copyfile(self.timeseries,tmpdir+'/raw.mda')
        
        print('Reading timeseries header...')
        HH=mdaio.readmda_header(tmpdir+'/raw.mda')
        num_channels=HH.dims[0]
        num_timepoints=HH.dims[1]
        duration_minutes=num_timepoints/self.samplerate/60
        print('Num. channels = {}, Num. timepoints = {}, duration = {} minutes'.format(num_channels,num_timepoints,duration_minutes))
        
        print('Creating .prb file...')
        prb_text=self._read_text_file(source_dir+'/template.prb')
        prb_text=prb_text.replace('$num_channels$','{}'.format(num_channels))
        prb_text=prb_text.replace('$radius$','{}'.format(self.adjacency_radius))
        geom=np.genfromtxt(self.geom, delimiter=',')
        geom_str='{\n'
        for m in range(geom.shape[0]):
            geom_str+='  {}: [{},{}],\n'.format(m,geom[m,0],geom[m,1]) # todo: handle 3d geom
        geom_str+='}'
        prb_text=prb_text.replace('$geometry$','{}'.format(geom_str))
        self._write_text_file(tmpdir+'/geometry.prb',prb_text)
        
        print('Creating .params file...')
        txt=self._read_text_file(source_dir+'/template.params')
        txt=txt.replace('$header_size$','{}'.format(HH.header_size))
        txt=txt.replace('$prb_file$',tmpdir+'/geometry.prb')
        txt=txt.replace('$dtype$',HH.dt)
        txt=txt.replace('$num_channels$','{}'.format(num_channels))
        txt=txt.replace('$samplerate$','{}'.format(self.samplerate))
        txt=txt.replace('$template_width_ms$','{}'.format(self.template_width_ms))
        txt=txt.replace('$spike_thresh$','{}'.format(self.spike_thresh))
        if self.detect_sign>0:
            peaks_str='positive'
        elif self.detect_sign<0:
            peaks_str='negative'
        else:
            peaks_str='both'
        txt=txt.replace('$peaks$',peaks_str)
        txt=txt.replace('$whitening_max_elts$','{}'.format(self.whitening_max_elts))
        txt=txt.replace('$clustering_max_elts$','{}'.format(self.clustering_max_elts))
        self._write_text_file(tmpdir+'/raw.params',txt)
        
        print('Running spyking circus...')
        #num_threads=np.maximum(1,int(os.cpu_count()/2))
        num_threads=1 # for some reason, using more than 1 thread causes an error
        cmd='spyking-circus {} -c {} '.format(tmpdir+'/raw.mda',num_threads)
        print(cmd)
        retcode=self._run_command_and_print_output(cmd)

        if retcode != 0:
            raise Exception('Spyking circus returned a non-zero exit code')

        result_fname=tmpdir+'/raw/raw.result.hdf5'
        if not os.path.exists(result_fname):
            raise Exception('Result file does not exist: '+result_fname)
        
        firings=sc_results_to_firings(result_fname)
        print(firings.shape)
        mdaio.writemda64(firings,self.firings_out)
        
        return True

if __name__ == "__main__":
    registry.process(sys.argv)
