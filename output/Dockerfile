# base on latest python image
FROM python:latest

# add our python program
ADD output.py ./
ADD infofile.py ./
# install dependent libraries
RUN pip install numpy 
RUN pip install matplotlib
RUN pip install uproot
RUN pip install awkward
RUN pip install vector
#RUN pip install os
RUN pip install pika
RUN pip install pyarrow
RUN pip install fsspec
# the command to run our program
CMD [ "python", "./output.py"]