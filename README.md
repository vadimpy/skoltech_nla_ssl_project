This repo contains the code for Skoltech NLA 2022 project "Understanding SSL dynamics without contrastive pairs".

**Understanding self-supervised Learning Dynamics without Contrastive Pairs**

Yuandong Tian, Xinlei Chen, Surya Ganguli

ICML 2021 [link](https://arxiv.org/abs/2102.06810), *Outstanding Paper Honorable Mention* 

To train BYOL SSL method on MNIST, run
```shell
$ python3 ssl/real-dataset/main_BYOL.py
```

To train DirectPred SSL method on MNIST, run
```shell
$ python main.py seed=1 method=byol trainer.max_epochs=100 trainer.predictor_params.has_bias=false \
  trainer.predictor_params.normalization=no_normalization network.predictor_head.mlp_hidden_size=null \
  trainer.predictor_reg=corr trainer.predictor_freq=1 trainer.dyn_lambda=0.3 trainer.dyn_eps=0.01 \
  trainer balance_type=boost_scale dataset=mnist
```
The results of the training can be validated via ```ssl/real-dataset/visualization.ipynb``` and ```ssl/real-dataset/direct_pred_visualization.ipynb``` notebooks.
