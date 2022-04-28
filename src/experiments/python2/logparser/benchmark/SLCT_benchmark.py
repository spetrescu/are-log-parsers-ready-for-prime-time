import sys

sys.path.append("../")
from logparser import SLCT, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = "../results/raw_results/SLCT_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {"log_format": "<Content>", "regex": [r"(\d+\.){3}\d+"], "support": 5},
    "BGL": {"log_format": "<Content>", "regex": [r"core\.\d+"], "support": 6},
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "support": 120,
    },
    "HealthApp": {"log_format": "<Content>", "regex": [], "support": 100},
    "HPC": {"log_format": "<Content>", "regex": [r"=\d+"], "support": 7},
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "support": 3,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "support": 18,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "support": 30,
    },
    "Windows": {"log_format": "<Content>", "regex": [r"0x.*?\s"], "support": 3},
    "Combined_Dataset": {"log_format": "<Content>", "regex": [], "support": 3},
    "Industry_Dataset": {"log_format": "<Content>", "regex": [], "support": 3},
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = SLCT.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        support=setting["support"],
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
