import sys

sys.path.append("../")
from logparser import Drain, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = (
    "../results/raw_results/Drain_results/"  # The output directory of parsing results
)
input_dir = "../../../../../data/refactored_logs"  # The input directory of log file

benchmark_settings = {
    "Apache": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+"],
        "st": 0.5,
        "depth": 4,
    },
    "BGL": {"log_format": "<Content>", "regex": [r"core\.\d+"], "st": 0.5, "depth": 4},
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "st": 0.5,
        "depth": 4,
    },
    "HealthApp": {"log_format": "<Content>", "regex": [], "st": 0.2, "depth": 4},
    "HPC": {"log_format": "<Content>", "regex": [r"=\d+"], "st": 0.5, "depth": 4},
    "Mac": {
        "log_format": "<Content>",
        "regex": [r"([\w-]+\.){2,}[\w-]+"],
        "st": 0.7,
        "depth": 6,
    },
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "st": 0.5,
        "depth": 5,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "st": 0.5,
        "depth": 4,
    },
    "Windows": {
        "log_format": "<Content>",
        "regex": [r"0x.*?\s"],
        "st": 0.7,
        "depth": 5,
    },
    "Combined_Dataset": {"log_format": "<Content>", "regex": [], "st": 0.7, "depth": 6},
    "Industry_Dataset": {"log_format": "<Content>", "regex": [], "st": 0.7, "depth": 6},
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = Drain.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        depth=setting["depth"],
        st=setting["st"],
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
