import sys

sys.path.append("../")
from logparser import LKE, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = "../results/raw_results/LKE_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+"],
        "split_threshold": 5,
    },
    "BGL": {"log_format": "<Content>", "regex": [r"core\.\d+"], "split_threshold": 30},
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "split_threshold": 3,
    },
    "HealthApp": {"log_format": "<Content>", "regex": [], "split_threshold": 50,},
    "HPC": {"log_format": "<Content>", "regex": [r"=\d+"], "split_threshold": 10},
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "split_threshold": 600,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "split_threshold": 8,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "split_threshold": 5,
    },
    "Windows": {"log_format": "<Content>", "regex": [r"0x.*?\s"], "split_threshold": 4},
    "Combined_Dataset": {
        "log_format": "<Content>",
        "regex": [],
        "split_threshold": 600,
    },
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = LKE.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        split_threshold=setting["split_threshold"],
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
