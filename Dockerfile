# FROM ubuntu:16.04

# # Pick up some TF dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#         build-essential \
#         curl \
#         libfreetype6-dev \
#         libhdf5-serial-dev \
#         libpng12-dev \
#         libzmq3-dev \
#         pkg-config \
#         python3 \
#         python3-pip \
#         python3-setuptools \
#         python3-tk \
#         software-properties-common \
#         rsync \
#         git \
#         rsync \
#         software-properties-common \
#         unzip \
#         && \
#         apt-get clean && \
#         rm -rf /var/lib/apt/lists/*

# #Install AWS-CLI
# # RUN python3 -m pip install --no-cache-dir --trusted-host pypi.python.org awscli
# RUN python3 pip install 

# WORKDIR "/app"
# # ADD requirements.txt /app/requirements.txt

# # Install tensorflow/numpy etc
# RUN python3 -m pip install --no-cache-dir --trusted-host pypi.python.org tensorflow -r requirements.txt

# # Generate synthetic data for testing
# ADD generate_synthetic_waveforms.py generate_synthetic_waveforms.py  
# RUN mkdir -p data
# RUN python3 generate_synthetic_waveforms.py --num_train 200 --num_valid 40 --num_test 80

# # TensorBoard
# EXPOSE 6006

# # IPython
# EXPOSE 8888

# # Copy the current directory contents into the container at /app
# ADD . /app

# CMD ["bash", "run.sh"]

FROM python:3.6

COPY ./requirements.txt . 

RUN python -m pip install -r requirements.txt

COPY . .

# CMD ["python", "nnclassification.py"]
CMD ["python", "printfs.py"]
