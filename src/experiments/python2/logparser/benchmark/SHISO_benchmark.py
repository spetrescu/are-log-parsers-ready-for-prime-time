import sys

sys.path.append("../")
from logparser import SHISO, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = "../results/raw_results/SHISO_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+"],
        "maxChildNum": 4,
        "mergeThreshold": 0.002,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "maxChildNum": 4,
        "mergeThreshold": 0.1,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "maxChildNum": 4,
        "mergeThreshold": 0.002,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "BGL": {
        "log_format": "<Content>",
        "regex": [r"core\.\d+"],
        "maxChildNum": 4,
        "mergeThreshold": 0.005,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "HPC": {
        "log_format": "<Content>",
        "regex": [r"=\d+"],
        "maxChildNum": 3,
        "mergeThreshold": 0.003,
        "formatLookupThreshold": 0.6,
        "superFormatThreshold": 0.4,
    },
    "Windows": {
        "log_format": "<Content>",
        "regex": [r"0x.*?\s"],
        "maxChildNum": 3,
        "mergeThreshold": 0.002,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "HealthApp": {
        "log_format": "<Content>",
        "regex": [],
        "maxChildNum": 4,
        "mergeThreshold": 0.0001,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "maxChildNum": 4,
        "mergeThreshold": 0.002,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "maxChildNum": 4,
        "mergeThreshold": 0.002,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
    "Combined_Dataset": {
        "log_format": "<Content>",
        "regex": [],
        "maxChildNum": 4,
        "mergeThreshold": 0.002,
        "formatLookupThreshold": 0.3,
        "superFormatThreshold": 0.85,
    },
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = SHISO.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        maxChildNum=setting["maxChildNum"],
        mergeThreshold=setting["mergeThreshold"],
        formatLookupThreshold=setting["formatLookupThreshold"],
        superFormatThreshold=setting["superFormatThreshold"],
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
