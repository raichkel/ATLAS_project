# base on latest python image
FROM python:latest

# add our python program
ADD main_input.py ./
ADD infofile.py ./
# install dependent libraries
RUN pip install numpy 
RUN pip install matplotlib
RUN pip install uproot
RUN pip install awkward
RUN pip install vector


# the command to run our program
CMD [ "python", "./main_input.py"]