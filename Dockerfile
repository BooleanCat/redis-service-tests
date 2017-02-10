from ubuntu:trusty

RUN apt-get update && apt-get install -y \
  make \
  build-essential \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  wget \
  curl \
  llvm \
  libncurses5-dev \
  libncursesw5-dev \
  xz-utils \
  git

# create test user
RUN useradd -ms /bin/bash test
RUN echo test:funky92horse | chpasswd
ENV TEST_HOME /home/test
USER test
ENV HOME /home/test
RUN mkdir $HOME/bin
ENV PATH "$PATH:$HOME/bin"
WORKDIR $HOME

# install direnv
RUN wget -q -O $HOME/bin/direnv https://github.com/direnv/direnv/releases/download/v2.10.0/direnv.linux-amd64
RUN chmod +rx $HOME/bin/direnv
RUN echo 'eval "$(direnv hook bash)"' >> $HOME/.bashrc

# install BOSH GO CLI
RUN wget -q -O $HOME/bin/bosh https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-0.0.147-linux-amd64
RUN chmod +rx $HOME/bin/bosh

# install pyenv
RUN git clone https://github.com/yyuu/pyenv.git $HOME/.pyenv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bashrc

# install Python
RUN pyenv install 3.6.0
RUN pyenv virtualenv 3.6.0 redis-service-test
RUN pyenv rehash
RUN pyenv local redis-service-test
ENV PATH $PATH:$PYENV_ROOT/shims
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# install test dependencies
ADD requirements.txt $HOME/requirements.txt
RUN /home/test/.pyenv/shims/pip install -r requirements.txt
RUN rm requirements.txt
