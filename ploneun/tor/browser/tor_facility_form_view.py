from five import grok
from plone.directives import dexterity, form
from ploneun.tor.content.tor_facility_form import ITORFacilityForm
from ploneun.tor.backref import back_references
from ploneun.consultant.vocabulary import resolve_value
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ITORFacilityForm)
    grok.require('zope2.View')
    grok.template('tor_facility_form_view')
    grok.name('view')

    def attachments(self):
        brains = self.context.portal_catalog({
            'portal_type': 'File',
            'path': {
                'query': '/'.join(self.context.getPhysicalPath()),
                'depth': 1
            }
        })

        result = []
        for brain in brains:
            obj = brain.getObject()
            unit = obj.getFile()
            icon = unit.getBestIcon()
            filename = unit.filename
            result.append({
                'icon': icon,
                'filename': filename,
                'obj': obj
            })
        return result

    def all_related_tors(self):
        return dict(related_to=[i.to_object for i in self.context.related_tor],
                    related_from=back_references(self.context, 'related_tor'))

    @property
    def tor_consultant(self):
        return self.context.related_consultant.to_object

    def get_country_name(self, obj):
        return resolve_value(obj, obj.country, 'ploneun.consultant.country')

    def resolve_value(self, context, value, vocabulary):
        factory = getUtility(IVocabularyFactory, name=vocabulary)
        vocab = factory(context)
        return vocab.getTerm(value).title

    def format_date(self, date):
        return date.strftime("%d %b %Y")
