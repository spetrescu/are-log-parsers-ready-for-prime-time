import pandas as pd
import os
import shutil

DATASETS = [
    "Apache",
    "BGL",
    "HDFS",
    "HealthApp",
    "HPC",
    "Mac",
    "OpenStack",
    "Spark",
    "Windows",
]


def refactor_log():
    for dset in DATASETS:
        if dset == "Apache":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print(str(line).split("]")[-1])
                    new_line = str(line).split("]")[-1].lstrip()
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "BGL":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print(" ".join(str(line).split(" ")[9:]).rstrip())
                    new_line = " ".join(str(line).split(" ")[9:])
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "HDFS":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print(" ".join(str(line).split(" ")[5:]).rstrip())
                    new_line = " ".join(str(line).split(" ")[5:])
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "HealthApp":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    new_line = " ".join(str(line).split("|")[3:])
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "HPC":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print(" ".join(str(line).split(" ")[6:]).rstrip())
                    new_line = " ".join(str(line).split(" ")[6:])
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "Mac":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print(" ".join(str(line).split(":")[3:]).lstrip())
                    new_line = ":".join(str(line).split(":")[3:]).lstrip()
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "OpenStack":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    new_line = "".join(str(line).split("-]")[1:]).lstrip()
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "Spark":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print(":".join(str(line).split(":")[3:]).lstrip())
                    new_line = ":".join(str(line).split(":")[3:]).lstrip()
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)
        if dset == "Windows":
            with open(f"../../data/logs/{dset}/{dset}_2k.log") as file:
                for line in file:
                    print("".join(str(line).split("    ")[5]).lstrip())
                    new_line = "".join(str(line).split("    ")[5]).lstrip()
                    refactored_log_path = (
                        f"../../data/refactored_logs/{dset}/{dset}_2k.log"
                    )
                    with open(refactored_log_path, "a+") as f:
                        f.write(new_line)


def append_df_to_a_new_csv_file(dataframe, path, dset_dir_path):
    if not os.path.exists(dset_dir_path):
        os.makedirs(dset_dir_path)
    dataframe.to_csv(path, mode="w", index=False, header=True)


def refactor_log_structured():
    for dset in DATASETS:
        print(f"Refactoring {dset} log_structured...")
        dataframe = pd.read_csv(
            f"../../data/logs/{dset}/{dset}_2k.log_structured.csv", encoding="utf-8"
        )
        refactored_log_structured_path = (
            f"../../data/refactored_logs/{dset}/{dset}_2k.log_structured.csv"
        )
        dset_dir_path = f"../../data/refactored_logs/{dset}"

        append_df_to_a_new_csv_file(
            dataframe=dataframe[["LineId", "Content", "EventId", "EventTemplate"]],
            path=refactored_log_structured_path,
            dset_dir_path=dset_dir_path,
        )


def refactor_log_templates():
    for dset in DATASETS:
        src = f"../../data/logs/{dset}/{dset}_2k.log_templates.csv"
        dst = f"../../data/refactored_logs/{dset}/{dset}_2k.log_templates.csv"
        shutil.copyfile(src, dst)


refactor_log_structured()
refactor_log()
refactor_log_templates()
