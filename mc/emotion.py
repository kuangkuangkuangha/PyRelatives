
import argparse
from mindspore import context
from easydict import EasyDict as edict


# LSTM CONFIG
lstm_cfg = edict({
    'num_classes': 2,   # 情感类别 positive negetive
    'learning_rate': 0.1,
    'momentum': 0.9,
    'num_epochs': 10,  
    'batch_size': 64,  # 32
    'embed_size': 300,  # 200
    'num_hiddens': 100,  # 隐藏维度128
    'num_layers': 2,  # 1
    'bidirectional': True, # false
    'save_checkpoint_steps': 390,
    'keep_checkpoint_max': 10
})

cfg = lstm_cfg

parser = argparse.ArgumentParser(description='MindSpore LSTM Example')
parser.add_argument('--preprocess', type=str, default='false', choices=['true', 'false'],
                    help='whether to preprocess data.')
parser.add_argument('--aclimdb_path', type=str, default="./datasets/aclImdb",
                    help='path where the dataset is stored.')
parser.add_argument('--glove_path', type=str, default="./datasets/glove",
                    help='path where the GloVe is stored.')
parser.add_argument('--preprocess_path', type=str, default="./preprocess",
                    help='path where the pre-process data is stored.')
parser.add_argument('--ckpt_path', type=str, default="./models/ckpt/nlp_application",
                    help='the path to save the checkpoint file.')
parser.add_argument('--pre_trained', type=str, default=None,
                    help='the pretrained checkpoint file path.')
parser.add_argument('--device_target', type=str, default="GPU", choices=['GPU', 'CPU'],
                    help='the target device to run, support "GPU", "CPU". Default: "GPU".')
args = parser.parse_args(['--device_target', 'GPU', '--preprocess', 'true'])

context.set_context(
        mode=context.GRAPH_MODE,
        save_graphs=False,
        device_target=args.device_target)

print("Current context loaded:\n    mode: {}\n    device_target: {}".format(context.get_context("mode"), context.get_context("device_target")))
