import sys

sys.path.append("../")
from logparser import Spell, evaluator
import os

n = len(sys.argv)
DATASET = str(sys.argv[1])
SIZE = str(sys.argv[2])

output_dir = "../results/raw_results/Spell_results/"
input_dir = "../../../../../data/refactored_logs"

benchmark_settings = {
    "Apache": {"log_format": "<Content>", "regex": [r"(\d+\.){3}\d+"], "tau": 0.6},
    "BGL": {"log_format": "<Content>", "regex": [r"core\.\d+"], "tau": 0.75},
    "HDFS": {
        "log_format": "<Content>",
        "regex": [r"blk_-?\d+", r"(\d+\.){3}\d+(:\d+)?"],
        "tau": 0.7,
    },
    "HealthApp": {"log_format": "<Content>", "regex": [], "tau": 0.5},
    "HPC": {"log_format": "<Content>", "regex": [r"=\d+"], "tau": 0.65},
    "Mac": {"log_format": "<Content>", "regex": [r"([\w-]+\.){2,}[\w-]+"], "tau": 0.6},
    "OpenStack": {
        "log_format": "<Content>",
        "regex": [r"((\d+\.){3}\d+,?)+", r"/.+?\s", r"\d+"],
        "tau": 0.9,
    },
    "Spark": {
        "log_format": "<Content>",
        "regex": [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"],
        "tau": 0.55,
    },
    "Windows": {"log_format": "<Content>", "regex": [r"0x.*?\s"], "tau": 0.7},
    "Combined_Dataset": {"log_format": "<Content>", "regex": [], "tau": 0.6},
    "Industry_Dataset": {"log_format": "<Content>", "regex": [], "tau": 0.6},
}


def parsing_logs(setting, indir, output_dir, log_file):
    parser = Spell.LogParser(
        log_format=setting["log_format"],
        indir=indir,
        outdir=output_dir,
        rex=setting["regex"],
        tau=setting["tau"],
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
