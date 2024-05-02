$env:PYTHONIOENCODING = "UTF-8"

Start-Job -ScriptBlock {echo "sort-requirements: "; sort-requirements -c .\requirements\prod.txt .\requirements\lint.txt .\requirements\test.txt }

cd ./chattr/

Start-Job -ScriptBlock {echo "black: "; black --check . }
Start-Job -ScriptBlock {echo "flake8: "; flake8 --show-source --statistics . }
Start-Job -ScriptBlock {echo "ruff: "; ruff check . }
Start-Job -ScriptBlock {echo "isort: "; isort --check . }

Start-Job -ScriptBlock {echo "djlint: "; djlint . }

Start-Job -ScriptBlock {echo "eslint: "; cd chattr-react; eslint --ext .jsx }

Get-Job | Wait-Job
Get-Job | Receive-Job

cd ..
