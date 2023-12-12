# base on latest python image
FROM python:latest

# add our python program
ADD higgs_script.py ./
ADD infofile.py ./
# install dependent libraries
RUN pip install numpy 
RUN pip install matplotlib
RUN pip install uproot
RUN pip install awkward
RUN pip install vector
# RUN pip install time
#RUN pip install math
# the command to run our program
CMD [ "python", "./higgs_script.py"]