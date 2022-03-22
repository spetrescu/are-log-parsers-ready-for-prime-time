import sys

sys.path.append("../")
from logparser import LogSig, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = "../results/raw_results/LogSig_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {"log_format": "<Content>", "regex": [r"(\d+\.){3}\d+"], "groupNum": 8},
    "BGL": {"log_format": "<Content>", "regex": [r"core\.\d+"], "groupNum": 500},
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "groupNum": 15,
    },
    "HealthApp": {"log_format": "<Content>", "regex": [], "groupNum": 200},
    "HPC": {"log_format": "<Content>", "regex": [r"=\d+"], "groupNum": 800},
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "groupNum": 250,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "groupNum": 50,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "groupNum": 20,
    },
    "Windows": {"log_format": "<Content>", "regex": [r"0x.*?\s"], "groupNum": 42},
    "Combined_Dataset": {"log_format": "<Content>", "regex": [], "groupNum": 250},
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = LogSig.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        groupNum=setting["groupNum"],
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
