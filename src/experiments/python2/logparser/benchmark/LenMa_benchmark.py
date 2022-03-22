import sys

sys.path.append("../")
from logparser import LenMa, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])


output_dir = "../results/raw_results/LenMa_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {
        "log_format": "<Content>",
        "CT": 0.3,
        "lowerBound": 0.4,
        "regex": [r"(\d+\.){3}\d+"],
        "threshold": 0.91,
    },
    "BGL": {"log_format": "<Content>", "regex": [r"core\.\d+"], "threshold": 0.7},
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "threshold": 0.9,
    },
    "HealthApp": {"log_format": "<Content>", "regex": [], "threshold": 0.5},
    "HPC": {"log_format": "<Content>", "regex": [r"=\d+"], "threshold": 0.8},
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "threshold": 0.86,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "threshold": 1,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "threshold": 0.9,
    },
    "Windows": {"log_format": "<Content>", "regex": [r"0x.*?\s"], "threshold": 0.78},
    "Combined_Dataset": {"log_format": "<Content>", "regex": [], "threshold": 0.86},
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = LenMa.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        threshold=setting["threshold"],
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
