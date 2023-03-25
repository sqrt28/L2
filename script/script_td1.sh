ls
cd /tmp
mkdir project
mkdir project/{data, doc, module}
echo "BARBOSA-SAM" > /tmp/project/README
touch /tmp/project/module/{core.py, main.py}
ls -R /tmp/project >  /tmp/project/contents.txt # -R  permet d'afficher les sous répertoires
cp -r /tmp/project /tmp/projectV2 #  -r permet de copier si dosier n'est pas vide
rm -r project # il faut utiliser -r car le dossier n'est pas vide
tar -cf pv2.tar /tmp/projectV2


