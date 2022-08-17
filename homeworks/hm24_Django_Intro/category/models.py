from django.db import models
from django.contrib.auth.models import User
# from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# class Category(MPTTModel):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)
#     parent = TreeForeignKey(
#         'self',
#         blank=True,
#         null=True,
#         related_name='child',
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#         unique_together = ('slug', 'parent',)
#         verbose_name_plural = "categories"
#
#     def __str__(self):
#         full_path = [self.name]
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#
#         return ' -> '.join(full_path[::-1])