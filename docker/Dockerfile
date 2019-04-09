FROM ubuntu/bionic

WORKDIR /root

RUN apt-get update

RUN apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        curl \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python \
        python-pip \
        python-setuptools \
        
        
RUN wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh \
    bash ~/Downloads/Anaconda2-2019.03-Linux-x86_64.sh

# generate training data
RUN git clone https://github.com/karaninder/Face2Face.git \
    cd Face2Face/training/ \
    conda env create -f environment.yml \
    wget https://dl.dropboxusercontent.com/s/2g04onlkmkq9c69/angela_merkel_speech.mp4 \
    wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 \
    python generate_train_data.py --file angela_merkel_speech.mp4 --num 400 --landmark-model shape_predictor_68_face_landmarks.dat \
    cd .. \

# train model

RUN cd external \
    mkdir photos \
    cd .. \
    mv training/landmarks training/original external/photos \
    cd external \
    python tools/process.py \
  	--input_dir photos/original \
  	--operation resize \
  	--output_dir photos/original_resized \
    python tools/process.py \
  	--input_dir photos/landmarks \
  	--operation resize \
  	--output_dir photos/landmarks_resized \
    python tools/process.py \
  	--input_dir photos/landmarks_resized \
  	--b_dir photos/original_resized \
  	--operation combine \
  	--output_dir photos/combined \
    python tools/split.py \
  	--dir photos/combined \
    python pix2pix.py \
	  --mode train \
	  --output_dir face2face-model \
	  --max_epochs 200 \
	  --input_dir photos/combined/train \
	  --which_direction AtoB \

# export model and run

RUN cd .. \
    cd training \
    python reduce_model.py --model-input face2face-model --model-output face2face-reduced-model \
    python freeze_model.py --model-folder face2face-reduced-model \
    python run_webcam.py --source 0 --show 0 --landmark-model shape_predictor_68_face_landmarks.dat --tf-model face2face-reduced-model/frozen_model.pb \

