# are-log-parsers-ready-for-industry
`README.md under construction ...` <br> <br>
This repository contains the code associated with ...

---

## Repository Structure
```
.
├── data
│   ├── logs/
│   └── refactored_logs/
├── pdf
│   └── are_log_parsers_ready_for_industry.pdf
├── src
│   ├── combine_datasets/
│   ├── experiments/
│   │   ├── python2/
│   │   │   ├── logparser/
│   │   │   │   ├── benchmark
│   │   │   │   ├── logparser
│   │   │   │   └── results
│   │   │   └── run_experiment_python2.sh 
│   │   └── python3/
│   │       ├── logparser/
│   │       │   ├── benchmark/
│   │       │   ├── logparser/
│   │       │   └── results/
│   │       └── run_experiment_python3.sh 
│   └── refactor_log_data/
└── README.md
```
- `data`
    - contains publicly available log data, namely nine datasets. These can be found under `data/logs/`
    - contains modified publicly available log data, used for running experiments. These can be found under `data/refactored_logs/`
- `pdf`
    - contains the document that contains a summarisation of the experiments and overall ideas
- `src`
    - contains the code used for constructing the combined dataset. This can be found under `src/combine_datasets/`
    - contains the code used for running the experiments, for Python 2 and Python 3 respectively. This can be found under `src/experiments/python2` and `src/experiments/python3`
    - contains the code used for refactoring the publicly available log datasets. This can be found under `refactor_log_data/`

---

## Setup
Below you can find instructions to reproduce the experiments. <br>
The following methods and datasets can be tested, in their respective environment.
```html
   Method      | Python 2 | Python 3 |
--------------------------------------
   AEL         |     X    |     -    |
   Drain       |     X    |     -    |
   IPLoM       |     X    |     -    |
   LenMa       |     X    |     -    |
   LFA         |     X    |     -    |
   LKE         |     X    |     -    |
   LogCluster  |     X    |     -    |
   LogMine     |     X    |     -    |
   LogSig      |     X    |     -    |
   SHISO       |     X    |     -    |
   SLCT        |     X    |     -    |
   Spell       |     X    |     -    |
   MoLFI       |     -    |     X    |
   NuLog       |     -    |     X    |
```

#### Python 2 Methods
1. `mkdir logparser && docker run --name logparser_py2 -it -v logparser:/logparser logpai/logparser:py2 bash`
2. `cd ~`
3. `git clone https://github.com/spetrescu/are-log-parsers-ready-for-industry.git`
4. `cd are-log-parsers-ready-for-industry`
5. `cd src`
6. `cd experiments`
7. `cd python2`
8. `sh run_experiment_python2.sh -m <METHOD> -d <DATASET>` <br>

After running the commands above, the results can be found under `src/experiments/python2/results`

#### Python 3 Methods

1. `mkdir logparser && docker run --name logparser_py3 -it -v logparser:/logparser logpai/logparser:py3 bash`
2. `cd ~`
3. `git clone https://github.com/spetrescu/are-log-parsers-ready-for-industry.git`
4. `cd are-log-parsers-ready-for-industry`
5. `cd src`
6. `cd experiments`
7. `cd python3`
8. `sh run_experiment_python3.sh -m <METHOD> -d <DATASET>` <br>

After running the commands above, the results can be found under `src/experiments/python3/results`

---

## Datasets Used
To run experiments, we used nine publicly available datasets:
1. `Apache`
2. `BGL`
3. `HDFS`
4. `HealthApp`
5. `HPC`
6. `Mac`
7. `OpenStack`
8. `Spark`
9. `Windows`

Each of the datasets was accompanied by three files, namely:
1. \<`DATASET`>_2k.log -> containing 2k logs.
2. \<`DATASET`>_2k.log_structured.csv -> Containing 2k logs with their respective labels.
3. \<`DATASET`>_2k.log_templates.csv -> Containing the templates found in the dataset. For example, if a dataset has 30 templates, their list can be found in this file.

For example, the `Apache` dataset has three files associated with it, namely:
1. Apache_2k.log
2. Apache_2k.log_structured.csv
3. Apache_2k.log_templates.csv

To create a workflow able to integrate seamlessly with our log datasets, we modified the publicly avaiable datasets. Namely, we reorganized them and excluded information that was considered out of scope. Additionally, we created a dataset that combined all the datasets. Specifically, we:

