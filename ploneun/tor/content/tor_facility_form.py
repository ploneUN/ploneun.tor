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
from plone.app.content.interfaces import INameFromTitle
from ploneun.consultant.content.consultant import IConsultant
from collective import dexteritytextindexer

from ploneun.tor import MessageFactory as _


# Interface class; used to define content-type schema.

class ITORFacilityForm(form.Schema, IImageScaleTraversable):
    """
    """
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u"Title of Contract"),
        description=_(''),
        required=True
        )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u"Brief Description"),
        description=_(u""),
        required=False
        )

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

    related_consultant = RelationChoice(
        title=_(u'Link to Consultant'),
        source=ObjPathSourceBinder(
            object_provides=IConsultant.__identifier__),
        required=False
    )

    dexteritytextindexer.searchable('tor_details')
    tor_details = RichText(
        title=_(u"Details"),
        description=_(u''),
        required=True,
        )

    dexteritytextindexer.searchable('performance')
    performance = RichText(
        title=_(u"Performance Feedback"),
        description=_(u''),
        required=False,
        )

    rating = schema.Bool(
        title=_(u"Based on your experience, would you hire this "
                u"consultant again or recommend her/him to colleagues? "
                u"(Yes / No)"),
        description=_(u''),
        required=False,
        default=None,
        )

    related_tor = RelationList(
        title=_(u'label_retalated_tor', u"Link to other TORs"),
        default=[],
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides='ploneun.tor.content'
                                '.tor_facility_form.ITORFacilityForm'
            )
        ),
        required=False
        )

    cpo_rpo_output = schema.TextLine(
        title=_(u"CPO/RPO output"),
        description=_(u''),
        required=False,
        )

    dexteritytextindexer.searchable('office')
    office = schema.Choice(                                                     
        title=u'ILO Office',                                             
        description=u'',
        required=True,                                                          
        default=None,
        source='ilo.vocabulary.offices'                                         
    )  



alsoProvides(ITORFacilityForm, IFormFieldProvider)


class NameFromTitle(grok.Adapter):
    grok.implements(INameFromTitle)
    grok.context(ITORFacilityForm)

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return u'TOR Facility Form'
