# honestpool
Честный BITCOIN PUZZLE POOL от HoMLoL
Добро пожаловать в честный pool, с открытым ПО VanitySearch от https://github.com/FixedPaul/VanitySearch-Bitcrack, а так же откртым API, все максимально четсно, открыто и прозрачно!
## Как это работает?
Диапазоны от пазлов разбиты на области, для 71 пазла это 67,108,864 областей. Для каждой области генерируются 5 проверочных адресов, которые нужно указать чтобы завершить область.
## Какое ПО?
ПО VanitySearch от https://github.com/FixedPaul/VanitySearch-Bitcrack
Можете как с этого репозитория скачать, так и по ссылке выше, код и структура в ПО не изменялась. Это было сделано для большего доверия.
## Автоматизация?
Да! Всю автоматизацию делает python скрипт, по api отправляет запрос на получения области, после чего добавляет адреса поиска в файл in.txt и запускает VanitySearch. Для структуризации он сохраняет наденые ключ в папку tmp_files_output_{номер пазла} (tmp_files_output_71) и под названием файла out_{номер пазла}_{номер области}.txt (out_71_1.txt). После завершения VanitySearch скрипт парсит файл с найдеными ключами (tmp_files_output_71/out_71_1.txt) проверяет есть ли искомый адрес (1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU) если такой есть он выводит информацию и завершает скрипт, так же добавляет в файл FOUND!!!!!!!!.txt, если же искомый адрес не был найден он отправляет найденые проверочные адреса с закрытыи ключами на сервер по api чтобы подтвердить и завершить область.
Думаю всем понятно что все максимально прозрачно и честно!)
## API
API: https://honestpool.ru

## `GET` /api/v1/getRange

Name |  Type | Required | Default Value | Info
--- | --- | --- |  --- | ---
idPuzzle |  string | no | 71 | Номер пазла. По умолчанию 71. Тестовый пзал 70.
numberRange|  string | no | random | Номер области. По умолчанию random.

### Примеры запросов

https://honestpool.ru/api/v1/getRange
https://honestpool.ru/api/v1/getRange?idPuzzle=71&numberRange=838640

### Пример ответа

```
{
  "ok": true,
  "idPuzzle": 71,
  "targetAddress": "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU",
  "startRangeHex": "40ccbef00000000000",
  "endRangeHex": "40ccbf000000000000",
  "numberRange": "838640",
  "bits": 44,
  "proofAddresses": [
    "15ZFxTfWZD8k855RUzPmshHHxVj4ErrH4s",
    "13xxGjoyPoWgCRRBWsMZVQoW8TMq2GjWo6",
    "19bLF3s55frjneyhuuXeprhqjaow1moESj",
    "14RDhNecss1CQMD3wQ3dJmCKX48QFWwetS",
    "17WLn2GAiAQWtzhJc7kobWeF1DL2WBKMWK"
  ]
}
```

## `POST` /api/v1/setRange

Name |  Type | Required | Info
--- | --- | --- |  --- | ---
idPuzzle |  string | yes | Номер пазла.
numberRange|  string | yes | Номер области.
checkProofAddresses|  json | yes | Проверочные адреса с закрытыми ключами в формате json
comment|  string | no | Комментарий к пройденой части

### Пример запроса

https://honestpool.ru/api/v1/setRange
post
```
{"idPuzzle":"71","numberRange":"1","checkProofAddresses":"{\"1AD4QW5Q6gibLdjwGyBDyyJrY54cvKQxGP\": \"405864A632D8FE0326\", \"1GspY6uX82kPCVeWQSTqTCKxu49f3EWf7x\": \"405864A635033E0461\", \"1HiodgLdFnuEANN61EEZRb7MCn6KSsRvxG\": \"405864A636719CC264\", \"1L1hBgmfEWrkpGczia2itvMYFN8cwb6Uuz\": \"405864A63AE54145CD\", \"1H3T5xWX3gNZ4ZPB7fgecvAsy2hFqk6G8C\": \"405864A63D52D0422A\"}","comment":"pool comment"}
```
### Пример ответа

```
{
  "ok": true,
  "text": "You have successfully completed the range 1 in 71 puzzles",
}
```
