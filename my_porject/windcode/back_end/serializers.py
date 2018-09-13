from rest_framework import serializers

from .blog import models as BlogModel
from .book import models as BookModel
from .toolbox import models as ToolBox

from .blog.models import Blog

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
