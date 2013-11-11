from five import grok
from plone.directives import dexterity, form
from ploneun.tor.content.tor_facility_form import ITORFacilityForm
from ploneun.tor.backref import back_references

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
