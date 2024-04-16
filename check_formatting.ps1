cd ./chattr/

black --check .
flake8 --show-source --statistics .
ruff check .
isort --check .
djlint .

cd chattr/chattr-react
eslint --ext .jsx

cd ..
