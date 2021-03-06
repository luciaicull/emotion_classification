import argparse
from pathlib import Path


def get_parser():
    p = argparse.ArgumentParser("classification")

    p.add_argument("--path", type=Path,
                   default="/home/yoojin/data/emotionDataset/final/save/", help="emotion data folder name")
    p.add_argument("--data_name", type=str,
                   default="splitted_hop_4_split_8.dat")

    p.add_argument("--hidden_size", type=int,
                   default=2)
    p.add_argument("--num_layers", type=int,
                   default=2)
                   
    p.add_argument("--learning_rate", type=float,
                   default=0.001)
    p.add_argument("--num_epoch", type=int,
                   default=100)
    p.add_argument("--batch_size", type=int,
                   default=1)

    return p
