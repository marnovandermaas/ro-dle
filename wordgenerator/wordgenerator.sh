aspell -d ro dump master | aspell -l ro expand | grep -E "^.{5}$" > allwords.ro.txt
cat allwords.ro.txt | grep -v "-" > nohyphen.ro.txt
