# UC2 pipeline using xenon-flow 

This is an instance of the LOFAR pipeline template into the LOFAR rest API (https://github.com/EOSC-LOFAR/lofar_workflow_api). 

The run_pipeline() function is modified to allow the inclusion of a third parameter to pass a calibrator observation along with the target becoming run_pipeline(observation1, observation2, \*\*kargs). 

It uses xenon-flow to start the computations on a given cluster using xenon and CWL.

The step-by-step guide to add a pipeline to  the LOFAR rest API is given [here](https://github.com/EOSC-LOFAR/LOFAR_pipeline_template).



