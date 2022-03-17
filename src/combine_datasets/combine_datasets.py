import pandas as pd
from natsort import natsorted
from natsort import natsort_keygen
import os

pd.options.mode.chained_assignment = None

datasets = [
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


def get_number_of_templates_in_df(dataframe):
    """
    :param dataframe: a pandas.DataFrame that contains structured events
    :return: number of unique templates
    """
    return dataframe["EventId"].nunique()


def append_to_a_new_csv_file(dataframe, new_csv_file, header):
    dataframe.to_csv(new_csv_file, mode="w", index=False, header=header)


def append_data_samples_to_csv_file(dataframe, csv_file, header):
    dataframe.to_csv(csv_file, mode="a", index=False, header=header)


DIVERSE_DATASET_STRUCTURED = (
    "../../data/refactored_logs/Combined_Dataset/Combined_Dataset_2k.log_structured.csv"
)
DSET_DIR_PATH = f"../../data/refactored_logs/Combined_Dataset"

if not os.path.exists(DSET_DIR_PATH):
    os.makedirs(DSET_DIR_PATH)

no_templates = []

abc = 0


def reindex_line_ids(dataframe, line_id):
    data_sample = dataframe

    data_sample["Visited"] = "False"
    data_sample = data_sample[
        ["LineId", "Content", "EventId", "EventTemplate", "Dataset", "Visited"]
    ]

    print("Now starting to replace starting from... line id = ", line_id)

    for el in natsorted(a):
        mask = (data_sample["LineId"] == el) & (data_sample["Visited"] == "False")
        data_sample["LineId"][mask] = line_id
        data_sample["Visited"][mask] = "True"
        line_id += 1

    data_sample = data_sample[
        ["LineId", "Content", "EventId", "EventTemplate", "Dataset"]
    ]

    return data_sample, line_id


def reindex_event_template_ids(dataframe, template_number):
    data_sample = dataframe

    print(
        "Number of unique templates in current df is: ",
        data_sample["EventId"].nunique(),
    )
    data_sample["Visited"] = "False"
    data_sample = data_sample[
        ["LineId", "Content", "EventId", "EventTemplate", "Dataset", "Visited"]
    ]

    a = data_sample["EventId"].unique()
    print("List of unique templates", natsorted(a), len(a))

    print("Now starting to replace... template_number = ", template_number)

    for el in natsorted(a):
        mask = (data_sample["EventId"] == el) & (data_sample["Visited"] == "False")
        data_sample["EventId"][mask] = f"E{template_number}"
        data_sample["Visited"][mask] = "True"
        template_number += 1

    a = data_sample["EventId"].unique()
    print("List of unique templates", natsorted(a), len(a))

    data_sample = data_sample[
        ["LineId", "Content", "EventId", "EventTemplate", "Dataset"]
    ].sort_values(by="LineId")

    return data_sample, template_number


def create_diverse_dataset_structured():
    num_of_samples = 222
    template_number = 1
    line_id = 1
    total_number_of_templates = 0
    for dset in datasets:
        print(f"\nSampling from {dset}...")
        df = pd.read_csv(
            f"../../data/refactored_logs/{dset}/{dset}_2k.log_structured.csv",
            encoding="utf-8",
        )
        df["Dataset"] = f"{dset}"
        df = df[["LineId", "Content", "EventId", "EventTemplate", "Dataset"]]

        if dset == "Mac":
            num_of_samples = 224
            data_sample = df.sample(n=num_of_samples)
            num_of_samples = 222
        else:
            data_sample = df.sample(n=num_of_samples)

        total_number_of_templates += data_sample["EventId"].nunique()

        data_sample, template_number = reindex_event_template_ids(
            data_sample, template_number
        )

        data_sample, line_id = reindex_line_ids(data_sample, line_id)

        if dset == "Apache":
            append_to_a_new_csv_file(
                dataframe=data_sample,
                new_csv_file=DIVERSE_DATASET_STRUCTURED,
                header=True,
            )
        else:
            append_data_samples_to_csv_file(
                dataframe=data_sample, csv_file=DIVERSE_DATASET_STRUCTURED, header=False
            )
    df = pd.read_csv(DIVERSE_DATASET_STRUCTURED, encoding="utf-8")
    print(df["LineId"].value_counts())

    lst = []
    for el in df["LineId"]:
        lst.append(el)
    lst = sorted(lst)
    for el in lst:
        print(el)

    print("Total number of templates sampled: ", total_number_of_templates)


def append_df_to_a_new_csv_file(dataframe, path):
    dataframe.to_csv(path, mode="w", index=False, header=True)


def create_combined_dataset_log():
    # print(f"Creating combined dataset...")
    dataframe = pd.read_csv(
        f"../../data/refactored_logs/Combined_Dataset/Combined_Dataset_2k.log_structured.csv",
        encoding="utf-8",
    )
    combined_log_path = (
        f"../../data/refactored_logs/Combined_Dataset/Combined_Dataset_2k.log"
    )
    count = 0
    for index, row in dataframe.iterrows():
        if count == 0:
            # print(row['Content'])
            line = str(row["Content"] + "\n")
            with open(combined_log_path, "w+") as f:
                f.write(line)
            count += 1
        else:
            # print(row['Content'])
            line = str(row["Content"] + "\n")
            with open(combined_log_path, "a+") as f:
                f.write(line)


def create_combined_dataset_templates():
    print(f"Creating combined dataset templates...")
    dataframe = pd.read_csv(
        f"../../data/refactored_logs/Combined_Dataset/Combined_Dataset_2k.log_structured.csv",
        encoding="utf-8",
    )
    templates_log_path = f"../../data/refactored_logs/Combined_Dataset/Combined_Dataset_2k.log_templates.csv"
    dataframe = (
        dataframe[["EventId", "EventTemplate"]]
        .drop_duplicates()
        .sort_values(by="EventId", key=natsort_keygen())
    )

    append_df_to_a_new_csv_file(
        dataframe=dataframe[["EventId", "EventTemplate"]], path=templates_log_path
    )


create_diverse_dataset_structured()
create_combined_dataset_log()
create_combined_dataset_templates()
