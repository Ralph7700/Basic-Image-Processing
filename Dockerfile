FROM python:3

ADD OpenCVtest.py /
ADD pillowtest.py /

RUN pip3 install -r requirements.txt

CMD [ "python", "./OpenCVtest.py" ]
CMD [ "python", "./pillowtest.py" ]