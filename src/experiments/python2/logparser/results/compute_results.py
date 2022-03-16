import sys
sys.path.append('../')
from logparser import Drain, evaluator
import os
import pandas as pd

#
import sys

n = len(sys.argv)
METHOD = str(sys.argv[1])

print(f"Now computing results for method {METHOD}...")

GROUND_TRUTH_FILE_PATHS = {
    "Apache": f"../../../../../data/logs/Apache/Apache_2k.log_structured.csv",
    "BGL": f"../../../../../data/logs/BGL/BGL_2k.log_structured.csv",
    "Combined_Dataset": f"../../../../../data/logs/Combined_Dataset/Combined_Dataset_2k.log_structured.csv",
    "HDFS": f"../../../../../data/logs/HDFS/HDFS_2k.log_structured.csv",
    "HealthApp": f"../../../../../data/logs/HealthApp/HealthApp_2k.log_structured.csv",
    "HPC": f"../../../../../data/logs/HPC/HPC_2k.log_structured.csv",
    "Mac": f"../../../../../data/logs/Mac/Mac_2k.log_structured.csv",
    "OpenStack": f"../../../../../data/logs/OpenStack/OpenStack_2k.log_structured.csv",
    "Spark": f"../../../../../data/logs/Spark/Spark_2k.log_structured.csv",
    "Windows": f"../../../../../data/logs/Windows/Windows_2k.log_structured.csv",
}

files_parsed = []

for file in os.listdir(f"final_results/{METHOD}_results/"):
    if file.endswith(".csv"):
        files_parsed.append(os.path.join(f"final_results/{METHOD}_results/", file))

dsets = []

for file in files_parsed:
    dset = str(file).split("/")[-1].split("_")[0]
    dsets.append(dset)

dsets = list(dict.fromkeys(dsets))

results = []
for dset in dsets:
    list_of_parsed_files_for_specific_dataset = [
        parsed_logfile_name
        for parsed_logfile_name in files_parsed
        if dset in parsed_logfile_name
    ]
    print(sorted(list_of_parsed_files_for_specific_dataset))

    for parsed_log_file in list_of_parsed_files_for_specific_dataset:
        groundtruth = GROUND_TRUTH_FILE_PATHS[f"{dset}"]
        parsedresult = parsed_log_file
        F1_measure, accuracy = evaluator.evaluate(
            groundtruth=groundtruth, parsedresult=parsedresult
        )
        results.append([dset, F1_measure, accuracy])


def append_to_a_new_csv_file(results, new_csv_file, header):
    df_result = pd.DataFrame(results, columns=["Dataset", "F1_measure", "Accuracy"])
    df_result.set_index("Dataset", inplace=True)
    df_result.T.to_csv("Drain_result.csv")


print("files", files_parsed)
print("dsets", dsets)
