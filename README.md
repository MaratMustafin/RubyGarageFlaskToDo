# RubyGarageFlaskToDo
Задание для поступления в RubyGarage,выполнено с использованием ЯП **python** и фрейморвка **Flask**

### __Live Demo__
[Ruby Garage ToDo](http://apofsyyys.pythonanywhere.com/)

### Запуск программы
```
virtualenv rubygarage
source ./rubygarage/bin/activate
pip install - requirements.txt
export FLASK_APP=todo.py
export FLASK_DEBUG=1
flask run
```
> Если не получилось, тогда заходите в requirements.txt и устанавливайте пакеты по одному, но это врядли =)

### __Folder Structure__
```
.
├── app
│   ├── main
│   │   ├── __init__.py 
│   │   └── views.py
│   ├── static
│   │   ├── css
│   │   │   ├── datepicker.min.css
│   │   │   └── main.css
│   │   └── js
│   │       ├── app.js
│   │       ├── datepicker.js
│   │       └── jquery.editable.min.js
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── mytask.html
│   │   ├── _priority.html
│   │   └── register.html
│   └── views.py
|   │── forms.py
|	|── models.py
│   │── __init__.py
├── config.py
├── migrations
├── README.md
├── requirements.txt
├── rubygarage.db
├── test.py
├── todo.py
└── venv
```

### __Database View__
```
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(50), 
	password_hash VARCHAR(64), 
	PRIMARY KEY (id)
);
CREATE TABLE projects (
	id INTEGER NOT NULL, 
	project_name VARCHAR(50), 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
CREATE TABLE tasks (
	id INTEGER NOT NULL, 
	task_name VARCHAR(50), 
	task_status BOOLEAN, 
	task_priority INTEGER, 
	date VARCHAR(100), 
	task_position INTEGER, 
	project_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_id) REFERENCES projects (id), 
	CHECK (task_status IN (0, 1))
);
```


### __Functional requirements__
1. I want to be able to create/update/delete projects - 100%
2. I want to be able to add tasks to my project - 100%
3. I want to be able to update/delete tasks - 100%
4. I want to be able to prioritize tasks into a project - 100%
5. I want to be able to choose deadline for my task - 100%
6. I want to be able to mark a task as 'done' - 100%

### __Technical requirements__
1. Flask
2. [Paper CSS](https://www.getpapercss.com/)
3. SQLite
4. JQuery UI
5. [air datepicker](http://t1m0n.name/air-datepicker/docs/index-ru.html)

### __Additional requirements__
1. It should work like one page WEB application and should use AJAX
technology, load and submit data without reloading a page. - 50% 
2. It should have user authentication solution and a user should only have access to their own projects and tasks. - 100%
3. It should have automated tests for the all functionality - 5%

### __SQL task__

Given tables:

01. tasks (id, name, status, project_id)
02. projects (id, name)

---

- get all statuses, not repeating, alphabetically ordered
```sql
select distinct status from task order by status;
```
- get the count of all tasks in each project, order by tasks count
descending
```sql
select projects.id, count(tasks.project_id) from projects left join tasks on tasks.project_id = projects.id group by projects.id order by tasks.status desc;
```
- get the count of all tasks in each project, order by projects
names
```sql
select projects.id, count(tasks.project_id) from projects left join tasks on tasks.project_id = projects.id group by projects.id order by projects.name;
```
- get the tasks for all projects having the name beginning with
"N" letter
```sql
select tasks.name from tasks where tasks.name like 'N%';
```
- get the list of all projects containing the 'a' letter in the middle of
the name, and show the tasks count near each project. Mention
that there can exist projects without tasks and tasks with
project_id = NULL
```sql
select projects.name as project,count(tasks.id) as tasks from projects left join tasks on projects.id = tasks.project_id where projects.name like '%a%' group by project;
```
- get the list of tasks with duplicate names. Order alphabetically
```sql
select name from tasks where name in (select name from tasks group by name having count(\*) > 1) order by name;
```
- get list of tasks having several exact matches of both name and
status, from the project 'Garage'. Order by matches count
```sql
select tasks.name, count(*) as count from tasks inner join projects on projects.id = project_id where projects.name like 'Garage' group by name,priority_id having count > 1 order by name;
```
- get the list of project names having more than 10 tasks in status
'completed'. Order by project_id
```sql
select projects.id as id,projects.name as project, count(tasks.id) as count from projects inner join tasks on projects.id = project_id where tasks.done = 'completed' group by id order by id
```
	
Спасибо за просмотр!
