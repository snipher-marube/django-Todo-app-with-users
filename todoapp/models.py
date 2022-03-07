from django.db import models
from django.utils import timezone
from django.utils.text import slugify

def week_one_hence():
    return timezone.now() + timezone.timedelta(days=7)

class TodoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=week_one_hence)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=week_one_hence)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('due_date',)

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
            has_slug = ToDoItem.objects.filter(slug=slug).exists()
            count = 1

            while has_slug:
                count += 1
                slug = slugify(self.title + '-' + str(count))
                has_slug = ToDoItem.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}: due{self.due_date}"

