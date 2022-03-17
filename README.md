# are-log-parsers-ready-for-industry
`README.md under construction ...` <br> <br>
This repository contains the code associated with ...

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

Each of these datasets was accompanied by three files, namely:
1. \<`DATASET`>_2k.log -> containing 2k logs.
2. \<`DATASET`>_2k.log_structured.csv -> Containing 2k logs with their respective labels.
3. \<`DATASET`>_2k.log_templates.csv -> Containing the templates found in the dataset. For example, if a dataset has 30 templates, their list can be found in this file.

For example, the `Apache` dataset has three files associated with it, namely:
1. Apache_2k.log
2. Apache_2k.log_structured.csv
3. Apache_2k.log_templates.csv

To create a workflow able to integrate seamlessly with our log datasets, we modified the publicly avaiable datasets. Namely, we reorganized them and excluded information that was considered out of scope. Specifically, for each dataset, we:
1. Modified labeled publicly avaialable data, such that:
    1. Ensured that the \<`DATASET`>_2k.log file type contained only log `Content` information. `META` information, such as `Timestamp`, `Date`, `Node`, etc. was considered out of scope. We provide an example below: for the Apache dataset, the Apache_2k.log dataset initially contained various `META` information, such as `Time` and `Level`. We removed this information and kept only the log `Content`.<br> <img src="https://user-images.githubusercontent.com/60047427/158858976-3725ff0a-16d2-4ca8-85b0-ec96f9550c90.png" alt="dataset_modification" width="700"/>
    3. Removed data columns in the \<`DATASET`>_2k.log_structured.csv files that were considered out of scope. Initially, each dataset had its own number of columns. A table of the what columns each dataset had can be found below.
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
       Apache:       | LineId | Content | EventId | EventTemplate | Dataset |
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
2. ...
