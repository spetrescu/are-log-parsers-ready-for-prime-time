import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from natsort import natsort_keygen

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
headers = {
    "Apache": [
        "Dataset",
        "LineId",
        "Time",
        "Level",
        "Content",
        "EventId",
        "EventTemplate",
    ],
    "Mac": [
        "Dataset",
        "LineId",
        "Month",
        "Date",
        "Time",
        "User",
        "Component",
        "PID",
        "Address",
        "Content",
        "EventId",
        "EventTemplate",
    ],
    "HealthApp": [
        "Dataset",
        "LineId",
        "Time",
        "Component",
        "Pid",
        "Content",
        "EventId",
        "EventTemplate",
    ],
    "HPC": [
        "Dataset",
        "LineId",
        "LogId",
        "Node",
        "Component",
        "State",
        "Time",
        "Flag",
        "Content",
        "EventId",
        "EventTemplate",
    ],
    "Default": [
        "Dataset",
        "LineId",
        "Time",
        "Level",
        "Content",
        "EventId",
        "EventTemplate",
    ],
}


def get_number_of_templates_in_df(dataframe):
    """
    :param dataframe: a pandas.DataFrame that contains structured events
    :return: number of unique templates
    """
    return dataframe["EventId"].nunique()


NUM_OF_SAMPLES = 222
DIVERSE_DATASET_STRUCTURED = (
    "../../data/logs/Combined_Dataset/Combined_Dataset_2k.log_structured.csv"
)
DIVERSE_DATASET_LOG = "../../data/logs/Combined_Dataset/Combined_Dataset_2k.log"
DIVERSE_DATASET_TEMPLATES = (
    "../../data/logs/Combined_Dataset/Combined_Dataset_2k.log_templates.csv"
)
no_templates = []


def append_to_a_new_csv_file(dataframe, new_csv_file, header):
    dataframe.to_csv(new_csv_file, mode="w", index=False, header=header)


def append_data_samples_to_csv_file(dataframe, csv_file, header):
    dataframe.to_csv(csv_file, mode="a", index=False, header=header)


def create_diverse_dataset_structured():
    for dset in datasets:
        print(f"Sampling from {dset}...")
        df = pd.read_csv(
            f"../../data/logs/{dset}/{dset}_2k.log_structured.csv", encoding="utf-8"
        )
        df["Dataset"] = f"{dset}"
        df_logs = pd.read_csv(f"../../data/logs/{dset}/{dset}_2k.log_structured.csv", sep='\t')
        print(df_logs)
        if dset == "Apache":
            df = df[headers[f"{dset}"]]
            data_sample = df.sample(n=NUM_OF_SAMPLES)
            print(data_sample.index)
            print(data_sample)
            print(df_logs.iloc[data_sample.index])
            append_to_a_new_csv_file(
                dataframe=data_sample,
                new_csv_file=DIVERSE_DATASET_STRUCTURED,
                header=True,
            )
            append_to_a_new_csv_file(
                dataframe=data_sample["Content"],
                new_csv_file=DIVERSE_DATASET_LOG,
                header=False,
            )
            append_to_a_new_csv_file(
                dataframe=data_sample[["Dataset", "EventId", "EventTemplate"]]
                .drop_duplicates()
                .sort_values(by="EventId", key=natsort_keygen()),
                new_csv_file=DIVERSE_DATASET_TEMPLATES,
                header=True,
            )
        elif dset == "Mac" or dset == "HealthApp" or dset == "HPC":
            df = df[headers[f"{dset}"]]
            if dset == "Mac":
                data_sample = df.sample(n=NUM_OF_SAMPLES + 2)
            else:
                data_sample = df.sample(n=NUM_OF_SAMPLES)
            append_data_samples_to_csv_file(
                dataframe=data_sample, csv_file=DIVERSE_DATASET_STRUCTURED, header=False
            )
            append_data_samples_to_csv_file(
                dataframe=data_sample["Content"],
                csv_file=DIVERSE_DATASET_LOG,
                header=False,
            )
            append_data_samples_to_csv_file(
                dataframe=data_sample[["Dataset", "EventId", "EventTemplate"]]
                .drop_duplicates()
                .sort_values(by="EventId", key=natsort_keygen()),
                csv_file=DIVERSE_DATASET_TEMPLATES,
                header=False,
            )
        else:
            df = df[headers["Default"]]
            data_sample = df.sample(n=NUM_OF_SAMPLES)
            append_data_samples_to_csv_file(
                dataframe=data_sample, csv_file=DIVERSE_DATASET_STRUCTURED, header=False
            )
            append_data_samples_to_csv_file(
                dataframe=data_sample["Content"],
                csv_file=DIVERSE_DATASET_LOG,
                header=False,
            )
            append_data_samples_to_csv_file(
                dataframe=data_sample[["Dataset", "EventId", "EventTemplate"]]
                    .drop_duplicates()
                    .sort_values(by="EventId", key=natsort_keygen()),
                csv_file=DIVERSE_DATASET_TEMPLATES,
                header=False,
            )
        no_of_sampled_templates = get_number_of_templates_in_df(data_sample)
        no_templates.append(no_of_sampled_templates)
        print("No. templates:", get_number_of_templates_in_df(data_sample))


def create_diverse_dataset_log():
    return 0


def create_diverse_dataset_templates():
    return 0

def remove_quotes_in_file(file):
    with open(file, 'r+') as infile:
        data = infile.read()
        data = data.replace("\"", "")
        infile.close()
    with open(file, 'w') as outfile:
        outfile.write(data)

def plot_data_distribution():
    x = np.arange(9)
    plt.title("Number of unique templates for each dataset sampled", fontsize=16)
    plt.bar(x, height=no_templates, color="#3D9CAE", edgecolor="grey")
    plt.xticks(
        x,
        [
            "Apache",
            "BGL",
            "HDFS",
            "HealthApp",
            "HPC",
            "Mac",
            "OpenStack",
            "Spark",
            "Windows",
        ],
    )
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel("Method", fontsize=12)
    plt.ylabel("Parsing accuracy", fontsize=12)
    plt.grid(True, color="gainsboro")
    plt.show()

    labels = [
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

    initial_unique_templates = [6, 121, 14, 75, 46, 341, 43, 36, 50]
    sampled_unique_templates = no_templates
    print(sampled_unique_templates)
    width = 0.85

    fig, ax = plt.subplots()
    ax.bar(
        labels,
        initial_unique_templates,
        width,
        label="Initial",
        color="#3D9CAE",
        edgecolor="grey",
    )
    plt.bar(
        labels,
        sampled_unique_templates,
        width,
        label="Sampled",
        color="#800000",
        edgecolor="grey",
    )
    ax.set_ylabel("No. of unique samples")
    ax.set_title("Uniquely sampled templates vs initial number of templates")
    plt.ylim([0, 350])
    ax.legend()
    ax.grid(axis="y", color="gainsboro")
    plt.show()

    plt.bar(labels, sampled_unique_templates, width, label="Sampled", color="#800000")
    plt.ylabel("No. of unique samples")
    plt.ylim([0, 350])
    plt.title("Uniquely sampled templates vs initial number of templates")
    plt.legend()
    plt.grid(axis="y", color="gainsboro")
    plt.show()

create_diverse_dataset_structured()
#plot_data_distribution()
