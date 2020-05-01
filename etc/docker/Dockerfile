# Dependencies container
FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04 AS dependencies

WORKDIR /tmp/
ADD bootstrap.sh .
RUN bash bootstrap.sh  \
  && rm -f bootstrap.sh

RUN apt purge -y python3-pip python-pip                      \
  && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python3 get-pip.py                                      \
  && rm -f get-pip.py


RUN pip3 uninstall --yes conan \
 && pip3 uninstall --yes conan_package_tools \
 && rm -rf /root/.conan \
 && pip3 install conan \
 && pip3 install conan_package_tools \
 && conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan \
 && conan remote add is https://api.bintray.com/conan/labviros/is  


ENV CONAN_USERNAME is
ENV CONAN_LOGIN_USERNAME is
ENV CONAN_CHANNEL stable

# build caffe and openpose packages
ADD etc/packages/ /tmp/packages/
WORKDIR /tmp/packages
RUN cd caffe/         \
  && python3 build.py \
  && cd ../openpose/  \
  && python3 build.py \
  && cd /tmp/         \
  && rm -rf packages

# genereal dependencies
WORKDIR /tmp/
ADD conanfile.py .
RUN mkdir -p build_conan                                             \
  && cd /tmp/build_conan                                             \
  && conan install .. -s compiler.libcxx=libstdc++11 --build=missing \
  && rm -rf /tmp/*

WORKDIR /
ADD etc/dataset/download.sh .
RUN ./download.sh && rm -f download.sh

# Build container
FROM dependencies as build

ADD . /project
WORKDIR /project 
RUN bash build.sh

RUN mkdir -v -p /tmp/deploy                                              \
  && mkdir -v -p /tmp/deploy/opt/is                                      \
  && libs=`find build/ -type f -name '*.bin' -exec ldd {} \;             \
  | cut -d '(' -f 1 | cut -d '>' -f 2 | sort | uniq`                     \
  && for lib in $libs; do cp --verbose --parents $lib /tmp/deploy; done  \
  && cp --verbose `find build/ -type f -name '*.bin'` /tmp/deploy/opt/is \
  && cp --verbose etc/conf/options.json /tmp/deploy/opt/is               \
  && cp --verbose etc/docker/entrypoint /tmp/deploy                      \
  && cp --verbose etc/dataset/download.sh /tmp/deploy                    \
  && cd /tmp/deploy                                                      \
  && ./download.sh                                                       \
  && rm -f download.sh                                                   \
  && cd /                                                                \
  && rm -rf /project

# Deployment container
FROM ubuntu:16.04
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64                                             \
  PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
  LIBRARY_PATH=/usr/local/cuda/lib64/stubs                                                                    \
  NVIDIA_VISIBLE_DEVICES=all                                                                                  \
  NVIDIA_DRIVER_CAPABILITIES=compute,utility
COPY --from=build /tmp/deploy /

WORKDIR /opt/is
ENTRYPOINT [ "/entrypoint" ]      
