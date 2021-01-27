# JBTEST
epic & amp;subtask

Stage 1
--------- Pedir en pipeline y comprobar que son .csv------------
** TODOS.csv --- csv exportado de jira current epics & subtasks --- se lee para crear global_data.csv
* Demanda_DummyCOMPARING.csv --- semanal que manda RH con toda la basura, se recibe de la pipeline --- se lee para crear dummy_data.csv

Stage 2
-------------- filtrar columnas importantes (new epics) ------------------
** global_data.csv --- columnas que nos interesan de jira current epics & subtasks
* dummy_data.csv --- columnas que nos interesan para crear epics & subtasks y actualizarlas (semanal)

Stage 3
-------------- ejecutar prueba.py ---------------------
INPUT: - global_data.csv
       - dummy_data.csv
epic_data.csv --- epics nuevos a crear --- OUTPUT import to ------> jira
EXPORT ----> from jira
NEW_TODOS.csv --- csv exportado de jira después de crear los nuevos epics --- se lee para crear new_global_data.csv

Stage 4
-------------- filtrar columnas importantes (subtasks) -------------------
new_global_data.csv --- columnas que nos interesan despues de crear epics y exportar de jira

Stage 5
-------------- ejecutar test.py 
INPUT: - new_global_data.csv
       - dummy_data.csv
subtask_finaldata.csv --- subtasks nuevas a crear --- OUTPUT import to -----> jira
