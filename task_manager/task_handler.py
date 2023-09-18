from .models import Task

class TaskManager:
    def __init__(self, user) -> None:
        self.user = user

    def create_task(self, title, description, due_date, status=False, assigned_to=None) -> Task:
        """
        Create a new task and associate it with the user.

        Args:
            title (str): The title of the task.
            description (str): The task description.
            due_date (date): The due date for the task.
            assigned_to (User, optional): The user to whom the task is assigned (if specified).

        Returns:
            Task: The created Task instance.
        """

        task = Task(
            title=title, 
            description=description,
            due_date=due_date,
            status=status,
            assigned_to=assigned_to or self.user
            )
        
        task.save()
        return task
    
    def delete_task(self, id) -> bool:
        try:
            task = Task.objects.get(id = id)

            task.delete()

            return True
        except Task.DoesNotExist:
            return False

        