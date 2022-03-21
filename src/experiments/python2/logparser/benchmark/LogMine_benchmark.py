import sys

sys.path.append("../")
from logparser import LogMine, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = "../results/raw_results/LogMine_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+"],
        "max_dist": 0.005,
        "k": 1,
        "levels": 2,
    },
    "BGL": {
        "log_format": "<Content>",
        "regex": [r"core\.\d+"],
        "max_dist": 0.01,
        "k": 2,
        "levels": 2,
    },
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "max_dist": 0.005,
        "k": 1,
        "levels": 2,
    },
    "HealthApp": {
        "log_format": "<Content>",
        "regex": [],
        "max_dist": 0.008,
        "k": 1,
        "levels": 2,
    },
    "HPC": {
        "log_format": "<Content>",
        "regex": [r"=\d+"],
        "max_dist": 0.0001,
        "k": 0.8,
        "levels": 2,
    },
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "max_dist": 0.004,
        "k": 1,
        "levels": 2,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "max_dist": 0.001,
        "k": 0.1,
        "levels": 2,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "max_dist": 0.01,
        "k": 1,
        "levels": 2,
    },
    "Windows": {
        "log_format": "<Content>",
        "regex": [r"0x.*?\s"],
        "max_dist": 0.003,
        "k": 1,
        "levels": 2,
    },
    "Combined_Dataset": {
        "log_format": "<Content>",
        "regex": [],
        "max_dist": 0.004,
        "k": 1,
        "levels": 2,
    },
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = LogMine.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        max_dist=setting["max_dist"],
        k=setting["k"],
        levels=setting["levels"],
    )
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
