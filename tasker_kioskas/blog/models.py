from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _



class Blog(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    description = models.TextField(_("description"), blank=True, max_length=10000)
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name="blogs",
    )


    class Meta:
        verbose_name = _("blog")
        verbose_name_plural = _("blogs")
        ordering = ['name', 'owner', 'description']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    