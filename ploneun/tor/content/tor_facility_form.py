from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from ploneun.tor import MessageFactory as _


# Interface class; used to define content-type schema.

class ITORFacilityForm(form.Schema, IImageScaleTraversable):
    """
    """
    startdate = schema.Date(
        title=_(u"Contract Start"),
        description=_(u''),
        required=True,
        )

    enddate = schema.Date(
        title=_(u"Contract End"),
        description=_(u''),
        required=True,
        )
    value_assignment = schema.Float(
        title=_(u"Value of Assignment in USD"),
        description=_(u''),
        required=True,
        )

    form.widget(performance=WysiwygFieldWidget)
    performance = schema.Text(
        title=_(u"Performance Feedback"),
        description=_(u''),
        required=True,
        )

alsoProvides(ITORFacilityForm, IFormFieldProvider)
