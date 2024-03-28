completed_tasks = [] # список выполненных задач
outstanding_tasks = [] # список не выполненнных задач

class Task():
    def __init__(self, number_task, task_description, due_date, status):
        self.number_task = number_task
        self.task_description = task_description
        self.due_date = due_date
        self.status = status

    def info(self):
        print(f'№ задачи: {self.number_task}')
        print(f'Описание задачи: {self.task_description}')
        print(f'Сроки ее выполнения: {self.due_date}')
        print(f'Статус задачи: {self.status}')

    def list_task(self, task):
        if self.status == 'выполнено':
            completed_tasks.append(task)
            print('Список выполненных задач: ')
            for i in completed_tasks:
                print(i.info())

        else:
            outstanding_tasks.append(task)
            print('Список не выполненных задач: ')
            for i in outstanding_tasks:
                print(i.info())


    def change_of_status(self, task):
        print(f'Статус задачи: {self.status}, хотите его изменить?')
        change = input('да/нет ')
        if change == 'да':
            if self.status == 'не выполнено':
                self.status = 'выполнено'
                task.list_task(task)
                print(f'Статус изменен: {self.status}')
            else:
                self.status = 'не выполнено'
                task.list_task(task)
                print(f'Статус изменен: {self.status}')
        else:
            print(f'Статус остался прежним: {self.status}')



task1 = Task(input('Введите № задачи: '), input('Ведите задачу: '), input('сроки ее выполнения: '), input('ее статус: '))
task2 = Task(input('Введите № задачи: '), input('Ведите задачу: '), input('сроки ее выполнения: '), input('ее статус: '))
task1.change_of_status()
task1.info()

task1.list_task(task1)
task2.list_task(task2)
