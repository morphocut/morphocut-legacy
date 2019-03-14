# Installation of MorphoCut on morphocluster-www

## System-wide

## User-wide

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
conda create -n morphocut python=3.7 h5py numpy pandas scipy -c conda-forge cmake cxx-compiler
conda activate morphocut
ssh-keygen -t rsa
# [Add SSH key as deploy key]
vim .ssh/config
chmod 600 ~/.ssh/config
git clone https://<deploy-token>:<password>@git.informatik.uni-kiel.de/sms/morphocut.git
cd morphocut
pip install -e .
```