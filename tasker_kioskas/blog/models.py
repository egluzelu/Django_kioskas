from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    description = models.TextField(_("description"), blank=True, max_length=10000)
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name="blogs",
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True, null=True)
    
    class Meta:
        verbose_name = _("blog")
        verbose_name_plural = _("blogs")
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    