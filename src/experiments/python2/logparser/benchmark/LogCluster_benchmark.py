import sys

sys.path.append('../')
from logparser import LogCluster, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = (
    "../results/raw_results/LogCluster_results/"
)
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {

    'Apache': {
        'log_format': '<Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'rsupport': 30
    },

    'BGL': {
        'log_format': '<Content>',
        'regex': [r'core\.\d+'],
        'rsupport': 2
    },

    'HDFS': {
        'log_format': '<Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'],
        'rsupport': 10
    },

    'HealthApp': {
        'log_format': '<Content>',
        'regex': [],
        'rsupport': 7,
    },

    'HPC': {
        'log_format': '<Content>',
        'regex': [r'=\d+'],
        'rsupport': 0.1
    },

    'Mac': {
        'log_format': '<Content>',
        'regex': [r'([\w-]+\.){2,}[\w-]+'],
        'rsupport': 0.2,
    },

    'OpenStack': {
        'log_format': '<Content>',
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
        'rsupport': 3,
    },

    'Spark': {
        'log_format': '<Content>',
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
        'rsupport': 10
    },

    'Windows': {
        'log_format': '<Content>',
        'regex': [r'0x.*?\s'],
        'rsupport': 0.2
    },

    'Combined_Dataset': {
        'log_format': '<Content>',
        'regex': [],
        'rsupport': 0.2,
    }
}

def parsing_logs(setting, indir, output_dir, log_file):
    parser = LogCluster.LogParser(indir, setting['log_format'], output_dir, rex=setting['regex'], rsupport=setting['rsupport'])
    parser.parse(log_file)

bechmark_result = []
for dataset, setting in benchmark_settings.items():
    if dataset == DATASET:

        print("=== Evaluation on %s ===" % dataset)
        logfile = str(DATASET + "/" + DATASET + "_" + SIZE + "k.log")
        indir = os.path.join(input_dir, os.path.dirname(logfile))
        log_file = os.path.basename(logfile)
        parsing_logs(setting, indir, output_dir, log_file)
        print("")
