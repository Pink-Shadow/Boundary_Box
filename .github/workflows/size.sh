#!/usr/bin/env bash

cd assets
files=$(ls *.jpg *.JPG)
wrong_files=()
for file in $files; do
    size=$(convert $file -print "%wx%h" /dev/null)
    if [ $size != "1920x1080" ]
    then
        echo "wrong size" $size $file >> ../removed_files.txt
        rm -f $file
        wrong_files+=($file) 
    fi
done
echo $wrong_files
python3 ../.github/workflows/update_json.py ${wrong_files[@]}