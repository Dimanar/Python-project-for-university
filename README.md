# Python-project-for-university
Проект по предмету "Программирование на Python"
## Девочка !!!!! которая танцует )
Суть задачи:
1. Реализовать приложение, с помошью языка программирования **python** и библиотеки **pygame**. Логика игры находиться в папке **src**  в файле *main_app.py*. В других файлах находяться вспомогательные классы:
* Класс-настройка - содержит обшие данные о программе.
* Класс Событие - служит как связная часть между ботом ( отвечает за управление голосом )  и программой.
* Классы Спрайты (унаследованы от *pygame.srite.Sprites*) -  служат за отрисовку самих спрайтов.
* Класс Бот - отвечает за распознавание голоса.

![Image alt](https://github.com/Dimanar/Python-project-for-university/raw/master/image/GAME.png)

2. Реализовать управление голосом, с помошью библиотек: *speech_recognition*, *pyttsx3*, *fuzzywuzzy*.
Допольнительно реализовал нечеткое сравнение слов с командами, для улучшения качества. Проверил работу бота с разной апаратурой и пришел в к выводу, что на низкочастотных микрофонах работает хуже, нежели обычно. 
В процессе было принято решение использовать потоки, для возможности работы с программой и ботом одновременно, использовал модуль *threading*. 

