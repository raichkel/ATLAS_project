# base on latest python image
FROM python:latest

# add our python program
ADD worker.py ./
ADD infofile.py ./
# install dependent libraries
RUN pip install numpy 
RUN pip install matplotlib
RUN pip install uproot
RUN pip install awkward
RUN pip install vector
RUN pip install pika
# some modules that made awkward break if I didn't have them...
RUN pip install pyarrow
RUN pip install fsspec
RUN pip install fcntl


# the command to run our program
CMD [ "python", "./worker.py"]