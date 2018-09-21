from modelestimator._bw_estimator.bw_estimator import bw_estimator
from modelestimator._handle_input.handle_input_file import handle_input_file
from modelestimator._bootstraper.bootstraper import bootstraper

def controller(FORMAT, BOOTSTRAP, RESAMPLINGS, threshold, FILE_NAME_LIST):
    MULTIALIGNMENT_LIST = []
    
    for FILE in FILE_NAME_LIST:
        MULTIALIGNMENT = handle_input_file(FILE, FORMAT)
        MULTIALIGNMENT_LIST.append(MULTIALIGNMENT) 
        
    if threshold == None:
        threshold = 0.001
    
    if BOOTSTRAP:
        MULTIALIGNMENT = MULTIALIGNMENT_LIST[0]
        BOOTSTRAP_NORM,_ = bootstraper(RESAMPLINGS, threshold, MULTIALIGNMENT)
        OUTPUT_STRING = "Bootstrap norm = " + str(BOOTSTRAP_NORM)
    else:
        Q, EQ = bw_estimator(threshold, MULTIALIGNMENT_LIST)
        OUTPUT_STRING = "Q =\n" + str(Q) + "\nEQ =\n" + str(EQ)   

    return OUTPUT_STRING