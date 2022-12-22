This repo contains the code for Skoltech NLA 2022 project "Understanding SSL dynamics without contrastive pairs".


**Understanding self-supervised Learning Dynamics without Contrastive Pairs**

Yuandong Tian, Xinlei Chen, Surya Ganguli

ICML 2021 [link](https://arxiv.org/abs/2102.06810), *Outstanding Paper Honorable Mention* 


Our review of the article is available [here](https://github.com/vadimpy/skoltech_nla_ssl_project/blob/skoltech_main/understanding_ssl_dynamics_overview.pdf).  


# Introduction
The codebase is built from this [repo](https://github.com/sthalles/PyTorch-BYOL), with proper modifications. It is used in the following two arXiv papers:

You will need to install [hydra](https://github.com/facebookresearch/hydra) for parameter configuration and supporting of sweeps.  


# Prerequisite

Please install `common_utils` package in https://github.com/yuandong-tian/tools2 before running the code. 

# Sample Usage 

To train BYOL SSL method on MNIST, run
```shell
$ python3 ssl/real-dataset/main_BYOL.py
```

To train DirectPred SSL method on MNIST, run
```shell
$ python ssl/real-dataset/main.py seed=1 method=byol trainer.max_epochs=100 trainer.predictor_params.has_bias=false \
  trainer.predictor_params.normalization=no_normalization network.predictor_head.mlp_hidden_size=null \
  trainer.predictor_reg=corr trainer.predictor_freq=1 trainer.dyn_lambda=0.3 trainer.dyn_eps=0.01 \
  trainer balance_type=boost_scale dataset=mnist
```
The results of the training can be validated via ```ssl/real-dataset/visualization.ipynb``` and ```ssl/real-dataset/direct_pred_visualization.ipynb``` notebooks.

# Results

Experimental study on MNIST: t-SNE embeddings visualization
<img width="681" alt="image" src="https://user-images.githubusercontent.com/32225404/209073671-8336442b-1f46-46a5-ba8f-3b5795969417.png">
