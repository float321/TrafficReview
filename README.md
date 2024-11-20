Структура проекта:
1.1) Папка data
В этой папке находятся все данные, необходимые для работы приложения. На данный момент в папке есть один csv файл, Input.csv. В нём находится информация о пробках на дороге, времени суток и балле пробок.

1.2) Папка src
В этой папке находится исходный код, который используется в приложении. Здесь есть:
  1) TrafficReviewing.py - основной файл, содержащий в себе связи между остальными файлами и выполняющий основные функции приложения.
  2) Tableopener.py - вспомогательный файл, который создаёт отдельный виждет с отсортированной таблицей, раскрашенной в зависимости от балла пробок.
  3) Calculatoropener.py - вспомогательый файл, который создаёт в отдельном окне мини-калькулятор. В нём есть все основные операции с числами для быстрого подсчёта.
  4) Mapopener.py - вспомогательный файл, который создаёт окно с онлайн картой, из которой можно получать данные для таблицы.
Все вспомогательные файлы импортируются в TrafficReview.py при помощи import. Именно так и создаётся связь между разными классами приложения.
