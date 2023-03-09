cd $(pwd)/$1
git init
git add *
git commit -m "add all files to staging environment"
git remote add origin https://github.com/AnverGadzhiev/$2.git
git branch -M main
git push -u origin main
cd -
