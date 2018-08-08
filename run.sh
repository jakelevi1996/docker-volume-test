#!/bin/bash

# Launch tensorboard in background to keep tabs
(tensorboard --logdir log &) &> /dev/null

# Launch synthetic data training. For testing
python3 train_agent.py --data syn --print_every 1 --num_epochs 20 --headless True

