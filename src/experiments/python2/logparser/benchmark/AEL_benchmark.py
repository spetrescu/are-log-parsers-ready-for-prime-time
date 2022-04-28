import sys

sys.path.append("../")
from logparser import AEL, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = (
    "../results/raw_results/AEL_results/"  # The output directory of parsing results
)
input_dir = "../../../../../data/refactored_logs"  # The input directory of log file

benchmark_settings = {
    "Apache": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+"],
        "minEventCount": 2,
        "merge_percent": 0.4,
    },
    "BGL": {
        "log_format": "<Content>",
        "regex": [r"core\.\d+"],
        "minEventCount": 2,
        "merge_percent": 0.5,
    },
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "minEventCount": 2,
        "merge_percent": 0.5,
    },
    "HealthApp": {
        "log_format": "<Content>",
        "regex": [],
        "minEventCount": 2,
        "merge_percent": 0.6,
    },
    "HPC": {
        "log_format": "<Content>",
        "regex": [r"=\d+"],
        "minEventCount": 5,
        "merge_percent": 0.4,
    },
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "minEventCount": 2,
        "merge_percent": 0.6,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "minEventCount": 6,
        "merge_percent": 0.5,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "minEventCount": 2,
        "merge_percent": 0.4,
    },
    "Windows": {
        "log_format": "<Content>",
        "regex": [r"0x.*?\s"],
        "minEventCount": 2,
        "merge_percent": 0.4,
    },
    "Combined_Dataset": {
        "log_format": "<Content>",
        "regex": [],
        "minEventCount": 2,
        "merge_percent": 0.6,
    },
    "Industry_Dataset": {
        "log_format": "<Content>",
        "regex": [],
        "minEventCount": 2,
        "merge_percent": 0.6,
    },
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = AEL.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        minEventCount=setting["minEventCount"],
        merge_percent=setting["merge_percent"],
        rex=setting["regex"],
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
