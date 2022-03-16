#!/bin/bash
usage="$(basename "$0") [-h] [-m method] [-d dataset] -- run experiment using method & dataset
where:
    -h  show instructions to run the script
    -m  set the method (default: Drain)
    -d  set the dataset (default: All datasets)
allowed methods:
 AEL
 Drain
 IPLoM
 LenMa
 LFA
 LKE
 LogCluster
 LogMine
 LogSig
 MoLFI
 SHISO
 SLCT
 Spell
allowed datasets:
 Apachegi
 BGL
 HDFS
 HealthApp
 HPC
 Mac
 OpenStack
 Spark
 Windows
 Combined_Dataset
 Industry_Dataset"

while getopts ":hm:d:" opt; do
  case $opt in
    h) echo "$usage"
    exit
    ;;
    m) method="$OPTARG"
    ;;
    d) dataset="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

if [ -z "$method" ]
then
      echo "\$method argument empty. \nRunning script with Drain as default method."
      method="Drain"
fi

if [ -z "$dataset" ]
then
      echo "\$dataset argument empty. Thus, running script over all datasets."
      dataset="Apache BGL HDFS HealthApp HPC Mac OpenStack Spark Windows Combined_Dataset"
fi

printf "Running method %s\n" "$method"
printf "Datasets used for current experiment: %s\n" "$dataset"

cd logparser/
cd benchmark/

echo "Running $method 10 times on 10 datasets...\n"
for d in $dataset
#for d in Apache
do
  for s in 2
  do
    for r in 1 2 3
    do
        python "$method"_benchmark.py $d $s $r
        echo "Parsing $d dataset of size "$s"k [run no $r]"
        cd ..
        cd results/
        mkdir -p "final_results/""$method""_results/"
        cp "raw_results/""$method""_results/${d}_2k.log_structured.csv" "final_results/""$method""_results/${d}_2k.log_structured_run_${r}.csv"
        cd ..
        cd benchmark/
    done
  done
done
echo "\nThe parsed logs yielded by this experiment can be found under results/\n"

cd ..
cd results/
python compute_results.py $method

echo "Computing accuracy results...\n"