### 1. Keep only log `Content`
Ensured that the \<`DATASET`>_2k.log file type contained only log `Content` information. `META` information, such as `Timestamp`, `Date`, `Node`, etc. was considered out of scope. We provide an example below: for the Apache dataset, the Apache_2k.log dataset initially contained various `META` information, such as `Time` and `Level`. We removed this information and kept only the log `Content`.<br> <img src="https://user-images.githubusercontent.com/60047427/158858976-3725ff0a-16d2-4ca8-85b0-ec96f9550c90.png" alt="dataset_modification" width="700"/>
### 2. Remove data columns in the \<`DATASET`>_2k.log_structured.csv files
We removed data columns in the \<`DATASET`>_2k.log_structured.csv files that were considered out of scope. Initially, each dataset had its own number of columns. A table of the what columns each dataset had can be found below.
```html
INITIAL DATASET |   C1   |  C2  |   C3  |    C4   |    C5   |       C6      |   C7  |     C8    |  C9  |  C10 |     C11    |  C12 |    C13    | C14 |  C15  |  C16  |  C17 |  C18  |  C19 |   C20   |    C21    |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Apache       | LineId | Time | Level | Content | EventId | EventTemplate |   -   |     -     |   -  |   -  |      -     |   -  |     -     |  -  |   -   |   -   |   -  |   -   |   -  |    -    |     -     |
   BGL          | LineId | Time | Level | Content | EventId | EventTemplate,| Label | Timestamp | Date | Node | NodeRepeat | Type | Component |  -  |   -   |   -   |   -  |   -   |   -  |    -    |     -     |
   HDFS         | LineId | Time | Level | Content | EventId | EventTemplate |   -   |     -     | Date |   -  |      -     |   -  | Component | Pid |   -   |   -   |   -  |   -   |   -  |    -    |     -     |      
   HealthApp    | LineId | Time |   -   | Content | EventId | EventTemplate |   -   |     -     |   -  |   -  |      -     |   -  | Component | Pid |   -   |   -   |   -  |   -   |   -  |    -    |     -     |       
   HPC          | LineId | Time |   -   | Content | EventId | EventTemplate |   -   |     -     |   -  | Node |      -     |   -  | Component |  -  | LogId | State | Flag |   -   |   -  |    -    |     -     |
   Mac          | LineId | Time |   -   | Content | EventId | EventTemplate |   -   |     -     | Date |   -  |      -     |   -  | Component | Pid |   -   |   -   |   -  | Month | User | Address |     -     |
   OpenStack    | LineId | Time | Level | Content | EventId | EventTemplate |   -   |     -     | Date |   -  |      -     |   -  | Component | Pid |   -   |   -   |   -  |   -   |   -  | Address | Logrecord |
   Spark        | LineId | Time | Level | Content | EventId | EventTemplate |   -   |     -     | Date |   -  |      -     |   -  | Component |  -  |   -   |   -   |   -  |   -   |   -  |    -    |     -     |
   Windows      | LineId | Time | Level | Content | EventId | EventTemplate |   -   |     -     | Date |   -  |      -     |   -  | Component |  -  |   -   |   -   |   -  |   -   |   -  |    -    |     -     |
```
For the modified datasets, we kept only four columns, and we added a new one - `Dataset`. This can be found below.
```html
MODIFIED DATASET |   C1   |    C2   |    C3   |       C4      |    C5   |
-------------------------------------------------------------------------
   Apache        | LineId | Content | EventId | EventTemplate | Dataset |
   BGL           | LineId | Content | EventId | EventTemplate | Dataset |
   HDFS          | LineId | Content | EventId | EventTemplate | Dataset |
   HealthApp     | LineId | Content | EventId | EventTemplate | Dataset |
   HPC           | LineId | Content | EventId | EventTemplate | Dataset |
   Mac           | LineId | Content | EventId | EventTemplate | Dataset |
   OpenStack     | LineId | Content | EventId | EventTemplate | Dataset |
   Spark         | LineId | Content | EventId | EventTemplate | Dataset |
   Windows       | LineId | Content | EventId | EventTemplate | Dataset |
Combined Dataset | LineId | Content | EventId | EventTemplate | Dataset |
```
### 3. Sample datasets and combine into new dataset
For each of the log files we sampled a fix number of logs (222). As 9 x 222 = 1998, we sample 224 logs from the Mac dataset (to have 2k logs). The decision to sample an extra 2 logs from the Mac dataset was basedd on the template distribution, where Mac has the higest number of templates. Below, we display the initial number of templates for each of the nine datasets. 
```html
Dataset    |   No. of templates  |
----------------------------------
Apache     |         6           |
BGL        |         121         |
HDFS       |         14          |
HealthApp  |         75          |
HPC        |         46          |
Mac        |         341         |
OpenStack  |         43          |
Spark      |         36          |
Windows    |         50          |
```
To visualise the number of templates in the initial/sampled datasets, below we plot the initial number of templates (in blue) and the number of templates sampled (in red). <br>
<img src="https://user-images.githubusercontent.com/60047427/158966494-bcda4d78-7c7e-46c7-a3a6-ddb800f4eb2d.png" alt="dataset_construction" width="700"/>

---

## Acknowledgements
We would like to thank ...
