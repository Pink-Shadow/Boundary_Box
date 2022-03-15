cd assets
files=$(ls *.jpg *.JPG)
wrong_files=()
for file in $files; do
    size=$(convert $file -print "%wx%h" /dev/null)
    if [ $size != "1920x1080" ]
    then
        echo "wrong size" $size $file
        echo "wrong size" $size $file >> ../removed_files.txt
        rm -f $file
        wrong_files+=($file) 
    else
        echo $file
    fi
done
echo $wrong_files
python3 ./update_json.py ${wrong_files[@]}